"""Check rangoric-srd's notes before the website builds them.

  python3 .github/scripts/check_notes.py [root] [--changed <file listing changed paths>]

- Frontmatter: every note's loads as strict YAML (a set of keys, no duplicate key), as the website's build needs.
- Links: every link into the SRD has a target, by path ([[rangoric-srd/...]]) or by name ([[Note]]), in a note's
  body and in its frontmatter. Links into the sources (based-on's paths, the Changelog's source and workshop
  columns) aren't checked, nor is the Changelog's body: it is history, and links to notes since renamed stay.

With --changed, a link problem fails the check only in a changed note; the rest are printed as warnings, so a PR
is held to its own notes. Frontmatter problems fail anywhere. Exit 1 on a failure.
"""
import os, re, sys
import yaml

args = [a for a in sys.argv[1:]]
CHANGED = None
if '--changed' in args:
    i = args.index('--changed')
    CHANGED = {l.strip() for l in open(args[i + 1], encoding='utf-8') if l.strip()}
    del args[i:i + 2]
ROOT = args[0] if args else '.'
PREFIX = 'rangoric-srd/'


class Strict(yaml.SafeLoader):
    pass


def no_dupes(loader, node, deep=False):
    seen = set()
    for k, _ in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in seen:
            raise yaml.YAMLError(f'duplicate key {key!r} (line {k.start_mark.line + 2})')
        seen.add(key)
    return loader.construct_mapping(node, deep)


Strict.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, no_dupes)

WIKI = re.compile(r'!?\[\[([^\]|#^]*)(?:[#^][^\]|]*)?(?:\|[^\]]*)?\]\]')
MD = re.compile(r'(?<!!)\[[^\]]*\]\(([^)\s]+)\)')

files, names = set(), {}
for d, dirs, fs in os.walk(ROOT):
    dirs[:] = [x for x in dirs if not x.startswith('.')]
    for f in fs:
        rel = os.path.relpath(os.path.join(d, f), ROOT).replace(os.sep, '/')
        files.add(rel)
        names.setdefault(f.lower(), []).append(rel)
        if f.endswith('.md'):
            names.setdefault(f[:-3].lower(), []).append(rel)


def exists(target):
    t = target.strip().rstrip('\\').strip()   # a table cell escapes the | as \|
    if t.startswith(PREFIX):
        t = t[len(PREFIX):]
        return t in files or t + '.md' in files
    return t.lower() in names


problems, warnings = [], []


for rel in sorted(f for f in files if f.endswith('.md')):
    text = open(os.path.join(ROOT, rel), encoding='utf-8').read().replace('\r\n', '\n')
    body = text
    links = problems if CHANGED is None or rel in CHANGED else warnings
    if text.startswith('---\n'):
        end = text.find('\n---', 3)
        if end == -1:
            problems.append(f'{rel}: frontmatter has no closing ---'); continue
        fm, body = text[4:end], text[end + 4:]
        try:
            data = yaml.load(fm, Loader=Strict) if fm.strip() else {}
            if data is not None and not isinstance(data, dict):
                problems.append(f'{rel}: frontmatter is not a set of keys')
        except yaml.YAMLError as e:
            problems.append(f'{rel}: frontmatter: {str(e).splitlines()[0]}')
        for m in WIKI.finditer(fm):   # only links into the SRD; based-on points at the sources
            if m.group(1).startswith(PREFIX) and not exists(m.group(1)):
                links.append(f'{rel}: frontmatter link has no target: [[{m.group(1)}]]')
    body = re.sub(r'```.*?```', '', body, flags=re.S)
    body = re.sub(r'`[^`\n]*`', '', body)
    if rel == 'Changelog.md':
        continue
    for m in WIKI.finditer(body):
        t = m.group(1)
        if not t or ('/' in t and not t.startswith(PREFIX)):
            continue   # a heading in this note, or a source path
        if not exists(t):
            links.append(f'{rel}: link has no target: [[{t}]]')
    for m in MD.finditer(body):
        t = m.group(1)
        if re.match(r'[a-z]+:', t) or t.startswith('#'):
            continue
        p = os.path.normpath(os.path.join(os.path.dirname(rel), t.split('#')[0])).replace(os.sep, '/')
        p = p.replace('%20', ' ')
        if p not in files and p + '.md' not in files:
            links.append(f'{rel}: link has no target: ({t})')

for w in warnings:
    print(f'::warning::{w}')
for p in problems:
    print(f'::error::{p}')
print(f'{len(problems)} problem(s); {len(warnings)} warning(s) in notes this change left alone; '
      f'{len([f for f in files if f.endswith(".md")])} notes')
sys.exit(1 if problems else 0)

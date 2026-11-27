"""Check rangoric-srd's notes before the website builds them.

  python3 .github/scripts/check_notes.py [root] [--changed <file>] [--added <file>]
  python3 .github/scripts/check_notes.py [root] --baseline [--folder <folder>]

- Frontmatter: every note's loads as strict YAML (a set of keys, no duplicate key), as the website's build needs.
  (check_frontmatter.mjs also parses it the way the website does.)
- Links: every link into the SRD has a target, by path ([[rangoric-srd/...]]) or by name ([[Note]]), in a note's
  body and in its frontmatter. Links into the sources (the Changelog's source and workshop columns) aren't
  checked, nor is the Changelog's body: it is history, and links to notes since renamed stay.
- Note rules: the README's "## Note rules" (every note but the root notes and legal/), then the folder's
  `<Folder> Note Rules.md`, then the subfolder's, each read from its tables and heading lists:
    `| Key | Required | Values |` under a heading naming a kind of note (its srd-type), or under "All notes"
    (every note in the folder) or the README's "Note rules". Required is yes, no, never (the key may not be there),
    or "when `key` is `value`" ("is not" too; any other "when ..." reads as no). Values is blank (anything), allowed words in backticks
    (`*` matches any text), `number`, `text`, `date`, `link to <folder>`, `list of ...`, or "list including
    `a` and `b`". A Values cell with other words in it is for Sweep to read, not checked here.
    "Headings, in order:" then a numbered list of headings (`# (name)` is the note's own name, or that name less
    a trailing "(...)" that only keeps file names unique), checked in
    order; one not listed is allowed unless the list ends with "(no others)".
  A folder whose Note Rules has a kind table holds every note in it to one of its kinds.
- Save wording: defenses replace saving throws (Saving Throws as Defenses, 2026-11-27), so no note under the README's
  Note rules but rules/Saving Throws.md and unearthed-arcana/ says "save DC", "DC 15 Reflex save", "Reflex DC 15",
  "Reflex save for half" or "makes a saving throw" (SAVE_WORDING), outside code and comments. Base save progressions
  ("good Fortitude saves") and a creature's own "Reflex check (1d20 + Reflex save bonus)" don't match.
- Edition names: the SRD's text doesn't name the rulesets it came from (Edition Labels on Main, 2026-11-26), so a
  changed note's text has no "(3.5)", "(Pathfinder)" or "(PF1)", and no bare Pathfinder, 3.5 or 3.0 (EDITION).
  Frontmatter, link targets and numbers ("d6 | 3.5", "3.5 for d6 HD") are skipped; legal/, the Changelog, the
  Note Rules notes and Rangoric SRD's sources table are exempt.
- Regeneration: every creature with regeneration names what stops it (Regeneration Pass, 2026-11-27), so a note in
  monsters/ but monsters/abilities/ has no "regeneration N" without a parenthesis after it ("regeneration 5 (acid or
  fire)"), in its frontmatter or its text outside code and comments (REGEN_UNNAMED).
- Tables of sources: SRD notes don't carry them (SRD Content Rules, "The SRD's text"; No Source Tables, 2026-11-27),
  so no note but legal/, the Changelog and Rangoric SRD has a table whose header has a cell that is exactly Source,
  Sources, Publisher, Source book or Book source (any case, emphasis ignored; SOURCE_HEADERS), outside code.
- Base Attack/Grapple: 3.5's "Base Attack/Grapple" line (any spacing or bold) and its `base-attack-grapple` key
  are gone (Adopting CMB and CMD; Atropal and Chichimec CMB, 2026-11-27): a stat block has Base Attack, CMB
  and CMD instead (OLD_GRAPPLE).
- Slips: a changed note's text, outside code and comments, has no doubled full stop that isn't part of an ellipsis or
  a ../ path ("60 ft..") and no ",," (Small Text Fixes, 2026-11-26; SLIPS). The Changelog is exempt. Doubled words and
  spaces before punctuation have right-as-written cases, so they stay in the workshop's scan.
- Feat links: a link labeled with a feat's name points to that feat's note, not to Feats All, another feat overview
  or another feat (or monsters/Monster Feats), and a feat link isn't split in two ("[[X|Craft Magic Arms and]]" then
  "[[X|Armor]]"). A label may add a tag like " (E)", and a replaced feat's old name may point to the feat that
  replaced it. Checked like links (Feat Links by Name, FN 1, 2026-11-27).
- Alignment tags: a note with a `descriptor:` list carries the tag `chaotic`, `lawful`, `good` or `evil` for each
  of the Chaotic, Lawful, Good and Evil descriptors in it, and none for one it lacks (Chaos and Law Descriptors,
  2026-11-27; Magic Overview's ^alignment-descriptors; ALIGNMENT).
- Two-skill feats: one feat names any two skills (Two-Skill Feats, 2026-11-27; SRD Content Rules, Feats), so a
  changed note in feats/ but Reciprocal Knowledge doesn't have a Benefit that is only a bonus on checks with two or
  more skills (and its "10 or more ranks" step-up). A bonus only in a situation ("when dealing with fey"), given to
  others, or beside another benefit doesn't match (TWO_SKILL).
- Languages: Linguistics' table ("Table: Common Languages and Their Alphabets") holds every language a note names
  (Protean Language, 2026-11-27), so a changed note's "<creatures> speak(s) A, B and C." and "Automatic Languages:"
  / "Bonus Languages:" lines name only languages that are rows in it, links dropped first. A line that's mostly not
  capitalized words ("speak with outsiders") isn't a language list (LANGUAGE).
- Linnorm: no note but legal/ and the Changelog says "linnorm" outside a [[path srd 3.5/...]] link; the SRD calls
  it the lindwurm (Linnorm to Lindwurm, 2026-11-27; LINNORM).
- Marks: a note marked `sweep: failing` lists its problems in `sweep-issues`; a listed problem is a warning, one
  not listed still fails. A marked note with no problems left, or a listed issue that's gone, is a warning. A note
  added by the change (--added) can't be marked.

With --changed, a link problem fails the check only in a changed note; the rest are printed as warnings, so a PR
is held to its own notes, and so is an edition name or a slip. Frontmatter and note-rule problems fail anywhere. Exit 1
on a failure.

--baseline marks every note (in --folder only, if given) that breaks a rule, and drops the marks from notes with
no problems left, writing frontmatter through frontmatter.py (a copy of the workshop's tools/frontmatter.py), so a
new rule starts green. Note Rules plan, NR 1 (2026-11-25).
"""
import datetime, fnmatch, json, os, re, sys
import yaml

sys.dont_write_bytecode = True   # no __pycache__ beside the notes
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontmatter as F

args = sys.argv[1:]


def opt(name, has_value=True):
    if name not in args:
        return None
    i = args.index(name)
    v = args[i + 1] if has_value else True
    del args[i:i + (2 if has_value else 1)]
    return v


changed_file, added_file = opt('--changed'), opt('--added')
BASELINE, FOLDER = opt('--baseline', False), opt('--folder')
CHANGED = {l.strip() for l in open(changed_file, encoding='utf-8') if l.strip()} if changed_file else None
ADDED = {l.strip() for l in open(added_file, encoding='utf-8') if l.strip()} if added_file else set()
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


def read(rel):
    return open(os.path.join(ROOT, rel), encoding='utf-8').read().replace('\r\n', '\n')


def split(text):
    """(frontmatter text or None, body, error)"""
    if not text.startswith('---\n'):
        return None, text, None
    end = text.find('\n---', 3)
    if end == -1:
        return None, text, 'frontmatter has no closing ---'
    return text[4:end], text[end + 4:], None


# ---- feat links (Feat Links by Name, FN 1) ----

FEAT_LINK = re.compile(r'\[\[([^\]|\\#]+)(#[^\]|\\]*)?(\\?\|)([^\]]*)\]\]')
FEAT_TAG = re.compile(r'^(.*?)( \([A-Z]{1,3}\))?$')   # Feats Compiled's "(E)", "(P)"...
feat_names, feat_replaced = set(), set()
for f in files:
    if f.startswith('feats/') and f.endswith('.md'):
        n = f.rsplit('/', 1)[-1][:-3]
        head = read(f).split('\n---', 1)[0]
        (feat_replaced if re.search(r'^replaced-by:', head, re.M) else feat_names).add(n)
feat_overviews = {n for n in feat_names if n.startswith('Feats ')} | {'Feats All'}


def feat_link_problems(body):
    """Links that name a feat but don't point to its note, as the plan's fn_scan.py finds them."""
    out = []
    links = [(n, m) for n, line in enumerate(body.split('\n')) for m in FEAT_LINK.finditer(line)]
    used = set()
    for k in range(len(links) - 1):
        (n1, a), (n2, b) = links[k], links[k + 1]
        if a.group(1) == b.group(1) and a.group(1).startswith(PREFIX + 'feats/') and n2 - n1 <= 2:
            name = a.group(4) + ' ' + b.group(4)
            if name in feat_names and name not in (a.group(4), b.group(4)):
                out.append(a.group(0) + ' ' + b.group(0))
                used |= {id(a), id(b)}
    for _, m in links:
        if id(m) in used:
            continue
        tgt, label = m.group(1), m.group(4)
        base = tgt.rsplit('/', 1)[-1]
        name = FEAT_TAG.match(label).group(1)
        to_feats = tgt.startswith(PREFIX + 'feats/')
        if tgt == PREFIX + 'feats/Feats All' and label != 'Feats All' and (name in feat_names or name in feat_replaced):
            out.append(m.group(0))
        elif to_feats and base in feat_overviews and name in feat_names and name != base:
            out.append(m.group(0))
        elif (to_feats or tgt == PREFIX + 'monsters/Monster Feats') and name in feat_names and name != base \
                and name not in feat_overviews and not m.group(2):
            out.append(m.group(0))
    return [f"a feat link that doesn't point to the feat it names: {x}" for x in out]


def strip_code(body):
    body = re.sub(r'```.*?```', '', body, flags=re.S)
    return re.sub(r'`[^`\n]*`', '', body)


# ---- the written rules ----

ROW = re.compile(r'^\|(.*)\|\s*$')
HEADING = re.compile(r'^(#{1,6})\s+(.*?)\s*$')
TICKS = re.compile(r'`([^`]*)`')
ITEM = re.compile(r'^\s*(\d+\.|\(no others\))')


def cells(line):
    return [c.strip() for c in re.split(r'(?<!\\)\|', ROW.match(line).group(1))]


def new_kind():
    return {'keys': {}, 'headings': None, 'only': False}


def parse_rules(text, top_section=None):
    """{kind: {'keys': {key: (required, values)}, 'headings': [...] or None, 'only': bool}} from a Note Rules note,
    or from the README's top_section (read as the "all" kind). Under a Note Rules note's headings, one whose text is
    a single srd-type word (in backticks or not) names a kind; "All notes" is the "all" kind."""
    _, body, _ = split(text)
    lines = re.sub(r'```.*?```', '', body, flags=re.S).split('\n')
    rules, kind, inside = {}, None, top_section is None
    i = 0
    while i < len(lines):
        line = lines[i]
        h = HEADING.match(line)
        if h:
            title = h.group(2).strip().strip('`').strip()
            if top_section is not None and len(h.group(1)) <= 2:
                inside = title.lower() == top_section.lower()
                kind = 'all' if inside else None
            elif inside and top_section is None:
                if title.lower() == 'all notes':
                    kind = 'all'
                elif re.fullmatch(r'[a-z0-9][a-z0-9-]*', title):
                    kind = title
                else:
                    kind = None
            i += 1
            continue
        if inside and kind and ROW.match(line) and [c.lower() for c in cells(line)][:3] == ['key', 'required', 'values']:
            r = rules.setdefault(kind, new_kind())
            i += 2   # the header and its --- line
            while i < len(lines) and ROW.match(lines[i]):
                c = cells(lines[i]) + ['', '']
                key = c[0].strip('`').strip()
                if key:
                    r['keys'][key] = (c[1], c[2])
                i += 1
            continue
        if inside and kind and re.fullmatch(r'Headings, in order:?', line.strip()):
            r = rules.setdefault(kind, new_kind())
            r['headings'] = []
            i += 1
            while i < len(lines):
                s = lines[i].strip()
                if not s:
                    if r['headings'] and not (i + 1 < len(lines) and ITEM.match(lines[i + 1])):
                        break
                elif ITEM.match(s):
                    item = re.sub(r'^\d+\.\s*', '', s)
                    if item.startswith('(no others)'):
                        r['only'] = True
                    else:
                        m = TICKS.search(item)
                        r['headings'].append((m.group(1) if m else item).strip())
                else:
                    break
                i += 1
            continue
        i += 1
    return rules


def merge(*sets):
    """Rules of later sets (a subfolder's) expand on earlier ones (its folder's), key by key."""
    out = {}
    for s in sets:
        for kind, r in s.items():
            o = out.setdefault(kind, new_kind())
            o['keys'].update(r['keys'])
            if r['headings'] is not None:
                o['headings'], o['only'] = r['headings'], r['only']
    return out


README_RULES = parse_rules(read('README.md'), 'Note rules') if 'README.md' in files else {}
NOTE_RULES = {}   # folder path -> its Note Rules
for rel in files:
    if rel.endswith(' Note Rules.md') and '/' in rel:
        NOTE_RULES[rel.rsplit('/', 1)[0]] = parse_rules(read(rel))


def folder_rules(rel):
    parts = rel.split('/')[:-1]
    return merge(*[NOTE_RULES[p] for p in ('/'.join(parts[:n]) for n in range(1, len(parts) + 1)) if p in NOTE_RULES])


def exempt(rel):
    """The root notes (README, Changelog, Rangoric SRD, Tag Register) and legal/ (Note Rules plan, Decision 5)."""
    return '/' not in rel or rel.startswith('legal/')


def is_date(v):
    if isinstance(v, (datetime.date, datetime.datetime)):
        return True
    return isinstance(v, str) and bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}([ T].*)?', v.strip()))


def show(v):
    s = v if isinstance(v, str) else json.dumps(v, default=str)
    return s if len(s) <= 40 else s[:37] + '...'


def match_one(v, spec):
    """None if v matches a single-value spec (a Values cell, not a list form), else a short reason."""
    s = spec.strip()
    if not s:
        return None
    m = re.fullmatch(r'(?:a\s+)?links?\s+to\s+(\S+)', s)
    if m:
        folder = m.group(1).strip('`').rstrip('/')
        targets = [x.group(1) for x in WIKI.finditer(v)] if isinstance(v, str) else []
        if not targets:
            return 'not a link'
        for t in targets:
            t = t[len(PREFIX):] if t.startswith(PREFIX) else t
            hits = [t] if '/' in t else [p[:-3] for p in names.get(t.lower(), [])]
            if not any(h.startswith(folder + '/') for h in hits):
                return f'not a link to {folder}'
        return None
    words, rest = TICKS.findall(s), TICKS.sub('', s)
    if not words and rest.strip().lower() in ('number', 'text', 'date'):
        words, rest = [rest.strip().lower()], ''
    if words and re.fullmatch(r'[\s,]*(?:(?:or|and)[\s,]*)*', rest):
        for w in words:
            if w == 'number' and isinstance(v, (int, float)) and not isinstance(v, bool):
                return None
            if w == 'text' and isinstance(v, str):
                return None
            if w == 'date' and is_date(v):
                return None
            if w in ('true', 'false') and isinstance(v, bool) and str(v).lower() == w:
                return None
            if isinstance(v, (str, int, float)) and not isinstance(v, bool) and fnmatch.fnmatchcase(str(v), w):
                return None
        return 'not allowed'
    return None   # prose: Sweep reads it


def check_value(key, v, spec):
    s = spec.strip()
    m = re.fullmatch(r'list\s+including\s+(.*)', s)
    if m:
        if not isinstance(v, list):
            return f'{key} not a list'
        missing = [w for w in TICKS.findall(m.group(1)) if not any(fnmatch.fnmatchcase(str(x), w) for x in v)]
        return f'{key} lacks {", ".join(missing)}' if missing else None
    m = re.fullmatch(r'list\s+of\s+(.*)', s)
    if m:
        if not isinstance(v, list):
            return f'{key} not a list'
        inner = re.sub(r'^(numbers|texts|dates)$', lambda x: x.group(1)[:-1], m.group(1).strip())
        for x in v:
            why = match_one(x, inner)
            if why:
                return f'{key} item {why}: {show(x)}'
        return None
    why = match_one(v, s)
    if why == 'not allowed':
        return f'{key} not allowed: {show(v)}'
    return f'{key} {why}' if why else None


def required(req, data):
    if req.strip().lower() == 'yes':
        return True
    m = re.fullmatch(r'when\s+`([^`]+)`\s+is\s+(not\s+)?`([^`]*)`', req.strip(), flags=re.I)
    if m:
        return (m.group(1) in data and str(data[m.group(1)]) == m.group(3)) != bool(m.group(2))
    return False


def apply_table(keys, data, out):
    for key, (req, spec) in keys.items():
        if req.strip().lower() == 'never':
            if key in data:
                out.append(f'{key} not allowed')
            continue
        if key not in data or data[key] is None:
            if required(req, data):
                out.append(f'no {key}')
            continue
        why = check_value(key, data[key], spec)
        if why:
            out.append(why)


def check_headings(rel, body, r, out):
    want = r['headings']
    if want is None:
        return
    name = rel.rsplit('/', 1)[-1][:-3]
    have = [(len(h.group(1)), h.group(2).strip()) for h in map(HEADING.match, strip_code(body).split('\n')) if h]

    # `# (name)` is the note's name, or the name without a trailing "(...)" that only keeps file names unique, as
    # "Stabilize (Action)" titled "# Stabilize" (Wilson, Note Rules 4.p2, 2026-11-25)
    # the name, without its trailing "(…)" differentiator, or with it as a plain word: "Tornado (Blessing)" may be
    # "# Tornado" or "# Tornado Blessing" (NR 7)
    names = {name, re.sub(r'\s*\([^()]*\)$', '', name), re.sub(r'\s*\(([^()]*)\)$', r' \1', name)}

    def norm(s):
        # a "/" or ":" a file name can't hold is "-" there: "Blindness-Deafness" is "# Blindness/Deafness" (NR 6);
        # a curly apostrophe matches a straight one (NR 7)
        return s.replace('\u2019', "'").replace('/', '-').replace(':', '-')
    names |= {norm(x) for x in names}

    def same(w, h):
        lvl = len(w) - len(w.lstrip('#'))
        text = w[lvl:].strip()
        return h[0] == lvl and ((h[1] in names or norm(h[1]) in names) if text == '(name)' else h[1] == text)

    i = 0
    for w in want:
        j = next((k for k in range(i, len(have)) if same(w, have[k])), None)
        shown = w.replace('(name)', name)
        if j is None:
            out.append(f'heading out of order: {shown}' if any(same(w, h) for h in have) else f'no heading {shown}')
            continue
        if r['only']:
            out.extend(f'heading not in Note Rules: {"#" * h[0]} {h[1]}' for h in have[i:j])
        i = j + 1
    if r['only']:
        out.extend(f'heading not in Note Rules: {"#" * h[0]} {h[1]}' for h in have[i:]
                   if not any(same(w, h) for w in want))


SAVE_WORDING = re.compile(
    r'\bsave DCs?\b'
    r'|\bDC \d+ (?:Fortitude|Reflex|Will|Fort|Ref)\.? sav(?:e|ing throw)s?\b(?! bonus)'
    r'|\b(?:Fortitude|Reflex|Will|Fort|Ref)\.? (?:save |saving throw )?DC \d+'
    r'|\bDC \d+[^.;\n]{0,25}?\bsaving throws?\b'
    r'|\b(?:Fortitude|Reflex|Will) (?:save|saving throw)s? (?:for half|negates|halves|partial)'
    r'|\b(?:makes?|making|attempts?|attempting|succeeds? (?:at|on)|succeeding (?:at|on)|fails?|failing|failed|allows?'
    r'|allowing)\s+(?:an?\s+|its\s+|her\s+|his\s+|their\s+)?(?:(?:Fortitude|Reflex|Will|new|second|successful)\s+)?'
    r'(?:saving throws?\b|(?:Fortitude|Reflex|Will) saves?\b(?! bonus))',
    re.I)


def save_wording(rel, body):
    """Save wording left in a note's text (Saving Throws as Defenses): rules/Saving Throws.md, which defines the old
    words, and unearthed-arcana/, kept as printed, may have it."""
    if rel == 'rules/Saving Throws.md' or rel.startswith('unearthed-arcana/'):
        return []
    text = re.sub(r'<!--.*?-->', '', strip_code(body), flags=re.S)
    return [f'save wording: {" ".join(m.group(0).split())}' for m in SAVE_WORDING.finditer(text)]


SOURCE_HEADERS = {'source', 'sources', 'publisher', 'source book', 'book source'}
TABLE_RULE = re.compile(r'^\|(?:\s*:?-+:?\s*\|)+\s*$')


def source_tables(rel, body):
    """Tables of sources in a note (No Source Tables): a table whose header row has a Source, Sources, Publisher,
    Source book or Book source cell. legal/, the Changelog and Rangoric SRD (its sources table) may have them."""
    if rel.startswith('legal/') or rel in ('Changelog.md', 'Rangoric SRD.md'):
        return []
    lines, out = strip_code(body).split('\n'), []
    for head, rule in zip(lines, lines[1:]):
        if ROW.match(head) and TABLE_RULE.match(rule.strip()):
            names = [re.sub(r'[*_]', '', c).strip().lower() for c in cells(head)]
            if any(n in SOURCE_HEADERS for n in names):
                out.append('a table of sources (SRD Content Rules: the SRD\'s text references only itself)')
    return list(dict.fromkeys(out))


OLD_GRAPPLE = re.compile(r'(?mi)^\W*base attack\W*\s*/\s*grapple\b')
GRAPPLE_PROBLEM = "3.5's Base Attack/Grapple line (use Base Attack, CMB and CMD: Combat Maneuvers)"


def old_grapple(data, body):
    """3.5's Base Attack/Grapple line or key left in a note (Atropal and Chichimec CMB)."""
    text = re.sub(r'<!--.*?-->', '', strip_code(body), flags=re.S)
    return [GRAPPLE_PROBLEM] if OLD_GRAPPLE.search(text) or 'base-attack-grapple' in data else []


REGEN_UNNAMED = re.compile(r'\bregeneration\s+\d+\b(?!\s*\()', re.I)
LINK_TEXT = re.compile(r'\[\[[^\]|]*\|([^\]]*)\]\]|\[\[([^\]]*)\]\]')


def regeneration_unnamed(rel, data, body):
    """A "regeneration N" that doesn't name what stops it (Regeneration Pass): monsters/ but monsters/abilities/,
    where the Regeneration note itself and its kin speak of regeneration in general."""
    if not rel.startswith('monsters/') or rel.startswith('monsters/abilities/'):
        return []
    fm = '\n'.join(str(v) for v in data.values())
    text = re.sub(r'<!--.*?-->', '', strip_code(body), flags=re.S)
    text = LINK_TEXT.sub(lambda m: m.group(1) if m.group(1) is not None else m.group(2).split('/')[-1], fm + '\n' + text)
    return [f'regeneration names nothing: {m.group(0)}' for m in REGEN_UNNAMED.finditer(text)]


ALIGNMENT = {'Chaotic': 'chaotic', 'Lawful': 'lawful', 'Good': 'good', 'Evil': 'evil'}


def alignment_tags(data):
    """A note's alignment tags against its descriptors (Chaos and Law Descriptors): each of Chaotic, Lawful, Good
    and Evil in `descriptor:` has its tag, and no alignment tag is there without its descriptor."""
    if 'descriptor' not in data:
        return []
    vals = data.get('descriptor') or []
    vals = [str(v) for v in (vals if isinstance(vals, list) else [vals])]
    tags = data.get('tags') or []
    tags = [str(t) for t in (tags if isinstance(tags, list) else [tags])]
    want = {ALIGNMENT[v] for v in vals if v in ALIGNMENT}
    have = {t for t in tags if t in ALIGNMENT.values()}
    return ([f'descriptor {d.capitalize()} without the tag {d}' for d in sorted(want - have)]
            + [f'tag {d} without the descriptor {d.capitalize()}' for d in sorted(have - want)])


EDITION = re.compile(r"\((?:Pathfinder|3\.5|PF1)\)|\bPathfinder(?:’s|'s)?\b"
                     r"|(?<![\d.|])\b3\.[05](?:’s|'s)?(?=[\s’'*]|$)(?! for d)")


def edition_names(rel, body):
    """Edition names in a note's text (Edition Labels on Main): what a reader sees, link targets dropped, rows of
    numbers skipped. legal/, the Changelog, the Note Rules notes and Rangoric SRD's sources table are exempt."""
    if rel.startswith('legal/') or rel == 'Changelog.md' or rel.endswith(' Note Rules.md'):
        return []
    out, skip = [], False
    for line in body.split('\n'):
        if rel == 'Rangoric SRD.md' and line.startswith('## '):
            skip = line.strip() == '## Sources it draws from'
        if skip:
            continue
        vis = re.sub(r'\[\[[^\]|]*\\?\|', '[[', line)
        vis = re.sub(r'\[\[[^\]|]*/([^\]|/]*)\]\]', r'[[\1]]', vis)
        if vis.lstrip().startswith('|') and re.fullmatch(r'[|\s\w.*]+', vis) and not re.search('[A-Za-z]{3}', vis):
            continue   # a row of numbers
        out += [f'edition name: {m.group(0)} -- {vis.strip()[:80]}' for m in EDITION.finditer(vis)]
    return out


TWO_SKILL = {
    'skill': re.compile(r"\[\[rangoric-srd/skills/[^\]|]*\\?\|([^\]]*)\]\]"),
    'bonus': re.compile(r"\+\d+ (?:\w+ )?bonus (?:on|to)\b"),
    'target': re.compile(r"bonus (?:on|to) (?:all )?(.*?)(?:\.|;|,? and (?:a|an|you|can)\b|$)"),
    'more': re.compile(r"bonus (?:on|to) .*?,? and (?:a|an|you|can)\b"),
    'situation': re.compile(r"\b(when|whenever|against|while|as long as|made to|to (?:identify|recall|avoid|resist"
                            r"|climb|swim|catch|maintain))\b|\bgrant\b", re.I),
    'step_up': re.compile(r"10 or more ranks|increases to \+\d"),
    'benefit': re.compile(r"^(?:\*\*)?Benefits?(?:\*\*)?:\s*(.*?)(?=^(?:\*\*)?(?:Special|Normal|Prerequisites?|Note)"
                          r"(?:\*\*)?:|^This feat is part of|^#|\Z)", re.S | re.M),
}


def two_skill_feat(rel, body):
    """A feat whose whole Benefit is a bonus on two or more skills (Two-Skill Feats): it's Reciprocal Knowledge."""
    if not rel.startswith('feats/') or rel.count('/') != 1 or rel == 'feats/Reciprocal Knowledge.md':
        return []
    m = TWO_SKILL['benefit'].search(body)
    if not m:
        return []
    two = other = 0
    for s in (s.strip() for s in re.split(r"(?<=\.)\s+(?=[A-Z_*])", m.group(1)) if s.strip()):
        names = [n for t in TWO_SKILL['target'].findall(s) for n in TWO_SKILL['skill'].findall(t)]
        if TWO_SKILL['bonus'].search(s) and len(names) >= 2:
            two += 1
            if TWO_SKILL['situation'].search(s) or TWO_SKILL['more'].search(s):
                other += 1
        elif not TWO_SKILL['step_up'].search(s):
            other += 1
    if two and not other:
        return ['a +2/+2 two-skill feat: use Reciprocal Knowledge (SRD Content Rules: Feats)']
    return []


LANGUAGE = {
    'line': re.compile(r'\b(?:speaks?|(?:Automatic|Bonus) Languages:)\s+([^.\n]+)'),
    'split': re.compile(r',\s*(?:and\s+|or\s+)?|\s+and\s+|\s+or\s+'),
    'word': re.compile(r'[A-Z][a-z]+(?: Sign Language)?'),
    'not': {'Linguistics', 'Languages'},
}
LANGUAGES = set()


def table_languages():
    """The language names in Linguistics' table (Protean Language)."""
    if 'skills/Linguistics.md' not in files:
        return set()
    return set(re.findall(r'^\| ([A-Z][\w ]*?) +\|', read('skills/Linguistics.md'), re.M)) - {
        'Language', 'Task', 'Writing Results'}


def languages(rel, body):
    """Languages a note's language lines name that Linguistics' table lacks (Protean Language)."""
    if rel == 'Changelog.md' or not LANGUAGES:
        return []
    out = []
    for m in LANGUAGE['line'].finditer(re.sub(r'\[\[[^\]]*\]\]', '', strip_code(body))):
        words = [w.strip(' *_') for w in LANGUAGE['split'].split(m.group(1))]
        named = [w for w in words if LANGUAGE['word'].fullmatch(w) and w not in LANGUAGE['not']]
        if len(named) < max(1, len(words) // 2):   # mostly not a language list ("speak with outsiders")
            continue
        out += [f'language not in Linguistics\' table: {w}' for w in named if w not in LANGUAGES]
    return list(dict.fromkeys(out))


LINNORM = re.compile(r'linnorm', re.I)


def linnorm(rel, text):
    """"linnorm" in a note, outside links into the sources (Linnorm to Lindwurm). legal/ and the Changelog are exempt."""
    if rel.startswith('legal/') or rel == 'Changelog.md':
        return []
    text = re.sub(r'\[\[path srd 3\.5/[^\]]*\]\]', '', text)
    return [f'linnorm (the SRD says lindwurm) -- {line.strip()[:80]}' for line in text.split('\n')
            if LINNORM.search(line)]


SLIPS = [(re.compile(r'(?<![.\]/])(?<!\.\.)\.\.(?![./])'), 'a doubled full stop'), (re.compile(r',,'), 'a doubled comma')]


def slips(rel, text):
    """Doubled full stops and commas in a note's text, outside code and comments (Small Text Fixes)."""
    if rel == 'Changelog.md':
        return []
    text = re.sub(r'<!--.*?-->|%%.*?%%', '', strip_code(text), flags=re.S)
    return [f'{name} -- {line.strip()[max(0, m.start() - 40):m.end() + 20]}' for line in text.split('\n')
            for pat, name in SLIPS for m in pat.finditer(line.strip())]


def rule_problems(rel, data, body):
    """The note's problems against the written rules, in the checker's words (also its sweep-issues lines)."""
    if exempt(rel):
        return source_tables(rel, body)
    out = source_tables(rel, body) + save_wording(rel, body) + old_grapple(data, body)
    folder = folder_rules(rel)
    data = {k: v for k, v in data.items() if k not in ('sweep', 'sweep-issues')}
    out += regeneration_unnamed(rel, data, body)
    out += alignment_tags(data)
    if 'all' in README_RULES:
        apply_table(README_RULES['all']['keys'], data, out)
    if 'all' in folder:
        apply_table(folder['all']['keys'], data, out)
        check_headings(rel, body, folder['all'], out)
    kinds = [k for k in folder if k != 'all']
    kind = data.get('srd-type')
    if kinds and kind is not None and kind != 'note-rules':   # a Note Rules note is held to the README only
        if str(kind) in folder:
            apply_table(folder[str(kind)]['keys'], data, out)
            check_headings(rel, body, folder[str(kind)], out)
        else:
            out.append(f'srd-type not in Note Rules: {show(kind)}')
    return list(dict.fromkeys(out))


def yaml_item(s):
    """A sweep-issues line as a YAML list item: plain where it loads back as itself, else double quoted."""
    try:
        if yaml.safe_load(s) == s and not re.search(r':\s|\s#', s):
            return s
    except yaml.YAMLError:
        pass
    return json.dumps(s, ensure_ascii=False)


# ---- the check ----

problems, warnings = [], []
marks = {}   # rel -> its problems, for --baseline
LANGUAGES = table_languages()

for rel in sorted(f for f in files if f.endswith('.md')):
    if FOLDER and not rel.startswith(FOLDER.rstrip('/') + '/'):
        continue
    text = read(rel)
    links = problems if CHANGED is None or rel in CHANGED else warnings
    fm, body, err = split(text)
    data = {}
    if err:
        problems.append(f'{rel}: {err}'); continue
    if fm is not None:
        try:
            data = (yaml.load(fm, Loader=Strict) if fm.strip() else {}) or {}
            if not isinstance(data, dict):
                problems.append(f'{rel}: frontmatter is not a set of keys'); continue
        except yaml.YAMLError as e:
            problems.append(f'{rel}: frontmatter: {str(e).splitlines()[0]}'); continue
        for m in WIKI.finditer(fm):   # only links into the SRD
            if m.group(1).startswith(PREFIX) and not exists(m.group(1)):
                links.append(f'{rel}: frontmatter link has no target: [[{m.group(1)}]]')

    found = rule_problems(rel, data, body)
    links.extend(f'{rel}: {p}' for p in edition_names(rel, body))
    links.extend(f'{rel}: {p}' for p in slips(rel, text))
    links.extend(f'{rel}: {p}' for p in linnorm(rel, text))
    links.extend(f'{rel}: {p}' for p in two_skill_feat(rel, body))
    links.extend(f'{rel}: {p}' for p in languages(rel, body))
    marked = data.get('sweep') == 'failing'
    listed = data.get('sweep-issues') or []
    listed = [str(x) for x in listed] if isinstance(listed, list) else [str(listed)]
    if BASELINE:
        if found != (listed if marked else []) or ('sweep' in data and not marked) or ('sweep-issues' in data and not found):
            marks[rel] = found
    else:
        if 'sweep' in data and not marked:
            problems.append(f'{rel}: sweep is {show(data["sweep"])}; the only mark is `failing`')
        if 'sweep-issues' in data and not marked:
            problems.append(f'{rel}: sweep-issues without sweep: failing')
        if marked and rel in ADDED:
            problems.append(f'{rel}: a note this change adds can\'t be marked sweep: failing; fix it instead')
        for p in found:
            (warnings if marked and p in listed else problems).append(f'{rel}: {p}' + (' (marked failing)' if marked and p in listed else ''))
        if marked and not found:
            warnings.append(f'{rel}: no problems left; drop sweep and sweep-issues')
        elif marked:
            warnings.extend(f'{rel}: fixed, drop it from sweep-issues: {p}' for p in listed if p not in found)

    if rel == 'Changelog.md':
        continue
    links.extend(f'{rel}: {p}' for p in feat_link_problems(strip_code(body)))
    body = strip_code(body)
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

if BASELINE:
    added = dropped = 0
    for rel, found in sorted(marks.items()):
        text = read(rel)
        if not text.startswith('---\n'):
            text = '---\n---\n' + text
        if found:
            text = F.set_key(text, 'sweep', 'failing', name=rel)
            text = F.set_key(text, 'sweep-issues', '\n' + '\n'.join(f'  - {yaml_item(p)}' for p in found), name=rel)
            added += 1
        else:
            text = F.remove_key(F.remove_key(text, 'sweep-issues', rel), 'sweep', rel)
            dropped += 1
        with open(os.path.join(ROOT, rel), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(text)
        print(f'marked {rel}: {"; ".join(found)}' if found else f'unmarked {rel}')
    print(f'baseline: {added} note(s) marked, {dropped} unmarked')
    sys.exit(0)

for w in warnings:
    print(f'::warning::{w}')
for p in problems:
    print(f'::error::{p}')
print(f'{len(problems)} problem(s); {len(warnings)} warning(s); {len([f for f in files if f.endswith(".md")])} notes')
sys.exit(1 if problems else 0)

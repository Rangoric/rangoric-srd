"""Read, set and check a note's frontmatter, strictly (Wilson, 2026-11-23; Retro 2026-11-23).

Frontmatter is checked wherever it's written, so a fault shows up when it's made, not when the website build fails.
Batch scripts and generators set keys through set_key() instead of hand regex edits: it replaces a key that's already
there and never adds a second one, and the result is loaded as strict YAML. batch.py commit (and merge, on the rerun
copy) runs check() on every changed note as the last line of defence.

    import frontmatter as F            # tools/ is on sys.path (see batch.py, or add it)
    text = F.set_key(text, 'group', '"[[rangoric-srd/monsters/shark/Sharks|Sharks]]"', before='status', name=rel)
    F.check(text, rel)                 # raises F.FrontmatterError naming the note
    data = F.load(text, rel)           # the frontmatter as a dict

Values are written as given (a YAML scalar, already quoted as needed). A key's value may run over several lines
(a list under it, as aliases can have); set_key replaces all of them.

Command line: frontmatter.py <file or folder>...  checks every .md under them and lists the bad ones (exit 1 if any).
"""
import os, re, sys
import yaml


class FrontmatterError(ValueError):
    pass


class _StrictLoader(yaml.SafeLoader):
    pass


def _no_duplicates(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise FrontmatterError(f'duplicate key {key!r} (line {key_node.start_mark.line + 2})')
        seen.add(key)
    return loader.construct_mapping(node, deep)


_StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates)


def split(text, name=''):
    """(frontmatter text without the --- lines, the rest). A note without frontmatter gives ('', text)."""
    if not text.startswith('---\n'):
        return '', text
    end = text.find('\n---\n', 3)
    if end == -1:
        if text.endswith('\n---'):
            return text[4:-4], ''
        raise FrontmatterError(f'{name}: frontmatter has no closing ---')
    return text[4:end], text[end + 5:]


def load(text, name=''):
    """The frontmatter as a dict, loaded strictly: duplicate keys and any YAML error raise FrontmatterError."""
    fm, _ = split(text, name)
    if not fm.strip():
        return {}
    try:
        data = yaml.load(fm, Loader=_StrictLoader)
    except FrontmatterError as e:
        raise FrontmatterError(f'{name}: {e}') from None
    except yaml.YAMLError as e:
        raise FrontmatterError(f'{name}: invalid YAML: {str(e).splitlines()[0]} {getattr(e, "problem_mark", "") or ""}'.strip()) from None
    if not isinstance(data, dict):
        raise FrontmatterError(f'{name}: frontmatter is not a set of keys')
    return data


def check(text, name=''):
    load(text, name)
    return text


def _key_span(lines, key):
    """Indexes [start, end) of a top-level key's lines (the key and any indented or list lines under it), or None."""
    pat = re.compile(r'^' + re.escape(key) + r'\s*:')
    hits = [i for i, l in enumerate(lines) if pat.match(l)]
    if len(hits) > 1:
        raise FrontmatterError(f'duplicate key {key!r} already there')
    if not hits:
        return None
    i = hits[0]
    j = i + 1
    while j < len(lines) and (lines[j].startswith((' ', '\t', '- ')) or lines[j] == '-'):
        j += 1
    return i, j


def set_key(text, key, value, before=None, name=''):
    """Set a top-level key to a YAML value (given as written, e.g. '"[[X|X]]"' or 'draft'). Replaces it if it's there;
    otherwise adds it before the key `before` (or at the end). The result is checked strictly."""
    fm, body = split(text, name)
    if not text.startswith('---\n'):
        raise FrontmatterError(f'{name}: no frontmatter to set {key!r} in')
    lines = fm.split('\n') if fm else []
    try:
        span = _key_span(lines, key)
    except FrontmatterError as e:
        raise FrontmatterError(f'{name}: {e}') from None
    new = (f'{key}:{value}' if value.startswith('\n') or value == '' else f'{key}: {value}').split('\n')
    if span:
        lines[span[0]:span[1]] = new
    else:
        at = len(lines)
        if before:
            b = _key_span(lines, before)
            if b:
                at = b[0]
        lines[at:at] = new
    out = '---\n' + '\n'.join(lines) + '\n---\n' + body
    return check(out, name)


def remove_key(text, key, name=''):
    fm, body = split(text, name)
    lines = fm.split('\n')
    span = _key_span(lines, key)
    if not span:
        return text
    del lines[span[0]:span[1]]
    return check('---\n' + '\n'.join(lines) + '\n---\n' + body, name)


def check_files(paths, root=None):
    """[(rel, error)] for every .md under paths whose frontmatter doesn't load strictly."""
    bad = []
    for p in paths:
        files = [p] if os.path.isfile(p) else [os.path.join(d, f) for d, _, fs in os.walk(p) if '/.git' not in d
                                                for f in fs if f.endswith('.md')]
        for fp in files:
            rel = os.path.relpath(fp, root) if root else fp
            try:
                load(open(fp, encoding='utf-8').read(), rel)
            except FrontmatterError as e:
                bad.append((rel, str(e)))
            except UnicodeDecodeError:
                bad.append((rel, f'{rel}: not UTF-8'))
    return bad


if __name__ == '__main__':
    bad = check_files(sys.argv[1:] or ['.'])
    for _, e in bad:
        print(e)
    print(f'{len(bad)} bad' if bad else 'all frontmatter loads')
    sys.exit(1 if bad else 0)

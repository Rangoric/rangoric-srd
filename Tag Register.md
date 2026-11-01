---
tags: [rangoric, rangoric/overview]
started: 2026-10-30
---

# Tag Register

Every game tag used in `rangoric-srd`: what it means, what it goes on, and how many notes carry it. A tag like *knowledge* groups things so a rule can say "Knowledge skills" and mean all of them. How Obsidian handles tags is in [Tags - Obsidian Help](https://obsidian.md/help/tags).

## How tags are written (2026-10-30)

- **Lowercase, no prefix**: `knowledge`, not `Knowledge` or `rangoric/knowledge`. Long term, game tags are only used in this SRD, so they don't need a prefix to stay apart from the reference SRDs.
- **In the `tags` property**, next to the note-kind tags each note already has (`rangoric`, `rangoric/skill`, `rangoric/feat`, and so on).
- **In rule text, with a capital**: "Knowledge skills", "Background skills".
- **No spaces.** A name with two words takes a hyphen, such as `item-creation`.
- **A tag that carries a rule** (more than a grouping) gets one home note that says what it means, and its row here links to it.

## Keep an eye on

- **How many there are.** If the list gets long, or one word starts meaning different things on different kinds of notes, it may be time for prefixes. For example, `skill/core` and `feat/metamagic` would sort skill tags and feat tags apart. Feats and skills are the likeliest to want one. That waits until it's clear how the tags shake out.
- **Overlaps.** If two tags mean nearly the same thing, merge them.
- **Counts.** Update each count when a batch adds or removes the tag.

## Game tags

| Tag | Goes on | Means | Home | Notes | Status |
| --- | --- | --- | --- | --- | --- |
| `core` | Skills | Generally useful to an adventurer; bought with core points | [[rangoric-srd/skills/Skills Overview\|Skills Overview]] | 26 skills | In use (2026-10-30) |
| `background` | Skills | Useful to a normal person; 1 background point per level, and the first one picked is a class skill | [[rangoric-srd/skills/Skills Overview\|Skills Overview]] | 7 skills (Craft, Profession, Performance, Appraise, Animal Handling, Linguistics, Lore) | In use (2026-10-30) |
| `knowledge` | Skills | A knowledge skill. Rules can say "any Knowledge skill" or "all Knowledge skills" | [[rangoric-srd/skills/Knowledge\|Knowledge]] | 8 skills (Arcana, Dungeoneering, Lore, Nature, Psionics, Society, Tactics, Theology) | In use (2026-10-30) |
| `magic` | Skills | A Magic skill: Arcana, Theology, Nature, Psionics. A "Magic skill check" uses whichever one fits (Identifying Magic), and each casting class lists its own | [[rangoric-srd/skills/Identifying Magic\|Identifying Magic]] | 4 skills | In use (2026-10-30) |
| `first-aid` | Actions | A First Aid action: either Fieldcraft or Medicine can make the check | [[rangoric-srd/actions/First Aid\|First Aid]] | 8 actions | In use (2026-10-31) |

## Candidates for later

From [[Working Folder/brainstorming/Future Ideas|Future Ideas]] (Tags). None of these are decided:

- Feat types: general, metamagic, item-creation, epic, and the rest.
- Spell schools, subschools and descriptors: fire, mind-affecting, and the rest.
- Monster types and subtypes, and psionic disciplines.

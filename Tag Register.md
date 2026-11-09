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
| `fighter-bonus` | Feats | A fighter can take it as a bonus feat, including the epic fighter's list. Pathfinder's Combat type will be a tag of its own | [[rangoric-srd/feats/Feats Overview#Fighter Bonus Feats\|Feats Overview]] | 532 feats | In use (2026-11-01) |
| `item-creation` | Feats | An item creation feat: lets its owner make a kind of magic or psionic item | [[rangoric-srd/feats/Feats Overview#Item Creation Feats\|Feats Overview]] | 23 feats | In use (2026-11-01) |
| `metamagic` | Feats | A metamagic feat: changes a spell, which then takes a higher-level slot | [[rangoric-srd/feats/Feats Overview#Metamagic Feats\|Feats Overview]] | 45 feats | In use (2026-11-01) |
| `style` | Feats | A style feat: sets a fighting stance, entered as a swift action, one at a time | [[rangoric-srd/feats/Feats Overview#Style Feats\|Feats Overview]] | 30 feats | In use (2026-11-07) |
| `critical` | Feats | A critical feat: adds an effect to a critical hit; one applies to a hit unless you have Critical Mastery | [[rangoric-srd/feats/Feats Overview#Critical Feats\|Feats Overview]] | 15 feats | In use (2026-11-09) |
| `teamwork` | Feats | A teamwork feat: works only with an ally who also has it, positioned as the feat says | [[rangoric-srd/feats/Feats Overview#Teamwork Feats\|Feats Overview]] | 35 feats | In use (2026-11-09) |
| `epic` | Feats | An epic feat: taken only at 21st level or higher | [[rangoric-srd/epic/Epic Feats#Acquiring Epic Feats\|Epic Feats]] | 158 feats | In use (2026-11-01) |
| `divine` | Feats | A divine feat: needs the ability to turn or rebuke undead, and spends uses of [[rangoric-srd/combat/Combat Special Attacks#^channel-energy\|channel energy]] | [[rangoric-srd/epic/Epic Feats#Divine Feats\|Epic Feats]] | 5 feats | In use (2026-11-01) |
| `wild` | Feats | A wild feat: needs wild shape, and usually spends uses of it | [[rangoric-srd/epic/Epic Feats#Wild Feats\|Epic Feats]] | 22 feats | In use (2026-11-01) |
| `psionic` | Feats | A psionic feat: only for manifesters; many use psionic focus | [[rangoric-srd/psionics/Psionic Feats\|Psionic Feats]] | 46 feats | In use (2026-11-01) |
| `metapsionic` | Feats | A metapsionic feat: changes a power, at a higher power point cost | [[rangoric-srd/psionics/Psionic Feats#Metapsionic Feats\|Psionic Feats]] | 13 feats | In use (2026-11-01) |
| `spelltouched` | Feats | A spelltouched feat (Unearthed Arcana): open only to someone affected by its spell | [[rangoric-srd/unearthed-arcana/Spelltouched Feats\|Spelltouched Feats]] | 17 feats | In use (2026-11-01) |

## Candidates for later

From [[Working Folder/brainstorming/Future Ideas|Future Ideas]] (Tags). None of these are decided:

- Spell schools, subschools and descriptors: fire, mind-affecting, and the rest.
- Monster types and subtypes, and psionic disciplines.

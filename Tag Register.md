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
| `fighter-bonus` | Feats | A fighter can take it as a bonus feat, including the epic fighter's list. Pathfinder's Combat type will be a tag of its own | [[rangoric-srd/feats/Feats Overview#Fighter Bonus Feats\|Feats Overview]] | 583 feats | In use (2026-11-01) |
| `item-creation` | Feats | An item creation feat: lets its owner make a kind of magic or psionic item | [[rangoric-srd/feats/Feats Overview#Item Creation Feats\|Feats Overview]] | 39 feats | In use (2026-11-01) |
| `metamagic` | Feats | A metamagic feat: changes a spell, which then takes a higher-level slot | [[rangoric-srd/feats/Feats Overview#Metamagic Feats\|Feats Overview]] | 54 feats | In use (2026-11-01) |
| `style` | Feats | A style feat: sets a fighting stance, entered as a swift action, one at a time | [[rangoric-srd/feats/Feats Overview#Style Feats\|Feats Overview]] | 30 feats | In use (2026-11-07) |
| `critical` | Feats | A critical feat: adds an effect to a critical hit; one applies to a hit unless you have Critical Mastery | [[rangoric-srd/feats/Feats Overview#Critical Feats\|Feats Overview]] | 17 feats | In use (2026-11-09) |
| `teamwork` | Feats | A teamwork feat: works only with an ally who also has it, positioned as the feat says | [[rangoric-srd/feats/Feats Overview#Teamwork Feats\|Feats Overview]] | 52 feats | In use (2026-11-09) |
| `racial` | Feats | A racial feat: open only to members of a race (or to those with one of its racial traits), as its prerequisites say. A grouping only, so race notes can list their feats | [[rangoric-srd/races/PC Races\|PC Races]] | 180 feats | In use (2026-11-10) |
| `epic` | Feats, magic items | An epic feat: taken only at 21st level or higher. An epic magic item: its `item-type` starts with Epic (made with the epic item creation feats, or an epic artifact) | [[rangoric-srd/epic/Epic Feats#Acquiring Epic Feats\|Epic Feats]], [[rangoric-srd/epic/Epic Magic Items\|Epic Magic Items]] | 158 feats, 119 magic items | In use (2026-11-01; magic items 2026-11-11) |
| `divine` | Feats | A divine feat: needs the ability to turn or rebuke undead, and spends uses of [[rangoric-srd/combat/Combat Special Attacks#^channel-energy\|channel energy]] | [[rangoric-srd/epic/Epic Feats#Divine Feats\|Epic Feats]] | 5 feats | In use (2026-11-01) |
| `wild` | Feats | A wild feat: needs wild shape, and usually spends uses of it | [[rangoric-srd/epic/Epic Feats#Wild Feats\|Epic Feats]] | 22 feats | In use (2026-11-01) |
| `psionic` | Feats | A psionic feat: only for manifesters; many use psionic focus | [[rangoric-srd/psionics/Psionic Feats\|Psionic Feats]] | 46 feats | In use (2026-11-01) |
| `metapsionic` | Feats | A metapsionic feat: changes a power, at a higher power point cost | [[rangoric-srd/psionics/Psionic Feats#Metapsionic Feats\|Psionic Feats]] | 13 feats | In use (2026-11-01) |
| `spelltouched` | Feats | A spelltouched feat: open only to someone affected by its spell | [[rangoric-srd/unearthed-arcana/Spelltouched Feats\|Spelltouched Feats]] | 17 feats | In use (2026-11-01) |
| `shadetouched` | Feats | A shadetouched feat: draws on necromantic energy, with uses per day and a cost in hit points | [[rangoric-srd/rules/path-of-shades/The Path of Shades#Shadetouched Feats\|The Path of Shades]] | 5 feats | In use (2026-11-10) |
| `sign` | Feats | A sign feat: a birth sign from star magic, taken only at 1st level; some pair a bonus with a drawback | [[rangoric-srd/rules/star magic/Star Magic#^sign-feats|Star Magic]] | 9 feats | In use (2026-11-10) |
| `flavor` | Flavor notes | Setting and flavor text, not rules: nothing else depends on it. A grouping only, so the folder's base can list it | [[rangoric-srd/flavor/Flavor Overview\|Flavor Overview]] | 74 notes | In use (2026-11-11) |
| `racial-trait/<category>` | Racial traits | The race builder category a racial trait belongs to (ability, defense, feat-skill, magical, movement, offense, senses, weakness, other); a race takes at most 3, 4 or 5 traits per category | [[rangoric-srd/races/race builder/Race Builder\|Race Builder]] | 77 notes: `ability` 0, `defense` 18, `feat-skill` 16, `magical` 22, `movement` 8, `offense` 7, `senses` 4, `weakness` 0, `other` 2 | In use (2026-11-10) |
| `racial-trait/<tier>` | Racial traits | The power level a racial trait needs (standard, advanced, monstrous) | [[rangoric-srd/races/race builder/Race Builder\|Race Builder]] | 77 notes: `standard` 77, `advanced` 0, `monstrous` 0 | In use (2026-11-10) |
| `eastern` | Weapons | An eastern weapon, from the martial traditions of Asia; rules that name eastern weapons mean these | [[rangoric-srd/equipment/Equipment Weapons#^eastern-weapons\|Equipment Weapons]] | 55 weapons | In use (2026-11-11) |
| `weapon-group/<group>` | Weapons | The weapon group a weapon is in, for class features that work with a group (such as fighter weapon training); a weapon can be in several. The lists in Equipment Weapons are built from these tags | [[rangoric-srd/equipment/Equipment Weapons#^weapon-groups\|Equipment Weapons]] | `axes` 23, `heavy-blades` 36, `light-blades` 34, `bows` 12, `close` 24, `crossbows` 10, `double` 24, `firearms` 21, `flails` 23, `hammers` 25, `monk` 12, `natural` 2, `pole-arms` 23, `spears` 22, `thrown` 40 | In use (2026-11-11) |

## Candidates for later

From [[Working Folder/brainstorming/Future Ideas|Future Ideas]] (Tags). None of these are decided:

- Spell schools, subschools and descriptors: fire, mind-affecting, and the rest.
- Monster types and subtypes, and psionic disciplines.

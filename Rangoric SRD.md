---
tags: [rangoric, rangoric/index]
---

# Rangoric SRD

My combined rules: one version of each rule, starting from the whole 3.5 SRD and adjusted from the other sources. The processed notes stay untouched as reference; everything here is mine.

## Sources it draws from

| Source | Folder | Good for |
| --- | --- | --- |
| 3.5 SRD | `fantasy srd 3.5` | The base: classes, feats, spells, monsters, Unearthed Arcana variants |
| Pathfinder 1e (PSRD) | `path srd 3.5` | Cleaned-up 3.5, monster creation and roles, Unchained variants |
| Pathfinder 1e (Foundry) | `path srd 3.5 foundry` | Later rulebooks, Occult, Unchained classes |
| Starfinder | `star srd 3.5` | Simpler stat blocks, universal creature rules, stamina/resolve |
| Modern SRD | `modern srd 3.5` | Generic classes, defense bonus, non-fantasy content |
| Individual books | `individual books/*` | Arms & Armor, Alchemy & Herbalists, Spells & Magic, Faeries, Encyclopaedia Arcane: Star Magic (mechanics only) |

## How it gets built

- **Start from a complete base.** The whole 3.5 SRD was copied in on 2026-10-15 (everything except the website's `tools` pages). Changes are made to the copy; the processed notes stay as reference.
- **Adjust piecemeal.** Pull in improvements from the other sources one area at a time, starting with what the [[Shared Core]] of the rogue-like and auto-battler needs.
- **Every entry links back.** Each note's `based-on` property names the notes it came from, so the original text is one click away. When an entry changes, set `change: modified` and log it in the [[Changelog]].
- **The copy is a fork.** Later fixes to the processed 3.5 notes don't flow into this folder; apply them here too, or re-copy notes that are still `status: base`.

## Folders

The 3.5 SRD's layout, as copied:

| Folder | What's in it |
| --- | --- |
| `legal` | The OGL with every Section 15 notice, and the sources' Product Identity |
| `rules` | Basics, alignment, races, carrying and movement, environment, traps, treasure, planes, conditions |
| `combat` | Actions, initiative, attacks of opportunity, movement, special attacks, injury and death |
| `classes`, `prestige-classes` | Base, NPC and prestige classes |
| `skills`, `feats` | One note per skill and feat |
| `class-options` | One note per class option (bloodlines, and later rage powers, talents, hexes…), in a folder per kind (added 2026-11-02) |
| `spells`, `powers` | One note per spell and psionic power, plus the class lists |
| `equipment`, `magic-items` | Weapons, armor, gear, materials; one note per magic item in type folders |
| `monsters` | One note per creature, with group folders (angel, demon, dragon, ghoul…) |
| `psionics`, `epic`, `divine` | The psionic, epic and divine rules, classes and items |
| `unearthed-arcana` | Optional and variant rules |
| `images` | Diagrams used by the facing and hex grid rules |
| `actions` | One note per action anyone can take, with its action type or how long it takes (added 2026-10-31) |

Each folder has an Index base.

## Properties

Every copied note keeps the SRD's own properties (`srd-type`, `school`, `level`, `hit-dice`…) and adds:

```yaml
based-on:                  # links to the notes it came from
  - "[[fantasy srd 3.5/feats/Power Attack|Power Attack (3.5)]]"
status: base               # base (unchanged copy), draft, playtest, settled
change: copied             # copied, modified, new
pi-review: scanned 2026-10-15   # scanned (scanner clean, not read), flagged (see pi-flags), or a date (reviewed in full)
tags: [rangoric, rangoric/feat]
```

Notes that pull from more than one source list each one under `based-on`, and can add `games: [rogue-like, auto-battler]`.

Topic tags go in the same `tags` list, lowercase and with no prefix, such as `core`, `background`, `knowledge` and `magic` on skills. Rule text capitalizes them ("Knowledge skills", "a Magic skill check"). The [[Tag Register]] lists every tag, the note that defines it and how many notes carry it.

## Decisions to make

- [x] Changed content: edit the copied note in place; `based-on` links to the original and the [[Changelog]] records the change
- [ ] Resolve the 11 notes with `pi-review: flagged` (their `pi-flags` property says why)
- [ ] Do feats, class features, talents and Starfinder theme features become one `talents` pool?
- [ ] Do spells, psionic powers and monster special attacks become one `abilities` format?
- [x] Races and creature types: one `ancestries` folder, or separate? Separate: races in `races`, creature types in `monsters` (2026-11-09)
- [ ] Which edition's numbers win by default when sources differ (3.5 or PF1)?

## Related

- [[Changelog]]: departures from the SRD, one line each
- [[Game Plans]]: what each game needs from this
- [[rangoric-srd/legal/Legal|Legal]]: the OGL with every source's Section 15 notice; include it with anything published

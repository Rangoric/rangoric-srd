---
srd-type: "spell"
section: "Spells"
school: "Divination"
level:
  - "Med 2"
  - "Mes 3"
  - "Occ 2"
  - "Psy 3"
  - "Spi 3"
components:
  - "V"
  - "S"
casting-time: "1 standard action"
range: "Close (25 ft. + 5 ft./2 levels)"
target: "One creature or object"
duration: "Concentration, up to 1 round/level"
defense: "None"
spell-resistance: "No"
book: "Occult Adventures"
based-on:
  - "[[path srd 3.5 foundry/spells/Analyze Aura|Analyze Aura (PF1 Foundry)]]"
status: draft
change: new
pi-review: 2026-11-16
tags: [rangoric, rangoric/spell]
---

# Analyze Aura

_Divination_

- **Level**: Med 2, Mes 3, Occ 2, Psy 3, Spi 3
- **Components**: V, S
- **Casting Time**: 1 standard action
- **Range**: Close (25 ft. + 5 ft./2 levels)
- **Target**: One creature or object
- **Duration**: Concentration, up to 1 round/level
- **Defense**: None
- **Spell Resistance**: No

You peer into the aura of one target creature or object, gaining valuable information about its condition and nature. Each round, choose one of the target's four [[rangoric-srd/rules/Auras|auras]]. This spell functions similarly to the [[rangoric-srd/skills/Perception#Read Aura|read aura]] occult skill unlock, but doesn't require checks and returns results on all the target's auras in an instant.

**Alignment Aura**: You study the target's spiritual nature to determine its alignment. You also learn the type and power of its alignment aura, as _[[rangoric-srd/spells/Detect Evil|detect evil]]_.

**Emotion Aura**: The colors playing within the target's aura reveal its emotional state, granting valuable insight into its psyche. You learn a general summary of the target's current disposition, as well as its attitude toward any other creatures within 30 feet of it. For the duration of the spell and for 1 hour afterward, you gain a +2 circumstance bonus on [[rangoric-srd/skills/Deception|Deception]], [[rangoric-srd/skills/Persuasion|Persuasion]], [[rangoric-srd/skills/Intimidation|Intimidation]], and [[rangoric-srd/skills/Sense Motive|Sense Motive]] checks you attempt against the target. Objects do not have emotion auras, except intelligent weapons and similar sentient oddities.

**Health Aura**: The flow of vital force animating the target becomes plainly visible, giving you insight into its physical condition. You know whether the target is unharmed or wounded, whether it is poisoned or diseased, and whether it is under any of the following conditions: confused, disabled, dying, nauseated, panicked, staggered, stunned, or unconscious. Further, your insight into the overall strength of the target's vital force reveals the total number of points available in its ki pool, grit pool, or similar resource. Objects and most undead creatures don't have health auras.

**Magic Aura**: You determine the number and power of all magical auras on the target (as _[[rangoric-srd/spells/Detect Magic|detect magic]]_ to determine a _[[rangoric-srd/spells/Magic Aura|magic aura]]_'s power), as well as the school of each aura. You can attempt [[rangoric-srd/skills/Mysticism|Mysticism]] checks to determine the school or identify properties of a magic item, as normal. If cast on an item, _analyze aura_ cuts through the obfuscation of the _[[rangoric-srd/spells/Magic Aura|magic aura]]_ spell.

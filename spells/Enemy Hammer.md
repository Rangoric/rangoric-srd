---
srd-type: "spell"
section: "Spells"
school: "Transmutation"
level:
  - "Occ 6"
  - "Psy 6"
  - "Sor/Wiz 6"
  - "Spi 6"
components:
  - "V"
  - "S"
  - "M"
casting-time: "1 standard action"
range: "Long (400 ft. + 40 ft./level)"
target: "One creature"
duration: "1 round/level (D)"
defense: "Fortitude partial"
spell-resistance: "Yes"
book: "Advanced Player's Guide"
based-on:
  - "[[path srd 3.5/spells/Enemy Hammer|Enemy Hammer (PF1)]]"
status: draft
change: new
pi-review: 2026-11-06
tags: [rangoric, rangoric/spell]
---

# Enemy Hammer

_Transmutation_

- **Level**: Occ 6, Psy 6, Sor/Wiz 6, Spi 6
- **Components**: V, S, M (puppet strings)
- **Casting Time**: 1 standard action
- **Range**: Long (400 ft. + 40 ft./level)
- **Target**: One creature
- **Duration**: 1 round/level (D)
- **Defense**: Fortitude partial
- **Spell Resistance**: Yes

You grab a creature with telekinesis and use it to batter nearby opponents or objects. You must target a specific creature when casting this spell and once you select that creature you cannot switch to another. Each round, as a standard action, you can attempt to hurl the target at any creature or object within 30 feet of it. You must make an attack roll whenever you use the target as a weapon. The attack bonus for this attack is equal to your caster level plus either your Intelligence or Charisma modifier (whichever is higher). If you successfully hit the new target with the creature both it and the creature take damage based on the creature's size.

## Table: Enemy Hammer: Creature Size/Damage Dealt

| Creature Size | Damage Dealt |
| ------------- | ------------ |
| Fine          | 1d4          |
| Diminutive    | 1d6          |
| Tiny          | 1d8          |
| Small         | 1d10         |
| Medium        | 2d6          |
| Large         | 2d8          |
| Huge          | 2d10         |
| Gargantuan    | 3d6          |
| Colossal      | 3d8          |

The spell attacks the target creature’s Fortitude each time you attempt to use it as a weapon. On a miss it can act normally, but on a hit it loses all actions for the round and ends its turn prone in a square adjacent to the target of your attack. However, if the creature chooses to resist your efforts to move it, taking no other actions for the round, it gets a +4 circumstance bonus to its Fortitude Defense against the spell. The spell ends immediately if the target creature dies or is destroyed.

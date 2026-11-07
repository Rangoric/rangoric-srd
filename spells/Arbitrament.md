---
srd-type: "spell"
section: "Spells"
school: "Evocation"
descriptor:
  - "Sonic"
level:
  - "Clr 7"
components:
  - "V"
casting-time: "1 standard action"
range: "40 ft."
target: "Non-neutral creatures in a 40-ft.-radius spread centered on you"
duration: "Instantaneous"
saving-throw: "Will partial, see text"
spell-resistance: "Yes"
book: "Planar Adventures"
based-on:
  - "[[path srd 3.5 foundry/spells/Arbitrament|Arbitrament (PF1 F)]]"
status: draft
change: new
pi-review: 2026-11-06
tags: [rangoric, rangoric/spell]
---

# Arbitrament

*Evocation \[Sonic\]*

  - **Level**: Clr 7
  - **Components**: V
  - **Casting Time**: 1 standard action
  - **Range**: 40 ft.
  - **Target**: Non-neutral creatures in a 40-ft.-radius spread centered on you
  - **Duration**: Instantaneous
  - **Saving Throw**: Will partial, see text
  - **Spell Resistance**: Yes

All chaotic evil, chaotic good, lawful evil, and lawful good creatures within the area of this spell suffer the following conditions, based on their Hit Dice.

| Hit Dice                | Effect                                 |
|-------------------------|----------------------------------------|
| Equal to caster level   | Sickened                               |
| Up to caster level - 1  | Sickened, staggered                    |
| Up to caster level - 5  | Nauseated, sickened, staggered         |
| Up to caster level - 10 | Killed, nauseated, sickened, staggered |

The effects are concurrent. A creature can attempt a Will save to reduce or negate the effects. If subject to multiple effects, the creature rolls once and applies the result to each effect.  
**Sickened**: The creature is sickened for 1d4 rounds (Will negates).  
**Staggered**: The creature is staggered for 2d4 rounds, or for 1d4 rounds on a successful Will save.  
**Nauseated**: The creature is nauseated for 1d10 minutes, or for 1d4 rounds on a successful Will save.  
**Killed**: Living creatures die, and undead creatures are destroyed. On a successful Will save, the creature instead takes 3d6 points of damage + 1 point per caster level (maximum +25). Furthermore, if you are on your home plane when you cast this spell, all chaotic evil, chaotic good, lawful evil, and lawful good extraplanar creatures within the area are banished to their home planes (Will negates, at a -4 penalty). Creatures so banished cannot return for at least 24 hours. This effect takes place regardless of whether the creatures hear the *arbitrament*. Creatures whose Hit Dice exceed your caster level are unaffected by *arbitrament*.

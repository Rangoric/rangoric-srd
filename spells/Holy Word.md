---
srd-type: "spell"
section: "Spells"
school: "Evocation"
descriptor:
  - "Good"
  - "Sonic"
level:
  - "Clr 7"
  - "Good 7"
components:
  - "V"
casting-time: "1 standard action"
range: "40 ft."
area: "Nongood creatures in a 40-ft.-radius spread centered on you"
duration: "Instantaneous"
saving-throw: "None or Will negates; see text"
spell-resistance: "Yes"
based-on:
  - "[[fantasy srd 3.5/spells/Holy Word|Holy Word (3.5)]]"
status: base
change: copied
pi-review: scanned 2026-10-15
tags: [rangoric, rangoric/spell]
---

# Holy Word

*Evocation \[Good, Sonic\]*

  - **Level**: Clr 7, Good 7
  - **Components**: V
  - **Casting Time**: 1 standard action
  - **Range**: 40 ft.
  - **Area**: Nongood creatures in a 40-ft.-radius spread centered on you
  - **Duration**: Instantaneous
  - **Saving Throw**: None or Will negates; see text
  - **Spell Resistance**: Yes

Any nongood creature within the area that hears the holy word suffers the following ill effects.

| HD                     | Effect                                                                                              |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| Equal to caster level  | [[rangoric-srd/rules/Special Abilities and Conditions#^deafened\|Deafened]]                      |
| Up to caster level -1  | [[rangoric-srd/rules/Special Abilities and Conditions#^blinded\|Blinded]], deafened              |
| Up to caster level -5  | [[rangoric-srd/rules/Special Abilities and Conditions#^paralyzed\|Paralyzed]], blinded, deafened |
| Up to caster level -10 | Killed, paralyzed, blinded, deafened                                                                |

The effects are cumulative and concurrent. No saving throw is allowed against these effects.

*Deafened*: The creature is deafened for 1d4 rounds.

*Blinded*: The creature is blinded for 2d4 rounds.

*Paralyzed*: The creature is paralyzed and [[rangoric-srd/rules/Special Abilities and Conditions#^helpless|helpless]] for 1d10 minutes.

*Killed*: Living creatures die. Undead creatures are destroyed.

Furthermore, if you are on your home plane when you cast this spell, nongood extraplanar creatures within the area are instantly banished back to their home planes. Creatures so banished cannot return for at least 24 hours. This effect takes place regardless of whether the creatures hear the holy word. The banishment effect allows a Will save (at a –4 penalty) to negate.

Creatures whose HD exceed your caster level are unaffected by holy word.

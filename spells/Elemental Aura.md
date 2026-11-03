---
srd-type: "spell"
section: "Spells"
school: "Evocation"
descriptor:
  - "Acid"
  - "Cold"
  - "Electricity"
  - "Fire"
level:
  - "Sor/Wiz 3"
components:
  - "V"
  - "S"
casting-time: "1 standard action"
range: "Personal"
target: "You"
duration: "1 round/level (D)"
saving-throw: "Reflex half; see text"
spell-resistance: "Yes"
based-on:
  - "[[path srd 3.5/spells/Elemental Aura|Elemental Aura (PF1)]]"
status: draft
change: new
pi-review: 2026-11-02
tags: [rangoric, rangoric/spell]
---

# Elemental Aura

*Evocation \[Acid, Cold, Electricity, Fire\]*

  - **Level**: Sor/Wiz 3
  - **Components**: V, S
  - **Casting Time**: 1 standard action
  - **Range**: Personal
  - **Target**: You
  - **Duration**: 1 round/level (D)
  - **Saving Throw**: Reflex half; see text
  - **Spell Resistance**: Yes

This spell forms an aura of energy around you, damaging all those that come near you. Choose an energy type: acid, cold, electricity, or fire. Creatures adjacent to you when this spell is cast and at the start of your turn take 2d6 points of energy damage of the selected type. This aura has an additional effect, depending upon the type of energy chosen.

**Acid**: Creatures affected by your aura take 1 point of ongoing acid damage per round for 1 round per three caster levels, and are sickened for the duration of the ongoing acid damage.

**Cold**: Creatures affected by your aura are fatigued. A creature that is already fatigued suffers no additional effect.

**Electricity**: Creatures affected by your aura are staggered for 1 round.

## Fire

Creatures affected by your aura catch on fire (see [[rangoric-srd/rules/Wilderness, Weather, and Environment#Catching on Fire|catching on fire]]).

Creatures adjacent to you are allowed a Reflex save to halve the damage and negate the additional effect. The aura's additional effects do not stack if a creature takes damage from your aura multiple times. You may only have one *elemental aura* in effect at one time. When you cast this spell to deal acid, cold, electricity, or fire damage, it is a spell of that type.

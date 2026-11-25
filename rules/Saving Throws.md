---
srd-type: "rule"
section: "Rules"
based-on:
  - "[[path srd 3.5/rules/pathfinder-unchained/Unchained Classes#Fractional Base Bonuses|Unchained Classes (PF1 Unchained)]]"
status: draft
change: new
pi-review: 2026-11-25
tags: [rangoric, rangoric/rule]
---

# Saving Throws

Instead of being a defense, we are going to change it to an attack like an attack roll.

So Saves start at 10+Modifier: whoever makes the attack rolls against 10 + the target's ability modifier + the target's save bonus. Once someone has a save marked as 'Good' it gets a plus 2, the first time any of their classes, prestige classes included, makes that save good; a later class that makes it good again doesn't add another. Then they advance as follows.

Each class names its saves in its Saving Throws line and its `fort`, `ref` and `will` properties.

Good save is +1/2 level.
Poor save is +1/3 level.

Fractions for the same save add together across all of a character's classes and prestige classes, good and poor alike, and the total is rounded down only at the end, as with [[rangoric-srd/rules/Base Attack Bonus|Base Attack Bonus]].

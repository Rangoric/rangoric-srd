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

Instead of the target rolling a save, whoever makes the effect rolls an attack against the target’s defense, like an attack roll against Armor Class.

So each save is a defense: Fortitude Defense, Reflex Defense and Will Defense. A defense is 10 + Modifier: whoever makes the attack rolls against 10 + the target's ability modifier + the target's save bonus, and hits when the roll meets or beats it. Once someone has a save marked as 'Good' it gets a plus 2, the first time any of their classes, prestige classes included, makes that save good; a later class that makes it good again doesn't add another. Then they advance as follows.

Each class names its saves in its Saving Throws line and its `fort`, `ref` and `will` properties.

Good save is +1/2 level.
Poor save is +1/3 level.

Fractions for the same save add together across all of a character's classes and prestige classes, good and poor alike, and the total is rounded down only at the end, as with [[rangoric-srd/rules/Base Attack Bonus|Base Attack Bonus]].

## Defenses

_Fortitude Defense_: It measures your ability to stand up to physical punishment or attacks against your vitality and health. Apply your Constitution modifier to it.

_Reflex Defense_: It tests your ability to dodge area attacks. Apply your Dexterity modifier to it.

_Will Defense_: It reflects your resistance to mental influence as well as many magical effects. Apply your Wisdom modifier to it.

Just like with saves, leaving off “Defense” is a normal shortcut where it reads clearly: “+7 vs Fortitude”, “the spell attacks its Will”. A bonus or penalty on a save is a bonus or penalty on that defense: “+2 on Will Defense”, “+2 on all defenses”.

## Attacking a Defense

Whoever makes the effect (a caster, a monster, a trap, a poison) rolls the attack: 1d20 + the effect’s attack bonus against the target’s defense. The GM rolls for a monster, trap or hazard. Something that isn’t anyone is still the attacker: a trap has an attack roll, and a poison attacks the target’s Fortitude Defense.

**Attack Bonus**: An effect’s attack bonus is written “+n”.

- A spell or power: its level + the caster’s casting ability modifier, plus anything that adds to it, such as Spell Focus ([[rangoric-srd/spells/Magic Overview#Defense|Magic Overview]]).
- A monster’s special ability: 1/2 the creature’s racial Hit Dice + the ability modifier it is based on ([[rangoric-srd/monsters/Monsters#Special Attacks and Special Qualities|Monsters]]).
- Anything else, such as a trap, a poison or an item: the bonus it gives.

An effect still written with a save DC has an attack bonus of the DC − 10: DC 17 is +7.

**Hits and Misses**: When the attack meets or beats the defense, the target fails its save and the effect happens in full. When the attack misses, the target defends against it: it is unaffected, or takes the lesser effect the effect names, such as half damage.

**No Automatic Results**: A natural 1 or a natural 20 on an attack against a defense is not an automatic miss or hit. Natural 1 and 20 matter only on attack rolls against Armor Class.

**Repeated Attacks**: An effect that allowed a new save each round, each day or at some other frequency attacks again each time, and the target is free of it when an attack misses, unless the effect says otherwise. “N consecutive saves” is “N consecutive misses”.

**Rerolls**: A target that could reroll a save makes the attacker reroll that attack instead, and keeps the result better for itself. This is **disadvantage** on the attack: the attacker rolls twice and takes the worse result. An ability that lets a target roll a save twice and take the better result gives the attacker disadvantage the same way. Rerolls stack: each source the target has adds one more roll, and the target keeps the best result for itself. An effect that gives a target a second save (such as another one the next round) gives the effect a second attack, which it must also hit.

**Voluntarily Lowering a Defense**: A creature can voluntarily lower a defense and willingly accept an effect’s result, as with a spell or power noted as harmless.

**Items Harmed**: When an attack that can harm objects beats a creature’s defense by 10 or more, an exposed item is harmed, as [[rangoric-srd/spells/Magic Overview#Defense|Items Surviving after a Saving Throw]] says.

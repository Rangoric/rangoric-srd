---
srd-type: "monster"
section: "Monsters"
group: "[[rangoric-srd/monsters/zombie/Zombie|Zombie]]"
book: "Bestiary"
based-on:
  - "[[path srd 3.5 foundry/monster-templates/Zombie|Zombie (PF1 Foundry)]]"
  - "[[path srd 3.5/monsters/Human Zombie|Human Zombie (PF1)]]"
  - "[[path srd 3.5 foundry/template-abilities/Staggered (Template Ability)|Staggered (Template Ability) (PF1 Foundry)]]"
status: draft
change: new
pi-review: 2026-11-23
tags: [rangoric, rangoric/monster]
---

# Alternate Zombie

Zombies are the animated corpses of dead creatures, forced into foul unlife via necromantic magic like _[[rangoric-srd/spells/Animate Dead|animate dead]]_. While the most commonly encountered zombies are slow and tough, others possess a variety of traits, allowing them to spread disease or move with increased speed.

Zombies are unthinking automatons, and can do little more than follow orders. When left unattended, zombies tend to mill about in search of living creatures to slaughter and devour. Zombies attack until destroyed, having no regard for their own safety.

Although capable of following orders, zombies are more often unleashed into an area with no command other than to kill living creatures. As a result, zombies are often encountered in packs, wandering around places the living frequent, looking for victims. Most zombies are created using _[[rangoric-srd/spells/Animate Dead|animate dead]]_. Such zombies are always of the standard type, unless the creator also casts _[[rangoric-srd/spells/Haste|haste]]_ or _[[rangoric-srd/spells/Remove Paralysis|remove paralysis]]_ to create fast zombies, or _[[rangoric-srd/spells/Contagion|contagion]]_ to create plague zombies.

This is the second version of the zombie template; the first is [[rangoric-srd/monsters/zombie/Zombie|Zombie]]. Its sample is the [[rangoric-srd/monsters/zombie/Human Zombie|human zombie]].

### Creating a Zombie

“Zombie” is an acquired template that can be added to any corporeal creature (other than an undead), referred to hereafter as the base creature.

**Challenge Rating**: This depends on the creature’s new total number of Hit Dice, as follows:

| HD    | CR  |
| ----- | --- |
| 1/2   | 1/8 |
| 1     | 1/4 |
| 2     | 1/2 |
| 3–4   | 1   |
| 5–6   | 2   |
| 7–8   | 3   |
| 9–10  | 4   |
| 11–12 | 5   |
| 13–16 | 6   |
| 17–20 | 7   |
| 21–24 | 8   |
| 25–28 | 9   |

**Alignment**: Always neutral evil.

**Type**: The creature’s type changes to [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities#^undead|undead]]. It retains any subtype except for alignment subtypes (such as good) and subtypes that indicate kind. It does not gain the augmented subtype. It uses all the base creature’s statistics and special abilities except as noted here.

**Armor Class**: Natural armor is based on the zombie’s size:

| Zombie Size     | Natural Armor Bonus |
| --------------- | ------------------- |
| Tiny or smaller | +0                  |
| Small           | +1                  |
| Medium          | +2                  |
| Large           | +3                  |
| Huge            | +4                  |
| Gargantuan      | +7                  |
| Colossal        | +11                 |

**Hit Dice**: Drop HD gained from class levels (minimum of 1) and change racial HD to d8s. Zombies gain a number of additional HD as noted on the following table.

| Zombie Size     | Bonus Hit Dice |
| --------------- | -------------- |
| Tiny or smaller | —              |
| Small or Medium | +1 HD          |
| Large           | +2 HD          |
| Huge            | +4 HD          |
| Gargantuan      | +6 HD          |
| Colossal        | +10 HD         |

Zombies use their Charisma modifiers to determine bonus hit points (instead of Constitution).

**Defenses**: Base save bonuses are Fort 11/3 HD, Ref 11/3 HD, and Will 11/2 HD + 2.

**Defensive Abilities**: Zombies lose their defensive abilities and gain all of the qualities and immunities granted by the undead type ([[rangoric-srd/monsters/abilities/Undead Traits|undead traits]]). Zombies gain [[rangoric-srd/monsters/abilities/Damage Reduction|DR]] 5/slashing.

**Speed**: Winged zombies can still fly, but maneuverability drops to clumsy. If the base creature flew magically, so can the zombie. Retain all other movement types.

**Attacks**: A zombie retains all the natural weapons, manufactured weapon attacks, and weapon proficiencies of the base creature. It also gains a slam attack that deals damage based on the zombie’s size, but as if it were one size category larger than its actual size (see [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities#^natural-weapons|Natural Attacks by Size]]).

**Special Attacks**: A zombie retains none of the base creature’s special attacks.

**Abilities**: Str +2, Dex –2. A zombie has no Con or Int score, and its Wis and Cha become 10.

**BAB**: A zombie’s base attack is equal to 3/4 its Hit Dice.

**Skills**: A zombie has no skill ranks.

**Feats**: A zombie loses all feats possessed by the base creature, and does not gain feats as its Hit Dice increase, but it does gain [[rangoric-srd/feats/Toughness|Toughness]] as a bonus feat.

**Special Qualities**: A zombie loses most special qualities of the base creature. It retains any extraordinary special qualities that improve its melee or ranged attacks. A zombie gains the following special quality.

**Staggered (Ex)**: Zombies have poor reflexes and can only perform a single move action or standard action each round. A zombie can move up to its speed and attack in the same round as a [[rangoric-srd/combat/Combat Special Attacks#Charge|charge]] action.

### Variant Zombies

The typical zombie is a slow-moving abomination that is tough to destroy. Yet this tough zombie is not the only type of zombie to plague crypts or stalk graveyards. Each of the following two variant zombies modifies the base zombie in a few simple ways.

#### Fast Zombie

Unlike the standard, plodding zombie, a fast zombie moves with a supernatural quickness.

**Speed**: Increase the base creature’s land speed by 10 feet.

**Defensive Abilities**: A fast zombie does not gain DR 5/slashing.

**Special Attacks**: A fast zombie gains the following special attack.

**Quick Strikes (Ex)**: Whenever a fast zombie takes a full-attack action, it can make one additional slam attack at its highest base attack bonus.

**Abilities**: As a standard zombie, except its Dexterity is increased by 2 instead of reduced by 2.

**Special Qualities**: A fast zombie does not gain the staggered special quality.

#### Plague Zombie

These zombies carry a terrible disease that perpetuates their undead lineage—those infected by a plague zombie’s contagion rise as zombies themselves when they perish.

**Defensive Abilities**: A plague zombie does not gain DR 5/slashing.

**Special Attacks**: A plague zombie gains the following special attacks.

**[[rangoric-srd/monsters/abilities/Death Burst|Death Burst]] (Ex)**: When a plague zombie dies, it explodes in a burst of decay. All creatures adjacent to the plague zombie are exposed to its plague as if struck by a slam attack, and the plague attacks their Fortitude, and on a hit they contract zombie rot.

**[[rangoric-srd/monsters/abilities/Disease|Disease]] (Su)**: The slam attack—as well as any other natural attacks—of a plague zombie carries the zombie rot disease.

[[rangoric-srd/rules/afflictions/Zombie Rot|Zombie rot]]: slam; _save_ Fort DC = 10 + 1/2 the zombie’s Hit Dice + the zombie’s Cha modifier; _onset_ 1d4 days; _frequency_ 1/day; _effect_ 1d2 Con, this damage cannot be healed while the creature is infected; _cure_ 2 consecutive misses. Anyone who dies while infected rises as a plague zombie in 2d6 hours.

---
srd-type: "overview"
section: "Unearthed Arcana"
based-on:
  - "[[fantasy srd 3.5/unearthed-arcana/Defence Variants|Defence Variants (3.5)]]"
status: draft
change: modified
pi-review: 2026-10-15
tags: [rangoric, rangoric/overview]
---

## Unearthed Arcana

### Armor as Damage Reduction

In the abstract d20 combat system, a character’s armor defends him by reducing the chance that an attack will deal damage. That system simplifies the realities of battle in order to streamline combat resolution. An attack that fails due to a character’s armor or natural armor doesn’t really fail to connect, but rather fails to connect with enough force to deal any damage. (That’s why touch attacks ignore a character’s armor and natural armor — the touch attack only needs to connect to deliver its effect, and need not actually breach the target’s armor.)

If you’re willing to add a layer of complexity to your combats, consider this variant. In this system, armor reduces the amount of damage dealt by an attack instead of merely turning would-be hits into misses. Armor still prevents some hits outright, but also reduces the deadliness of attacks that do connect. In essence, the system "gives up" some of armor’s ability to turn hits into misses in exchange for a small reduction in damage dealt by any given attack.

##### Armor Damage Reduction Values

In this system, armor offers two benefits against attacks: a minor bonus to AC, which functions just like the armor bonus in the standard d20 rules but is usually lower in value; and [[rangoric-srd/rules/Special Abilities and Conditions#Damage Reduction|damage reduction]]. See [[rangoric-srd/unearthed-arcana/Defence Variants|Table: Armor and Damage Reduction]] for the armor bonus and DR values for common armor types. (All other armor statistics, such as maximum Dexterity bonus, armor check penalty, and arcane spell failure chance, are unchanged.)

For armors not covered on [[rangoric-srd/unearthed-arcana/Defence Variants|Table: Armor and Damage Reduction]], you can determine the new armor values and damage reduction based on the standard armor bonus. To determine the armor’s damage reduction, divide the armor’s normal armor bonus by 2 (rounding down). To determine the armor’s new armor bonus, subtract the DR from the normal armor bonus. For example, studded leather has a normal armor bonus of +3. That gives it a DR of 1/- (half of 3, rounded down) and a new armor bonus of +2 (3 minus 1).

**Table: Armor and Damage Reduction**

| Armor           | Armor Bonus (1) | Damage Reduction |
| --------------- | --------------- | ---------------- |
| Light armor     |                 |                  |
| Padded          | +1             | none             |
| Leather         | +1             | 1/-              |
| Studded leather | +2             | 1/-              |
| Chain shirt     | +2             | 2/-              |
| Medium armor    |                 |                  |
| Hide            | +2             | 1/-              |
| Scale mail      | +2             | 2/-              |
| Chainmail       | +3             | 2/-              |
| Breastplate     | +3             | 2/-              |
| Heavy armor     |                 |                  |
| Splint mail     | +3             | 3/-              |
| Banded mail     | +3             | 3/-              |
| Half-plate      | +4             | 3/-              |
| Full plate      | +4             | 4/-              |

1.  Add any enhancement bonus to this value.

##### Magic Armor

An armor’s enhancement bonus (if any) increases its armor bonus to AC, but has no effect on the armor’s damage reduction. A +3 chain shirt, for example, adds +5 to AC and grants damage reduction 2/-.

##### Stacking Damage Reduction

The [[rangoric-srd/rules/Special Abilities and Conditions#Damage Reduction|damage reduction]] granted by armor stacks with other damage reduction of the same type (that is, damage reduction that has a dash after the number). A 7th-level barbarian wearing a breastplate has DR 3/- (1/- from his class levels and 2/- from his armor). A fighter wearing full plate armor who is the target of a [[rangoric-srd/spells/Stoneskin|stoneskin]] spell, however, has DR 4/- from the armor and 10/adamantine from the spell.

##### Shields

Shields function normally in this variant, granting their full shield bonus to AC. Unlike with armor, a shield’s effectiveness is measured wholly by its ability to keep an attack from connecting with your body.

##### Natural Armor

A creature’s natural armor also provides a modicum of [[rangoric-srd/rules/Special Abilities and Conditions#Damage Reduction|damage reduction]]. Divide the monster’s natural armor bonus (not including any enhancement bonus) by 5 to determine the monster’s damage reduction. The same value is subtracted from the monster’s natural armor bonus to find the monster’s new AC. These calculations are summarized in [[rangoric-srd/unearthed-arcana/Defence Variants|Table: Natural Armor and Damage Reduction]].

If the creature already has damage reduction, either add the value gained from natural armor (if the existing damage reduction is of the same type) or treat it as a separate DR value (if it is of a different type).

For example, a [[rangoric-srd/monsters/Mummy|mummy]] normally has a natural armor bonus of +10. This gives it DR 2/-, and its natural armor bonus is reduced by 2 points to +8 (making it’s AC 18). Since the mummy already has DR 5/- as a special quality, its total damage reduction becomes DR 7/-.

A mature adult [[rangoric-srd/monsters/chromatic-dragons/Red Dragon|red dragon]] has a natural armor bonus of +24. This gives it DR 4/-, and its natural armor bonus is reduced by 4 points to +20 (making its AC 28). The dragon’s existing damage reduction is 10/magic, so the two damage reduction values remain separate.

Finally, a [[rangoric-srd/monsters/giant/Frost Giant|frost giant]] has a +9 natural armor bonus, so it gains DR 1/- from natural armor. The chain shirt it wears gives it an additional DR 2/-. If the frost giant were a 7th-level barbarian, the barbarian class levels would give it DR 1/-. These three values add up to DR 4/-. The giant’s AC would be 20 (10, +8 natural armor bonus, +2 chain shirt).

**Table: Natural Armor and Damage Reduction**

| Natural Armor Bonus | Damage Reduction | Subtract from Natural Armor |
| ------------------- | ---------------- | --------------------------- |
| 0-4                 | none             | 0                           |
| 5-9                 | 1/-              | 1                           |
| 10-14               | 2/-              | 2                           |
| 15-19               | 3/-              | 3                           |
| 20-24               | 4/-              | 4                           |
| 25-29               | 5/-              | 5                           |
| 30-34               | 6/-              | 6                           |
| 35-39               | 7/-              | 7                           |
| 40-44               | 8/-              | 8                           |

##### Behind the Curtain: Armor as DR

It’s pretty easy to see the effect of this variant system: attacks hit more often, but do less damage. What does that really mean?

Low-level combat tends to be less dangerous for armored characters. Although their ACs are lower (and thus their chance of being damaged is higher), this is more than offset by the reduced damage suffered by attacks. A typical goblin warrior, for instance, can barely hurt a character wearing splint mail, because the armor’s damage reduction entirely negates the damage dealt by an average hit. Even though the goblin will hit more often, it will likely end up dealing less total damage over the course of a typical battle.

A mid-level fighter in full plate armor must still be cautious when fighting an ogre, but his armor reduces the ogre’s average damage by 25% while only increasing its chance to hit by 20% — a net gain for the fighter.

At higher levels, however, the balance shifts back in favor of monsters that deal large amounts of damage per hit. When facing a Huge earth elemental, a fighter in full plate will be hit 20% more often (due to the 4-point reduction in AC), but his 4 points of damage reduction now only reduces his opponent’s average damage by less than 17%. Advantage: elemental. Thus, high-level characters must be more careful when battling monsters with extreme damage-dealing capability.

##### Combo: Defence Bonus and Damage Reduction

You can combine the [[#Defence Bonus|defense bonus]] variant and the armor as damage reduction variant in a variety of ways to create a more complex system.

Using both systems as written, many characters will wear armor even if the armor bonus provided is lower than the defense bonus gained from class level. Because the character gets the higher of his defense bonus or armor bonus, the character can wear armor and benefit from its damage reduction while relying on his defense bonus for a higher Armor Class.

If that’s not to your liking, you can rule that a character’s armor bonus overrides his defense bonus, even if the defense bonus is higher. This forces characters to make a tough choice between having a high AC and having damage reduction.

### Damage Conversion

In the standard d20 rules, armor reduces the chance of a character taking damage in combat—but that’s the limit of its protection. In this variant, armor not only protects in that manner, but also turns fatal blows into less-threatening hits. Armored characters are often more easily battered into unconsciousness than brought down by lethal damage. It’s a system that works well in campaigns with a great deal of combat between armored foes, but in which magical healing is not common. It’s also ideal in a world where ethical or legal standards dictate that subduing or capturing opponents is preferable to killing them.

##### Armor Damage Conversion

Armor, in addition to adding a bonus to AC, also converts lethal damage from physical attacks into nonlethal damage. (Shields provide a shield bonus to AC, as normal, but do not convert damage.)

Each time an armor-wearing character is struck by an attack that deals lethal damage, the amount of damage dealt to the character is reduced by an amount equal to the armor bonus (including enhancement) of the armor worn. The character takes and equal amount of nonlethal damage. Damage that is not affected by [[rangoric-srd/rules/Special Abilities and Conditions#Damage Reduction|damage reduction]] (energy damage and the like) is not converted.

For example, while wearing +1 full plate (total armor bonus +9), someone is struck by an arrow for 6 points of damage. Since the armor can convert up to 9 points of damage per attack, the entire 6 points is converted from lethal damage to nonlethal damage. Their hit point total remains the same, but he increases his nonlethal damage total by 6 points. Later, a hill giant strikes them for a whopping 22 points of damage. The armor converts 9 points of this damage to nonlethal damage, but the remaining 13 points are deducted from their hit points.

**Nonlethal Damage:** An armor-wearing character can ignore nonlethal damage equal to his armor bonus. (In effect, armor grants [[rangoric-srd/rules/Special Abilities and Conditions#Damage Reduction|damage reduction]] equal to its armor bonus against nonlethal attacks.) ^nonlethal-damage

**Natural Armor:** At your option, you can make natural armor work in the same manner. However, this means that almost no defeated monster is truly dead, which may prove problematic (see [[#Behind the Curtain: Damage Conversion|Behind The Curtain: Damage Conversion]]). This rule also interacts strangely with [[rangoric-srd/rules/Special Abilities and Conditions#Regeneration|regeneration]] — since all damage dealt to a creature with regeneration is treated as nonlethal damage, a regenerating creature with armor or natural armor actually takes less damage than normal when using this system. In case of regenerating creatures, consider eliminating the rule that natural armor works in the same manner. ^natural-armor-and-damage-conversion

##### Behind the Curtain: Damage Conversion

With this system, a character still takes as much damage from a hit as in the normal combat rules. Barring any magical healing delivered during the fight, a battle lasts just as long as in a standard game. Since nonlethal damage goes away faster than lethal damage, though, characters can recuperate from their battles relatively quickly, even without magical healing, making this variant ideal for low-magic campaigns.

However, healing spells become potentially doubly effective, since they heal an equal amount of lethal and nonlethal damage.

Nonlethal attacks become less frightening to armored opponents. A fighter in full plate simply has no fear of unarmed opponents, since they have little chance of injuring him. (Of course, they can still [[rangoric-srd/combat/Combat Maneuvers#Overrun|overrun]], [[rangoric-srd/combat/Combat Maneuvers#Trip|trip]], or [[rangoric-srd/combat/Combat Maneuvers#Grapple|grapple]] him, so he’d be wise to keep and eye on them all the same.)

Another effect is that defeated foes remain alive (and unconscious) unless dispatched after the fight. This can decrease character mortality dramatically — since most characters who fall in battle will be merely unconscious, but not dying — but it also introduces the potentially ugly postcombat scene of the characters feeling it necessary to slit the throats of their unconscious foes. Some characters, particulary paladins or other chivalrous types, may suffer serious moral qualms.

This variant is probably best for campaigns in which it’s acceptable for the bad guys to survive a fight. Perhaps a defeated villain’s honor prevents him from returning to plague the heroes at a later date, or maybe the style of your setting rewards characters for defeating opponents without killing them outright (such as in a swashbuckling campaign). Otherwise, characters may feel that they are punished for refusing to murder unconscious foes with regularity, since those enemies will certainly recover from their injuries and vow vengeance against the PCs. Encounters in the campaign may often involve fighting the same opponents again and again, rather than fighting new monsters and opponents.

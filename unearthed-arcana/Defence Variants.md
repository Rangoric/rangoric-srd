---
srd-type: "overview"
section: "Unearthed Arcana"
based-on:
  - "[[fantasy srd 3.5/unearthed-arcana/Defence Variants|Defence Variants (3.5)]]"
  - "[[individual books/Arms & Armor v3.5/rules/Armor as Damage Reduction|Armor as Damage Reduction (Arms & Armor)]]"
  - "[[individual books/Arms & Armor v3.5/tables/Table 4.7 DR by Armor|Table 4.7: DR by Armor (Arms & Armor)]]"
  - "[[individual books/Arms & Armor v3.5/tables/Table 4.8 Armor Class or Damage Reduction|Table 4.8: Armor Class or Damage Reduction? (Arms & Armor)]]"
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

### Armor as Damage Reduction (Arms & Armor)

A second version of [[#Armor as Damage Reduction|armor as damage reduction]], from *Arms & Armor*. It gives the standard armors the same armor bonus and damage reduction as Table: Armor and Damage Reduction above, adds values for *Arms & Armor*’s armors, and changes how magic armor, critical hits and some weapon qualities work. *Arms & Armor* gives [[rangoric-srd/magic-items/armor/Elven Chain|elven chain]] an armor bonus of +3 and DR 2/–. ^armor-as-dr-arms-and-armor

Encasing one’s body in armor is an important protective measure for an adventurer to embrace. Vorpal, sharpness, and crushing weapons can cause grievous injury with a single swing. The rules presented below serve to augment this protection, providing more incentive to wear armor. Wearing armor gives you both Damage Reduction and Armor Class, as on Table: Arms & Armor’s Armor and Damage Reduction, below.

##### What Kind of DR?

Wearing armor means keeping track of the various kinds of DR that you have. Each one is different, so it’s important to know what kind of attack you’re facing and what sorts of defenses you have against it. Armor DR only stacks if it’s the same types of DR; the DR granted by the barbarian class ability stacks with armor DR, for instance.

Fine and Diminutive creatures automatically ignore DR from armor—there’s just no way to defend against their attacks: They’re able to easily penetrate the folds and joints in the armor to strike home. That means that a human in plate is susceptible to the strike of a grig, a swarm of bees, and other minute hazards.

##### Armor Class or DR?

As adventurers equip themselves for the trials and tribulations that lie ahead of them, questions of what stacks with what and how DR and AC interact are liable to arise. Table: Armor Class or Damage Reduction? provides the specifics on how magic and DR interact.

**Table: Armor Class or Damage Reduction?**

| Type | Example | Effect |
| --- | --- | --- |
| Enchanted armor | *+2 studded leather* | Adds to Armor Class |
| Shield | Heavy steel shield | Adds to Armor Class |
| Bracers (1) | *[[rangoric-srd/magic-items/wondrous-items/Bracers of Armor|bracers of armor]] +10* | Adds to Armor Class |
| Natural armor | *[[rangoric-srd/magic-items/wondrous-items/Amulet of Natural Armor|amulet of natural armor]] +6* | Adds to Armor Class |
| Damage reduction | Barbarian ability | Stacks with armor DR |
| Magic item | *[[rangoric-srd/magic-items/rings/Ring of Ironskin|ring of ironskin]]* | Separate; DR 15/adamantine |
| Spell | *[[rangoric-srd/spells/Mage Armor|mage armor]]* | Adds to Armor Class (2) |

1 *Wearing bracers adds to Armor Class, making a creature tougher to hit but not adding any other bonus that actual armor grants under these rules. Bracers of armor +5 don’t grant the DR that chainmail does, for instance; they only add +5 to Armor Class.*

2 *Spells work (and stack) as they always do; as both bracers of armor and mage armor provide an armor bonus, their effects don’t stack with each other or with wearing armor that grants AC of +4 or better.*

*Example*: A 19th-level barbarian with a base DR of 5/– from his class abilities is wearing *+3 scale mail* and a [[rangoric-srd/magic-items/rings/Ring of Ironskin|ring of ironskin]]. That makes his DR 7/– or 15/adamantine. During the first round of combat, he’s attacked by two fighters wielding adamantine longswords (where he’ll have his DR 7/–) and a rogue wielding a *+4 short sword* (where he’ll have his DR 15/adamantine).

##### Enchanted Armor

The base versions of armor have the same qualities as those on [[rangoric-srd/equipment/Equipment Armor|Table: Armor and Shields]]. Adding enchantments to armor makes it better than its nonmagical counterparts, as detailed below.

**Armor Check Penalties**: These decrease equal to the amount of enchantment placed in the armor. For example, *scale mail +2* would have an armor check penalty of -2 (normally -4). It’s possible to completely remove penalties by highly enchanting armor, but you never receive a bonus for over-enchantment (*scale mail +5* wouldn’t grant a +1 bonus, for instance).

**Maximum Dexterity Adjustment**: This increase is equal to the amount of enchantment placed into the armor. For example, *scale mail +2* has a Maximum Dexterity Adjustment of +5 (normally only +3).

**Arcane Spell Failure**: The maximum reduction allowed is 20% (granted by using both the [[rangoric-srd/magic-items/armor-abilities/Spellcasting|spellcasting]] and [[rangoric-srd/magic-items/armor-abilities/Weightless (Armor Special Ability)|weightless]] armor qualities).

**Speed**: A creature’s speed is normally limited by its race and armor selection, but the armor factor can be negated by adding the *[[rangoric-srd/magic-items/armor-abilities/Weightless (Armor Special Ability)|weightless]]* quality to armor.

**Table: Arms & Armor’s Armor and Damage Reduction**

The standard armors aren’t repeated here; they have the values on Table: Armor and Damage Reduction above.

%% generated: armor damage reduction %%

| Armor                                                                                  | Armor Bonus (1) | Damage Reduction |
| -------------------------------------------------------------------------------------- | --------------- | ---------------- |
| Light armor                                                                            |                 |                  |
| [[rangoric-srd/equipment/armor/Fetish Armor\|Fetish]]                                  | 0               | none             |
| [[rangoric-srd/equipment/armor/Silken Web\|Silken web]]                                | 0               | none             |
| [[rangoric-srd/equipment/armor/Armored Robe\|Armored robe]]                            | +1              | none             |
| [[rangoric-srd/equipment/armor/Soft Leather Half Armor\|Soft leather half armor]]      | +1              | none             |
| [[rangoric-srd/equipment/armor/Quilled Aketon\|Aketon, quilled]]                       | +1              | none             |
| [[rangoric-srd/equipment/armor/Cleric's Vest\|Cleric's vest]]                          | +1              | none             |
| [[rangoric-srd/equipment/armor/Woven Cord Armor\|Woven cord]]                          | +1              | none             |
| [[rangoric-srd/equipment/armor/Holy Vestments\|Holy vestments]]                        | +1              | none             |
| [[rangoric-srd/equipment/armor/Reversible Bardic Doublet\|Doublet, reversible bardic]] | +1              | none             |
| [[rangoric-srd/equipment/armor/Chainmail Corset\|Chainmail corset]]                    | +1              | 1/–              |
| [[rangoric-srd/equipment/armor/Shadow Doublet\|Doublet, shadow]]                       | +1              | none             |
| [[rangoric-srd/equipment/armor/Bishop's Mantle\|Bishop's mantle]]                      | +1              | none             |
| [[rangoric-srd/equipment/armor/Barkskin Armor\|Barkskin]]                              | +1              | 1/–              |
| [[rangoric-srd/equipment/armor/Bardic Armor\|Bardic]]                                  | +1              | 1/–              |
| [[rangoric-srd/equipment/armor/Beaded Armor\|Beaded]]                                  | +1              | 1/–              |
| [[rangoric-srd/equipment/armor/Reinforced Cleric's Robe\|Cleric's robe, reinforced]]   | +1              | 1/–              |
| [[rangoric-srd/equipment/armor/Robe of Yew Leaves\|Robe of yew leaves]]                | +1              | 1/–              |
| [[rangoric-srd/equipment/armor/Fine Leather\|Fine leather]]                            | +1              | 1/–              |
| [[rangoric-srd/equipment/armor/Web Armor\|Web]]                                        | +1              | 1/–              |
| [[rangoric-srd/equipment/armor/Elven Leafweave\|Elven leafweave]]                      | +1              | 1/–              |
| [[rangoric-srd/equipment/armor/Buckskin Armor\|Buckskin]]                              | +2              | 1/–              |
| [[rangoric-srd/equipment/armor/Double Leather\|Double leather]]                        | +2              | 1/–              |
| [[rangoric-srd/equipment/armor/Studded Web\|Studded web]]                              | +2              | 1/–              |
| [[rangoric-srd/equipment/armor/Bone Exoskeleton\|Bone exoskeleton]]                    | +2              | 1/–              |
| [[rangoric-srd/equipment/armor/Plated Leather\|Plated leather]]                        | +2              | 2/–              |
| [[rangoric-srd/equipment/armor/Sap Hide\|Sap hide]]                                    | +2              | 2/–              |
| [[rangoric-srd/equipment/armor/Silver Spiderweave\|Spiderweave, silver]]               | +2              | 2/–              |
| [[rangoric-srd/equipment/armor/Heartwood Shirt\|Heartwood shirt]]                      | +2              | 2/–              |
| Medium armor                                                                           |                 |                  |
| [[rangoric-srd/equipment/armor/Bone Plate\|Bone plate]]                                | +2              | 1/–              |
| [[rangoric-srd/equipment/armor/Clay Armor\|Clay armor]]                                | +2              | 1/–              |
| [[rangoric-srd/equipment/armor/Slat Armor\|Slat armor]]                                | +2              | 1/–              |
| [[rangoric-srd/equipment/armor/Crested Hide Mail\|Hide mail, crested]]                 | +2              | 1/–              |
| [[rangoric-srd/equipment/armor/Fur-Lined Hide Mail\|Hide mail, fur-lined]]             | +2              | 1/–              |
| [[rangoric-srd/equipment/armor/Hauberk\|Hauberk]]                                      | +2              | 1/–              |
| [[rangoric-srd/equipment/armor/Glacier Beast Hide\|Hide, glacier beast]]               | +2              | 1/–              |
| [[rangoric-srd/equipment/armor/Oaken Tree Bark Armor\|Oaken tree bark armor]]          | +2              | 2/–              |
| [[rangoric-srd/equipment/armor/Wooden Plate\|Wooden plate]]                            | +2              | 2/–              |
| [[rangoric-srd/equipment/armor/Scaled Brigandine\|Brigandine, scaled]]                 | +2              | 2/–              |
| [[rangoric-srd/equipment/armor/Sculpted Scale Mail\|Sculpted scale mail]]              | +2              | 2/–              |
| [[rangoric-srd/equipment/armor/Aeroglass Plate\|Aeroglass plate]]                      | +2              | 2/–              |
| [[rangoric-srd/equipment/armor/Woodweave Coat\|Woodweave coat]]                        | +2              | 2/–              |
| [[rangoric-srd/equipment/armor/Bone Mail\|Bone mail]]                                  | +3              | 2/–              |
| [[rangoric-srd/equipment/armor/Ringmail\|Ringmail]]                                    | +3              | 2/–              |
| [[rangoric-srd/equipment/armor/Iron Mantle\|Iron mantle]]                              | +3              | 2/–              |
| [[rangoric-srd/equipment/armor/Shock Shell\|Shock shell]]                              | +3              | 2/–              |
| [[rangoric-srd/equipment/armor/Traveler's Plate\|Traveler's plate]]                    | +3              | 2/–              |
| [[rangoric-srd/equipment/armor/Heraldic Coin Armor\|Heraldic coin armor]]              | +3              | 2/–              |
| [[rangoric-srd/equipment/armor/Rigid Breastplate\|Rigid breastplate]]                  | +3              | 3/–              |
| [[rangoric-srd/equipment/armor/Shalik Plate\|Shalik plate]]                            | +4              | 3/–              |
| Heavy armor                                                                            |                 |                  |
| [[rangoric-srd/equipment/armor/Taskmaster Armor\|Taskmaster armor]]                    | +3              | 3/–              |
| [[rangoric-srd/equipment/armor/Steelwood Splint\|Splint, steelwood]]                   | +3              | 3/–              |
| [[rangoric-srd/equipment/armor/Gemstone Mail\|Morbius mail]]                           | +3              | 3/–              |
| [[rangoric-srd/equipment/armor/Plant Fiber Plate\|Plant fiber plate]]                  | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Articulated Half-Plate\|Articulated half-plate]]        | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Daggered Plate\|Daggered plate]]                        | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Gnarled Mail\|Gnarled mail]]                            | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Blue Bone Mail\|Volt polar mail]]                       | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Lancer's Half-Plate\|Lancer's half-plate]]              | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Armor of the Beetle\|Armor of the beetle]]              | +5              | 4/–              |
| [[rangoric-srd/equipment/armor/Double Plate\|Double plate]]                            | +6              | 6/–              |

1 *Add any enhancement bonus to this value.*

%% end generated %%

##### Critical Hits

Creatures critically hit while wearing armor keep their DR, reducing the amount of damage they suffer.

**Vorpal/Bludgeoning/Piercing Qualities**: Some weapons have the ability to slice or crush the limbs from opponents on a successful hit. Wearing armor now gives the creature a chance to avoid such pitfalls. The chance to avoid this ability is as follows: Creatures struck must make a saving throw using their base armor DR as a bonus against a DC of 15 (some weapons with these qualities have higher DCs). If the save succeeds, the special quality (but not the damage) is negated. If the save is failed, the usual effects occur. Armor can be hardened and made more resistant with armor qualities.

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

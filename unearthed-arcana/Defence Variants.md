---
srd-type: "overview"
section: "Unearthed Arcana"
book: ["Unearthed Arcana", "Arms & Armor v3.5", "Ultimate Combat"]
based-on:
  - "[[fantasy srd 3.5/unearthed-arcana/Defence Variants|Defence Variants (3.5)]]"
  - "[[individual books/Arms & Armor v3.5/rules/Armor as Damage Reduction|Armor as Damage Reduction (Arms & Armor)]]"
  - "[[individual books/Arms & Armor v3.5/tables/Table 4.7 DR by Armor|Table 4.7: DR by Armor (Arms & Armor)]]"
  - "[[individual books/Arms & Armor v3.5/tables/Table 4.8 Armor Class or Damage Reduction|Table 4.8: Armor Class or Damage Reduction? (Arms & Armor)]]"
  - "[[path srd 3.5/rules/ultimate-combat/variant-rules/Armor as Damage Reduction|Armor as Damage Reduction (PF1 UC)]]"
  - "[[path srd 3.5/rules/ultimate-combat/variant-rules/Variant Rules (Variant Rules)|Variant Rules (PF1 UC)]]"
  - "[[path srd 3.5/rules/ultimate-combat/Critical defense DC = critical hit roll + 1-2 attacker's base attack bonus + 1 for each critical feat + 1 for each size category larger attacker is than target|Critical defense DC (PF1 UC)]]"
status: draft
change: modified
pi-review: 2026-10-15
tags: [rangoric, rangoric/overview]
---

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
| Padded          | +1              | none             |
| Leather         | +1              | 1/-              |
| Studded leather | +2              | 1/-              |
| Chain shirt     | +2              | 2/-              |
| Medium armor    |                 |                  |
| Hide            | +2              | 1/-              |
| Scale mail      | +2              | 2/-              |
| Chainmail       | +3              | 2/-              |
| Breastplate     | +3              | 2/-              |
| Heavy armor     |                 |                  |
| Splint mail     | +3              | 3/-              |
| Banded mail     | +3              | 3/-              |
| Half-plate      | +4              | 3/-              |
| Full plate      | +4              | 4/-              |

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

### Armor as Damage Reduction, Second Version

A second version of [[#Armor as Damage Reduction|armor as damage reduction]]. It gives the standard armors the same armor bonus and damage reduction as Table: Armor and Damage Reduction above, adds values for more armors, and changes how magic armor, critical hits and some weapon qualities work. It gives [[rangoric-srd/magic-items/armor/Elven Chain|elven chain]] an armor bonus of +3 and DR 2/–. ^armor-as-dr-arms-and-armor

Encasing one’s body in armor is an important protective measure for an adventurer to embrace. Vorpal, sharpness, and crushing weapons can cause grievous injury with a single swing. The rules presented below serve to augment this protection, providing more incentive to wear armor. Wearing armor gives you both Damage Reduction and Armor Class, as on Table: Second Version Armor and Damage Reduction, below.

##### What Kind of DR?

Wearing armor means keeping track of the various kinds of DR that you have. Each one is different, so it’s important to know what kind of attack you’re facing and what sorts of defenses you have against it. Armor DR only stacks if it’s the same types of DR; the DR granted by the barbarian class ability stacks with armor DR, for instance.

Fine and Diminutive creatures automatically ignore DR from armor—there’s just no way to defend against their attacks: They’re able to easily penetrate the folds and joints in the armor to strike home. That means that a human in plate is susceptible to the strike of a grig, a swarm of bees, and other minute hazards.

##### Armor Class or DR?

As adventurers equip themselves for the trials and tribulations that lie ahead of them, questions of what stacks with what and how DR and AC interact are liable to arise. Table: Armor Class or Damage Reduction? provides the specifics on how magic and DR interact.

**Table: Armor Class or Damage Reduction?**

| Type             | Example                                                                                              | Effect                     |
| ---------------- | ---------------------------------------------------------------------------------------------------- | -------------------------- |
| Enchanted armor  | _+2 studded leather_                                                                                 | Adds to Armor Class        |
| Shield           | Heavy steel shield                                                                                   | Adds to Armor Class        |
| Bracers (1)      | _[[rangoric-srd/magic-items/wondrous-items/Bracers of Armor +1\|bracers of armor]] +10_              | Adds to Armor Class        |
| Natural armor    | _[[rangoric-srd/magic-items/wondrous-items/Amulet of Natural Armor +1\|amulet of natural armor]] +6_ | Adds to Armor Class        |
| Damage reduction | Barbarian ability                                                                                    | Stacks with armor DR       |
| Magic item       | _[[rangoric-srd/magic-items/rings/Ring of Ironskin\|ring of ironskin]]_                              | Separate; DR 15/adamantine |
| Spell            | _[[rangoric-srd/spells/Mage Armor\|mage armor]]_                                                     | Adds to Armor Class (2)    |

1 _Wearing bracers adds to Armor Class, making a creature tougher to hit but not adding any other bonus that actual armor grants under these rules. Bracers of armor +5 don’t grant the DR that chainmail does, for instance; they only add +5 to Armor Class._

2 _Spells work (and stack) as they always do; as both bracers of armor and mage armor provide an armor bonus, their effects don’t stack with each other or with wearing armor that grants AC of +4 or better._

_Example_: A 19th-level barbarian with a base DR of 5/– from his class abilities is wearing _+3 scale mail_ and a [[rangoric-srd/magic-items/rings/Ring of Ironskin|ring of ironskin]]. That makes his DR 7/– or 15/adamantine. During the first round of combat, he’s attacked by two fighters wielding adamantine longswords (where he’ll have his DR 7/–) and a rogue wielding a _+4 short sword_ (where he’ll have his DR 15/adamantine).

##### Enchanted Armor

The base versions of armor have the same qualities as those on [[rangoric-srd/equipment/Equipment Armor|Table: Armor and Shields]]. Adding enchantments to armor makes it better than its nonmagical counterparts, as detailed below.

**Armor Check Penalties**: These decrease equal to the amount of enchantment placed in the armor. For example, _scale mail +2_ would have an armor check penalty of -2 (normally -4). It’s possible to completely remove penalties by highly enchanting armor, but you never receive a bonus for over-enchantment (_scale mail +5_ wouldn’t grant a +1 bonus, for instance).

**Maximum Dexterity Adjustment**: This increase is equal to the amount of enchantment placed into the armor. For example, _scale mail +2_ has a Maximum Dexterity Adjustment of +5 (normally only +3).

**Arcane Spell Failure**: The maximum reduction allowed is 20% (granted by using both the [[rangoric-srd/magic-items/armor-abilities/Spellcasting|spellcasting]] and [[rangoric-srd/magic-items/armor-abilities/Weightless (Armor Special Ability)|weightless]] armor qualities).

**Speed**: A creature’s speed is normally limited by its race and armor selection, but the armor factor can be negated by adding the _[[rangoric-srd/magic-items/armor-abilities/Weightless (Armor Special Ability)|weightless]]_ quality to armor.

**Table: Second Version Armor and Damage Reduction**

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
| [[rangoric-srd/equipment/armor/Gemstone Mail\|Gemstone mail]]                          | +3              | 3/–              |
| [[rangoric-srd/equipment/armor/Plant Fiber Plate\|Plant fiber plate]]                  | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Articulated Half-Plate\|Articulated half-plate]]        | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Daggered Plate\|Daggered plate]]                        | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Gnarled Mail\|Gnarled mail]]                            | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Blue Bone Mail\|Blue bone mail]]                        | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Lancer's Half-Plate\|Lancer's half-plate]]              | +4              | 3/–              |
| [[rangoric-srd/equipment/armor/Armor of the Beetle\|Armor of the beetle]]              | +5              | 4/–              |
| [[rangoric-srd/equipment/armor/Double Plate\|Double plate]]                            | +6              | 6/–              |

1 _Add any enhancement bonus to this value._

%% end generated %%

##### Critical Hits

Creatures critically hit while wearing armor keep their DR, reducing the amount of damage they suffer.

**Vorpal/Bludgeoning/Piercing Qualities**: Some weapons have the ability to slice or crush the limbs from opponents on a successful hit. Wearing armor now gives the creature a chance to avoid such pitfalls. The chance to avoid this ability is as follows: Creatures struck must make a saving throw using their base armor DR as a bonus against a DC of 15 (some weapons with these qualities have higher DCs). If the save succeeds, the special quality (but not the damage) is negated. If the save is failed, the usual effects occur. Armor can be hardened and made more resistant with armor qualities.

### Armor as Damage Reduction, Third Version

As this option significantly revises how the game works, players and GMs should be extremely careful when deciding whether or not to incorporate it into an existing campaign, and should be prepared for an additional layer of complexity and potential slowdowns in gameplay as everyone at the table works on getting up to speed.

This version replaces the rules for Armor Class with a Defense score, so it can't be combined with the [[#Armor as Damage Reduction|first]] or [[#Armor as Damage Reduction, Second Version|second version]] above, or with the defense bonus variant. ^armor-as-dr-third-version

While the armor and Armor Class system presented in the core rules is tried and tested, some players may yet have a sense that it feels slightly off. That is to say, if a suit of armor is actually protecting the wearer from attacks that strike but simply fail to cause the wearer harm, why then do we say that armor reduces the chance of a hit? The abstraction has been clarified in the rules by defining what it means to be “hit” in combat as actually being “hit in such a way as to effectively cause harm,” but this explanation is still not enough for some players.

The following is an alternative system that allows armor to absorb the damage of attacks, rather than a system that provides an abstract way of determining when a hit does actual harm. It is a variant to the base system of the game. It is for GMs who want armor to reduce damage rather than increase Armor Class, and replaces the normal rules for armor.

In this system, a creature no longer has an Armor Class. Instead it has a Defense score that a foe's attack roll must meet or exceed to hit the creature. Then any damage is reduced by [[rangoric-srd/rules/Special Abilities and Conditions#Damage Reduction|damage reduction]] based on the creature's armor worn and any natural armor bonus the creature has. Furthermore, armor has a chance of reducing all critical hits to normal hits, by replacing the confirmation roll for critical hits with a critical defense check made by the creature threatened by the critical hit.

##### Defense

In this alternative system, a creature does not have an Armor Class (AC); it instead has a Defense score. Defense is similar to touch AC in the standard rules, but it also adds the shield bonus (including any enhancement bonus to the shield), and any enhancement bonus to armor.

**Defense = 10 + shield bonus + Dexterity modifier + other modifiers (including armor's enhancement bonus, but not armor bonus or natural armor bonus)**

Defense represents how easy or difficult it is to hit a creature. The shield bonus is added because a creature is considered to be actively blocking attacks with its shield whenever it can, which is whenever it would gain its Dexterity bonus to AC and not be flat-footed.

**Losing Dexterity Bonus to Defense**: Situations or effects that would cause you to lose your Dexterity bonus to AC instead cause you to lose your Dexterity bonus to Defense. Also, whenever you lose your Dexterity bonus to Defense, you also lose any shield bonus to Defense, since when you lose your Dexterity bonus to AC, you also lose the ability to properly respond to attacks with your shield.

**Flat-Footed Defense**: You do not gain your Dexterity or shield bonus to your Defense if you are [[rangoric-srd/rules/Special Abilities and Conditions#^flat-footed|flat-footed]] or lose your Dexterity bonus to Defense; thus, your Flat-Footed Defense is equal to your Defense minus your Dexterity bonus and shield bonus.

**Defense and Using a Shield without Proficiency**: When a creature uses a shield it is not proficient with, it takes that shield's armor check penalty as a penalty to the shield bonus, along with the other penalties for using a shield without proficiency. Furthermore, it also takes this penalty to its Flat-Footed Defense, as the shield actually gets in the way instead of defending against incoming attacks.

##### Armor Bonus as Damage Reduction

Armor in this system keeps all of its normal statistics and qualities, but its armor bonus (including any enhancement bonus added to armor bonus and natural armor bonus) is converted to DR/armor. The DR an armor provides is equal to its total armor bonus with a +1 bonus at 5th level or at 5 Hit Dice, with an increase to that bonus of +1 for every five levels above 5th level, or every 5 Hit Dice over 5 Hit Dice (to a maximum of +4 to DR at 20th level or at 20 or more Hit Dice), provided that the creature wearing the armor is also proficient with the armor.

**Using Armor without Proficiency**: Creatures using armor they are not proficient with do not gain the bonus per level or Hit Dice to the DR, on top of any of the other normal penalties for using armor without proficiency.

**DR/Armor**: This type of DR blocks the damage of all attacks that would normally be affected by DR, based on the composition of the armor (see Table: Armor Composition and DR). Unlike most forms of damage reduction, DR/armor stacks with other types of DR. For instance, when fighting a skeleton with DR 5/bludgeoning and DR 4/armor (+2 for armor, +2 for natural armor), the skeleton's DR/armor reduces 9 points of damage from non-bludgeoning attacks, and 4 damage from bludgeoning weapon attacks. Magic weapons and attacks from Large or larger creatures bypass the DR 4/armor, but not the DR 5/bludgeoning.

**Table: Armor Composition and DR**

| Material             | DR Provided   | Attacker Size to Bypass DR |
| -------------------- | ------------- | -------------------------- |
| Nonmagical armor (1) | DR/magic      | Large                      |
| Magical armor (1)    | DR/adamantine | Huge                       |
| Adamantine armor (1) | DR/—          | Gargantuan                 |

1 _Brilliant energy weapons bypass any DR provided by armor. In addition, DR from armor is halved if a creature is grappled or entangled, and does not apply when a creature is helpless or pinned._

###### Natural Armor Bonus and DR

Like a creature's armor bonus, a natural armor bonus is also converted into damage reduction. If a creature is wearing armor and has a natural armor bonus, the creature adds its armor bonus to its natural armor bonus to determine the amount of DR/armor that it has (see Table: Natural Armor Conversion to DR).

For instance, if a creature wearing a _+2 chain shirt_ has DR 6/armor is then subject to a _[[rangoric-srd/spells/Barkskin|barkskin]]_ spell cast by a 6th-level druid (gaining a +3 natural armor bonus), its DR becomes DR 9/armor for the duration of the spell. This DR is bypassed by adamantine, or the attacks of Huge or larger creatures.

A creature that has both DR from a source other than armor and a natural armor bonus gains the effects of an enhanced form of DR, similar to how the composition of the armor grants special DR/armor defenses (see Table: Armor Composition and DR). If a creature has magical armor, natural armor, and DR, it takes the best form of the special protection provided by both its armor and its mix of DR and natural armor to its DR/armor.

For instance, if a creature has natural armor and DR/magic and is wearing adamantine armor, that creature's DR/armor functions as DR/—, and can be bypassed by Gargantuan or larger creatures, since the adamantine armor provides the best of the two damage reductions.

**Table: Natural Armor Conversion to DR**

| Natural Armor/DR                 | DR Provided   | Attacker Size to Bypass DR |
| -------------------------------- | ------------- | -------------------------- |
| Natural armor                    | DR/magic      | Large                      |
| Natural armor with DR/magic      | DR/adamantine | Huge                       |
| Natural armor with DR/adamantine | DR/—          | Gargantuan                 |
| Natural armor with DR/—          | DR/— (1)      | Colossal                   |
| Natural armor with DR/epic       | DR/epic (1)   | n/a                        |

1 _A creature that already has DR/— or DR/epic increases its DR by an amount equal to its natural armor bonus._

**Unusual Creatures and Armor DR**: Amorphous or incorporeal creatures have an easier time bypassing DR/armor. When they attack a creature with DR/armor, they typically treat that DR as a fraction of the DR/armor. Attacks by incorporeal creatures entirely ignore the DR unless that DR comes from a force effect or from armor with the _[[rangoric-srd/magic-items/armor-abilities/Ghost Touch (Armor Special Ability)|ghost touch]]_ special armor quality. These traits are detailed in Table: Unusual Creatures and Armor DR.

**Table: Unusual Creatures and Armor DR**

| Attacking Creature Type       | DR Modifier                                                                                                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Amorphous (1)                 | ×1/2                                                                                                                                          |
| Incorporeal                   | ×0 (×1 if DR is from a force effect or _[[rangoric-srd/magic-items/armor-abilities/Ghost Touch (Armor Special Ability)\|ghost touch]]_ armor) |
| Swarm of Tiny creatures       | ×1/2                                                                                                                                          |
| Swarm of Diminutive creatures | ×1/4                                                                                                                                          |
| Swarm of Fine creatures       | ×0                                                                                                                                            |

1 _Elementals, oozes, oozelike creatures, and any creature with the amorphous defensive ability._

##### Critical Hits and Defense

In this alternative system, when a creature threatens a critical hit, it does not make a critical hit confirmation roll. Instead, the target of that critical hit makes a critical defense check instead. A critical defense check is 1d20 + a bonus equal to the creature's DR + the creature's Dexterity modifier (up to the maximum Dexterity bonus allowed by any armor worn) + the sum of any deflection and shield bonus to Defense.

**Critical defense check bonus = creature's DR + Dexterity modifier + shield bonus to Defense + deflection bonus**

The DC of the check is based on the die roll for the critical threat. It is further modified by the base attack bonus of the attacking creature, how many critical feats the attacking creature has (if any; 10 maximum), and a bonus relationship between the size of the attacking creature and the target of the critical hit, if the attacking creature is larger than the creature it attacked.

**Critical defense DC = critical hit roll + 1/2 attacker's base attack bonus + 1 for each critical feat + 1 for each size category larger attacker is than target**

For instance, if a Medium creature is hit with a crossbow fired by a Medium 6th-level fighter with two critical feats, and the critical threat attack roll is a 19, the target of the potential critical hit makes a critical defense check with a DC of 24 to reduce the critical hit to a normal hit. If the target is wearing _+1 leather armor_, has a Dexterity of 18, and is using a _+1 buckler_, that target would have a +9 bonus on the critical defense check to reduce the critical hit to a normal hit. On a roll of 15 or higher, the critical hit is reduced to a normal hit, and the target takes normal damage for the hit (which is reduced by its DR). If the creature firing the crossbow had rolled a 20, the target of the critical hit would need to roll a 16 or higher on its critical defense check to reduce the impact of the critical hit, making it a normal hit.

On a failed critical defense check, the target of the critical hit takes the damage for the critical hit. That damage is still reduced by the target of the critical hit's DR.

**Fortification Special Armor Quality**: The _[[rangoric-srd/magic-items/armor-abilities/Fortification|fortification]]_ special armor quality acts in concert with the check, coming into play if the armor check fails.

### Damage Conversion

In the standard d20 rules, armor reduces the chance of a character taking damage in combat—but that’s the limit of its protection. In this variant, armor not only protects in that manner, but also turns fatal blows into less-threatening hits. Armored characters are often more easily battered into unconsciousness than brought down by lethal damage. It’s a system that works well in campaigns with a great deal of combat between armored foes, but in which magical healing is not common. It’s also ideal in a world where ethical or legal standards dictate that subduing or capturing opponents is preferable to killing them.

##### Armor Damage Conversion

Armor, in addition to adding a bonus to AC, also converts lethal damage from physical attacks into nonlethal damage. (Shields provide a shield bonus to AC, as normal, but do not convert damage.)

Each time an armor-wearing character is struck by an attack that deals lethal damage, the amount of damage dealt to the character is reduced by an amount equal to the armor bonus (including enhancement) of the armor worn. The character takes and equal amount of nonlethal damage. Damage that is not affected by [[rangoric-srd/rules/Special Abilities and Conditions#Damage Reduction|damage reduction]] (energy damage and the like) is not converted.

For example, while wearing +1 full plate (total armor bonus +9), someone is struck by an arrow for 6 points of damage. Since the armor can convert up to 9 points of damage per attack, the entire 6 points is converted from lethal damage to nonlethal damage. Their hit point total remains the same, but he increases his nonlethal damage total by 6 points. Later, a hill giant strikes them for a whopping 22 points of damage. The armor converts 9 points of this damage to nonlethal damage, but the remaining 13 points are deducted from their hit points.

**Nonlethal Damage:** An armor-wearing character can ignore nonlethal damage equal to his armor bonus. (In effect, armor grants [[rangoric-srd/rules/Special Abilities and Conditions#Damage Reduction|damage reduction]] equal to its armor bonus against nonlethal attacks.) ^nonlethal-damage

**Natural Armor:** At your option, you can make natural armor work in the same manner. However, this means that almost no defeated monster is truly dead, which may prove problematic (see [[#Behind the Curtain: Damage Conversion|Behind The Curtain: Damage Conversion]]). This rule also interacts strangely with [[rangoric-srd/monsters/abilities/Regeneration|regeneration]] — since all damage dealt to a creature with regeneration is treated as nonlethal damage, a regenerating creature with armor or natural armor actually takes less damage than normal when using this system. In case of regenerating creatures, consider eliminating the rule that natural armor works in the same manner. ^natural-armor-and-damage-conversion

##### Behind the Curtain: Damage Conversion

With this system, a character still takes as much damage from a hit as in the normal combat rules. Barring any magical healing delivered during the fight, a battle lasts just as long as in a standard game. Since nonlethal damage goes away faster than lethal damage, though, characters can recuperate from their battles relatively quickly, even without magical healing, making this variant ideal for low-magic campaigns.

However, healing spells become potentially doubly effective, since they heal an equal amount of lethal and nonlethal damage.

Nonlethal attacks become less frightening to armored opponents. A fighter in full plate simply has no fear of unarmed opponents, since they have little chance of injuring him. (Of course, they can still [[rangoric-srd/combat/Combat Maneuvers#Overrun|overrun]], [[rangoric-srd/combat/Combat Maneuvers#Trip|trip]], or [[rangoric-srd/combat/Combat Maneuvers#Grapple|grapple]] him, so he’d be wise to keep and eye on them all the same.)

Another effect is that defeated foes remain alive (and unconscious) unless dispatched after the fight. This can decrease character mortality dramatically — since most characters who fall in battle will be merely unconscious, but not dying — but it also introduces the potentially ugly postcombat scene of the characters feeling it necessary to slit the throats of their unconscious foes. Some characters, particulary paladins or other chivalrous types, may suffer serious moral qualms.

This variant is probably best for campaigns in which it’s acceptable for the bad guys to survive a fight. Perhaps a defeated villain’s honor prevents him from returning to plague the heroes at a later date, or maybe the style of your setting rewards characters for defeating opponents without killing them outright (such as in a swashbuckling campaign). Otherwise, characters may feel that they are punished for refusing to murder unconscious foes with regularity, since those enemies will certainly recover from their injuries and vow vengeance against the PCs. Encounters in the campaign may often involve fighting the same opponents again and again, rather than fighting new monsters and opponents.

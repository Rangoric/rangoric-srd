---
srd-type: "rules"
section: "Rules"
book: "Ultimate Equipment"
based-on:
  - "[[path srd 3.5/rules/ultimate-equipment/appendix/Treasure Generator|Treasure Generator (PF1)]]"
status: draft
change: new
pi-review: 2026-11-24
tags: [rangoric, rangoric/rules]
---

# Treasure Generator

The following system gives GMs a way to generate random treasure to reward players after completing an encounter or otherwise recovering valuables. The following system gives guidance to the GM to determine the type of treasure given based on the nature of the monsters or encounter.

Some rolls might generate treasure worth more than the expected average, others will likely generate less. The GM should decide whether or not to allow such variance, and adjust his rolls accordingly if he desires more even treasure distribution (rerolling as necessary to get closer to the expected value).

When using these rules to generate random treasure, you need to know the general type of encounter and level of treasure to be assigned (usually related to the total challenge faced). The Challenge Rating of the encounter determines the overall approximate value of the treasure to be gained. The makeup of adversaries in the encounter generally dictates the types of treasure that can be gained by overcoming its challenges.

Use the two following steps to figure out how much treasure to award characters and determine which treasure types are used in generating the specific items to appear in that treasure.

## Step 1: Determine Treasure Budget

The first step is to determine the amount of treasure you can budget for an encounter. Start by determining the overall Challenge Rating of the encounter and the advancement rate of the group. Refer to the [[#^treasure-values-by-advancement-speed|Treasure Values by Advancement Speed table]] to determine the base value of the treasure for an encounter in terms of gold pieces. You might wish to award greater treasures than what the value indicates. In such a case, hold back on awarding treasure for a number of encounters, in effect "banking" the value for one larger reward. Alternatively, you might decide to simply have a game with a higher amount of treasure in general, increasing all the base values by 50% or more.

**Table: Treasure Values by Advancement Speed**

| Average Party Level | Slow      | Medium    | Fast       |
| ------------------- | --------- | --------- | ---------- |
| 1                   | 170 gp    | 260 gp    | 400 gp     |
| 2                   | 350 gp    | 550 gp    | 800 gp     |
| 3                   | 550 gp    | 800 gp    | 1,200 gp   |
| 4                   | 750 gp    | 1,150 gp  | 1,700 gp   |
| 5                   | 1,000 gp  | 1,550 gp  | 2,300 gp   |
| 6                   | 1,350 gp  | 2,000 gp  | 3,000 gp   |
| 7                   | 1,750 gp  | 2,600 gp  | 3,900 gp   |
| 8                   | 2,200 gp  | 3,350 gp  | 5,000 gp   |
| 9                   | 2,850 gp  | 4,250 gp  | 6,400 gp   |
| 10                  | 3,650 gp  | 5,450 gp  | 8,200 gp   |
| 11                  | 4,650 gp  | 7,000 gp  | 10,500 gp  |
| 12                  | 6,000 gp  | 9,000 gp  | 13,500 gp  |
| 13                  | 7,750 gp  | 11,600 gp | 17,500 gp  |
| 14                  | 10,000 gp | 15,000 gp | 22,000 gp  |
| 15                  | 13,000 gp | 19,500 gp | 29,000 gp  |
| 16                  | 16,500 gp | 25,000 gp | 38,000 gp  |
| 17                  | 22,000 gp | 32,000 gp | 48,000 gp  |
| 18                  | 28,000 gp | 41,000 gp | 62,000 gp  |
| 19                  | 35,000 gp | 53,000 gp | 79,000 gp  |
| 20+                 | 44,000 gp | 67,000 gp | 100,000 gp |

^treasure-values-by-advancement-speed

_Rangoric’s own Treasure Values per Encounter column, in [[rangoric-srd/rules/Treasure#Using the Treasure Table|Treasure]], is the one the Treasure lines of Rangoric’s monsters multiply (standard, double, triple, incidental and NPC gear are defined in [[rangoric-srd/monsters/Monsters|Monsters]]), and [[rangoric-srd/unearthed-arcana/XP and GP Values by CR|XP and GP Values by CR]] lists the values by CR and advancement speed. This table is the Generator’s own, by average party level and speed._

After determining the base value of an encounter depending on its CR, next check the treasure line in the individual stat blocks for all creatures involved. In the case of mixed groups of enemies, use the most generous treasure entry. The treasure entry for the creatures involved affects the overall reward of the encounter as follows.

**None**: The creature does not typically possess treasure and an encounter solely against creatures with this treasure type should not award any treasure. You can still award treasure for this encounter if uncommon circumstances warrant it. The value that would have been awarded for this encounter can be saved to increase the value of a treasure from a later encounter.

**Incidental**: Creatures with this treasure type have little if any treasure. Reduce the base treasure value by half (50%).

**Standard**: The creature has the normal amount of treasure. Do not adjust the base treasure value.

**Double**: The creature has more than average treasure. Double the base treasure value.

**Triple**: The creature has a large amount of treasure. Triple the base treasure value.

### NPC Gear

Creatures with this treasure type have a different treasure value. Discard the base treasure value and look up the value for each individual creature on the [[#^npc-gear|NPC Gear table]]. Each creature's treasure should be determined individually. If a creature with this treasure type is part of a mixed group, deduct this value from the base treasure value for the rest of the creatures in the group.

If your campaign uses the fast experience progression, treat the NPCs as one level higher when determining the treasure value. If your campaign is using the slow experience progression, treat the NPC as one level lower when determining treasure value.

**Table: NPC Gear**

| Basic Level<sup>1</sup> | Heroic Level<sup>1</sup> | Treasure Value |
| ----------------------- | ------------------------ | -------------- |
| 1                       | —                        | 260 gp         |
| 2                       | 1                        | 390 gp         |
| 3                       | 2                        | 780 gp         |
| 4                       | 3                        | 1,650 gp       |
| 5                       | 4                        | 2,400 gp       |
| 6                       | 5                        | 3,450 gp       |
| 7                       | 6                        | 4,650 gp       |
| 8                       | 7                        | 6,000 gp       |
| 9                       | 8                        | 7,800 gp       |
| 10                      | 9                        | 10,050 gp      |
| 11                      | 10                       | 12,750 gp      |
| 12                      | 11                       | 16,350 gp      |
| 13                      | 12                       | 21,000 gp      |
| 14                      | 13                       | 27,000 gp      |
| 15                      | 14                       | 34,800 gp      |
| 16                      | 15                       | 45,000 gp      |
| 17                      | 16                       | 58,500 gp      |
| 18                      | 17                       | 75,000 gp      |
| 19                      | 18                       | 96,000 gp      |
| 20                      | 19                       | 123,000 gp     |
| —                       | 20                       | 159,000 gp     |

^npc-gear

<sup>1</sup> Basic level NPCs typically have class levels only in NPC classes.<sup>2</sup> Heroic level NPCs have levels in standard character classes.

This value is treated like a budget, to be spent on the relevant treasure tables (as determined in Step 2), purchasing groupings that establish a number of rolls you must make to determine the exact treasure gained.

## Step 2: Determine Treasure Type

To determine the type of treasures gained from an encounter, examine the types of creatures in the encounter and the general setting of the encounter. The types of treasure garnered from encounters can vary wildly depending on the types of creatures encountered. For example, the treasure found in the lair of a troll (remnants of its previous meals, no doubt) is sure to be different than the treasure found in the burial crypt of an ancient mummy. While the troll's treasure might contain coins and small objects such as potions or rings, the mummy's crypt might hold gems, art objects, and ancient magic items. Even if these types of treasures are worth approximately the same value, their exact composition is different.

The following section looks at each creature type individually and describes what treasures a particular type usually has. Each creature type lists a number of different treasure types, denoted by letters, which are described in detail in Step 3. Not every creature of each type will follow these guidelines, so weigh each carefully before deciding what treasure type best fits the creature. Note that a creature typically has treasure of only one type, but in some circumstances it might fit the encounter to have treasures of multiple different types as part of the reward.

### Aberration

Many aberrations have little use for treasure, possessing only what hangs from the remains of their previous victims. Others are cunning adversaries that use various magic items and treasure to enhance their abilities.

**Treasure Types**: A, B, D, E (add F, G, H if the creature is cunning).

### Animal

Animals place little to no value on treasure, instead leaving such coins and objects with the remains of their meals. For those with treasure, it is typically found in their lairs, scattered amid bones and other refuse.

**Treasure Types**: A, B, D, E.

### Construct

The only treasure carried by constructs is usually part of their construction, such as a weapon or magic item. Constructs are, however, typically used to guard more valuable treasures or magic items.

**Treasure Types**: E, F (add B, C, H if the creature is guarding a treasure).

### Dragon

Known for their valuable treasures, dragons often brood over vast piles of coins, gems, magic items, and other expensive objects.

**Treasure Types**: A, B, C, H, I.

### Fey

Above all other things, fey value items of magic and beauty. They have little use for tools of trade and commerce used by the more civilized races, such as coins and valuables.

**Treasure Types**: B, C, D, G.

### Humanoid

Creatures of this type are quite varied, but even the most primitive humanoids use gear and magic items to some extent. In bigger groups such as communities, humanoids often posses larger amounts of treasure that they collectively guard.

**Treasure Types**: A, B, D, E, F, G (add H for an entire community).

### Magical Beast

Caring little for valuables, most magical beasts are only in search of their next meal. The lairs of these creatures are often strewn with a few valuable trinkets and magic items.

**Treasure Types**: A, B, D, E.

### Monstrous Humanoid

Most monstrous humanoids care only about treasures that they can use, although some have been known to hoard valuables in their lairs.

**Treasure Types**: A, B, c, D, E, H.

### Ooze

Oozes have no concept of treasure and leave any they find behind as they search for their next meal. Any treasure they might carry is entirely accidental.

**Treasure Types**: A, B, D.

### Outsider

Outsiders are one of the most varied creature types and as a result might truly have any type of treasure on them or hidden in their lair. The GM should consider the creature individually to determine the treasure type that best fits the outsider.

**Treasure Types**: any.

### Plant

Like animals, plant creatures do not care for treasure, and any that might be found where they grow is simply the indigestible remnants of a previous victim.

**Treasure Types**: A, B, D, E.

### Undead

The treasure carried by undead varies depending on whether or not the creature is intelligent. Unintelligent undead typically only possess meager valuables carried on themselves in life, rarely actually using such treasures, while intelligent undead take advantage of a wide variety of magic items in order to destroy the living.

**Treasure Types**: A, B, D, E (add F, G for intelligent undead).

### Vermin

Like other mindless creatures, vermin do not covet treasure, although such creatures are sometimes found infesting areas where valuables are kept.

**Treasure Types**: A, B, D.

## Step 3: Generate Treasure

Once the total approximate value has been determined and the treasure types selected, all that remains is to select the actual treasures. Each treasure type has a wide variety of rewards, each with its own approximate gold piece value. Select a number of rewards whose total gold piece value is equal to the total value of the treasure to be awarded for defeating the encounter. For example, in an encounter against a group of trolls, the GM determines that he wants to give out items from treasure types B and E with a total value of 5,000 gp. He selects two rewards from those presented in type B with a value of 1,000 gp each and one from type E with a value of 3,000 gp. Alternatively, he could have selected one reward from type E worth 5,000 gp, or five rewards from type B worth 1,000 gp each, or any other combination that adds up to a total of 5,000 gp.

Each reward lists one or more random rolls you need to make to determine the actual treasure. For example, an entry might specify that the reward contains 5d10 × 10 gold pieces, 2 random potions from the minor potion table, and 1 item from the minor wondrous item table. The actual, final value might vary from the amount listed for the reward, but over time these random rolls should average out, giving the PCs the right amount of treasure needed to face challenges of their level.

Many of the rewards require you to generate a random magic item from one of the other tables located throughout the core rules. In most cases, the reward specifies which table you should roll on and where that table can be found.

**Selecting Rewards**: The GM should take care in deciding what rewards to give the PCs. In most cases, the GM should settle for the largest reward her budget allows, filling any excess budget with lesser rewards and coins (usually type A treasure). This gives the PCs a chance to get some of the more powerful magic items that are appropriate for their level. Selecting a larger number of smaller rewards grants a larger number of items, but they will be of comparatively lesser value in terms of usefulness.

### Treasure Types

Treasure comes in many shapes and forms, from simple coins and lustrous gems to magic swords and powerful staves. Due to the numerous different kinds of treasure, this system organizes them into types to make it easy to assign them to an encounter. The types share some of the various kinds of treasures (such as coins and potions), but each is aimed at a specific sort of encounter, as noted below in their descriptions.

**Type A, Coins**: Treasure of this type consists entirely of coins. Coins can be found in nearly any encounter.

**Type B, Coins and Gems**: Similar to Type A treasure, this type also includes gemstones, some of which can be quite valuable. It is typically found in a small cache or as part of a larger treasure roll.

**Type C, Art Objects**: Often overlooked, these items are valuable for their beauty and craftsmanship and are made with precious metals, gems, and other fine materials. Art objects are typically displayed in residences or placed in small vaults for safekeeping.

**Type D, Coins and Small Objects**: This category consists of coins and small magic items, such as potions, rings, scrolls, and wands. Such treasure is typically found in the lairs of beasts or as a small hoard in a monster den.

**Type E, Armor and Weapons**: Consisting solely of weapons and armor, treasure of this type can be found in armories, stored in a den, or even in use by a monster.

**Type F, Combatant Gear**: This treasure type is made up of items that would typically be carried by a monster that relies on melee or ranged combat. It includes armor, coins, potions, weapons, and wondrous items.

**Type G, Spellcaster Gear**: This treasure type is carried by creatures with spellcasting abilities, and includes coins, potions, scrolls, staves, wands, and wondrous items.

**Type H, Lair Treasure**: This treasure type can contain items of nearly any variety, but it focuses primarily on treasure of lesser individual value. It frequently includes a large number of magic items, coins, and other valuables.

**Type I, Treasure Hoard**: Truly the greatest of the treasure types, this can contain virtually any type of item. It usually serves as the reward for many challenging encounters, saved up and placed in one location.

### Treasure Type Tables

Each table lists rewards by their value: choose rewards that add up to the treasure’s budget.

#### Type A Treasure, Coins

Treasure of this type is made up entirely of coins. While it usually does not make a difference to their overall value, the GM may wish to consider the origin of the coins and what is minted on each side. Such details add depth to the world and might lead to further adventures.

**Table: Type A Treasure, Coins**

| Value     | Reward                            |
| --------- | --------------------------------- |
| 1 gp      | 5d10 cp, 3d4 sp                   |
| 5 gp      | 2d6 × 10 cp, 4d8 sp, 1d4 gp       |
| 10 gp     | 5d10 × 10 cp, 5d10 sp, 1d8 gp     |
| 25 gp     | 2d4 × 100 cp, 3d6 × 10 sp, 4d4 gp |
| 50 gp     | 4d4 × 100 cp, 4d6 × 10 sp, 8d6 gp |
| 100 gp    | 6d8 × 10 sp, 3d4 × 10 gp          |
| 200 gp    | 2d4 × 100 sp, 4d4 × 10 gp, 2d4 pp |
| 500 gp    | 6d6 × 10 gp, 8d6 pp               |
| 1,000 gp  | 2d4 × 100 gp, 10d10 pp            |
| 5,000 gp  | 4d8 × 100 gp, 6d10 × 10 pp        |
| 10,000 gp | 2d4 × 1,000 gp, 12d8 × 10 pp      |
| 50,000 gp | 2d6 × 1,000 gp, 8d10 × 100 pp     |

#### Type B Treasure, Coins and Gems

This treasure is made up solely of coins and gemstones, which can generally be traded for their full value. The gemstones make up the majority of the value for these rewards. Note that you can replace any gemstone with a piece of simple jewelry that is one grade lower, or a piece of complex jewelry that is two grades lower.

**Table: Type B Treasure, Coins and Gems**

| Value     | Reward                                                                                                     |
| --------- | ---------------------------------------------------------------------------------------------------------- |
| 10 gp     | Grade 1 gemstone                                                                                           |
| 15 gp     | 2d6 × 10 cp, 4d8 sp, 1d4 gp, grade 1 gemstone                                                              |
| 25 gp     | 5d10 sp, 1d4 gp, two grade 1 gemstones                                                                     |
| 50 gp     | Grade 2 gemstone                                                                                           |
| 50 gp     | 3d6 × 10 sp, 3d6 gp, three grade 1 gemstones                                                               |
| 75 gp     | 1d4 × 10 sp, 1d4 gp, two grade 1 gemstones, grade 2 gemstone                                               |
| 100 gp    | Grade 3 gemstone                                                                                           |
| 100 gp    | 3d8 × 10 sp, 4d8 gp, two grade 1 gemstones, grade 2 gemstone                                               |
| 150 gp    | Grade 2 gemstone, grade 3 gemstone                                                                         |
| 200 gp    | 3d6 × 10 sp, 2d4x10 gp, four grade 1 gemstones, grade 3 gemstone                                           |
| 250 gp    | 2d4 × 10 gp, two grade 2 gemstones, grade 3 gemstone                                                       |
| 500 gp    | Grade 4 gemstone                                                                                           |
| 500 gp    | 2d4 × 10 gp, 2d4 pp, two grade 2 gemstones, three grade 3 gemstones                                        |
| 750 gp    | 2d4 × 10 gp, two grade 2 gemstones, grade 3 gemstone, grade 4 gemstone                                     |
| 1,000 gp  | Grade 5 gemstone                                                                                           |
| 1,000 gp  | 3d6 × 10 gp, 4d4 pp, three grade 3 gemstones, grade 4 gemstone                                             |
| 2,500 gp  | 2d4 × 100 gp, two grade 4 gemstones, grade 5 gemstone                                                      |
| 5,000 gp  | Grade 6 gemstone                                                                                           |
| 5,000 gp  | 2d4 × 100 gp, 2d4x10 pp, two grade 4 gemstones, three grade 5 gemstones                                    |
| 10,000 gp | Five grade 5 gemstones, grade 6 gemstone                                                                   |
| 20,000 gp | 4d8 × 100 gp, 6d10x10 pp, three grade 6 gemstones                                                          |
| 50,000 gp | 4d4 × 10 pp, ten grade 3 gemstones, four grade 4 gemstones, six grade 5 gemstones, eight grade 6 gemstones |

#### Type C Treasure, Art Objects

This treasure is made up art objects, which can generally be traded for their full value.

**Table: Type C Treasure, Art Objects**

| Value     | Reward                                                                                               |
| --------- | ---------------------------------------------------------------------------------------------------- |
| 50 gp     | Grade 1 art object                                                                                   |
| 100 gp    | Grade 2 art object                                                                                   |
| 100 gp    | Two grade 1 art objects                                                                              |
| 150 gp    | Grade 1 art object, grade 2 art object                                                               |
| 200 gp    | Two grade 2 art objects                                                                              |
| 250 gp    | Three grade 1 art objects, grade 2 art object                                                        |
| 500 gp    | Grade 3 art object                                                                                   |
| 500 gp    | Four grade 1 art objects, three grade 2 art objects                                                  |
| 750 gp    | Three grade 1 art objects, two grade 2 art objects, grade 3 art object                               |
| 1,000 gp  | Grade 4 art object                                                                                   |
| 1,000 gp  | Two grade 3 art objects                                                                              |
| 1,500 gp  | Grade 3 art object, grade 4 art object                                                               |
| 2,000 gp  | Two grade 4 art objects                                                                              |
| 2,500 gp  | Five grade 2 art objects, two grade 3 art objects, grade 4 art object                                |
| 5,000 gp  | Grade 5 art object                                                                                   |
| 5,000 gp  | Four grade 3 art objects, three grade 4 art objects                                                  |
| 7,500 gp  | Grade 3 art object, two grade 4 art objects, grade 5 art object                                      |
| 10,000 gp | Grade 6 art object                                                                                   |
| 10,000 gp | Five grade 4 art objects, grade 5 art object                                                         |
| 15,000 gp | Grade 5 art object, grade 6 art object                                                               |
| 20,000 gp | Two grade 5 art objects, grade 6 art object                                                          |
| 50,000 gp | Ten grade 3 art objects, five grade 4 art objects, four grade 5 art objects, two grade 6 art objects |

#### Type D Treasure, Coins and Small Objects

This treasure is made up coins and small magic items, such as potions, scrolls, and wands.

**Table: Type D Treasure, Coins and Small Objects**

| Value     | Reward                                                                                          |
| --------- | ----------------------------------------------------------------------------------------------- |
| 50 gp     | 3d6 × 10 sp, 4d4 gp, lesser minor scroll                                                        |
| 50 gp     | 2d4 × 10 sp, 2d4 gp, lesser minor potion                                                        |
| 100 gp    | 4d6 × 10 sp, 3d10 gp, lesser minor potion, lesser minor scroll                                  |
| 150 gp    | 2d4 × 10 sp, 6d6 gp, greater minor scroll                                                       |
| 200 gp    | 2d4 × 10 sp, 4d6 gp, greater minor potion, lesser minor scroll                                  |
| 250 gp    | 3d6 × 10 sp, 3d6 gp, 1d4 pp, two lesser minor potions, greater minor scroll                     |
| 300 gp    | 2d4 × 10 sp, 6d6 gp, greater minor potion, greater minor scroll                                 |
| 400 gp    | Greater minor potion, two greater minor scrolls                                                 |
| 500 gp    | 2d4 × 10 gp, 1d4 pp, lesser medium potion, greater minor scroll                                 |
| 500 gp    | 2d4 × 10 gp, 1d4 pp, two greater minor potions, greater minor scroll                            |
| 750 gp    | 7d6 gp, greater minor scroll, lesser minor wand                                                 |
| 1,000 gp  | 4d4 × 10 gp, 3d6 pp, lesser medium potion, lesser medium scroll                                 |
| 1,000 gp  | 2d4 × 10 gp, 2d4 pp, lesser medium potion, lesser minor wand                                    |
| 1,500 gp  | Greater minor wand                                                                              |
| 1,500 gp  | 4d4 × 10 gp, 3d6 pp, greater medium potion, greater medium scroll                               |
| 2,000 gp  | Greater medium potion, greater minor wand                                                       |
| 2,000 gp  | 2d4 × 10 gp, 2d4 pp, lesser medium potion, two greater medium scrolls                           |
| 3,000 gp  | 3d6 × 10 gp, 4d4 pp, greater medium potion, greater medium scroll, greater minor wand           |
| 4,000 gp  | 3d6 × 10 gp, 4d4 pp, greater medium scroll, two greater minor wands                             |
| 5,000 gp  | 2d4 × 10 gp, 2d4 pp, three lesser major potions, two greater medium scrolls, greater minor wand |
| 7,500 gp  | 2d6 pp, lesser major scroll, lesser medium wand                                                 |
| 7,500 gp  | 5d6 pp, two greater major potions, two greater major scrolls                                    |
| 10,000 gp | Greater medium wand                                                                             |
| 10,000 gp | 4d6 pp, greater major potion, greater major scroll, lesser medium wand                          |
| 15,000 gp | Lesser major wand                                                                               |
| 15,000 gp | 9d10 pp, three greater major potions, two lesser major scrolls, greater medium wand             |
| 20,000 gp | 4d4 × 10 gp, 2d4x10 pp, two greater major potions, greater major scroll, lesser major wand      |
| 20,000 gp | 6d6 × 10 gp, three lesser major potions, greater major wand                                     |
| 25,000 gp | Five greater major scrolls, greater medium wand                                                 |
| 30,000 gp | 6d6 pp, four greater major potions, three greater major scrolls, greater major wand             |
| 50,000 gp | 8d4 × 10 pp, four greater major scrolls, two greater major wands                                |

#### Type E Treasure, Armor and Weapons

This treasure is made up entirely of armor and weapons. Note that the value of some types of armor and weapons can significantly increase the value of some low-level rewards.

**Table: Type E Treasure, Armor and Weapons**

| Value      | Reward                                                          |
| ---------- | --------------------------------------------------------------- |
| 200 gp     | Masterwork light armor or shield                                |
| 300 gp     | Masterwork medium armor                                         |
| 350 gp     | Masterwork weapon                                               |
| 1,000 gp   | Masterwork heavy armor                                          |
| 1,500 gp   | Lesser minor armor                                              |
| 2,500 gp   | Lesser minor weapon                                             |
| 3,000 gp   | Greater minor armor                                             |
| 3,000 gp   | Masterwork medium armor, masterwork shield, lesser minor weapon |
| 4,000 gp   | Lesser minor armor, lesser minor weapon                         |
| 5,500 gp   | Greater minor armor, lesser minor weapon                        |
| 6,000 gp   | Greater minor weapon                                            |
| 7,500 gp   | Lesser minor armor, greater minor weapon                        |
| 8,000 gp   | Greater minor armor, two lesser minor weapons                   |
| 9,000 gp   | Greater minor armor, greater minor weapon                       |
| 10,000 gp  | Lesser medium armor, lesser minor weapon                        |
| 13,000 gp  | Lesser medium weapon                                            |
| 13,000 gp  | Lesser medium armor, greater minor weapon                       |
| 15,000 gp  | Greater medium armor, lesser minor weapon                       |
| 20,000 gp  | Lesser medium armor, lesser medium weapon                       |
| 25,000 gp  | Greater minor armor, greater medium weapon                      |
| 30,000 gp  | Lesser major armor, lesser minor weapon, greater minor weapon   |
| 30,000 gp  | Lesser medium armor, greater medium weapon                      |
| 35,000 gp  | Lesser major armor, lesser medium weapon                        |
| 35,000 gp  | Lesser minor armor, lesser major weapon                         |
| 40,000 gp  | Greater major armor, greater minor weapon                       |
| 50,000 gp  | Greater major armor, lesser medium weapon                       |
| 75,000 gp  | Greater minor armor, greater major weapon                       |
| 100,000 gp | Greater major armor, greater major weapon                       |

#### Type F Treasure, Combatant Gear

Treasure of this type represents the typical gear that might be carried by a creature that frequently finds itself in combat without the aid of spells or magic. These rewards include coins only if needed to round out the total value to an easily used number. Note that the value of some types of armor and weapons can significantly increase the value of some low-level rewards.

**Table: Type F Treasure, Combatant Gear**

| Value      | Reward                                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------------------------------ |
| 50 gp      | 2d4 × 10 sp, 2d4 gp, lesser minor potion                                                                                 |
| 250 gp     | 2d4 × 10 sp, 2d4 gp, masterwork light armor or shield, lesser minor potion                                               |
| 350 gp     | 2d4 × 10 sp, 2d4 gp, masterwork medium armor, lesser minor potion                                                        |
| 400 gp     | 2d4 × 10 sp, 2d4 gp, masterwork weapon, lesser minor potion                                                              |
| 500 gp     | Masterwork weapon, greater minor potion                                                                                  |
| 750 gp     | 6d6 gp, masterwork medium armor, masterwork weapon, two lesser minor potions                                             |
| 1,000 gp   | Masterwork heavy armor                                                                                                   |
| 1,500 gp   | Masterwork heavy armor, masterwork weapon, greater minor potion                                                          |
| 2,000 gp   | Lesser minor armor, masterwork weapon, two greater minor potions                                                         |
| 3,000 gp   | Masterwork medium armor, lesser minor weapon, greater minor potion                                                       |
| 4,000 gp   | Lesser minor armor, masterwork weapon, lesser minor wondrous item, greater minor potion                                  |
| 5,000 gp   | Masterwork medium armor, lesser minor weapon, lesser minor wondrous item, greater minor potion                           |
| 6,000 gp   | Lesser minor armor, lesser minor weapon, lesser minor wondrous item                                                      |
| 7,500 gp   | Greater minor armor, lesser minor weapon, lesser minor ring                                                              |
| 10,000 gp  | Greater minor armor, lesser minor weapon, lesser minor ring, lesser minor wondrous item, three greater minor potions     |
| 10,000 gp  | Greater minor armor, greater minor weapon, two greater medium potions                                                    |
| 12,500 gp  | Greater minor armor, lesser minor weapon, greater minor wondrous item, two greater medium potions                        |
| 15,000 gp  | Greater minor armor, greater minor weapon, greater minor ring                                                            |
| 20,000 gp  | Lesser medium armor, greater minor weapon, greater minor wondrous item, two greater medium potions                       |
| 25,000 gp  | Lesser medium armor, lesser medium weapon, lesser minor ring, lesser minor wondrous item, two greater medium potions     |
| 30,000 gp  | Lesser medium armor, lesser medium weapon, two lesser minor rings, greater minor wondrous items                          |
| 40,000 gp  | Lesser medium armor, lesser medium weapon, lesser medium ring, greater minor wondrous item, two greater medium potions   |
| 50,000 gp  | Greater medium armor, greater medium weapon, lesser medium wondrous item, two lesser major potions                       |
| 60,000 gp  | Greater medium armor, greater medium weapon, two greater minor rings, two greater minor wondrous items                   |
| 75,000 gp  | Lesser major armor, greater medium weapon, greater minor ring, greater medium wondrous item, three greater major potions |
| 100,000 gp | Lesser major armor, lesser major weapon, lesser medium ring, greater minor ring, two lesser medium wondrous items        |

#### Type G Treasure, Spellcaster Gear

Treasure of this type represents the typical gear that might be carried by a spellcasting creature. These rewards include coins only if needed to round out the total value to an easily used number.

**Table: Type G Treasure, Spellcaster Gear**

| Value      | Reward                                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 50 gp      | 2d4 × 10 sp, 2d4 gp, lesser minor potion                                                                                                   |
| 75 gp      | 2d4 gp, lesser minor potion, lesser minor scroll                                                                                           |
| 100 gp     | Lesser minor potion, two lesser minor scrolls                                                                                              |
| 150 gp     | Lesser minor scroll, greater minor scroll                                                                                                  |
| 200 gp     | Two lesser minor potions, greater minor scroll                                                                                             |
| 250 gp     | Two greater minor scrolls                                                                                                                  |
| 500 gp     | Three lesser minor potions, three greater minor scrolls                                                                                    |
| 750 gp     | Greater minor potion, lesser minor wand                                                                                                    |
| 1,000 gp   | 7d6 gp, three greater minor scrolls, lesser minor wand                                                                                     |
| 1,500 gp   | 3d6 × 10 gp, Lesser medium potion, lesser medium scroll, lesser minor wand                                                                 |
| 2,000 gp   | 2d4 × 10 gp, masterwork weapon, two lesser medium scrolls, lesser minor wand                                                               |
| 2,500 gp   | Two greater medium potions, greater minor wand                                                                                             |
| 3,000 gp   | Greater medium potion, two lesser medium scrolls, greater minor wand                                                                       |
| 4,000 gp   | Lesser minor wondrous item, greater medium potion, greater minor wand                                                                      |
| 5,000 gp   | Lesser minor ring, lesser minor wondrous item, two lesser medium scrolls                                                                   |
| 6,000 gp   | Lesser minor ring, lesser minor wondrous item, greater medium potion, greater minor wand                                                   |
| 7,500 gp   | Two greater medium potions, lesser minor scroll, lesser medium wand                                                                        |
| 10,000 gp  | Lesser minor ring, lesser minor wondrous item, lesser medium wand                                                                          |
| 12,500 gp  | Lesser minor ring, greater minor wondrous item, two greater medium scrolls, two greater minor wands                                        |
| 15,000 gp  | Lesser minor ring, lesser medium rod, lesser medium wand                                                                                   |
| 20,000 gp  | Greater minor ring, greater minor wondrous item, greater medium potion, two greater medium scrolls, lesser medium wand                     |
| 25,000 gp  | Lesser minor ring, lesser medium wand, greater medium wand, greater minor wondrous item                                                    |
| 30,000 gp  | Greater minor ring, lesser medium wondrous item, lesser major scroll, greater medium wand                                                  |
| 40,000 gp  | Lesser minor weapon, lesser medium staff, greater medium rod, two lesser minor wondrous items, lesser medium wand                          |
| 50,000 gp  | Greater minor ring, two lesser medium wondrous items, lesser major potion, three greater medium scrolls, lesser major wand                 |
| 60,000 gp  | Lesser medium staff, greater medium rod, greater medium wondrous item, greater medium potion, two lesser major scrolls, lesser medium wand |
| 75,000 gp  | Lesser minor weapon, greater medium staff, greater medium wondrous item, three greater major scrolls, greater major wand                   |
| 100,000 gp | Lesser major ring, greater medium rod, lesser major staff, lesser major scroll, greater medium wand                                        |

#### Type H Treasure, Lair Treasure

Rewards from this type of treasure represent the kinds of items that might be found in the lair of one or more creatures. Though they can be of any type, this treasure tends to include a fair number of coins and smaller magic items.

**Table: Type H Treasure, Lair Treasure**

| Value      | Reward                                                                                                                                                                                   |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 500 gp     | 4d4 × 100 cp, 3d6 × 10 sp, 2d4 × 10 gp, masterwork weapon, lesser minor potion, lesser minor scroll, grade 2 gemstone                                                                    |
| 1,000 gp   | 2d4 × 100 cp, 2d6 × 100 sp, 6d6 gp, greater minor potion, greater minor scroll, lesser minor wand, three grade 1 gemstones                                                               |
| 2,500 gp   | 3d6 × 10 sp, 2d4 gp, masterwork heavy armor, masterwork weapon, two lesser medium potions, two greater minor scrolls, grade 2 gemstone                                                   |
| 5,000 gp   | 2d4 × 10 gp, 4d6 pp, masterwork weapon, lesser minor ring, greater medium potion, lesser medium scroll, greater minor wand                                                               |
| 7,500 gp   | 4d4 × 10 gp, 6d6 pp, lesser minor weapon, lesser minor wondrous item, two greater medium potions, greater minor wand, two grade 3 gemstones                                              |
| 10,000 gp  | 4d8 × 10 gp, 6d10 pp, greater minor armor, lesser minor ring, lesser minor wondrous item, lesser medium scroll, greater minor wand, grade 4 gemstone                                     |
| 15,000 gp  | 4d4 × 10 gp, 4d4 × 10 pp, greater minor armor, lesser minor wondrous item, two greater medium potions, two greater medium scrolls, lesser medium wand, one grade 3 gemstone              |
| 20,000 gp  | 2d4 × 10 pp, greater minor ring, two lesser minor wondrous items, two greater medium potions, two lesser major scrolls, lesser medium wand                                               |
| 25,000 gp  | 6d10 × 10 gp, 6d6 pp, lesser medium armor, lesser minor weapon, greater minor wondrous item, two lesser major scrolls, lesser medium wand, grade 4 gemstone                              |
| 30,000 gp  | 6d6 × 10 gp, 2d4 × 10 pp, greater minor weapon, lesser medium wondrous item, greater medium wand, three grade 3 gemstones                                                                |
| 40,000 gp  | 4d4 × 10 gp, 4d4 × 10 pp, lesser medium ring, lesser medium rod, two greater major potions, two lesser major scrolls, lesser major wand                                                  |
| 50,000 gp  | 4d4 × 10 pp, greater medium armor, lesser medium staff, lesser medium wondrous item, greater major scroll, lesser medium wand, grade 5 gemstone                                          |
| 75,000 gp  | 2d8 × 100 gp, 4d4 × 10 pp, greater minor weapon, greater medium ring, greater medium staff, three greater major potions, greater major scroll, lesser major wand, grade 5 gemstone       |
| 100,000 gp | 8d6 × 100 gp, 4d4 × 10 pp, lesser major ring, lesser major wondrous item, three greater major potions, greater major scroll, lesser medium wand, two grade 5 gemstones, grade 6 gemstone |

#### Type I Treasure, Treasure Hoard

Rewards from this type of treasure represent the kinds of items that might be found in the vault of an entire community of creatures or in the hoard of a mighty beast such as a dragon. While this reward can include items of any type, it focuses on coins, gems, and larger, more valuable items.

**Table: Type I Treasure, Treasure Hoard**

| Value      | Reward                                                                                                                                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5,000 gp   | 4d4 × 1,000 cp, 6d6 × 100 sp, 2d4 × 100 gp, 6d6 pp, lesser minor armor, greater minor wand, five grade 3 gemstones, grade 3 art object                                                                                          |
| 10,000 gp  | 4d4 × 1,000 cp, 6d6 × 100 sp, 2d4 × 100 gp, 6d6 pp, greater minor armor, lesser minor weapon, lesser minor wondrous item, greater medium scroll, grade 4 gemstone, grade 3 art object                                           |
| 15,000 gp  | 2d4 × 1,000 cp, 6d4 × 100 sp, 3d6 × 10 gp, 6d6 pp, greater minor ring, two lesser minor wondrous items, two greater medium potions, greater minor wand, grade 4 gemstone, grade 3 art object                                    |
| 20,000 gp  | 2d4 × 1,000 cp, 6d4 × 100 sp, 3d6 × 10 gp, 6d6 pp, greater minor armor, lesser medium rod, greater minor wondrous item, two lesser major potions, greater medium scroll, three grade 3 art objects                              |
| 25,000 gp  | 2d4 × 1,000 cp, 6d4 × 100 sp, 3d6 × 10 gp, 6d6 pp, lesser medium staff, two lesser minor wondrous items, greater medium potion, lesser medium wand, two grade 2 gemstones, two grade 3 gemstones, grade 4 gemstone              |
| 30,000 gp  | 2d4 × 1,000 cp, 6d4 × 100 sp, 3d6 × 10 gp, 6d6 pp, lesser medium armor, greater minor weapon, lesser medium wondrous item, two lesser major scrolls, grade 4 art object                                                         |
| 40,000 gp  | 4d4 × 1,000 cp, 6d6 × 100 sp, 2d4 × 100 gp, 6d6 pp, lesser medium weapon, greater medium rod, greater major potion, greater medium scroll, lesser medium wand, three grade 3 art objects, two grade 4 art objects               |
| 50,000 gp  | 4d4 × 10,000 cp, 6d6 × 1,000 sp, 4d4 × 100 gp, 2d4 × 10 pp, greater minor armor, two greater minor weapons, greater medium staff, greater minor wondrous item, grade 5 gemstone                                                 |
| 60,000 gp  | 2d4 × 10,000 cp, 2d4 × 1,000 sp, 2d4 × 100 gp, 2d4 × 10 pp, greater medium weapon, greater medium rod, lesser medium wondrous item, greater major scroll, two greater minor wands, grade 4 gemstone, five grade 2 art objects   |
| 75,000 gp  | 2d4 × 10,000 cp, 2d4 × 1,000 sp, 2d4 × 100 gp, 2d4 × 10 pp, lesser major armor, greater medium ring, lesser medium staff, greater medium wand, grade 6 gemstone, grade 4 art object                                             |
| 100,000 gp | 2d4 × 10,000 cp, 2d4 × 1,000 sp, 2d4 × 100 gp, 2d4 × 10 pp, lesser medium weapon, greater medium ring, lesser major rod, greater medium wondrous item, two greater major potions, lesser medium scroll, two grade 4 art objects |
| 125,000 gp | 4d4 × 10,000 cp, 6d6 × 1,000 sp, 4d4 × 100 gp, 2d8 × 10 pp, greater major armor, lesser medium weapon, lesser major staff, two greater major scrolls, greater major wand, grade 6 gemstone, three grade 4 art objects           |
| 150,000 gp | 4d4 × 10,000 cp, 6d6 × 1,000 sp, 4d4 × 100 gp, 2d8 × 10 pp, greater medium armor, lesser major ring, greater major wondrous item, greater major wand                                                                            |
| 200,000 gp | 4d4 × 10,000 cp, 6d6 × 1,000 sp, 4d4 × 100 gp, 2d8 × 10 pp, greater major weapon, two lesser medium rings, lesser major staff, lesser major wondrous item, lesser major wand, three grade 5 gemstones, grade 4 gemstone         |
| 300,000 gp | 8d4 × 10,000 cp, 12d6 × 1,000 sp, 8d4 × 100 gp, 2d8 × 10 pp, greater major weapon, lesser major ring, greater major staff, greater major wondrous item, greater medium wand, grade 6 gemstone, grade 6 art object               |

### Rewards

The rewards name what to roll. Coins are the dice shown. Gemstones and art objects are rolled by grade on [[rangoric-srd/rules/treasure-generator/Random Gems and Art Objects|Random Gems and Art Objects]]; potions and oils on [[rangoric-srd/rules/treasure-generator/Random Potions and Oils|Random Potions and Oils]]; scrolls on [[rangoric-srd/rules/treasure-generator/Random Arcane Scrolls|Random Arcane Scrolls]] and [[rangoric-srd/rules/treasure-generator/Random Divine Scrolls|Random Divine Scrolls]]; wands on [[rangoric-srd/rules/treasure-generator/Random Wands|Random Wands]]; the kind of armor, shield or weapon on [[rangoric-srd/rules/treasure-generator/Random Armor and Weapons|Random Armor and Weapons]], with the enhancement from [[rangoric-srd/magic-items/Magic Armor and Weapons|Magic Armor and Weapons]]; wondrous items on [[rangoric-srd/magic-items/Wondrous Items by Slot|Wondrous Items by Slot]]; and rings, rods and staves on [[rangoric-srd/magic-items/Magic Potions, Rings, and Rods|Magic Potions, Rings, and Rods]] and [[rangoric-srd/magic-items/Magic Scrolls, Staffs, and Wands|Magic Scrolls, Staffs, and Wands]].

_Rangoric’s [[rangoric-srd/rules/Treasure|Treasure]] has its own tables for the same rewards (its Treasure, Gems and Art Objects tables, and the tables in Magic Scrolls, Staffs, and Wands, Magic Armor and Weapons and Expanded Random Magic Arms and Armor). Use either: the Generator’s rewards resolve inside its own tables, and Treasure’s tables stay as they are._

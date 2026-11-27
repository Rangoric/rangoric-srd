---
srd-type: "designer-reference"
section: "Design Notes"
status: draft
pi-review: 2026-11-24
tags: [rangoric, rangoric/designer-reference]
---

# Monster Creation

_The benchmarks in this note are the source game’s: its tables of statistics by CR, Hit Dice, size and treasure compare new monsters with that game’s monsters and challenge ratings, so use them as a guide for how much a monster of a given CR should do, and check a new monster against Rangoric’s own monsters of the same CR._

Creating a monster is part science and part art. While most monsters follow a general pattern of their overall power and abilities as related to their Challenge Rating (CR), there are many exceptions. Some monsters, for example, have significantly more hit points or a higher AC than the average for their CR, but make up for this advantage by being weak in other areas. Other monsters have significantly higher average damage, but have a lower attack bonus.

The following guidelines are provided to assist in monster creation and to help balance a creation for its CR.

## Step 1: Concept

The first step in creating a new monster is to define its concept and role in the game. Generally, this involves picking the monster's CR, type, physical appearance, and manner of fighting. Once you have these basic pieces of information, you should find a number of similar monsters of the same type and roughly the same CR for comparison purposes.

**Table: Monster Statistics by CR**

| CR  | Hit Points | Armor Class | High Attack | Low Attack | Average Damage High | Average Damage Low | Primary Ability Attack | Secondary Ability Attack | Good Defense | Poor Defense |
| --- | ---------- | ----------- | ----------- | ---------- | ------------------- | ------------------ | ---------------------- | ------------------------ | ------------ | ------------ |
| 1/2 | 10         | 11          | 1           | 0          | 4                   | 3                  | 1                      | –2                       | 13           | 10           |
| 1   | 15         | 12          | 2           | 1          | 7                   | 5                  | 2                      | –1                       | 14           | 11           |
| 2   | 20         | 14          | 4           | 3          | 10                  | 7                  | 3                      | –1                       | 15           | 11           |
| 3   | 30         | 15          | 6           | 4          | 13                  | 9                  | 4                      | 0                        | 16           | 12           |
| 4   | 40         | 17          | 8           | 6          | 16                  | 12                 | 5                      | 0                        | 17           | 13           |
| 5   | 55         | 18          | 10          | 7          | 20                  | 15                 | 5                      | 1                        | 18           | 14           |
| 6   | 70         | 19          | 12          | 8          | 25                  | 18                 | 6                      | 1                        | 19           | 15           |
| 7   | 85         | 20          | 13          | 10         | 30                  | 22                 | 7                      | 2                        | 20           | 16           |
| 8   | 100        | 21          | 15          | 11         | 35                  | 26                 | 8                      | 2                        | 21           | 17           |
| 9   | 115        | 23          | 17          | 12         | 40                  | 30                 | 8                      | 3                        | 22           | 18           |
| 10  | 130        | 24          | 18          | 13         | 45                  | 33                 | 9                      | 3                        | 23           | 19           |
| 11  | 145        | 25          | 19          | 14         | 50                  | 37                 | 10                     | 4                        | 24           | 20           |
| 12  | 160        | 27          | 21          | 15         | 55                  | 41                 | 11                     | 5                        | 25           | 21           |
| 13  | 180        | 28          | 22          | 16         | 60                  | 45                 | 11                     | 5                        | 26           | 22           |
| 14  | 200        | 29          | 23          | 17         | 65                  | 48                 | 12                     | 6                        | 27           | 22           |
| 15  | 220        | 30          | 24          | 18         | 70                  | 52                 | 13                     | 6                        | 28           | 23           |
| 16  | 240        | 31          | 26          | 19         | 80                  | 60                 | 14                     | 7                        | 29           | 24           |
| 17  | 270        | 32          | 27          | 20         | 90                  | 67                 | 14                     | 8                        | 30           | 25           |
| 18  | 300        | 33          | 28          | 21         | 100                 | 75                 | 15                     | 8                        | 30           | 26           |
| 19  | 330        | 34          | 29          | 22         | 110                 | 82                 | 16                     | 9                        | 31           | 26           |
| 20  | 370        | 36          | 30          | 23         | 120                 | 90                 | 17                     | 10                       | 32           | 27           |

## Step 2: Target Statistics

Once you have a creature's type and CR determined, use Table: Monster Statistics by CR to determine its approximate statistics by CR. These values are a rough guideline only. You will notice that many of the existing monsters do not follow these guidelines exactly. Most monsters excel in one of these areas, usually in the amount of damage dealt, but lag in one or two other areas to help balance them out. When referring to Table: Monster Statistics by CR, keep the following points in mind.

**CR**: This is the approximate CR of the monster. This number might change as design progresses.

**Hit Points**: This is the approximate hit point total for the monster. Note that creatures with particularly high Armor Classes or defenses, or a number of resistances, might have a lower number. Outsiders and constructs typically have lower hit point totals.

**Armor Class**: This is the average Armor Class for a creature of this CR. When it comes time to design the creature's protections, keep this number in mind. Creatures with hit points above the average often have lower Armor Class values to compensate.

**High Attack**: This is the average total attack bonus for a creature of this CR. This value is for creatures that are primarily melee or ranged combatants. Creatures with a higher than normal average damage typically have a lower attack value to compensate.

**Low Attack**: This is the average total attack bonus for a creature of this CR that does not rely upon melee or ranged attacks to deal damage. This includes most creatures that rely on spells and spell-like abilities in combat.

### Average Damage

This is the average amount of damage dealt by a creature of this CR if all of its attacks are successful. To determine a creature's average damage, add the average value for all of the damage dice rolled (as determined by Table: Average Die Results) to the damage modifier for each attack.

A creature that relies on melee or ranged weapons in combat should have average damage within the range of high and low damage.

A creature with higher than normal attack bonuses will often deal lower damage, while a creature with lower than normal attack bonuses will often deal higher damage.

**Primary Ability Attack**: This is the average attack bonus for any spells, spell-like abilities, and special abilities (such as breath weapons) possessed by a creature of this CR that relies on such attacks in combat. If an ability is particularly powerful, it might have a lower attack bonus to compensate.

**Secondary Ability Attack**: This is the average attack bonus for spells and special abilities for a creature that does not rely on such attacks in combat. Generally, an attack bonus should not be lower than this number.

**Good Defense**: This is the average defense for a creature of this CR if the defense is one of the creature's good saves (10 + the save bonus).

### Poor Defense

This is the average defense for a creature of this CR if the defense is one of the creature's poor saves.

**Table: Average Die Results**

| Die Type                                                                                                        | Average Result\* |
| --------------------------------------------------------------------------------------------------------------- | ---------------- |
| d4                                                                                                              | 2.5              |
| d6                                                                                                              | 3.5              |
| d8                                                                                                              | 4.5              |
| d10                                                                                                             | 5.5              |
| d12                                                                                                             | 6.5              |
| d20                                                                                                             | 10.5             |
| \*Always round down after multiplying. For example, treat the average of 1d4 as 2, and the average of 2d4 as 5. |                  |

## Step 3: Hit Dice

The next step in creating a monster is to determine the approximate number of Hit Dice it has. Hit Dice determine a wide variety of other statistics, including the creature's feats, skills, hit points, attack bonuses, and special ability attack bonuses.

A creature's total number of Hit Dice depends on a number of factors, but the two most important are its CR and its type. Table: Creature Hit Dice lists the average number of Hit Dice for each creature type, depending on its CR. While many of the existing monsters are close to these values, some are not. This is because they have higher or lower average hit points to balance out their Armor Class or resistances.

**Table: Creature Hit Dice**

| Creature Type      | Challenge Rating 1/2 | Challenge Rating 1 | Challenge Rating 2 | Challenge Rating 3 | Challenge Rating 4 | Challenge Rating 5 | Challenge Rating 6 | Challenge Rating 7 | Challenge Rating 8 | Challenge Rating 9 | Challenge Rating 10 | Challenge Rating 11 | Challenge Rating 12 | Challenge Rating 13 | Challenge Rating 14 | Challenge Rating 15 | Challenge Rating 16 | Challenge Rating 17 | Challenge Rating 18 | Challenge Rating 19 | Challenge Rating 20 |
| ------------------ | -------------------- | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| Aberration         | 1                    | 2                  | 3                  | 4                  | 5                  | 7                  | 9                  | 10                 | 12                 | 14                 | 15                  | 16                  | 17                  | 19                  | 20                  | 22                  | 24                  | 26                  | 28                  | 30                  | 34                  |
| Animal             | 1                    | 2                  | 3                  | 4                  | 5                  | 7                  | 9                  | 10                 | 12                 | 14                 | 15                  | 16                  | 17                  | 19                  | 20                  | 22                  | 24                  | 26                  | 28                  | 30                  | 34                  |
| Construct          | 1                    | 2                  | 3                  | 4                  | 5                  | 6                  | 8                  | 9                  | 10                 | 12                 | 13                  | 14                  | 16                  | 18                  | 19                  | 20                  | 21                  | 23                  | 25                  | 28                  | 31                  |
| Dragon             | 1                    | 2                  | 3                  | 4                  | 5                  | 6                  | 7                  | 8                  | 9                  | 11                 | 12                  | 13                  | 14                  | 16                  | 17                  | 18                  | 19                  | 21                  | 23                  | 25                  | 29                  |
| Fey                | 2                    | 3                  | 4                  | 5                  | 6                  | 8                  | 10                 | 12                 | 13                 | 15                 | 17                  | 18                  | 20                  | 22                  | 23                  | 25                  | 26                  | 28                  | 31                  | 33                  | 37                  |
| Humanoid           | 1                    | 2                  | 3                  | 4                  | 5                  | 7                  | 9                  | 10                 | 12                 | 14                 | 15                  | 16                  | 17                  | 19                  | 20                  | 22                  | 24                  | 26                  | 28                  | 30                  | 34                  |
| Magical beast      | 1                    | 2                  | 3                  | 4                  | 5                  | 6                  | 8                  | 9                  | 10                 | 12                 | 13                  | 14                  | 16                  | 18                  | 19                  | 20                  | 21                  | 23                  | 25                  | 28                  | 31                  |
| Monstrous humanoid | 1                    | 2                  | 3                  | 4                  | 5                  | 6                  | 8                  | 9                  | 10                 | 12                 | 13                  | 14                  | 16                  | 18                  | 19                  | 20                  | 21                  | 23                  | 25                  | 28                  | 31                  |
| Ooze               | 1                    | 2                  | 3                  | 4                  | 5                  | 7                  | 9                  | 10                 | 12                 | 14                 | 15                  | 16                  | 17                  | 19                  | 20                  | 22                  | 24                  | 26                  | 28                  | 30                  | 34                  |
| Outsider           | 1                    | 2                  | 3                  | 4                  | 5                  | 6                  | 8                  | 9                  | 10                 | 12                 | 13                  | 14                  | 16                  | 18                  | 19                  | 20                  | 21                  | 23                  | 25                  | 28                  | 31                  |
| Plant              | 1                    | 2                  | 3                  | 4                  | 5                  | 7                  | 9                  | 10                 | 12                 | 14                 | 15                  | 16                  | 17                  | 19                  | 20                  | 22                  | 24                  | 26                  | 28                  | 30                  | 34                  |
| Undead             | 1                    | 2                  | 3                  | 4                  | 5                  | 7                  | 9                  | 10                 | 12                 | 14                 | 15                  | 16                  | 17                  | 19                  | 20                  | 22                  | 24                  | 26                  | 28                  | 30                  | 34                  |
| Vermin             | 1                    | 2                  | 3                  | 4                  | 5                  | 7                  | 9                  | 10                 | 12                 | 14                 | 15                  | 16                  | 17                  | 19                  | 20                  | 22                  | 24                  | 26                  | 28                  | 30                  | 32                  |

**Table: Size**

| Size       | Minimum CR | Maximum CR | Base Str | Base Dex | Base Con |
| ---------- | ---------- | ---------- | -------- | -------- | -------- |
| Fine       | —          | 2          | 1        | 18       | 8        |
| Diminutive | —          | 4          | 1        | 16       | 8        |
| Tiny       | —          | 6          | 2        | 14       | 8        |
| Small      | —          | —          | 6        | 12       | 8        |
| Medium     | —          | —          | 10       | 10       | 10       |
| Large      | 2          | —          | 18       | 8        | 14       |
| Huge       | 4          | —          | 26       | 6        | 18       |
| Gargantuan | 6          | —          | 34       | 6        | 22       |
| Colossal   | 8          | —          | 42       | 6        | 26       |

## Step 4: Size

Now that you have the creature's average statistics, it's time to pick its size. Most creatures range in size from Small to Huge, but other sizes are not uncommon. A creature's size sets a baseline for its physical ability scores and its natural weapon damage (as noted in the [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities#^natural-weapons|Natural Attacks]] description in the [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities|Universal Monster Rules]]). You should pick a size that fits well with the creature's intended role in the game and Challenge Rating. If you decide to give a creature an unusual size for its CR or HD, you should justify the unusual choice in the monster's description to account for the discrepancy—in most cases, such unusually sized monsters should be highly magical in nature. See Table: Size for more information on creature sizes and expected scores.

**Minimum/Maximum CR**: These values list the minimum and the maximum challenge ratings a creature of the indicated size should fall between.

**Base Str, Base Dex, Base Con**: These list the average scores for a creature of this size. Your specific monster's Strength, Dexterity, or Constitution might vary greatly from these numbers, but if they do, you should pay close attention to how these variances affect its other statistics.

## Step 5: Abilities

Once you have determined a creature's size, type, and Hit Dice, it's time to move on to its ability scores. The bonuses granted from these ability scores should increase a creature's hit points, attack bonuses, and defenses to the approximate values presented on Table: Monster Statistics by CR.

A creature's physical ability scores (Strength, Dexterity, and Constitution) should be relatively close to the base values presented on Table: Size, depending on its size. Creatures with a few Hit Dice but a high average hit point total should have a higher than normal Constitution.

A creature's mental ability scores (Intelligence, Wisdom, and Charisma) are largely defined by the creature's concept. The base for all of these abilities is 10. Creatures that rely on spells and spell-like abilities in combat should have one mental ability score that stands out (usually Charisma). Creatures incapable of speech have an Intelligence score of 2 or lower. Unintelligent undead, constructs, oozes, plants, and vermin rarely have an Intelligence score.

## Step 6: Skills and Feats

Using Table: Creature Statistics by Type, determine how many skill ranks your creature has based on its type and Hit Dice. Assign these ranks as determined by the creature's concept. A creature's class skill is determined by its type. Creatures with a low Intelligence typically only have ranks in Dexterity- and Strength-based skills.

After you have assigned skills, it's time to assign the creature's feats. Each creature with an Intelligence score receives a number of feats equal to 1 + 1 per every 2 Hit Dice after the first (so, 1 at 1 HD, 2 at 3 HD, etc.). A creature must qualify to take a feat as normal. See Table: Statistics Summary for a quick feat calculation chart.

**Table: Statistics Summary**

| HD  | Fast BAB | Medium BAB | Slow BAB | Good Save | Bad Save | Feats |
| --- | -------- | ---------- | -------- | --------- | -------- | ----- |
| 1   | +1       | +0         | +0       | +2        | +0       | 1     |
| 2   | +2       | +1         | +1       | +3        | +0       | 1     |
| 3   | +3       | +2         | +1       | +3        | +1       | 2     |
| 4   | +4       | +3         | +2       | +4        | +1       | 2     |
| 5   | +5       | +3         | +2       | +4        | +1       | 3     |
| 6   | +6       | +4         | +3       | +5        | +2       | 3     |
| 7   | +7       | +5         | +3       | +5        | +2       | 4     |
| 8   | +8       | +6         | +4       | +6        | +2       | 4     |
| 9   | +9       | +6         | +4       | +6        | +3       | 5     |
| 10  | +10      | +7         | +5       | +7        | +3       | 5     |
| 11  | +11      | +8         | +5       | +7        | +3       | 6     |
| 12  | +12      | +9         | +6       | +8        | +4       | 6     |
| 13  | +13      | +9         | +6       | +8        | +4       | 7     |
| 14  | +14      | +10        | +7       | +9        | +4       | 7     |
| 15  | +15      | +11        | +7       | +9        | +5       | 8     |
| 16  | +16      | +12        | +8       | +10       | +5       | 8     |
| 17  | +17      | +12        | +8       | +10       | +5       | 9     |
| 18  | +18      | +13        | +9       | +11       | +6       | 9     |
| 19  | +19      | +14        | +9       | +11       | +6       | 10    |
| 20  | +20      | +15        | +10      | +12       | +6       | 10    |
| 21  | +21      | +15        | +10      | +12       | +7       | 11    |
| 22  | +22      | +16        | +11      | +13       | +7       | 11    |
| 23  | +23      | +17        | +11      | +13       | +7       | 12    |
| 24  | +24      | +18        | +12      | +14       | +8       | 12    |
| 25  | +25      | +18        | +12      | +14       | +8       | 13    |
| 26  | +26      | +19        | +13      | +15       | +8       | 13    |
| 27  | +27      | +20        | +13      | +15       | +9       | 14    |
| 28  | +28      | +21        | +14      | +16       | +9       | 14    |
| 29  | +29      | +21        | +14      | +16       | +9       | 15    |
| 30  | +30      | +22        | +15      | +17       | +10      | 15    |

## Step 7: Other Statistics

Using Table: Monster Statistics by CR, Table: Creature Statistics by Type, and Table: Statistics Summary, you can now determine many of the creature's other statistics.

When building a creature's Armor Class, start by adding armor, shield, and natural armor bonuses to its Dexterity modifier. If a creature does not wear armor, give it a tougher hide to get it near its average AC. Remember that creatures with higher hit point totals might have a lower Armor Class, whereas creatures with fewer hit points might have a higher Armor Class. If a creature's Armor Class deviates from the average by more than 5 points, it might not be the right CR.

When determining a creature's attack bonuses, refer to the guidelines from Table: Monster Statistics by CR based on the creature's CR. If the bonus is too low, consider increasing the creature's Strength or Dexterity, or increasing the amount of damage it deals to above the average. If the bonus is too high, consider decreasing the creature's Strength or Dexterity, or decrease the amount of damage it deals. If this value is significantly different, and the creature is intended to rely on melee or ranged attacks, consider adjusting the creature's CR.

Use Table: Average Die Results to determine the number of damage dice, combined with damage bonuses, that the creature needs to reach the average damage for its CR. The creature might need additional or more damaging attacks to approach the average. Remember that creatures that primarily deal damage with other abilities, such as spells, do not need to meet the average damage for their attacks. You can also use Table: Average Die Results to determine a creature's average hit points. Remember that PC class levels provide the maximum number of hit points at 1st level.

Repeat this process for a creature's defenses. If the defenses are too high, consider altering the ability scores on which they are based.

When determining a creature's speed, first decide if it has any alternative modes of movement, such as burrow, climb, fly, or swim. Most Medium creatures have a base speed of 30 feet. Quadrupeds and Large creatures increase this by 10 feet each. Smaller creatures decrease this base speed by 10 feet. If a creature is particularly fast or slow, modify the base speed by 10 feet. Burrow and climb speeds are usually half a creature's base speed, while flying speeds are roughly double. Remember to give a creature the appropriate skills for any unusual movement methods.

**Table: Creature Statistics by Type**

| Type                                                                                                                                                                                    | Hit Die | Base Attack Bonus (BAB) | Good Saving Throws | Skill Ranks\*      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------- | ------------------ | ------------------ |
| Aberration                                                                                                                                                                              | d8      | HD × 3/4 (Medium BAB)   | Will               | 4 + Int mod per HD |
| Animal                                                                                                                                                                                  | d8      | HD × 3/4 (Medium BAB)   | Fort, Ref          | 2 + Int mod per HD |
| Construct                                                                                                                                                                               | d10     | HD (Fast BAB)           | —                  | 2 + Int mod per HD |
| Dragon                                                                                                                                                                                  | d12     | HD (Fast BAB)           | Fort, Ref, Will    | 6 + Int mod per HD |
| Fey                                                                                                                                                                                     | d6      | HD × 1/2 (Slow BAB)     | Ref, Will          | 6 + Int mod per HD |
| Humanoid                                                                                                                                                                                | d8      | HD × 3/4 (Medium BAB)   | Varies (any one)   | 2 + Int mod per HD |
| Magical beast                                                                                                                                                                           | d10     | HD (Fast BAB)           | Fort, Ref          | 2 + Int mod per HD |
| Monstrous humanoid                                                                                                                                                                      | d10     | HD (Fast BAB)           | Ref, Will          | 4 + Int mod per HD |
| Ooze                                                                                                                                                                                    | d8      | HD × 3/4 (Medium BAB)   | —                  | 2 + Int mod per HD |
| Outsider                                                                                                                                                                                | d10     | HD (Fast BAB)           | Varies (any two)   | 6 + Int mod per HD |
| Plant                                                                                                                                                                                   | d8      | HD × 3/4 (Medium BAB)   | Fort               | 2 + Int mod per HD |
| Undead                                                                                                                                                                                  | d8      | HD × 3/4 (Medium BAB)   | Will               | 4 + Int mod per HD |
| Vermin                                                                                                                                                                                  | d8      | HD × 3/4 (Medium BAB)   | Fort               | 2 + Int mod per HD |
| \* As long as a creature has an Intelligence of at least 1, it gains a minimum of 1 skill point per Hit Die. Creatures with an Intelligence score of “—” gain no skill points or feats. |         |                         |                    |                    |

## Step 8: Special Abilities and Qualities

Monsters are different from characters in that they can have all sorts of different special abilities and qualities. Each of these is tied closely to the creature's concept, allowing it to fill a specific role in the game. For examples, look at the existing monsters. Monsters should use abilities from the [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities|Universal Monster Rules]] whenever possible, instead of creating new yet similar abilities—when you do create new abilities, use the [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities|Universal Monster Rules]] as a template for how to present and create the new abilities.

Most special abilities that cause damage, such as breath weapons, attack a defense (Fortitude, Reflex, or Will depending on the ability). The attack bonus for almost all special abilities is equal to 1/2 the creature's Hit Dice + a relevant ability modifier (usually Constitution or Charisma depending on the ability). Special abilities that add to melee and ranged attacks generally do not attack a defense, as they rely on the attacks hitting to be useful.

Special senses and resistances to certain energy types are common in creatures of CR 5 and lower. Damage reduction, energy immunities, and regeneration are more common in creatures above CR 5. Spell resistance and immunities become more common above CR 10. As a general rule a creature's spell resistance should equal its CR + 11.

## Step 9: Treasure

A creature should have an amount of treasure appropriate to its CR. See [[rangoric-srd/unearthed-arcana/XP and GP Values by CR|Table: XP and GP Values by CR]] for a list of treasure totals based on CR; Rangoric’s own treasure per encounter is [[rangoric-srd/rules/Treasure#Using the Treasure Table|Treasure Values per Encounter]]. For some creatures, their treasure consists of the loot from their recent meals strewn across their lairs, while for others it consists of a greed-fueled hoard or even gear it uses in combat. Make sure to account for any weapons or armor that the creature is using, as determined by step 7.

## Step 10: Details

Now that you have all of the creature's statistics sorted out, it's time to fill in all the details—such as name, alignment, space, reach, environment, and ecology—as you see fit.

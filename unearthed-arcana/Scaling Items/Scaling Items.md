---
srd-type: "rules"
section: "Unearthed Arcana"
book: "Pathfinder Unchained"
based-on:
  - "[[path srd 3.5/rules/pathfinder-unchained/Scaling Items|Scaling Items (PF1 Unchained)]]"
status: draft
change: new
pi-review: 2026-11-23
tags: [rangoric, rangoric/rules]
---

# Scaling Items

Typically, player characters find themselves buying and selling magic items as they gain levels to keep up with the increasing threats they face. Items come and go from each character's inventory with such frequency that they hardly have the chance to impact the game's story. Scaling items, however, increase in power along with the characters who carry them, allowing an old and cherished item to develop and retain its utility rather than being sold and forgotten.

Scaling items work like normal magic items, but they gain new powers as their wielders gain levels, and their existing powers sometimes also improve. Additional item powers appear in a scaling magic item's entry with a header indicating the character level at which they unlock.

The caster level of the item scales up as well. A scaling item's effective caster level is its listed caster level or the character level of its wielder, whichever is higher, to a maximum of the item's highest-level ability. For instance, if an item has a base caster level of 5th and additional abilities at 7th and 9th levels, it's treated as caster level 8th in the hands of an 8th-level character, but is treated as only caster level 9th in the hands of a 10th-level character.

Each scaling item has a base price that represents its value to a character whose level is equal to or less than the item's caster level. As the item's caster level increases in the hands of a more powerful character, the item's value increases as well. The values of such items fall into three categories (baubles, prizes, and wonders), which indicate the rough percentage of the character's wealth a scaling item represents.

The weakest items, baubles, represent 5% of a PC's [[rangoric-srd/rules/Treasure#^character-wealth-by-level|character wealth at her level]] and can be compared to consumable magic items (even though baubles aren't destroyed by use). Items in the middle category, prizes, represent 15% of a PC's suggested wealth and correspond to magic items of moderate power. An item of the most valuable category, wonders, represents 30% of a PC's suggested wealth and corresponds to a major magic item, such as a fighter's most beloved and powerful sword. Wonders exceed the normal cost assumptions of the game at their highest level. Such items approach the power of minor artifacts, though they're not indestructible and can still be created normally.

## Adjusting Treasure

Since scaling items improve as characters level up, they effectively add wealth to their owners over time. To balance this out, the Game Master should reduce treasure awards in proportion to how many scaling items the party has. This can be done per character or for the whole group, as described below. Note that the original level and price of a scaling item don't matter once the character's level exceeds the minimum caster level of the item, since the item accrues value based on its category (bauble, prize, or wonder), not on its original price. The adjustments to treasure awards are the same for all items in a category.

**Table: Value of Scaling Items**

| Level | Bauble (5%) | Prize (15%) | Wonder (30%) |
| ----- | ----------- | ----------- | ------------ |
| 1st   | 15 gp       | 45 gp       | 90 gp        |
| 2nd   | 50 gp       | 150 gp      | 300 gp       |
| 3rd   | 150 gp      | 450 gp      | 900 gp       |
| 4th   | 300 gp      | 900 gp      | 1,800 gp     |
| 5th   | 525 gp      | 1,575 gp    | 3,150 gp     |
| 6th   | 800 gp      | 2,400 gp    | 4,800 gp     |
| 7th   | 1,175 gp    | 3,525 gp    | 7,050 gp     |
| 8th   | 1,650 gp    | 4,950 gp    | 9,900 gp     |
| 9th   | 2,300 gp    | 6,900 gp    | 13,800 gp    |
| 10th  | 3,100 gp    | 9,300 gp    | 18,600 gp    |
| 11th  | 4,100 gp    | 12,300 gp   | 24,600 gp    |
| 12th  | 5,400 gp    | 16,200 gp   | 32,400 gp    |
| 13th  | 7,000 gp    | 21,000 gp   | 42,000 gp    |
| 14th  | 9,250 gp    | 27,750 gp   | 55,500 gp    |
| 15th  | 12,000 gp   | 36,000 gp   | 72,000 gp    |
| 16th  | 15,750 gp   | 47,250 gp   | 94,500 gp    |
| 17th  | 20,500 gp   | 61,500 gp   | 129,000 gp   |
| 18th  | 26,500 gp   | 79,500 gp   | 159,000 gp   |
| 19th  | 34,250 gp   | 102,750 gp  | 205,500 gp   |
| 20th  | 44,000 gp   | 132,000 gp  | 264,000 gp   |
^value-of-scaling-items

**Per Character**: If you apply the scaling item treasure reduction for each character, do so after dividing up shares of treasure for the characters. Reduce the treasure received by a character with a scaling item by the percentage listed for the item's category (5% for baubles, 15% for prizes, and 30% for wonders). If the character has multiple scaling items, combine the percentages before adjusting the amount of treasure.

For example, a PC with a wonder and a prize would receive 45% less treasure, because the PC has effectively already received that amount of treasure in the form of the items' increased values. Since the value of a scaling item is based on wealth for an entire level, apply this adjustment to every treasure allotment the character receives. If you'd prefer to keep the adjustments more tied to the game world, you can instead replace the character's lost treasure share with a magical substance that must be used to increase the power of scaling items. This might be magical residue, vibrant crystals, or spellbook-style pages of magical phrases that increase the item's power. In any case, this substance should be treated as almost worthless to sell, and therefore useful only for upgrading scaling items.

**Group Basis**: You can use the scaling items of the whole party to adjust treasure. This implementation works best if all or most of the characters possess scaling items, and no character possesses a far higher number than the others. This method has the advantage of hiding behind the scenes, requiring no in-game justification. Add up the percentages of all scaling items owned by all PCs. Divide this percentage by the number of PCs, and reduce the total value of treasure the party finds by that percentage before dividing it among the characters. For example, if a group of four PCs have between them one bauble, three prizes, and a wonder, their treasure is reduced by 20% (80% divided by 4).

## Maximum Level

Many scaling items unlock new powers all the way up to 20th level. Others reach the caps on their abilities at lower levels. Once an item reaches the level of its most powerful ability, stop adjusting treasure for that item. At that point, the scaling item is considered fully "paid for."

## Mismatched Levels

If a PC receives a scaling item of a caster level lower than her character level, she effectively receives an item that's worth more than the price listed in the stat block. Reference [[#^value-of-scaling-items|Table: Value of Scaling Items]] and use the PC's level to estimate how much the item is really worth to that PC, and use that purchase price as its treasure value. Giving an item with a caster level higher than the character's level doesn't present the same problems; it just means the PC won't be unlocking the item's higher-level powers for some time. Don't reduce treasure for such an item until the PC's level exceeds the item's caster level.

## Buying and Selling

Selling a scaling item presents a tricky balance proposition. Such an item is worth more to a higher-level buyer, and a high-level seller has spent more effective wealth acquiring and keeping the item. The maximum amount a PC can get for a scaling item is half the value (as normal for selling magic items) listed on [[#^value-of-scaling-items|Table: Value of Scaling Items]] for the item's category and the PC's current level. To get this amount, the PC must find a motivated buyer of her level or higher, which may involve considerable time and effort. If the PC must sell in a hurry, she might get 25% of the listed value, or even less. A PC can't sell a scaling item for more than 50% of the item's value for her current level, even if she sells it to a higher-level NPC.

## Crafting

Scaling items must be crafted at their highest level of power, with a cost determined by referencing [[#^value-of-scaling-items|Table: Value of Scaling Items]]. Start with the value listed on the table for the item's category and its highest-level ability. Divide this by 2 to get the crafting cost, and add the value of any nonmagical armor or weapon component. The crafting cost is always much higher than the market price of a scaling item, since the crafting cost is based on the full set of abilities but the market price is based on the minimum caster level. When a PC crafts a scaling item, he doesn't need to pay any further cost in reduced treasure for keeping the item, because the full value of the item has already been accounted for. When setting the DC for crafting a scaling item, use the item's highest-level ability instead of its base caster level. Crafting also costs experience points as in the base rules (1/25 of the base price, see [[rangoric-srd/magic-items/Creating Magic Items|Creating Magic Items]]); the costs given here are the gp only.

## Pricing New Scaling Items

To determine the price when creating a new scaling item, determine the cost of the base item without any of the level-based upgrades, and increase that price based on each additional ability as described below.

**Pricing the Base Item**: First, decide whether the new item is a wonder (best for major items), a prize (best for utility items), or a bauble (suitable for items that are interesting but not significant). Price the base item according to the normal rules for [[rangoric-srd/magic-items/Creating Magic Items|creating magic items]]. Then, using the column on [[#^value-of-scaling-items|Table: Value of Scaling Items]] that corresponds to the item's category, find the lowest gp value that includes that initial price. Use that value to determine the item's starting caster level.

**Adding Scaling Abilities**: Use the following steps to assign additional abilities and spells, and the levels at which those abilities unlock.

*Adding Unlockable Abilities*: Determine the first unlockable ability or increase in power. Price the item again, using the new ability plus all the abilities of the base item; you will use this price to determine the level at which the ability unlocks (see below). However, because many scaling items have a large range of limited-use abilities, following the standard rules can result in items that are too expensive for their actual utility. Therefore, on worn items, you should typically waive the 50% increase in price for an additional power unless it's a particularly useful ability or has a strong synergy with the item's other abilities. For instance, if you create a set of gloves with a *[[rangoric-srd/spells/Burning Hands|burning hands]]* effect, you wouldn't need to pay the extra cost for a higher-level ability that grants you fire resistance, but you would for an ability that grants fire resistance to all allies within 10 feet of you since that ability complements *[[rangoric-srd/spells/Burning Hands|burning hands]]* so well.

*Adding Spells*: Assign a price for any spells the item allows its owner to use. [[#^spell-prices|Table: Spell Prices]] includes the typical prices of one daily use of spells at different caster levels. Because the price of spells varies based on the item's caster level, it's usually best to price other abilities first, then estimate the finished caster level, then price the spell at that caster level. If a spell doesn't improve significantly at higher caster levels, price it using the item's minimum caster level. If the spell becomes more powerful with level increases (as does *[[rangoric-srd/spells/Fireball|fireball]]*), use the caster level of the level at which it's unlocked to determine its price. Cap a spell's caster level at the highest level that makes a significant difference, such as 10th level for *[[rangoric-srd/spells/Fireball|fireball]]*. Generally, if only the spell's duration changes with caster level, spells with a duration of 1 minute per level or 1 round per level should use the full caster level, but those with longer durations (10 minutes per level or more) should use the minimum caster level.

Remember to readjust the price at each further power unlock level, since the caster level of the item will match the owner's level. On a worn item, waive the standard 50% price increase on the additional spells.

*Assigning an Unlock Level*: Now that you have a cost for the next scaling ability, assign a level at which that ability unlocks. This follows the same process as the Pricing the Base Item step, but using the new cost. You should usually round down, but if you're almost at the higher-level price, bump up the level. For example, a prize that priced out at 8,000 gp at a given set of powers would unlock those powers at 9th level (6,900 gp), but if the price hits 9,000 gp, the abilities should instead unlock at 10th level (9,300 gp).

**Completing the Item**: Repeat this process for each set of new powers. Try to add a new unlockable ability every 2 to 4 levels. It's not necessary to scale every item all the way to 20th level, however—stop when the set of abilities feels complete.

**Table: Spell Prices (One Use per Day), spell level across, caster level down**

| CL   | 0        | 1        | 2         | 3         | 4         | 5         | 6         | 7         | 8         | 9         |
| ---- | -------- | -------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| 1st  | 180 gp   | 360 gp   | —         | —         | —         | —         | —         | —         | —         | —         |
| 2nd  | 360 gp   | 720 gp   | —         | —         | —         | —         | —         | —         | —         | —         |
| 3rd  | 540 gp   | 1,080 gp | 2,160 gp  | —         | —         | —         | —         | —         | —         | —         |
| 4th  | 720 gp   | 1,440 gp | 2,880 gp  | —         | —         | —         | —         | —         | —         | —         |
| 5th  | 900 gp   | 1,800 gp | 3,600 gp  | 5,400 gp  | —         | —         | —         | —         | —         | —         |
| 6th  | 1,080 gp | 2,160 gp | 4,320 gp  | 6,480 gp  | —         | —         | —         | —         | —         | —         |
| 7th  | 1,260 gp | 2,520 gp | 5,040 gp  | 7,560 gp  | 10,080 gp | —         | —         | —         | —         | —         |
| 8th  | 1,440 gp | 2,880 gp | 5,760 gp  | 8,640 gp  | 11,520 gp | —         | —         | —         | —         | —         |
| 9th  | 1,620 gp | 3,240 gp | 6,480 gp  | 9,720 gp  | 12,960 gp | 16,200 gp | —         | —         | —         | —         |
| 10th | 1,800 gp | 3,600 gp | 7,200 gp  | 10,800 gp | 14,400 gp | 18,000 gp | —         | —         | —         | —         |
| 11th | 1,980 gp | 3,960 gp | 7,920 gp  | 11,880 gp | 15,840 gp | 19,800 gp | 23,760 gp | —         | —         | —         |
| 12th | 2,160 gp | 4,320 gp | 8,640 gp  | 12,960 gp | 17,280 gp | 21,600 gp | 25,920 gp | —         | —         | —         |
| 13th | 2,340 gp | 4,680 gp | 9,360 gp  | 14,040 gp | 18,720 gp | 23,400 gp | 28,080 gp | 32,760 gp | —         | —         |
| 14th | 2,520 gp | 5,040 gp | 10,080 gp | 15,120 gp | 20,160 gp | 25,200 gp | 30,240 gp | 35,280 gp | —         | —         |
| 15th | 2,700 gp | 5,400 gp | 10,800 gp | 16,200 gp | 21,600 gp | 27,000 gp | 32,400 gp | 37,800 gp | 43,200 gp | —         |
| 16th | 2,880 gp | 5,760 gp | 11,520 gp | 17,280 gp | 23,040 gp | 28,800 gp | 34,560 gp | 40,320 gp | 46,080 gp | —         |
| 17th | 3,060 gp | 6,120 gp | 12,240 gp | 18,360 gp | 24,480 gp | 30,600 gp | 36,720 gp | 42,840 gp | 48,960 gp | 55,080 gp |
| 18th | 3,240 gp | 6,480 gp | 12,960 gp | 19,440 gp | 25,920 gp | 32,400 gp | 38,880 gp | 45,360 gp | 51,840 gp | 58,320 gp |
| 19th | 3,420 gp | 6,840 gp | 13,680 gp | 20,520 gp | 27,360 gp | 34,200 gp | 41,040 gp | 47,880 gp | 54,720 gp | 61,560 gp |
| 20th | 3,600 gp | 7,200 gp | 14,400 gp | 21,600 gp | 28,800 gp | 36,000 gp | 43,200 gp | 50,400 gp | 57,600 gp | 64,800 gp |
^spell-prices

## Standalone Scaling Items

A GM can include specific scaling items as individual pieces of treasure even if she isn't using the scaling items system in her game. The base item can be used without any of the higher-level upgrades, or the GM can pick a higher level and create an individual item that has the base abilities plus one or more unlocked levels. She should use the standard price for that level of scaling item, as described on [[#^value-of-scaling-items|Table: Value of Scaling Items]].

For example, a GM could give out a [[rangoric-srd/unearthed-arcana/Scaling Items/weapons/Spear of the Huntmaster|spear of the huntmaster]] as a CL 6th item worth 3,202 gp with just the base abilities, a CL 8th item worth 4,950 gp with the base abilities plus the 8th-level unlockable ability, a CL 10th item worth 9,300 gp with the base abilities plus the 8th- and 10th-level unlockable abilities, and so on.

## Scaling Items

The following scaling items include several examples of wonders, prizes, and baubles.

### Specific Armor and Shields

The following section includes armor and shields with unusual powers and magical abilities. Magic armor can have abilities that need to be activated to function or powers that work passively and constantly.

- [[rangoric-srd/unearthed-arcana/Scaling Items/armor/Armageddon Plate|Armageddon Plate]] (wonder, CL 5th, 2,650 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/armor/Armor of the Celestial Host|Armor of the Celestial Host]] (prize, CL 9th, 6,900 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/armor/Dragonshield|Dragonshield]] (prize, CL 14th, 28,557 gp)

### Specific Weapons

The following section includes weapons with unusual powers and magical abilities. Magic weapons can have abilities that need to be activated to function or powers that work passively and constantly.

- [[rangoric-srd/unearthed-arcana/Scaling Items/weapons/Legacy Arrow|Legacy Arrow]] (bauble, CL 4th, 305 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/weapons/Multimetal Mace|Multimetal Mace]] (prize, CL 6th, 2,650 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/weapons/Sacred Avenger|Sacred Avenger]] (wonder, CL 6th, 4,800 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/weapons/Spear of the Huntmaster|Spear of the Huntmaster]] (prize, CL 6th, 2,650 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/weapons/Thirsting Blade|Thirsting Blade]] (wonder, CL 6th, 4,800 gp)

### Rings

Rings bestow magical powers upon their wearers. Anyone can use a ring, but a character can gain the benefits of only two magic rings at a time.

- [[rangoric-srd/unearthed-arcana/Scaling Items/rings/Fivefold Rings of Fire|Fivefold Rings of Fire]] (prize, CL 10th, 10,800 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/rings/Ring of the Drake (Flame)|Ring of the Drake (Flame)]] (prize, CL 9th, 6,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/rings/Ring of the Drake (Forest)|Ring of the Drake (Forest)]] (prize, CL 9th, 6,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/rings/Ring of the Drake (Frost)|Ring of the Drake (Frost)]] (prize, CL 9th, 6,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/rings/Ring of the Drake (Sea)|Ring of the Drake (Sea)]] (prize, CL 9th, 6,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/rings/Ring of the Earthlord|Ring of the Earthlord]] (wonder, CL 6th, 4,800 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/rings/Ring of the Trickster|Ring of the Trickster]] (prize, CL 4th, 1,080 gp)

### Rods

Rods are scepterlike devices that have unique magical powers and usually do not have any charges. Anyone can use a rod.

- [[rangoric-srd/unearthed-arcana/Scaling Items/rods/Mimetic Rod|Mimetic Rod]] (bauble, CL 7th, 1,350 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/rods/Rod of the Deadlord|Rod of the Deadlord]] (wonder, CL 9th, 16,005 gp)

### Staves

A staff is a long shaft that stores several spells. Staves usually hold spells grouped by a theme and sometimes possess other abilities that they grant to the wielder. A staff has 10 charges when created but can be recharged by a spellcaster with the appropriate spells.

- [[rangoric-srd/unearthed-arcana/Scaling Items/staves/Staff of the Pyre Lord|Staff of the Pyre Lord]] (wonder, CL 8th, 8,800 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/staves/Staff of Ways|Staff of Ways]] (prize, CL 10th, 8,000 gp)

### Wondrous Items

Wondrous items are diverse. Some must be worn in a specific magic item slot in order to work, while others must merely be possessed and used. "Wondrous item" is a catchall category for anything that doesn't fall into other groups, such as weapons, staves, and so on. Anyone can use a wondrous item, unless the item specifies otherwise.

There are two main categories of wondrous items: slotted and slotless. Slotted items take up a magic item slot, and must be worn by those who want to benefit from them.

- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Arachnid Cloak|Arachnid Cloak]] (prize, CL 4th, 900 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Bag of Endless Holding|Bag of Endless Holding]] (bauble, CL 10th, 3,100 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Bat Cloak|Bat Cloak]] (prize, CL 4th, 900 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Beaker of Plentiful Poisons|Beaker of Plentiful Poisons]] (prize, CL 7th, 3,600 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Boots of Readiness|Boots of Readiness]] (bauble, CL 9th, 2,650 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Boots of the Elven Spirit|Boots of the Elven Spirit]] (bauble, CL 10th, 3,100 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Bracelets of the Fey Touch|Bracelets of the Fey Touch]] (bauble, CL 4th, 480 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Brutish Boots|Brutish Boots]] (wonder, CL 8th, 5,814 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Cloak of the Elven Spirit|Cloak of the Elven Spirit]] (bauble, CL 12th, 5,400 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Cord of Unearthly Grace|Cord of Unearthly Grace]] (prize, CL 8th, 5,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Crystal Tiara|Crystal Tiara]] (wonder, CL 3rd, 1,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Dragon Robe|Dragon Robe]] (wonder, CL 12th, 38,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Eternal Feather Token|Eternal Feather Token]] (bauble, CL 4th, 2,650 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Filthy Rags|Filthy Rags]] (prize, CL 8th, 5,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Flask of Reconcoction|Flask of Reconcoction]] (bauble, CL 4th, 2,650 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Force Bracers|Force Bracers]] (prize, CL 8th, 5,950 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Forgemaster's Gauntlets|Forgemaster's Gauntlets]] (prize, CL 7th, 3,750 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Fruitful Sash|Fruitful Sash]] (bauble, CL 5th, 710 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Galvanic Gauntlets|Galvanic Gauntlets]] (prize, CL 5th, 1,882 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Glorious Gorget|Glorious Gorget]] (prize, CL 8th, 5,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Gloves of Cloud Shaping|Gloves of Cloud Shaping]] (prize, CL 8th, 5,400 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Heart of the Elder Tree|Heart of the Elder Tree]] (wonder, CL 9th, 14,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Heroic Saddle|Heroic Saddle]] (prize, CL 8th, 6,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Lantern Pendant|Lantern Pendant]] (prize, CL 4th, 1,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Mark of the Grinning Skull|Mark of the Grinning Skull]] (bauble, CL 8th, 2,000 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Mask of Mad Memories|Mask of Mad Memories]] (prize, CL 6th, 2,500 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Necklace of Infernos|Necklace of Infernos]] (prize, CL 10th, 9,300 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Pearl of Puissance|Pearl of Puissance]] (prize, CL 5th, 1,575 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Pouch of Pixie Dust|Pouch of Pixie Dust]] (bauble, CL 1st, 15 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Robe of the Faerie Queen|Robe of the Faerie Queen]] (wonder, CL 6th, 4,800 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Spectacles of Thought-Seeing|Spectacles of Thought-Seeing]] (prize, CL 7th, 3,600 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Star of Vision|Star of Vision]] (prize, CL 11th, 14,400 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Stargazer's Glass|Stargazer's Glass]] (bauble, CL 7th, 1,250 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Strand of Many Prayer Beads|Strand of Many Prayer Beads]] (prize, CL 4th, 900 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Vest of Golden Leaves|Vest of Golden Leaves]] (prize, CL 6th, 2,400 gp)
- [[rangoric-srd/unearthed-arcana/Scaling Items/wondrous-items/Vest of Eldritch Preservation|Vest of Eldritch Preservation]] (prize, CL 9th, 8,000 gp)

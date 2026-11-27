---
srd-type: "rule"
section: "Rules"
status: draft
pi-review: 2026-11-25
tags: [rangoric, rangoric/rule]
---

# Base Attack Bonus

Like [[rangoric-srd/rules/Saving Throws|Saving Throws]], we will be using fractional BAB, so medium and weak BABs don't fall that far behind based on which level someone leaves off at.

Each class gives one of three base attack bonus progressions, named in its Base Attack Bonus line and its `bab` property:

| Progression | Base attack bonus per level |
| ----------- | --------------------------- |
| Full        | 1                           |
| Medium      | 3/4                         |
| Weak        | 1/2                         |

**More than one class**: every base attack bonus fraction a character has, from all of their classes and prestige classes, adds together, and the total is rounded down only at the end.

**Table: Base Attack Bonus by Level** ^table-base-attack-bonus-by-level

A character with levels in only one class has the base attack bonus below for their level, with the fraction kept. A base attack bonus of +6 or more gives extra attacks with a full attack ([[rangoric-srd/combat/Combat Actions#^multiple-attacks|Multiple Attacks]]), shown in brackets: each is 5 lower than the one before.

| Level | Full                 | Medium              | Weak           |
| ----- | -------------------- | ------------------- | -------------- |
| 1st   | +1                   | +0 3/4              | +0 1/2         |
| 2nd   | +2                   | +1 1/2              | +1             |
| 3rd   | +3                   | +2 1/4              | +1 1/2         |
| 4th   | +4                   | +3                  | +2             |
| 5th   | +5                   | +3 3/4              | +2 1/2         |
| 6th   | +6 (+6/+1)           | +4 1/2              | +3             |
| 7th   | +7 (+7/+2)           | +5 1/4              | +3 1/2         |
| 8th   | +8 (+8/+3)           | +6 (+6/+1)          | +4             |
| 9th   | +9 (+9/+4)           | +6 3/4 (+6/+1)      | +4 1/2         |
| 10th  | +10 (+10/+5)         | +7 1/2 (+7/+2)      | +5             |
| 11th  | +11 (+11/+6/+1)      | +8 1/4 (+8/+3)      | +5 1/2         |
| 12th  | +12 (+12/+7/+2)      | +9 (+9/+4)          | +6 (+6/+1)     |
| 13th  | +13 (+13/+8/+3)      | +9 3/4 (+9/+4)      | +6 1/2 (+6/+1) |
| 14th  | +14 (+14/+9/+4)      | +10 1/2 (+10/+5)    | +7 (+7/+2)     |
| 15th  | +15 (+15/+10/+5)     | +11 1/4 (+11/+6/+1) | +7 1/2 (+7/+2) |
| 16th  | +16 (+16/+11/+6/+1)  | +12 (+12/+7/+2)     | +8 (+8/+3)     |
| 17th  | +17 (+17/+12/+7/+2)  | +12 3/4 (+12/+7/+2) | +8 1/2 (+8/+3) |
| 18th  | +18 (+18/+13/+8/+3)  | +13 1/2 (+13/+8/+3) | +9 (+9/+4)     |
| 19th  | +19 (+19/+14/+9/+4)  | +14 1/4 (+14/+9/+4) | +9 1/2 (+9/+4) |
| 20th  | +20 (+20/+15/+10/+5) | +15 (+15/+10/+5)    | +10 (+10/+5)   |

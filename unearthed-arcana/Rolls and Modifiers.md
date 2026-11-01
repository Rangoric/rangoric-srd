---
srd-type: "overview"
section: "Unearthed Arcana"
based-on:
  - "[[fantasy srd 3.5/unearthed-arcana/Rolls and Modifiers|Rolls and Modifiers (3.5)]]"
status: draft
change: modified
pi-review: scanned 2026-10-15
tags: [rangoric, rangoric/overview]
---

## Unearthed Arcana

### Bell Curve Rolls

Here’s perhaps the most fundamental variant to the d20 rules: Don’t use a d20\! Instead, roll 3d6 whenever you would roll a d20, applying bonuses and penalties normally. The possible results when rolling 3d6 (or any other multiple dice) form a bell curve — that is, a range of odds that favors average results much more than extreme results.

##### Behind the Curtain: The Bell Curve

In general, this variant leads to a grittier d20 game, because there will be far fewer very good or very bad rolls. Not only can you no longer roll 1, 2, 19 or 20, but most rolls will be clustered around the average of 10.5. With a d20, every result is equally likely; you have a 5% chance of rolling an 18 and a 5% chance of rolling a 10. With 3d6, there’s only one possible combination of dice that results in an 18 (three sixes, obviously), but there are twenty-four combinations that result in a 10. Players used to the thrill of rolling high and the agony of a natural 1 will get that feeling less often — but it may be more meaningful when it does happen. Good die rolls are a fundamental reward of the game, and it changes the character of the game when the rewards are somewhat stronger but less frequent.

Game balance shifts subtly when you use the bell curve variant. Rolling 3d6 gives you a lot more average rolls, which favors the stronger side in combat. And in the d20 game, that’s almost always the PCs. Many monsters — especially low-CR monsters encountered in groups — rely heavily on a lucky shot to damage PCs. When rolling 3d6, those lucky shots are fewer and farther between. In a fair fight when everyone rolls a 10, the PCs should win almost every time. The bell curve variant adheres more tightly to that average (which is the reason behind the reduction in CR for monsters encountered in groups).

Another subtle change to the game is that the bell curve variant awards bonuses relatively more and the die roll relatively less, simply because the die roll is almost always within a few points of 10. A character’s skill ranks, ability scores, and gear have a much bigger impact on success and failure than they do in the standard d20 rules.

##### Rules for Rolling

This system requires several changes to how rolls are made.

**Automatic Successes and Failures:** Automatic successes (for attack rolls and saves) happen on a natural 18, and automatic failures on a natural 3. Neither occurs as often as in standard d20 (less than 1/2% of the time as opposed to 5% of the time). ^automatic-successes-and-failures

**Taking 20 and taking 10:** You can’t take 20 using the bell curve variant. Instead, you have two new options: You can take 16, which makes the task take ten times as long, or you can take 18, which makes the task take one hundred times as long. As with the rules for taking 20, you can only take 16 and 18 when you have plenty of time, when you aren’t distracted, and when the task carries no consequences for failure. For a check that normally requires a standard action, taking 16 uses up 1 minute and taking 18 uses up 10 minutes. ^taking-20-and-taking-10

The rules for taking 10 remain unchanged.

**Threat Range:** Because it’s no longer possible to roll a natural 19 or 20, the threat ranges of weapons change in the bell curve variant. Refer to the following table. ^threat-range

With the bell curve variant, the narrowest threat range becomes slightly more narrow (4.6% rather than 5%), and the new 14-18 range (16%) falls between the old 18-20 and 17-20 ranges. But because the [[rangoric-srd/feats/Improved Critical|Improved Critical]] feat and the [[rangoric-srd/spells/Keen Edge|keen edge]] spell double threat ranges, characters still improve their weapons in every case, despite the flat spot on the table.

There’s no table entry for a threat range of 16-20 because no combination weapons, feats, and magic can attain it in the standard d20 rules.

**Table: Threat Range Conversion**

| Old Threat Range | New Threat Range |
| ---------------- | ---------------- |
| 20               | 16-18            |
| 19-20            | 15-18            |
| 18-20            | 14-18            |
| 17-20            | 14-18            |
| 15-20            | 13-18            |

##### Monster Challenge Ratings

Any time creatures are encountered in groups of four or more, reduce their CR by 1. For example, a single troll is CR 5, and two trolls are CR 5 each (and thus a EL 7 encounter). But four trolls are only CR 4 each (making a EL 8 encounter).

Monsters with fractional CRs move down to the next lowest fraction when encountered in groups of four or more; the goblin (ordinarily CR 1/2) becomes CR 1/3, for example.

##### The Luck Domain

The granted power of the [[rangoric-srd/classes/Cleric Domains|Luck domain]] changes, because simple rerolls aren’t as useful in the bell curve variant as they are in the standard rules. When electing to reroll a result, a cleric with access to the Luck domain rolls a 4d6 for the reroll (instead of a 3d6), dropping the lowest die. For example, if you rolled 2, 5, 6 and 6, you would drop the 2 for a total of 17.

The Luck domain’s spells change as well, with auspicious odds replacing protection from energy at 3rd level and mass auspicious odds replacing break enchantment at 5th level.

###### Auspicious Odds

Evocation

  - **Level**: Luck 3
  - **Components**: V, S, M, DF
  - **Casting Time**: 1 standard action
  - **Range**: Touch
  - **Target**: Creature Touched
  - **Duration**: 1 minute/level; see text
  - **Saving Throw**: Will negates (harmless)
  - **Spell Resistance**: Yes (harmless)

Whenever making an attack roll, saving throw, ability check, or skill check, the subject rolls 4d6 and drops the lowest single die roll from the total rather than rolling 3d6. If, on a single roll, all four die results are 1s, the spell immediately ends.

*Material Component:* A copper piece.

###### Auspicious Odds, Mass

Evocation

  - **Level**: Luck 5
  - **Range**: Close (25 0 5ft./2 levels)
  - **Target**: One creature/three levels, no two of which can be more than 30 ft. apart
  - **Duration**: 1 round/level; see text

As [[#Auspicious Odds|auspicious odds]], except that this spell affects multiple targets and the duration is shorter. If, on a single roll, all four die results are 1s, the spell immediately ends for that subject only, unless it’s the caster, in which case it ends for everyone.

### Players Roll All the Dice

In large combats, players often have little control over the outcome of events when it isn’t their turn. This can lead to boredom if a player’s attention drifts between his turns, threatening to distance him from the outcome of events.

One method of dealing with this problem is to put more dice rolling into your players’ hands: allow your players to make all of the dice rolls during the combat.

##### Attacking and Defending

With this variant, PCs make their attacks just like they do in the standard rules. Their opponents, however, do not. Each time an enemy attacks a PC, the character’s player rolls a defense check. If that defense check equals or exceeds the attack score of the enemy, the attack misses.

To determine a creature’s attack score, add 11 to the creature’s standard attack modifier (the number it would use, as either a bonus or penalty to its attack roll, if it were attacking an ordinary situation using the standard rules). For instance, an [[rangoric-srd/monsters/ogre/Ogre|ogre]] has a standard attack modifier of +8 with its greatclub. That means that it’s attack score is 19.

To make a defense check, roll 1d20 and add any modifiers that normally apply to your Armor Class (armor, size, deflection, and the like). This is effectively the same as rolling d20, adding your total AC, and then subtracting 10.

|                |                                 |
| -------------- | ------------------------------- |
| Attack Score:  | 11 + enemy’s attack bonus       |
| Defense Check: | 1d20 + character’s AC modifiers |

If a player rolls a natural 1 on a defense check, his character’s opponent has scored a threat (just as if it had rolled a natural 20 on its attack roll). Make another defense check; if it again fails to avoid the attack, the opponent has scored a critical hit.

When a PC attacks an opponent, he makes an attack roll against the opponent’s AC as normal.

##### Saving Throws and Save Scores

With this variant, NPCs and other opponents no longer make saving throws to avoid special attacks of player characters. Instead, each creature has a Fortitude, Reflex, and Will score. These scores are equal to 11 + the creature’s Fortitude, Reflex, and Will save modifiers.

Any time you cast a spell or use a special attack that forces an opponent to make a saving throw, instead make a magic check to determine your success. To make a magic check, roll 1d20 and add all the normal modifiers to any DC required by the spell or special attack (including the appropriate ability modifier, the spell’s level if casting a spell, the adjustment for [[rangoric-srd/feats/Spell Focus|Spell Focus]], and so on).

If the result of the magic check equals or exceeds the appropriate save score (Fortitude, Reflex or Will, depending on the special ability), the creature is affected by the spell or special attack as if it had failed its save. If the result is lower than the creature’s Fortitude, Reflex or Will score (as appropriate to the spell or special attack used), the creature is affected as if it had succeeded on its save.

|                  |                                                        |
| ---------------- | ------------------------------------------------------ |
| Magic Check:     | 1d20 + spell level + ability modifer + other modifiers |
| Fortitude Score: | 11 + enemy’s Fortitude save modifier                   |
| Reflex Score:    | 11 + enemy’s Reflex save modifier                      |
| Will Score:      | 11 + enemy’s Will save modifier                        |

If a player rolls a natural 20 on a magic check, the creature’s equipment may take damage (just as if it had rolled a natural 1 on its save; see Items Surviving after a Saving Throw).

##### Spell Resistance

If a PC has spell resistance, his player makes a spell resistance check against each incoming spell that allows spell resistance. A spell resistance check is 1d20 plus the PC’s spell resistance, minus 10.

The DC of this check is equal to 11 + the attacker’s caster level, plus any modifiers that normally apply to the attacker’s caster level check to overcome spell resistance (such as from the [[rangoric-srd/feats/Spell Penetration|Spell Penetration]] feat). That value is known as the attacker’s caster level score. If the spell resistance check equals or exceeds this number, the spell fails to penetrate the PC’s spell resistance.

To beat a creature’s spell resistance, a player makes a caster level check (1d20 + caster level) against its spell resistance, just as in the standard rules.

|                         |                                          |
| ----------------------- | ---------------------------------------- |
| Spell Resistance Check: | 1d20 + SR - 10                           |
| Caster Level Score:     | 11 + attacker’s caster level + modifiers |

##### Behind the Curtain: Players Rolling Dice

This variant takes a lot of the work out of the GM’s hands, since he no longer needs to make attack rolls, saving throws, or caster level checks to overcome spell resistance for his NPCs and monsters. That can free up his attention for more important things, such as NPC tactics, special spell effects, terrain, and the like.

Conversely, it requires the players to become much more active and aware of what’s going on. No longer can players snooze through all the turns but their own: They’ll be rolling more dice than ever before — which (among other benefits) gives them the feeling of having greater control over their successes and failures.

One drawback is that it takes away some of the GM’s ability to adjust encounters on the fly. Since the GM isn’t rolling the dice, he can’t fudge a result to give the characters a break (or take one away). Thus, it requires him to be more precise in his estimation of Challenge Ratings and encounter levels.

### Variable Modifiers

If static modifiers for attack rolls, checks, and other d20 rolls has made the game too predictable, you can try using variable modifiers instead.

Essentially, the variable modifier system replaces any modifier higher that +1 or lower than -1 with one or more additional dice added to or subtracted from the basic d20 roll.

For example, at 1st level a character normally has an attack bonus of +4 when swinging his dwarven waraxe. Instead of rolling 1d20+4 to determine the attack’s success, the player would roll 1d20+1d8. The actual modifier added to the 1d20 roll might then be any value from 1 to 8, making the final result less predictable, even though the average would remain virtually the same.

Effectively, for every point of bonus or penalty beyond 1, the "die size" of the variable modifier increases by one step, as shown on the tables below.

Starting at a modifier of +11 or -11, the pattern simply repeats every 10 points. A +13 bonus is the same as a +10 bonus (+1d20) added to a +3 bonus (+1d6), and thus the character would roll 1d20 and add 1d20 + 1d6. Similarly, a -15 penalty would be the same as a -10 penalty (-1d20) and a -5 penalty (-1d10) added together. When the Variable Penalties table gives a penalty suchg as "-(1d20 + 1d10)", it means add together the rolls of the dice inside the parentheses and treat the total as a penalty on the check.

Use variable modifiers only when adjusting the roll of a d20. Don’t apply them to damage rolls, hit point rolls, percentile rolls, or any other roll that does not involve a d20.

##### Taking 10 and Taking 20

Avoid using variable modifiers when a character takes 10 or takes 20 on a skill check. Since those two rules rely on a certain level of predictability, a character who takes 10 or takes 20 should apply the normal static modifier to his roll rather than using the less predictable variable modifier. Otherwise, even simple tasks can become uneccessarily dangerous.

**Table: Variable Bonuses**

| Static Bonus | Dice          | Average Bonus |
| ------------ | ------------- | ------------- |
| +1          | +1           | +1           |
| +2          | +1d4         | +2.5         |
| +3          | +1d6         | +3.5         |
| +4          | +1d8         | +4.5         |
| +5          | +1d10        | +5.5         |
| +6          | +1d12        | +6.5         |
| +7          | +2d6         | +7           |
| +8          | +3d4         | +7.5         |
| +9          | +2d8         | +9           |
| +10         | +1d20        | +10.5        |
| +11         | +1d20 + 1    | +11.5        |
| +12         | +1d20 + 1d4  | +13          |
| +13         | +1d20 + 1d6  | +14          |
| +14         | +1d20 + 1d8  | +15          |
| +15         | +1d20 + 1d10 | +16          |
| +16         | +1d20 + 1d12 | +17          |
| +17         | +1d20 + 2d6  | +17.5        |
| +18         | +1d20 + 3d4  | +18          |
| +19         | +1d20 + 2d8  | +19.5        |
| +20         | +2d20        | +21          |

… and so on.

**Table: Variable Penalties**

| Static Penalty | Dice            | Average Penalty |
| -------------- | --------------- | --------------- |
| -1            | -1             | -1             |
| -2            | -1d4           | -2.5           |
| -3            | -1d6           | -3.5           |
| -4            | -1d8           | -4.5           |
| -5            | -1d10          | -5.5           |
| -6            | -1d12          | -6.5           |
| -7            | -2d6           | -7             |
| -8            | -3d4           | -7.5           |
| -9            | -2d8           | -9             |
| -10           | -1d20          | -10.5          |
| -11           | -(1d20 + 1)    | -11.5          |
| -12           | -(1d20 + 1d4)  | -13            |
| -13           | -(1d20 + 1d6)  | -14            |
| -14           | -(1d20 + 1d8)  | -15            |
| -15           | -(1d20 + 1d10) | -16            |
| -16           | -(1d20 + 1d12) | -17            |
| -17           | -(1d20 + 2d6)  | -17.5          |
| -18           | -(1d20 + 3d4)  | -18            |
| -19           | -(1d20 + 2d8)  | -19.5          |
| -20           | -2d20          | -21            |

… and so on.

##### Behind the Curtain: Variable Modifiers

On average, variable modifiers are about 1/2 point higher or lower than static modifiers — in other words, an average result on a check with a variable bonus is about 1/2 point higher than the same check with a static bonus, while an average result on a check with a variable penalty is about 1/2 point lower. Since the majority of checks made by player characters have a bonus rather than a penalty, this system is slightly advantageous to player characters. However, it also increases the randomness of the result, and randomness tends to favor monsters over PCs.

If you use this variant, don’t allow players to choose between using variable modifiers and static modifiers on a case-by-case basis. Instead, all d20 rolls should use the variable modifier system. It’s possible to allow some characters to use the variable modifiers while other use static modifiers, but doing this runs the risk of creating a perception of inequality between characters.

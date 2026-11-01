---
srd-type: "overview"
section: "Unearthed Arcana"
based-on:
  - "[[fantasy srd 3.5/unearthed-arcana/Injury Variants|Injury Variants (3.5)]]"
status: draft
change: modified
pi-review: scanned 2026-10-15
tags: [rangoric, rangoric/overview]
---

## Unearthed Arcana

### Injury

The d20 game’s hit point system is an easy and effective way of measuring character health — but it’s somewhat abstract. This variant eliminates hit points, and simply determines whether characters are hurt or killed every time they’re hit in combat.

##### Determining Injuries

When using the injury variant, characters no longer have hit points. Instead, a character’s injuries accumulate until he becomes [[rangoric-srd/unearthed-arcana/Injury Variants|disabled]] or [[#Dying|dying]] (or [[#Staggered|staggered]] or [[#Unconscious|unconscious]], if he has taken nonlethal damage).

When a character or creature takes damage, divide the damage dealt by the attack by 5 (rounding up). The result is the damage value of the attack. For example, if you are hit by an attack that deals 12 points of damage, the attack has a damage value of 3 (12 divided by 5, rounded up).

To determine if you are injured, make a Fortitude save to resist injury. The DC is 15 + the damage value.

If you succeed on the save, you suffer no ill effect from the attack.

If you fail the save by less than 10, you have taken a hit. (If the attack dealt nonlethal damage, the hit is a nonlethal hit.) Each hit you take imposes a cumulative -1 modifier on future Fortitude saves to resist injury.

If you fail the save by 10 or more, you are [[rangoric-srd/unearthed-arcana/Injury Variants|disabled]]. (If the attack dealt nonlethal damage, you are [[#Staggered|staggered]].)

**Automatic Success and Failure:** A natural 20 on a Fortitude save to resist injury is treated as an automatic success, just as normal. A natural 1 is always treated as if the save failed by 10 or more. ^automatic-success-and-failure

**Table: Determining Injuries**

| Saving Throw Result  | Lethal Damage           | Nonlethal Damage          |
| -------------------- | ----------------------- | ------------------------- |
| Success              | No effect               | No effect                 |
| Failed by 1 to 9     | [[#Hit\|Hit]]           | Nonlethal hit             |
| Failed by 10 or more | [[#Disabled\|Disabled]] | [[#Staggered\|Staggered]] |

##### Condition Descriptions

Use the descriptions below to determine the game effects from a failed saving throw to resist injury.

###### Hit

A hit means you have suffered some minor injury. Every hit imposes a cumulative -1 penalty on all Fortitude saves to resist injury.

If a [[#Disabled|disabled]] character suffers a hit, he becomes [[#Dying|dying]].

###### Disabled

A disabled character is conscious, but can only take a single move action or standard action each turn (nor can he take full-round actions). He moves at half speed. Taking a move action doesn’t risk further injury, but performing any standard action (or any other action the GM deems strenuous, including some free actions such as casting a [[rangoric-srd/feats/Quicken Spell|quickened]] spell) worsens the character’s condition to dying (unless the action involved healing; see below).

If 5 or more points of magical healing are applied to a disabled character, he is no longer disabled.

A character can be both [[#Staggered|staggered]] and disabled. Becoming staggered while disabled does not worsen a character’s condition to dying. If a staggered and disabled character receives at least 5 points of healing, both conditions are removed.

A disabled character who suffers a hit or a disabled result from an attack becomes [[#Dying|dying]].

###### Dying

A dying character is [[#Unconscious|unconscious]] and near death. Each round on his turn, a dying character must make a Fortitude save, DC 10, +1 per turn after the first) to become [[rangoric-srd/rules/Special Abilities and Conditions#^stable|stable]]. Penalties suffered from hits apply to this saving throw.

If the character fails the save, he [[rangoric-srd/rules/Special Abilities and Conditions#^dead|dies]].

If the character succeeds on the save by less than 5, he does not die but does not improve. He is still dying and must continue to make Fortitude saves every round.

If the character succeeds on the save by 5 or more, he becomes conscious and [[#Disabled|disabled]].

Another character can improve a dying character’s condition to [[rangoric-srd/rules/Special Abilities and Conditions#^stable|stable]] by making a DC 15 [[rangoric-srd/skills/Fieldcraft|Fieldcraft]] check as a standard action (this provokes attacks of opportunity).

A dying character who suffers a hit or a [[#Disabled|disabled]] result from an attack is [[rangoric-srd/rules/Special Abilities and Conditions#^dead|killed]].

###### Nonlethal Hit

A nonlethal hit means you have been battered and bruised and are in less than top condition. Every nonlethal hit you take imposes a cumulative -1 penalty on your Fortitude saves to resist injury from nonlethal damage. Nonlethal hits do not affect Fortitude saves against lethal damage.

For example, a character with 4 hits and 3 nonlethal hits has a -4 penalty on Fortitude saves to resist injury from lethal damage, but a -7 penalty on saves to resist injury from non-lethal damage.

A [[#Staggered|staggered]] character (see below) who suffers a nonlethal hit or becomes staggered as the result of an attack becomes [[#Unconscious|unconscious]].

###### Staggered

Being staggered is identical to being [[#Disabled|disabled]] (see above), except that if a character’s condition worsens, he becomes [[#Unconscious|unconscious]] instead of [[#Dying|dying]].

If 5 or more points of magical healing are applied to a staggered character, he is no longer staggered.

A character can be both [[#Disabled|disabled]] and staggered. Becoming disabled while staggered does not worsen your condition to [[#Unconscious|unconscious]]. If a staggered and disabled character receives at least 5 points of healing, both conditions are removed.

A staggered character who suffers a nonlethal hit or a staggered result from an attack falls [[#Unconscious|unconscious]].

###### Unconscious

An unconscious character falls to the floor, [[rangoric-srd/rules/Special Abilities and Conditions#^helpless|helpless]] and incapable of action. Additional nonlethal hits have no effect on the character. When he recovers one nonlethal hit, he becomes conscious.

##### Healing

Over time, or through magical healing, a character can reduce the number of hits he has. Some creatures have special abilities that affect the way in which they heal hits.

###### Natural Healing

With a full night’s rest, a character heals 1 hit per 2 character levels (minimum 1 hit per night). If he undergoes complete bed rest for 24 hours, he heals a number of hits equal to his character level. Any significant interruption during the rest period prevents the character from healing that night.

Nonlethal hits heal more quickly. A character heals nonlethal hits at a rate of 1 hit per hour per two character levels (minimum 1 hit per hour). If the GM chooses, he can prorate this healing so that it occurs more uniformly. For instance, a 12th-level character heals 6 nonlethal hits per hour; instead, the GM can allow her to heal 1 nonlethal hit per 10 minutes.

###### Magical Healing

For every 5 points of magical healing administered, a character eliminates 1 lethal hit and 1 nonlethal hit.

###### Special Healing Abilities

Some creatures have extraordinary or supernatural powers of healing.

**Fast Healing:** A creature with fast healing can remove 1 lethal hit and 1 nonlethal hit per round per 5 points of fast healing (minimum 1 hit of each type). For example, a [[rangoric-srd/monsters/Vampire Spawn|vampire spawn]] has fast healing 2; it can therefore eliminate 1 hit and 1 nonlethal hit per round. ^fast-healing

A creature with fast healing may add its fast healing value to Fortitude saves made to become [[rangoric-srd/unearthed-arcana/Injury Variants|stable]] when [[#Dying|dying]]. A dying vampire spawn, for example, gets a +2 bonus on its Fortitude saves to become stable.

**Regeneration:** A creature with regeneration treats all damage as nonlethal, except for specific types of damage, given in the creature’s description, that affect it normally (such as a [[rangoric-srd/monsters/troll/Troll|troll’s]] vulnerability to acid and fire). A creature with regeneration can remove 1 nonlethal hit per round per 5 points of regeneration (minimum 1 hit). ^regeneration

##### Special Damage Defenses

Some creatures have special defenses against damage, such as [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities#^DR|damage reduction]] or [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities#^resistance-to-energy|resistance to energy]]. Certain spells and effects also provide defenses against damage.

###### Bonus Hit Points

Effects or abilities that normally give you bonus hit points (such as the [[rangoric-srd/feats/Toughness|Toughness]] feat or the [[rangoric-srd/spells/Aid|aid]] spell) instead add to your Fortitude saves to resist injury. For every 5 bonus hit points granted by the effect (round fractions up), add a +1 bonus on the save. For example, Toughness gives you a +1 on Fortitude saves to resist injury.

Extra hit points granted by an increased Constitution score don’t add to this save bonus, since your high Constitution already gives you a bonus on your Fortitude saves.

###### Damage Reduction and Resistance to Energy

Damage reduction adds to your Fortitude save to resist injury. For every 5 points of damage reduction that apply against the incoming attack (round fractions up), add a +1 bonus on the save. For instance, a creature with DR 10/magic gains a +2 bonus on Fortitude saves to resist injury from damage dealt by nonmagical weapons.

Resistance to energy works the same way. A creature with resistance to fire 15 gains a +3 bonus on Fortitude Saves to resist fire damage.

###### Dealing Damage to Objects

Objects can suffer the effects of lethal damage just as creatures can. Nonmagical, unattended objects have a base Fortitude save bonus of +0. A magic item has a Fortitude save bonus equal to +2 +1/2 its caster level. An item attended by a character makes saving throws as the character (or, in the case of a magic item, uses its own saving throw if better).

Add an object’s hardness to its Fortitude saves to resist injury. Furthermore, for every additional inch of thickness beyond the first, an object gains a +1 bonus on its save.

Magic weapons, armor, and shields also add their enhancement bonus to their Fortitude saves against damage

An object that takes any lethal hits has a cumulative -1 penalty on its future saves to resist injury from lethal damage, just as with characters. An object that is rendered [[rangoric-srd/unearthed-arcana/Injury Variants|disabled]] is broken or destroyed instead.

Objects are immune to nonlethal damage and thus don’t have to make Fortitude saves to resist injury from attacks that deal nonlethal damage.

###### Creatures without Constitution Scores

Some creatures, such as undead and constructs, do not have Constitution scores. Creatures without Constitution scores have a +4 bonus on Fortitude saves to resist injury. However, a creature with no constitution score that becomes [[rangoric-srd/unearthed-arcana/Injury Variants|disabled]] is destroyed instead.

Creatures that do not have Constitution scores are immune to nonlethal damage and thus don’t have to make Fortitude saves to resist injury from attacks that deal nonlethal damage.

##### Special Damage Effects

This system changes the way some special damage effects work.

###### Coup de Grace

A coup de grace is handled as a normal attack, except that the result of the Fortitude save is treated as one category worse. (The save DC is usually higher than normal, as well, since the coup de grace is considered a critical hit and thus deals extra damage.)

On a successful save, the target takes 1 hit (or 1 nonlethal hit, if a nonlethal attack was used). If the save fails by less than 10, the target is [[rangoric-srd/unearthed-arcana/Injury Variants|disabled]] (or [[#Staggered|staggered]]); and if the save fails by 10 or more, the target is [[#Dying|dying]] (or [[#Unconscious|unconscious]]).

###### Massive Damage

There is no massive damage threshold in this variant, since the greater the damage dealt, the higher the chance that a character will become [[#Unconscious|unconscious]] or [[#Dying|dying]].

The GM could rule that a Fortitude save to resist injury that fails by 20 or more results in the character being rendered dying (or becoming unconscious, if the damage is nonlethal damage). This introduces the very real possibility that a single hit (such as a critical hit or a sneak attack) can take a character out.

### Reserve Points

This variant gives each character a capacity to recover quickly from injury. This capacity, measured as reserve points, replenishes lost hit points quickly after a fight. Thus, characters may be wounded and near death by the end of a fight, but then recover to full strength (or nearly full strength) before the next fight begins.

Reserve points work particularly well in low-magic campaigns or any game in which healing is rare, expensive, or otherwise hard to get.

##### Behind the Curtain: Reserve Points

Even though this variant effectively doubles a character’s number of hit points, he can’t take a beating over and over again without depleting his capacity to recover. Reserve points effectively double the number of hit points a character can lose over the course of multiple fights but do not increase the damage a character can withstand in a single fight.

##### Using Reserve Points

A character’s quantity of reserve points is equal to his full normal hit point total.

After a character becomes injured (by losing hit points), reserve points begin automatically converting to hit points at the rate of 1 per minute of nonstrenuous activity (such as resting or hiking, but not climbing, swimming or fighting). Thus, for each minute of nonstrenuous activity, the character regains 1 hit point and loses 1 reserve point.

For example, a character has 22 hit points, so he also has 22 reserve points. In a battle with orcs, he takes 6 points of damage, dropping his hit points to 16. After the fight, his reserve points begin to "convert" to hit points. Over the course of the next 6 minutes, his reserve point total drops by 6 and his hit point total increases by 6, up to his maximum of 22. During the next fight, he takes 24 points of damage, dropping him to -2, and then is dying for 5 rounds before stabilizing, leaving him at -7 hit points. Over the next 16 minutes his remaining 16 reserve points convert to hit points. After 7 minutes he’s conscious but disabled (0 hp). After 8 minutes he’s back on his feet (1 hp), and after all 16 minutes he’s up to 9 hit points and 0 reserve points.

**Nonlethal damage:** Reserve points can also reduce a character’s nonlethal damage total. For each reserve point that converts to a hit point, a character also subtracts 1 point from his nonlethal damage. In addition, a character can take astandard action to "spend" a number of reserve points equal to or less than his HD to reduce his nonlethal damage an equal amount. (If a character has the [[rangoric-srd/feats/Endurance|Endurance]] feat, the GM might choose to make this a move action, to reflect the fact that such characters can more easily perservere through exhausting situations.) ^nonlethal-damage-and-reserve-points

##### Replenishing Reserve Points

Characters naturally regain lost reserve points at the same rate that they naturally heal lost hit points. If a character receives any magical healing, that healing is applied first to the character’s lost hit points. Any excess healing left over after the character’s hit points are restored to full normal is applied to increase the character’s current reserve point total (up to its normal maximum).

For example, a character normally has 22 hit points, but he’s down to 9 hp and 0 reserve points. He drinks a potion of cure moderate wounds, rolling 2d8 + 3 and getting a result of 15. The first 13 points replenish his hit points; the remainder go to his reserve points. He now has 22 hit points and 2 reserve points.

##### Constitution Changes

If a character’s Constitution modifier goes up or down, his reserve points go up or down just as his hit points do. If a decrease in Constitution would drop a character’s reserve points below 0, any excess reduction is deducted from his current hit points.

### Massive Damage Thresholds and Results

The massive damage rule is designed for games of heroic fantasy. It maintains the remote possibility that a single blow from a mighty opponent can kill a character, regardless of that character’s actual hit points.

Altering the massive damage rules can dramatically change the character’s attitude about combat. A lower threshold (the amount of damage that triggers a Fortitude save to avoid death) makes combat more deadly, perhaps turning any hit into a potentially life-threatening injury. On the other hand, a less deadly result on a failed save ([[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconsciousness]] instead of death, for instance) makes combat less dangerous, making a character’s current hit point total more important than any single hit.

Here, then, are several alternative massive damage thresholds and results. You can combine different variants to create your own custom system. For instance, you might combine the [[#^hd-based-threshold|HD-based threshold]] variant with the [[#^size-based-threshold|size-based threshold]] variant to create a massive damage threshold that takes into account both a creature’s Hit Dice and size.

Regardless of the variant you use, each player should record his character’s massive damage threshold somewhere on the character sheet (to avoid mid-battle calculations), and the GM might want to add massive damage threshold values to monster and NPC statistics blocks for the same reason.

##### Alternative Threshold Levels

The 50-point threshold in the standard d20 rules can be altered in several ways.

**Constitution-Based Threshold:** A character’s massive damage threshold is equal to his Constitution score. Whenever he takes damage from a single hit that equals or exceeds his current Constitution score, he must succeed on a DC 15 Fortitude save or suffer the effects of massive damage. ^consitution-based-threshold

If an attack deals hit point damage and also changes the character’s Constitution score (such as a strike with a poisoned weapon), apply all effects of the hit before determining whether the damage is enough to trigger the saving throw. For instance, a character with a 14 Constitution is hit by a greatsword coated with [[rangoric-srd/rules/Special Abilities and Conditions|black adder venom]]. The attack deals 12 points of damage, but the character also fails his Fortitude save against the poison and takes 3 points of Constitution damage. This lowers his Constitution — and hence his massive damage threshold — to 11. Since the damage exceeds the threshold, the character must now make a Fortitude save to avoid the effect of massive damage.

**HD-Based Threshold:** A character’s massive damage threshold is equal to 25, +2 per Hit Die. Whenever a character takes damage from a single hit that equals or exceeds this value, he must succeed on a DC 15 Fortitude save or suffer the effects of massive damage. ^hd-based-threshold

For example, a 5th-level human fighter has a massive damage threshold of 35 (25 + \[2 × 5\]). A fire giant has a massive damage threshold of 55 (25 + \[2 × 15\]).

**Size-Based Threshold:** A creature’s massive damage threshold is equal to 50, plus or minus 10 points for every size category larger or smaller than Medium. Whenever a creature takes damage that equals or exceeds this value, it must succeed on a DC 15 Fortitude save or suffer the effects of massive damage. ^size-based-threshold

##### Alternative Save Failure Results

Failed massive damage Fortitude save results can be alterd in several ways.

**Dying Result:** Instead of a failed Fotitude save against massive damage resulting in instant death, a failed save results in a character being reduced to -1 hit point. The character becomes [[rangoric-srd/rules/Special Abilities and Conditions#^dying|dying]] and [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]], but can still become [[rangoric-srd/rules/Special Abilities and Conditions#^stable|stable]] or be helped by his friends, just like any other character who is reduced to -1 hp. ^dying-result

**Near-Death Result:** Alternatively, instead of a failed Fortitude save against massive damage resulting in instant death, a failed save results in a character being reduced to -8 hp. The character is very close to death (having only a round or two to become [[rangoric-srd/rules/Special Abilities and Conditions#^stable|stable]] or receive help), but isn’t automatically killed. ^near-death-result

**Variable Result:** For an added bit of random chance, a character who fails his Fortitude save against massive damage rolls 1d10 to determine his negative hit point total. A roll of 1 to 9 indicates that the character is [[rangoric-srd/rules/Special Abilities and Conditions#^dying|dying]] (at -1 hp on a 1, -2 hp on a 2, and so forth). A roll of 10 leaves the character with -10 hit points, which means he is [[rangoric-srd/rules/Special Abilities and Conditions#^dead|dead]]. ^variable-result

##### Scaling the Saving Throw

Another way to tweak the massive damage system is to scale the Fortitude save DC based on the damage taken. For every 10 points of damage dealt by an attack in excess of a character’s massive damage threschold, increase his Fortitude save DC by 2. This rule functions the same regardless of the threshold you choose to use.

For instance, if you use the standard 50-point threshold, a hit that deals 50 to 59 points of damage requires a DC 15 save, 60 to 69 points DC 17, 70 to 79 points DC 19, and so forth. If you use the Constitution-based threshold, a character with a Constitution of 15 would have to make a DC 15 Fortitude save when taking 15 to 24 points from a single attack, DC 17 for 25 to 34 points, DC 19 for 35 to 44 points, and so on.

##### Combining Massive Damage Variants

The massive damage variants given above can be combined in a number of ways.

To combine the [[rangoric-srd/unearthed-arcana/Injury Variants|Constitution-based threshold]] variant with the [[#^hd-based-threshold|HD-based system]], simply use a character’s Constitution score instead of 25 to determine a character’s massive damage threshold. For example, a 3rd-level character with a Constitution of 14 has a massive damage threshold of 20 (14 + \[3 × 2\]). In most cases, this calculation results in a threshold lower than the HD-based threshold but still higher than the Constitution-based threshold — retaining the "grittiness" of the Constitution-based system for low-to mid-level characters, while allowing higher-level characters to become braver in combat.

You can easily combine the [[#^hd-based-threshold|HD-based system]] with the [[#^size-based-threshold|size-based variant]]: Use half of the base value for size instead of 20 to determine the massive damage threshold. For instance, a 1st-level human fighter (a Medium character) has a massive damage threshold of 27 (half of 50 is 25, plus 2 × 1).

You probably shouldn’t combine the [[rangoric-srd/unearthed-arcana/Injury Variants|Constitution-based system]] with the [[#^size-based-threshold|size-based variant]], since the threshold is already low enough that reducing it for Small or smaller characters unduly punishes them.

The alternate save failure results can be combined with any of the alternative threshold levels.

##### Behind the Curtain: Massive Damage Rules

The variant systems for massive damage affect the game in different ways.

The [[rangoric-srd/unearthed-arcana/Injury Variants|Constitution-based threshold]] variant is deadiler than the standard massive damage system, since the threshold is so much lower. It’s best for low-level, low-power games, or campaigns bent on "gritty realism" in combat. You may want to allow characters the option of increasing their thresholds without improving their Constitution scores. For instance, a feat called Improved Damage Threshold that increased a character’s damage threshold by 3 would allow a low-Constitution character to increase his massive damage threshold quickly and easily.

Unlike most other massive damage thresholds, the [[#^hd-based-threshold|HD-based variant]] scales up with a character as he gains levels. At lower levels, the threshold is lower than the normal value, but still high enough that it rarely matters. At higher levels, a character’s massive damage threshold exceeds the value given in the standard d20 rules, increasing such characters’ survivability in combat. It favors monsters whose Hit Dice greatly exceed their Challenge Ratings, such as giants and dragons, since their massive damage thresholds will end up higher than those of the characters fighting them.

The [[#^size-based-threshold|size-based threshold]] variant hurts halfling and gnome PCs, as well as familiars and some animal companions. It generally favors monsters, since monsters tend to be larger than PCs.

The [[#^dying-result|dying save result variant]] tends to create less deadly combats, since a single save doesn’t spell automatic death. Still, a failed save can be just as critical to the tide of battle as in the standard system — a [[rangoric-srd/rules/Special Abilities and Conditions#^dying|dying]] character is every bit as useless as a [[rangoric-srd/rules/Special Abilities and Conditions#^dead|dead]] one, and is likely to bleed off resources from one or more other characters who attempt to save him from death.

The [[#^near-death-result|near-death result]] is almost as deadly as the standard system, but it gives a character a slim chance of surviving. It is particularly suited for heroic campaigns in which characters often find themselves at the brink of death, only to pull back from the edge at the last possible moment.

The [[#^variable-result|variable result]] system is less deadly than the standard rules (since it allows for the likelihood that a character will survive for at least a few rounds), but removes the predictability of the [[#^dying-result|dying result]] and [[#^near-death-result|near death result]] variants. A lucky character might be reduced only to -1 hp, while an unlucky character might have mere seconds to survive until passing into the great beyond — if he gets any time at all.

Finally, the [[#Scaling the Saving Throw|scaling saving throw]] option makes high-level combat particularly dangerous to characters with poor Fortitude saves. Since those characters also tend to have low hit points, combat becomes doubly deadly, since they now must worry about individual attacks from powerful opponents as well as the normal attrition of hit points.

### Vitality and Wound Points

The vitality and wound points system was originally developed as a more cinematic method of handling damage than the traditional hit point system. The system allows for characters to improve the amount of punishment they can withstand as they go up in level, while still allowing for a single lucky attack to take down a character.

##### Behind the Curtain: Vitality and Wound Points

Characters using this system should be more wary in combat, which can turn deadly in the space of a few lucky rolls. But they can also bounce back from a fight much more quickly. For that reason, this variant is an ideal system for low-magic campaigns or games where healing is otherwise rare.

A very weak creature in this system tends to be tougher to kill than in a standard d20 game, since its Constitution score is often higher than the number of hit points it might have had. Very big creatures are also more durable, due to their size modifier. This is reflected in the CR adjustments given in the variant rules.

Creatures capable of dealing a large amount of damage on a single hit become significantly more deadly in this system, since a lucky attack roll can give a deadly blow to almost any character. For critical hits, consider reducing the additional damage from bonus damage dice (such as a flaming sword or a rogue’s sneak attack) to only 1 point per die. (Such attacks deal normal damage on noncritical hits.) That’s still pretty scary when fighting a high-level rogue, but not quite as terrifying as facing the possibility of an extra 5 or 10 dice of wound point damage with a successful sneak attack critical hit. You may find other places where damage needs adjustment in this system as well; don’t be afraid to tinker when needed to keep your game fun and exciting.

Constitution damage is especially deadly under this variant, since every point of Constitution damage reduces wound points by 1 and every 2 points of damage reduces vitality by a number of points equal to the character’s HD. If a character’s Constitution is reduced to 0, he dies even if he has wound points remaining.

##### Vitality Points

Vitality points are a measure of a character’s ability to turn a direct hit into a graze or a glancing blow with no serious consequences. Like hit points in the standard d20 rules, vitality points go up with level, giving high-level characters more ability to shrug off attacks. Most types of damage reduce vitality points.

Characters gain vitality points as they gain levels. Just as with hit points in the standard d20 rules, at each level a character rolls a vitality die and adds his Constitution modifier, adding the total to his vitality point total. (And, just as with hit points, a character always gains at least 1 vitality point per level, regardless of his roll or Constitution modifier.) A 1st-level character gets the maximum vitality die result rather than rolling, as shown on [[rangoric-srd/unearthed-arcana/Injury Variants|Table: Vitality Points]] below.

**Table: Vitality Points**

| Class     | Vitality Points at 1st level | Vitality Die |
| --------- | ---------------------------- | ------------ |
| Barbarian | 12 + Con mod                 | d12          |
| Bard      | 6 + Con mod                  | d6           |
| Cleric    | 8 + Con mod                  | d8           |
| Druid     | 8 + Con mod                  | d8           |
| Fighter   | 10 + Con mod                 | d10          |
| Monk      | 8 + Con mod                  | d8           |
| Paladin   | 10 + Con mod                 | d10          |
| Ranger    | 8 + Con mod                  | d8           |
| Rogue     | 6 + Con mod                  | d6           |
| Sorcerer  | 4 + Con mod                  | d4           |
| Wizard    | 4 + Con mod                  | d4           |

##### Wound Points

Wound points measure how much true physical damage a character can withstand. Damage reduces wound points only after all vitality points are gone, or when a character is struck by a critical hit. A character has a number of wound points equal to her current Constitution score.

##### Critical Hits

A critical hit deals the same amount of damage as a normal hit, but that damage is deducted from wound points rather than from vitality points. Critical hits do not deal extra damage; for that reason, no weapon in this system has a damage multiplier for its critical hits.

Any critical hit automatically overcomes a creature’s [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities#^DR|damage reduction]], regardless of whether or not the attack could normally do so.

Most weapons retain their normal critical threat range. If a weapon normally has a critical multiplier greater than ×2, the weapon’s threat range expands by 1 point per additional multiplier, as indicated on the table below.

**Table: Critical Multiplier to Threat Range Conversion**

| Multiplier | New Threat Range |
| ---------- | ---------------- |
| ×3         | 19-20            |
| ×4         | 18-20            |
| ×5         | 17-20            |

##### Injury and Death

Vitality and wound points together measure how hard a character is to hurt and kill. The damage from each successful attack and each fight accumulates, dropping a character’s vitality point or wound point total until he runs out of points.

###### Nonlethal Damage

This system doesn’t differentiate between lethal and nonlethal damage. Attacks and effects that normally deal nonlethal damage reduce vitality points, except on a critical hit, in which case they reduce wound points.

###### 0 Vitality Points

At 0 vitality points, a character can no longer avoid taking real physical damage. Any additional damage he receives reduces his wound points.

###### Taking Wound Damage

The first time a character takes wound damage — even a single point — he becomes [[rangoric-srd/rules/Special Abilities and Conditions#^fatigued|fatigued]]. A fatigued character can’t run or charge and takes a -2 penalty to Strength and Dexterity until he has rested for 8 hours (or until the wound damage is healed, if that occurs first). Additional wound damage doesn’t make the character [[rangoric-srd/rules/Special Abilities and Conditions#^exhausted|exhausted]].

In addition, any time an attack deals wound damage to a character, he must succeed on a Fortitude saving thow (DC 5 + number of wound points lost from the attack) or be [[rangoric-srd/rules/Special Abilities and Conditions#^stunned|stunned]] for 1d4 rounds. (During that time, any other character can take a standard action to help the stunned character recover; doing so ends the stunned condition.)

###### 0 Wound Points

Wound points cannot drop below 0; any damage that would cause a character’s wound point total to drop below 0 simply causes the character to have 0 wound points.

At 0 wound points, a character is [[#^disabled-and-wound-points|disabled]] and must attempt a DC 15 Fortitude save. If he succeeds on the save, he is merely disabled. If he fails, he falls [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]] and begins [[#^dying-and-wound-points|dying]].

**Disabled:** A disabled character is conscious, but can only take a single move or standard action each turn (but not both, nor can she take full-round actions). She moves at half speed. Taking move actions doesn’t risk further injury, but performing any standard action (or any other action the GM deems strenuous, including some free actions such as casting a [[rangoric-srd/feats/Quicken Spell|quickened]] spell) worsen the character’s condition to [[#^dying-and-wound-points|dying]] (unless it involved healing; see below). ^disabled-and-wound-points

**Dying:** A dying character is [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]] and near death. Each round on his turn, a dying character must make a Fortitude save (DC 10, +1 per turn after the first) to become [[#Stable Characters and Recovery|stable]]. ^dying-and-wound-points

If the character fails the save, he dies.

If the character succeeds on the save by less than 5, he does not die but does not improve. He is still dying and must continue to make Fortitude saves every round.

If the character succeeds on the save by 5 or more but by less than 10, he becomes [[#Stable Characters and Recovery|stable]] but remains [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]].

If the character succeeds on the save by 10 or more, he becomes conscious and [[#^disabled-and-wound-points|disabled]].

Another character can make a dying character [[#Stable Characters and Recovery|stable]] by succeeding on a DC 15 Fieldcraft check as a standard action (which provokes attacks of opportunity).

###### Stable Characters and Recovery

A stable character is [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]]. Every hour, a stable character must succeed on a Fortitude save (DC 10, +1 per hour after the first) to remain stable.

If the character fails the save, he becomes [[#^dying-and-wound-points|dying]].

If the character succeeds on the save by less than 5, he does not get any worse, but does not improve. He is still stable and [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]], and must continue to make Fortitude saves every hour.

If the character succeeds on the save by 5 or more, he becomes conscious and [[#^disabled-and-wound-points|disabled]].

An unaided stable, conscious character at 0 wound points has a 10% chance to start recovering wound points naturally that day.

Once an unaided character starts recovering wound points naturally, he is no longer in danger of dying.

**Recovering with Help:** A dying character can be made stable with a DC 15 [[rangoric-srd/skills/Fieldcraft|Fieldcraft]] check (a standard action that provokes attacks of opportunity). One hour after a tended, dying character becomes stable, roll d%. He has a 10% chance of regaining consciousness, at which point he becomes [[rangoric-srd/unearthed-arcana/Injury Variants|disabled]]. If he remains [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]], he has the same chance to regain consciousness every hour. Even while unconscious, he recovers wound points naturally, becoming conscious and able to resume normal activity when his wound points rise to 1 or higher. ^recovering-with-help

##### Special Damage Situations

The vitality point system changes the way some special damage effects work.

###### Coup de Grace

A coup de grace functions normally in that it automatically hits and scores a critical hit (and thus the damage dealt is applied to the target’s wound points). If the defender survives the damage, he must make a Fortitude save (DC 10 + the amount of damage dealt) or die.

###### Massive Damage

The massive damage rule does not apply under this system.

##### Healing

After taking damage, a character can recover vitality and wound points through natural healing (over the course of hours or days), or by magic. In any case, a character can’t regain vitality points or wound points above his full normal totals.

###### Natural Healing

Characters recover vitality points at a rate of one vitality point per hour per character level.

With a full night’s rest, a character recovers 1 wound point per character level (minimum 1 per night), or twice that amount with complete bed rest for 24 hours. Any significant interruption during the rest period prevents the character from healing that night.

###### Assisted Healing

A character who provides [[rangoric-srd/skills/Fieldcraft|long-term care]] doubles the rate at which a wounded character recovers lost vitality and wound points.

###### Magical Healing

Spells that heal hit point damage work somewhat differently in this system. For spells that heal a variable amount of hit point damage based on a die roll (such as [[rangoric-srd/spells/Cure Light Wounds|cure light wounds]]), apply the actual die roll as restored vitality points, and any modifier to the die roll (such as caster level, for cure spells) as restored wound points.

For example, cure moderate wounds heals 2d8 points of damage, +1 point per caster level (maximum +10). Under this system, a 10th-level cleric could cast it to heal 2d8 vitality points and 10 wound points.

Spells or effects that return a number of hit points not based on a die roll, such as [[rangoric-srd/spells/Heal (Spell)|heal]], apply the healing to lost wound points first, then to lost vitality. For example, an 11th-level cleric casting heal has 110 points of healing to apply. If the target has taken 12 points of wound damage and 104 points of vitality damage, the spell heals all the wound damage and 98 points of the vitality damage, leaving the target with only 6 points of vitality damage remaining.

##### NPCs and Monsters

Vitality points are only granted by the "heroic" classes, such as the standard character classes and various prestige classes. The NPC classes — adept, aristocrat, commoner, expert and warrior — grant no vitality points (either at 1st level or thereafter). Such characters have wound points equal to their Constitution score. Thus, a typical 1st-level orc warrior has no vitality points and 12 wound points. All damage dealt to such creatures is applied to their wound points.

Most monsters, on the other hand, have both wound points and vitality points. For Small, Medium and Large creatures, a monster’s wound point total is equal to its current Constitution score. Creatures smaller or larger than that have their wound point total multiplied by a factor based on their size, as indicated on the table.

A monster’s vitality point total is equal to the number of hit points it would normally have, based on its type and Constitution score. The GM may choose not to assign vitality points to creatures that pose little or no threat to PCs, such as domesticated herd animals.

**Table: Wound Points Size Multiplier**

| Size       | Wound Point Multiplier |
| ---------- | ---------------------- |
| Fine       | ×1/8                   |
| Diminutive | ×1/4                   |
| Tiny       | ×1/2                   |
| Small      | ×1                     |
| Medium     | ×1                     |
| Large      | ×1                     |
| Huge       | ×2                     |
| Gargantuan | ×4                     |
| Colossal   | ×8                     |

###### Creatures without Constitution Scores

Some creatures, such as undead and constructs, do not have Constitution scores. If a creature has no Constitution score, it has no vitality points. Instead, it has wound points equal to the number of vitality points it would have based on its HD and type. Such creatures are never [[rangoric-srd/rules/Special Abilities and Conditions#^fatigued|fatigued]] or [[rangoric-srd/rules/Special Abilities and Conditions#^stunned|stunned]] by wound damage.

###### Bonus Hit Points

If a creature would have bonus hit points based on its type, these are treated as bonus wound points. (For example, a Medium [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities#^construct|construct]] gets 20 bonus wound points.) The same holds true for any permanent effect that increases a character’s hit point total (such as the [[rangoric-srd/feats/Toughness|Toughness]] feat, which adds 3 to the character’s wound point total).

###### Damage Reduction

[[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities#^DR|Damage reduction]] functions normally, reducing damage dealt by attacks. However, any critical hit automatically overcomes a creature’s damage reduction, regardless of whether the attack could normally do so. For example, a critical hit against a skeleton (DR 5/bludgeoning) overcomes the creature’s damage reduction even if it was hit with a weapon that does not deal bludgeoning damage.

###### Fast Healing

Creatures with [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities#^fast-healing|fast healing]] regain vitality points at an exceptionally fast rate, usually 1 or more vitality points per round, as given in the creature’s description (for example, a [[rangoric-srd/monsters/Vampire|vampire]] has fast healing 5).

If a creature with fast healing has no Constitution score, fast healing restores lost wound points instead. The same doesn’t apply to creatures that have no vitality points but do have a Constitution score (such as a human warrior or domestic animal). Such creatures gain no benefit from fast healing.

###### Regeneration

All damage dealt to creatures with [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities#^regeneration|regeneration]] is vitality point damage, even in the case of critical hits. The creature automatically heals vitality point damage at a fixed rate per round, as given in the entry (for example, a [[rangoric-srd/monsters/troll/Troll|troll]] has regeneration 5). A regenerating creature that runs out of vitality points becomes [[rangoric-srd/rules/Special Abilities and Conditions#^fatigued|fatigued]] just as if it had taken wound point damage. Excess damage, however, does not reduce its wound points. Certain attack forms, typically fire and acid, automatically deal wound damage to a regenerating creature, though it may attempt a Fortitude save (DC 10 + damage dealt) to convert this to vitality damage, which it can regenerate normally. Otherwise, regeneration functions as described in the standard rules and in individual monster descriptions.

##### Monster Challenge Ratings

Increase the CR of any Gargantuan or Colossal creature by +1, unless the creature does not have a Constitution score.

Monsters with fractional CRs move up to the next highest fraction. The kobold (ordinarily CR 1/4) becomes CR 1/3, for example, while the goblin (normally CR 1/2) becomes CR 1.

### Death and Dying

Under the standard d20 rules, [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconsciousness]] and death are predictable states: When a character reaches negative hit points, he goes unconscious. When he reaches -10, he dies.

This variant takes away some of that predictability. No longer does a dying character have a set number of rounds to live. This heightens the tension in combat when one of your allies has fallen, because you don’t know exactly when the clock is going to run out.

##### Behind the Curtain: Death and Dying

This variant system increases a character’s chance of surviving in combat against monsters that deal out tremendous amounts of damage per attack, since any character brought to 0 hit points against such a creature has a chance of survival. It eliminates the fear that every high-level character has faced: taking damage from a creature’s attack that knocks him down close to 0 hit points, knowing that a second attack is coming and it will probably send him well below -10 hit points.

This variant also reduces some of the swing factor of massive damage, since a single blown save won’t make the difference between life and death. In fights against monsters who can routinely deliver 50 or more points of damage per hit — not terribly uncommon at higher levels — this keeps combat from being a grim game of "Who will be the first to roll a natural 1?"

##### 0 Hit Points

With this variant, characters can’t be reduced to negative hit points — 0 is the minimum. There is no automatic hit point total at which a character dies. Instead, any character who takes damage that reduces his hit points to 0 must make a Fortitude save to avoid falling [[rangoric-srd/rules/Special Abilities and Conditions|unconscious]] or [[#^dying-and-death|dying]].

##### The Fortitude Save

When a character’s hit points are reduced to 0, he must attempt a Fortitude save (DC 10, +2 per 10 points of damage dealt by the attack or effect). Success means the character is [[#^disabled-and-death|disabled]]; failure indicates that he is [[#^dying-and-death|dying]]. Failure by 10 or more means the character is [[#^dead-and-death|dead]]. (If the character rolls a natural 1, he is dying. Calculate the numeric result; if he missed the DC by 10 or more, he is dead.)

The possible results of the save are as follows.

**Disabled:** A disabled character is conscious, but can only take a single move or standard action each turn (but not both, nor can she take full-round actions). She moves at half speed. Taking move actions doesn’t risk further injury, but if a disabled character takes any standard action (or any other action the GM deems strenuous, including some free actions such as casting a [[rangoric-srd/feats/Quicken Spell|quickened]] spell), she must succeed on a Fortitude save (against the same DC as the save made when reduced to 0 hit points) to remain disabled; otherwise, she becomes [[#^dying-and-death|dying]] after she completes the action. If a disabled character takes any lethal damage, she must make a new Fortitude save (DC 10, +2 per 10 points of damage dealt by the attack or effect), but any result other than [[#^dead-and-death|dead]] means the character is now dying. A disabled character who is dealt (or who is currently suffering from) any nonlethal damage becomes [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]] (since the character’s nonlethal damage now exceeds his hit points) but does not begin dying. ^disabled-and-death

**Dying:** A dying character is [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]] and near death. Each round on his turn, a dying character must make a Fortitude save (DC 10, +1 per turn after the first) to become [[#^stable-and-death|stable]]. ^dying-and-death

If the character fails the save, he [[#^dead-and-death|dies]].

If the character succeeds on the save by less than 5, he does not die but does not improve. He is still dying and must continue to make Fortitude saves every round.

If the character succeeds on the save by 5 or more but by less than 10, he becomes stable but remains unconscious.

If the character succeeds on the save by 10 or more, he becomes conscious and [[#^disabled-and-death|disabled]].

Another character can make a dying character [[#^stable-and-death|stable]] by succeeding on a DC 15 [[rangoric-srd/skills/Fieldcraft|Fieldcraft]] check as a standard action (which provokes attacks of opportunity).

**Stable:** A stable character is [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]]. Every hour, a stable character must succeed on a Fortitude save (DC 10, +1 per hour after the first) to remain stable. ^stable-and-death

If the character fails the save, he becomes [[#^dying-and-death|dying]].

If the character succeeds on the save by less than 5, he does not get any worse, but does not improve. He is still stable and [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]], and must continue to make Fortitude saves every hour.

If the character succeeds on the save by 5 or more, he becomes conscious and has 1 hit point.

Another character can grant a stable character a +2 bonus on his Fortitude save to remain stable by tending to him for at least 10 minutes during the hour between saves and by making a DC 15 [[rangoric-srd/skills/Fieldcraft|Fieldcraft]] check.

**Dead:** A dead character’s soul immediately departs the body, and getting it back into the body is a major hassle. Unless you have access to powerful divine magic, you can’t do much to a dead character except go through his pockets for loose gold pieces. ^dead-and-death

##### Healing

A [[#^disabled-and-death|disabled]], [stable](stable-and-death), or [dying](dying-and-death) character has 0 hit points. Healing that raises her above 0 hit points makes her conscious and fully functional again, just as if she had never been reduced to 0. A spellcaster retains the spellcasting ability she had before dropping to 0 hit points. (Of course, a character suffering from nonlethal damage equal to or in excess of her current hit points must still deal with the ramification of that state.)

For example, Tirsa is smashed by a hill giant’s club for 26 points of damage, but she only has 14 hit points left. She is reduced to 0 hit points. She must immediately attempt a DC 14 Fortitude save (base DC 10, +4 because the damage dealt was at least 20 points but less than 30 points). She rolls a 5, so she is [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]] and [[#^dying-and-death|dying]]. (Had she rolled any worse, the attack would have killed her outright.)

On her next turn, she must succeed on a DC 10 Fortitude save to become [[rangoric-srd/unearthed-arcana/Injury Variants|stable]]. She rolls a 13, which is enough to remain dying but not good enough to become stable. Next round, the DC increases to 11, and she rolls a 16. Since that result exceeds the DC by at least 5 points, Tirsa becomes stable but remains [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]]. Assuming that she isn’t healed by her friends (or slain by her enemies) in the meantime, she must succeed on a DC 10 Fortitude save 1 hour later to remain stable.

##### Massive Damage

If a single attack deals sufficient damage to force a saving throw against massive damage (typically 50 points, though if you use a variant system — see [[#Massive Damage Thresholds and Results|Massive Damage Thresholds and Results]], above — that amount may vary dramatically), the target of the attack makes a Fortitude save as normal. If the save fails, the target’s hit point total is reduced to 0, and he must immediately attempt a second Fortitude save (DC 10, +2 per 10 points of damage dealt by the attack or effect) to determine if he is [[#^dead-and-death|dead]], [[#^dying-and-death|dying]], or merely [disabled](disabled-and-death) (as outlined above).

For example, a character is blasted by the fiery breath of an old red dragon. Failing his Reflex save, he takes 88 points of fire damage. Thankfully, he wears a major ring of fire resistance, which reduces this damage by 20 points to 68. This number is far lower than his current hit points, but is enough damage to trigger a DC 15 Fortitude save due to massive damage. Unfortunately, he rolls a natural 1 on the saving throw and is reduced to 0 hit points. He must now attempt a Fortitude save to see if he is merely disabled, dying, or if this attack slays him outright. The DC is 22 (base 10, +12 because the damage dealt is at least 60 points but not 70 points). This time he rolls a 23, which is good enough to remain [[#^disabled-and-death|disabled]]. He remains conscious, but may attempt only a standard action or a move action (plus free actions) each round, and if he tkes a standard action, he must take another DC 22 Fortitude save to remain disabled after taking that action. If he fails that save, or if he takes even a single point of lethal damage, he is rendered [[rangoric-srd/rules/Special Abilities and Conditions#^unconscious|unconscious]] and begins [[#^dying-and-death|dying]] (or may be slain outright).

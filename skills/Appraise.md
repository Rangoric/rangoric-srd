---
srd-type: "skill"
section: "Skills"
book: "Occult Adventures"
key-ability: "Int"
based-on:
  - "[[path srd 3.5/rules/pathfinder-unchained/Skill Unlocks|Skill Unlocks (PF1 Unchained)]]"
  - "[[fantasy srd 3.5/skills/Appraise|Appraise (3.5)]]"
  - "[[fantasy srd 3.5/epic/Epic Skills|Epic Skills (3.5)]]"
  - "[[path srd 3.5 foundry/rules/Skills#Psychometry|Psychometry (PF1 Foundry)]]"
status: draft
change: modified
pi-review: scanned 2026-10-15
tags: [rangoric, rangoric/skill, background]
---

# Appraise

**Check**: You can appraise common or well-known objects with a DC 12 Appraise check. Failure means that you estimate the value at 50% to 150% (2d6+3 times 10%) of its actual value.

Appraising a rare or exotic item requires a successful check against DC 15, 20, or higher. If the check is successful, you estimate the value correctly; failure means you cannot estimate the item’s value.

A [[rangoric-srd/equipment/gear/Magnifying Glass|magnifying glass]] helps with Appraise checks on small or highly detailed items, such as a gem, and a [[rangoric-srd/equipment/gear/Scale, Merchant's|merchant’s scale]] helps with items valued by weight, including anything made of precious metals. These bonuses stack.

**Action**: Appraising an item takes 1 minute (ten consecutive full-round actions).

**Try Again**: No. You cannot try again on the same object, regardless of success.

**Special**: Dwarves are better at appraising items made of stone or metal; see the [[rangoric-srd/races/Dwarf|dwarf]].

The master of a [[rangoric-srd/classes/Wizard#Familiars|raven familiar]] gains a bonus on Appraise checks.

**Untrained**: For common items, failure on an untrained check means no estimate. For rare items, success means an estimate of 50% to 150% (2d6+3 times 10%).

## Advanced Uses

The character can sense magical auras in objects.

| Task         | DC  |
| ------------ | --- |
| Detect magic | 50  |

_Detect Magic_: The character can sense if an item has a magical aura. He or she can then use [[rangoric-srd/skills/Mysticism|Mysticism]] to learn more about the item as if he or she had already cast detect magic on the item. This requires a full-round action.

## Unlocks

You gain these only through [[rangoric-srd/feats/Signature Skill|Signature Skill]] or a class feature such as the [[rangoric-srd/classes/Rogue#^rogue-edge|rogue’s edge]]; see [[rangoric-srd/skills/Skills Overview#^skill-unlocks|Skill Unlocks]].

**5 Ranks**: A successful DC 20 Appraise check reveals whether an item is magical, and a second check (DC = 25 + the item's caster level) unveils its properties. You can use Appraise to detect non-written forgeries and counterfeits.

**10 Ranks**: You can determine the most expensive object a creature is wearing or wielding (or in a 5-foot cube) as a standard action by succeeding at a DC 20 check. You never make a wildly inaccurate appraisal of an item's value.

**15 Ranks**: Determining the most expensive object as above is a move action. You can use 10 + your Appraise bonus, at a –10 penalty, in place of your Will Defense to disbelieve a figment or glamer.

**20 Ranks**: Determining the most expensive object as above is a move action, and if the check succeeds, you gain a +2 circumstance bonus on [[rangoric-srd/combat/Combat Maneuvers|combat maneuver]] checks to [[rangoric-srd/combat/Combat Maneuvers#Steal|steal]] that object or disarm a creature of that object for 1 minute.

## Occult Unlocks

Occult skill unlocks need the ability to cast [[rangoric-srd/spells/Magic Overview#Psychic Magic|psychic spells]] or the [[rangoric-srd/feats/Psychic Sensitivity|Psychic Sensitivity]] feat; see [[rangoric-srd/skills/Skills Overview#^occult-unlocks|Occult Skill Unlocks]] for who can use them and how often.

### Psychometry

You can read the psychic impressions left on objects or in places by previous owners and events.

**Items that help**: [[rangoric-srd/equipment/gear/Psychometrist's Gloves|psychometrist's gloves]], a [[rangoric-srd/magic-items/wondrous-items/Sensory Deprivation Hood|sensory deprivation hood]].

**Check**: Once per day, you can concentrate for 1 minute while touching an item or place, receiving flashes of insight about its nature and ownership. After the minute, you attempt a DC 15 Appraise check to decipher the visions. You learn one piece of information, chosen by the GM, about its historical significance or its last owner, such as a glimpse of the last owner’s appearance or emotional state when it last used the item. You learn one more piece for every 10 by which your result exceeds the DC, as long as you concentrate for 1 more minute for each piece. If you fail by less than 5, or the item has no significant psychic imprint, you learn nothing. If you fail by 5 or more, the item seems psychically significant even if it isn’t, and what you learn is wildly inaccurate.

If you use psychometry on an item affected by _[[rangoric-srd/spells/Charge Object|charge object]]_ or _[[rangoric-srd/spells/Implant False Reading|implant false reading]]_, you automatically learn all the information the spell imprinted, and the spell also attacks your Will. If the item is affected by _implant false reading_, on a miss you realize the information is false and can learn the true information as well. On a hit, or if the item is affected by _charge object_, you believe the information is true.

**Action**: Reading an object takes at least 1 minute of uninterrupted concentration.

**Try Again**: Yes. Readings on an object or place always give the same results unless its circumstances or ownership have changed, but more checks might reach further back into its history. A false imprint doesn’t attack you again. You can still use psychometry only once per day.

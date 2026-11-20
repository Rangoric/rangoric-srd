---
srd-type: "skill"
section: "Skills"
book: "Occult Adventures"
key-ability: "Int"
trained-only: true
based-on:
  - "[[path srd 3.5/rules/pathfinder-unchained/Skill Unlocks|Skill Unlocks (PF1 Unchained)]]"
  - "[[modern srd 3.5/skills/Treat Injury|Treat Injury (Modern)]]"
  - "[[star srd 3.5/rules/Skills|Skills (Starfinder)]]"
  - "[[fantasy srd 3.5/skills/Craft|Craft (3.5)]]"
  - "[[path srd 3.5 foundry/rules/Skills#Faith Healing|Faith Healing (PF1 Foundry)]]"
status: draft
change: new
pi-review: 2026-10-31
tags: [rangoric, rangoric/skill, core]
---

# Medicine

Medicine is the trained study of the body and how to mend it: treating wounds and illness, surgery, and making remedies. It came from Modern’s Treat Injury and Starfinder’s Medicine (2026-10-31). Without training you can still give first aid through [[rangoric-srd/skills/Fieldcraft|Fieldcraft]].

## First Aid

Medicine can take any [[rangoric-srd/actions/First Aid|First Aid]] action: stabilizing the dying, long-term care, and treating wounds, deadly wounds, poison and disease.

## Restoring Hit Points

**Check**: With a [[rangoric-srd/equipment/gear/Healer's Kit|healer’s kit]], a DC 15 check restores 1d4 hit points to a character who has lost some, up to his or her full normal total. This can be used successfully on a character only once per day.

**Action**: Full-round action.

## Reviving

**Check**: With a [[rangoric-srd/equipment/gear/Healer's Kit|healer’s kit]], a DC 15 check removes the dazed, stunned or unconscious condition from a character. You can’t revive an unconscious character at –1 hit points or lower without first stabilizing him or her.

**Action**: Standard action.

## Surgery

**Check**: With surgical tools (a surgery kit, in modern settings), a DC 20 check restores 1d6 hit points per character level of the patient, up to his or her full normal total. Surgery can be used successfully on a character only once in 24 hours. The patient is fatigued for 24 hours, minus 2 hours for every point by which you beat the DC, but never less than 6 hours.

Installing or removing a cybernetic implant, in settings that have them, is also surgery.

**Action**: 1d4 hours, plus 1 hour for every point below 0 hit points the patient has fallen.

## Making Remedies

You make antitoxin and other remedies with Medicine instead of Craft (alchemy), following the [[rangoric-srd/skills/Craft|Craft]] rules for time, raw materials and alchemical equipment. Antitoxin has a DC of 25. In tech settings, drugs and medicines are made the same way.

## For Every Use

**Try Again**: Yes for restoring hit points, reviving and surgery.

**Special**: Without the right kit or tools you take a –4 penalty. You can restore your own hit points with a –5 penalty, but you can’t revive yourself or operate on yourself.

## Unlocks

You gain these only through [[rangoric-srd/feats/Signature Skill|Signature Skill]] or a class feature such as the [[rangoric-srd/classes/Rogue#^rogue-edge|rogue’s edge]]; see [[rangoric-srd/skills/Skills Overview#^skill-unlocks|Skill Unlocks]].

**5 Ranks**: When you [[rangoric-srd/actions/Treat Deadly Wounds|treat deadly wounds]], the target recovers hit points and ability damage as if it had rested for a full day.

**10 Ranks**: When you [[rangoric-srd/actions/Treat Deadly Wounds|treat deadly wounds]], the target recovers hit points as if it had rested for a full day with long-term care.

**15 Ranks**: When you [[rangoric-srd/actions/Treat Deadly Wounds|treat deadly wounds]], the creature recovers hit point and ability damage as if it had rested for 3 days.

**20 Ranks**: When you [[rangoric-srd/actions/Treat Deadly Wounds|treat deadly wounds]], the target recovers hit point and ability damage as if it had rested for 3 days with long-term care.

## Occult Unlocks

Occult skill unlocks need the ability to cast [[rangoric-srd/spells/Magic Overview#Psychic Magic|psychic spells]] or the [[rangoric-srd/feats/Psychic Sensitivity|Psychic Sensitivity]] feat; see [[rangoric-srd/skills/Skills Overview#^occult-unlocks|Occult Skill Unlocks]] for who can use them and how often.

### Faith Healing

You apply esoteric principles to temporarily suspend or remove curses, diseases and ability damage.

**Items that help**: a [[rangoric-srd/equipment/gear/Portable Sweat Lodge|portable sweat lodge]].

**Check**: You can use faith healing once per day. The DC and effect of the Medicine check depend on the task you attempt. You can’t use faith healing on yourself.

*Restore Vitality*: You suppress [[rangoric-srd/rules/Special Abilities and Conditions#^ability-damaged|ability damage]]. You perform a 1-hour ceremony, then attempt a Medicine check against the DC of the effect that caused the ability damage. If you succeed, you suppress 1 point of ability damage for 1 hour, plus 1 more point and 1 more hour for every 5 by which your result exceeds the DC. A creature can benefit from this treatment no more than once per day.

*Suspend Affliction*: You treat one [[rangoric-srd/rules/Afflictions#Curse|curse]], [[rangoric-srd/rules/Afflictions#Disease|disease]] or [[rangoric-srd/rules/Afflictions#Poison|poison]] affecting a creature. You enter a deep trance for 1 hour while you treat the subject, then attempt your Medicine check. If you succeed, you suspend the affliction’s effects for 1 hour, plus 1 hour for every 5 by which you exceed the DC. This time doesn’t count against the effect’s duration (if any). The affliction can still be cured by other means while it’s suspended.

*Remove Affliction*: You can try to remove an affliction permanently in an 8-hour ceremony, after which you attempt a Medicine check. If your result is at least double the affliction’s DC, the sufferer can attempt another saving throw against the original DC to cast off the effect permanently.

| Task | DC |
| --- | --- |
| Restore vitality | Effect’s save DC |
| Suspend affliction | Affliction’s save DC |
| Remove affliction | Double the affliction’s save DC |

**Action**: Restoring vitality and suspending an affliction each take 1 hour in a quiet place. Removing an affliction permanently takes 8 hours of heavy activity.

**Try Again**: Varies. A creature can’t be the subject of faith healing more than once per day. You can’t try again to remove an affliction permanently.

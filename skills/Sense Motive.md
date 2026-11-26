---
srd-type: "skill"
section: "Skills"
book: "Occult Adventures"
key-ability: "Wis"
based-on:
  - "[[path srd 3.5/skills/Sense Motive|Sense Motive (PF1)]]"
  - "[[path srd 3.5/rules/pathfinder-unchained/Skill Unlocks|Skill Unlocks (PF1 Unchained)]]"
  - "[[fantasy srd 3.5/skills/Sense Motive|Sense Motive (3.5)]]"
  - "[[fantasy srd 3.5/epic/Epic Skills|Epic Skills (3.5)]]"
  - "[[path srd 3.5 foundry/rules/Skills#Prognostication|Prognostication (PF1 Foundry)]]"
status: draft
change: modified
pi-review: scanned 2026-10-15
tags: [rangoric, rangoric/skill, core]
---

# Sense Motive

**Check**: A successful check lets you avoid being bluffed (see the Deception skill). You can also use this skill to determine when “something is up” (that is, something odd is going on) or to assess someone’s trustworthiness.

| Task                      | Sense Motive DC |
| ------------------------- | --------------- |
| Hunch                     | 20              |
| Sense enchantment         | 25 or 15        |
| Discern secret message    | Varies          |
| Discern partial alignment | 60              |
| Discern full alignment    | 80              |
| Detect surface thoughts   | 100             |

_Hunch_: This use of the skill involves making a gut assessment of the social situation. You can get the feeling from another’s behavior that something is wrong, such as when you’re talking to an impostor. Alternatively, you can get the feeling that someone is trustworthy. If you fail by 5 or more, you might infer false information.

_Sense Enchantment_: You can tell that someone’s behavior is being influenced by an enchantment effect (by definition, a mind-affecting effect), even if that person isn’t aware of it. The usual DC is 25, but if the target is dominated (see dominate person), the DC is only 15 because of the limited range of the target’s activities.

_Discern Secret Message_: You may use Sense Motive to detect that a hidden message is being transmitted via the Deception skill. In this case, your Sense Motive check is opposed by the Deception check of the character transmitting the message. For each piece of information relating to the message that you are missing, you take a –2 penalty on your Sense Motive check. If you succeed by 4 or less, you know that something hidden is being communicated, but you can’t learn anything specific about its content. If you beat the DC by 5 or more, you intercept and understand the message. If you fail by 4 or less, you don’t detect any hidden communication. If you fail by 5 or more, you infer some false information.

**Action**: Trying to gain information with Sense Motive generally takes at least 1 minute, and you could spend a whole evening trying to get a sense of the people around you.

**Try Again**: No, though you may make a Sense Motive check for each Deception check made against you.

**Special**: A [[rangoric-srd/classes/Ranger#^ranger-favored-enemy|ranger]] gains a bonus on Sense Motive checks when using this skill against a favored enemy.

## Advanced Uses

The character can discern a target’s alignment and even detect surface thoughts.

_Discern Partial Alignment_: This use of the skill lets a character discern one component of a target’s alignment. When making the check, the character states whether he or she is trying to discern the law-chaos or good-evil component. A character can’t retry the check, and he or she can’t use this to discern more than one component of the alignment (but see below). The target must be visible and within 30 feet of the character.

_Discern Full Alignment_: This use of the skill lets a character determine both components of a target’s alignment. The character can’t retry the check. The target must be visible and within 30 feet of the character.

_Detect Surface Thoughts_: This lets a character read the surface thoughts of a single target (as the 3rd-round effect of the detect thoughts spell). There is no defense against this effect, though the target can use Deception to disguise his or her surface thoughts (see the Deception skill description), in which case this becomes an opposed check (any result lower than 100 automatically fails). The target must be visible and within 30 feet of the character.

## Unlocks

You gain these only through [[rangoric-srd/feats/Signature Skill|Signature Skill]] or a class feature such as the [[rangoric-srd/classes/Rogue#^rogue-edge|rogue’s edge]]; see [[rangoric-srd/skills/Skills Overview#^skill-unlocks|Skill Unlocks]].

**5 Ranks**: If you were aware of an opponent before rolling initiative (such as when you ambush an enemy or negotiations break down into combat, but not when both sides happen upon each other or you are surprised), you can attempt a Sense Motive check as part of your initiative check (DC = 11 + the highest Deception modifier among your opponents or DC 15, whichever is higher). If you succeed, you gain a +1 bonus on the initiative check, plus an additional +1 for every 5 by which you exceeded the DC.

**10 Ranks**: After 1 minute of conversation, you can read a creature's surface thoughts (as detect thoughts)by attempting a Sense Motive check at a –20 penalty opposed by the creature's Deception check.

**15 Ranks**: You can read surface thoughts as above after 1 round. In addition, when attacked, you can attempt a Sense Motive check as an immediate action opposed by your target's attack roll. A successful check grants a +2 insight bonus to your AC against attacks from that specific opponent for 1 minute.

**20 Ranks**: You can read surface thoughts as above as a standard action. A successful check to gain an insight bonus to your AC also negates the attack that triggered it.

## Occult Unlocks

Occult skill unlocks need the ability to cast [[rangoric-srd/spells/Magic Overview#Psychic Magic|psychic spells]] or the [[rangoric-srd/feats/Psychic Sensitivity|Psychic Sensitivity]] feat; see [[rangoric-srd/skills/Skills Overview#^occult-unlocks|Occult Skill Unlocks]] for who can use them and how often.

### Prognostication

You are skilled in folk divination. The most common methods are cartomancy (reading cards), cheiromancy (reading palms), crystallomancy (crystal-gazing), extispicy (reading animal entrails), horoscopy (reading a creature’s birth stars), oneiromancy (interpreting dreams), osteomancy (reading cast bones) and pyromancy (reading flames).

**Items that help**: a [[rangoric-srd/equipment/gear/Prognostication Manual|prognostication manual]].

**Check**: Once per day, you can predict a creature’s fortune for the near future. You spend 10 minutes interpreting the means of divination at your disposal, then the GM attempts a secret Sense Motive check against a DC modified by the subject’s Hit Dice (see the table). The result can give you basic insight into the subject’s nature, including its alignment, class and levels or Hit Dice, and might reveal clues to its immediate future. Reading the immediate future as _[[rangoric-srd/spells/Augury|augury]]_ has a chance of a meaningful reading equal to 60% plus 5% for every point by which the check result exceeds the DC (to a maximum of 90%). With one check, you learn everything whose DC you meet: for instance, with a result of 22 against a creature with 2 HD, you learn its alignment and class, but not its level, HD or fortune.

| Task                          | DC                 |
| ----------------------------- | ------------------ |
| Determine alignment           | 15 + creature’s HD |
| Determine class               | 20 + creature’s HD |
| Determine level or HD         | 25 + creature’s HD |
| Determine fortune as _augury_ | 25 + creature’s HD |

**Action**: Reading a creature’s fortune takes 10 minutes of uninterrupted contemplation, and the subject must be present.

**Try Again**: Yes. You can read a creature’s fortune repeatedly, but only once per 24 hours.

**Special**: Items crafted for the sole purpose of prognostication give a +2 circumstance bonus on Sense Motive checks to prognosticate.

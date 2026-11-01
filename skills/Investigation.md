---
srd-type: "skill"
section: "Skills"
key-ability: "Int"
based-on:
  - "[[fantasy srd 3.5/skills/Search|Search (3.5)]]"
  - "[[fantasy srd 3.5/epic/Epic Skills|Epic Skills (3.5)]]"
  - "[[modern srd 3.5/skills/Investigate|Investigate (Modern)]]"
  - "[[modern srd 3.5/skills/Research|Research (Modern)]]"
status: draft
change: new
pi-review: 2026-10-31
tags: [rangoric, rangoric/skill, core]
---

# Investigation

Investigation is finding things, working out what they mean, and digging through records. It took over from Search (2026-10-31) and added Modern's Investigate and Research. [[rangoric-srd/skills/Perception|Perception]] notices what's happening around you; Investigation is the careful, deliberate look.

## Searching

**Check**: You generally must be within 10 feet of the object or surface to be searched. The table below gives DCs for typical tasks involving the Investigation skill.

| Task                                                | Investigation DC                               |
| --------------------------------------------------- | --------------------------------------- |
| Ransack a chest full of junk to find a certain item | 10                                      |
| Notice a typical secret door or a simple trap       | 20                                      |
| Find a difficult nonmagical trap (rogue only) (1)   | 21 or higher                            |
| Find a magic trap (rogue only) (1)                  | 25 + level of spell used to create trap |
| Notice a well-hidden secret door                    | 30                                      |
| Find a footprint                                    | Varies (2)                              |
| Sense magic | 60 |

1 *Dwarves can also find traps built into or out of stone; see the dwarf’s [[rangoric-srd/rules/PC Races#^dwarf-stonecunning|stonecunning]].*

2 *A successful Investigation check can find a footprint or similar sign of a creature’s passage,  
but it won’t let you find or follow a trail. See the [[rangoric-srd/feats/Track|Track]] feat for the appropriate DC.*

**Action**: It takes a full-round action to search a 5-foot-by-5-foot area or a volume of goods 5 feet on a side.

**Special**: Elves and half-elves are better at Investigation checks, and an elf can notice a secret door just by passing near it; see the [[rangoric-srd/rules/PC Races#Elves|elf]] and [[rangoric-srd/rules/PC Races#Half-Elves|half-elf]].

The spells explosive runes, fire trap, glyph of warding, symbol, and teleportation circle create magic traps that a character with trapfinding can find by making a successful Investigation check and then can attempt to disarm by using [[rangoric-srd/skills/Engineering|Engineering]]. Identifying the location of a snare spell has a DC of 23. Spike growth and spike stones create magic traps that can be found using Investigation, but against which Engineering checks do not succeed. See the individual spell descriptions for details.

Active abjuration spells within 10 feet of each other for 24 hours or more create barely visible energy fluctuations. These fluctuations give you a +4 bonus on Investigation checks to locate such abjuration spells.

**Restriction**: Anyone can use Investigation to find simple traps, but finding harder ones takes [[rangoric-srd/classes/Rogue#^rogue-trapfinding|trapfinding]]. (Exception: The spell find traps temporarily enables a cleric to use the Investigation skill as if he were a rogue.)

A dwarf, even one without trapfinding, can use the Investigation skill to find difficult traps built into or out of stone; see the dwarf’s [[rangoric-srd/rules/PC Races#^dwarf-stonecunning|stonecunning]].

## Advanced Uses

The character can sense the presence of magic in an area.

*Sense Magic*: The character senses the presence of any active magical effects in the area being searched. The character can’t determine the number, strength, or type of the effects.

## Analyzing Clues

**Check**: You can make an Investigation check to get more out of a clue you've found: what made a mark, how old a bloodstain is, which way a struggle went. This doesn't find clues where there are none. It only draws more information from one you already have.

The base DC to analyze a clue is 15, modified by how long ago the clue was left and how much the scene has been disturbed.

| Circumstances | DC Modifier |
| --- | --- |
| Every day since the event (maximum +10) | +2 |
| Scene is outdoors | +5 |
| Scene slightly disturbed | +2 |
| Scene moderately disturbed | +4 |
| Scene extremely disturbed | +6 |

**Collecting Evidence**: Where there are laboratories that study evidence, you can collect and prepare a piece of evidence for one with a DC 15 Investigation check. This takes an evidence kit; without one, you take a –4 penalty. If you succeed, the lab can use it. If you fail, the lab takes a –5 penalty on its checks, and if you fail by 5 or more, the evidence can't be used. If you succeed by 10 or more, the lab gets a +2 circumstance bonus on its checks.

**Action**: Analyzing a clue is a full-round action. Collecting evidence takes 1d4 minutes per object.

**Try Again**: Analyzing a clue again gives nothing new unless another clue turns up. Evidence can't be collected twice unless there's more of it.

## Research

**Check**: You can research a topic in a library, archive, set of records or database. The GM decides how obscure the topic is (the more obscure, the higher the DC) and what information can be found where you're looking. A successful check gives you a general idea of the topic, as long as the information is there to be found. The higher the result, the more complete the information. To find one specific fact, date, map or similar detail, add +5 to +15 to the DC.

**Action**: A Research check takes 1d4 hours.

**Try Again**: Yes. You can take 10 or take 20 on a Research check.

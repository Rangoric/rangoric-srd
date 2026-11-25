---
srd-type: "overview"
section: "Monsters"
book: "Bestiary"
based-on:
  - "[[path srd 3.5/rules/bestiary/monster-advancement/Adding Class Levels|Adding Class Levels (PF1)]]"
status: draft
change: new
pi-review: 2026-11-24
tags: [rangoric, rangoric/overview]
---

# Adding Class Levels (Alternate)

Of all the methods of advancing a monster, adding class levels requires the most adjudication and careful comparison. Some classes truly add to the power and abilities of some monster types, while others do not. For example, adding levels of barbarian to a hill giant can be a great addition, whereas adding levels of sorcerer is less useful. When adding class levels to a creature, take the following three steps.

## Step 1: Determine Creature's Role

When adding class levels to a creature, the first step is to determine what role the base creature fulfills: combat, spell, skill or special, as described in [[rangoric-srd/monsters/Monster Roles|Monster Roles]], which also lists the roles of many monsters. A creature can fall into more than one role if its abilities are diverse.

**Table: Monsters with Class Levels**

| Monster Role                                                                                     | Barbarian, Fighter, Ranger | Cleric, Druid, Sorcerer, Wizard | Bard, Rogue | Monk, Paladin |
| ------------------------------------------------------------------------------------------------ | -------------------------- | ------------------------------- | ----------- | ------------- |
| Combat                                                                                           | Key                        | —                               | —           | —             |
| Spell                                                                                            | —                          | Key\*                           | —           | —             |
| Skill                                                                                            | Key                        | —                               | Key         | —             |
| Special                                                                                          | —                          | —                               | —           | —             |
| \* This class is only key if its spellcasting levels stack with those possessed by the creature. |                            |                                 |             |               |

^monsters-with-class-levels

## Step 2: Add Class Levels

Once you have determined the creature's role, it's time to add class levels. The first step of this process is to modify the creature's ability scores. Creatures with class levels receive +4, +4, +2, +2, +0, and –2 adjustments to their ability scores, assigned in a manner that enhances their class abilities. Creatures with NPC class levels do not receive adjustments to their ability scores.

Next, add the class levels to the monster, making all of the necessary additions to its HD, hit points, BAB, CMB, CMD, feats, skills, spells, and class features. If the creature possesses class features (such as spellcasting or sneak attack) for the class that is being added, these abilities stack. This functions just like adding class levels to a character without racial Hit Dice.

A monster with class levels always possesses treasure equal to an NPC of a level equal to the monster's final CR (as calculated in Step 3, below). To determine the value of this gear, use the value listed for a heroic NPC of that level, as listed in [[rangoric-srd/rules/Treasure Generator#^npc-gear|Table: NPC Gear]]. Once a total GP value is determined, follow the rules for outfitting an NPC as outlined in that section. Gear should help a monster with class levels remain challenging and retain statistics close to those presented on [[rangoric-srd/design-notes/Monster Creation|Table: Monster Statistics by CR]].

## Step 3: Determine CR

Determining the final CR for a creature with class levels requires careful consideration. While adding a class level to a monster that stacks with its existing abilities and role generally adds 1 to its CR for each level taken, adding classes that do not stack is more complicated.

[[#^monsters-with-class-levels|Table: Monsters with Class Levels]] gives general guidelines regarding which core classes add directly to a monster's abilities based on its role. Classes that are marked “key” generally add 1 to a creature's CR for each level added. Classes marked with a “—” increase a creature's CR by 1 for every 2 class levels added until the number of levels added are equal to (or exceed) the creature's original CR, at which point they are treated as “key” levels (adding 1 to the creature's CR for each level added). Creatures that fall into multiple roles treat a class as key if either of its roles treat the class as key. Note that levels in NPC classes are never considered key.

This is the second version of these rules; the first is Adding Class Levels in [[rangoric-srd/monsters/Improving Monsters|Improving Monsters]] (associated and nonassociated class levels).

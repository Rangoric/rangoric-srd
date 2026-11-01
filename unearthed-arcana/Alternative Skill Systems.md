---
srd-type: "overview"
section: "Unearthed Arcana"
based-on:
  - "[[fantasy srd 3.5/unearthed-arcana/Alternative Skill Systems|Alternative Skill Systems (3.5)]]"
status: draft
change: modified
pi-review: scanned 2026-10-15
tags: [rangoric, rangoric/overview]
---

## Unearthed Arcana

### Alternative Skill Systems

When compared to the combat maneuvers and magical talents of the characters in the game, the skill system often appears to run a distant third in importance. It is, however, a detailed part of the d20 game system and a place where you'll often spend a considerable amount of time if you create detailed PCs, NPCs, or monsters to use in your game. The variant skill systems discussed here eliminate some of the complexity of the standard skill system, but at the expense of fewer opportunities for customization.

##### Maximum Ranks, Limited Choices

This variant skill system allows for some customization during character creation and during character advancement. It allows for more up-front choices and fewer down the road. In general, this system works for players and game masters who want the versatility of the skill system but don't want to worry about counting up every skill points and adjusting skills every level. It's particularly useful for game masters who are creating NPCs from scratch.

Essentially, this system treats each skill as either a known skill or an unknown skill. A character is considered to have the maximum number of ranks allowable in any skill known to that character, and no ranks in any skill unknown to that character.

###### Learning Skills

Each character begins play knowing a number of skills equal to the number of skill points his character would gain with each new class level. When creating a character, choose a number of skills known based on your first class level (see [[rangoric-srd/unearthed-arcana/Alternative Skill Systems|Table: Skills by Class]]). Human characters add one to their number of known skills.

For classes or monster types not listed on the table, simply assign a number of skills known equal to the number of skill points gained at each new level or Hit Dice, plus the character's or monsters intelligence modifier.

Note whether each skill known is a class skill or cross-class skill for your character, based on his starting class.

**Table: Skills By Class**

| Class     | Number of Skills Known (1) |
| --------- | -------------------------- |
| Barbarian | 4 + Int modifier           |
| Bard      | 6 + Int modifier           |
| Cleric    | 2 + Int modifier           |
| Druid     | 4 + Int modifier           |
| Fighter   | 2 + Int modifier           |
| Monk      | 4 + Int modifier           |
| Paladin   | 2 + Int modifier           |
| Ranger    | 6 + Int modifier           |
| Rogue     | 8 + Int modifier           |
| Sorcerer  | 2 + Int modifier           |
| Wizard    | 2 + Int modifier           |

1.  Minimum of one skill known, regardless of Intelligence penalty.

For example, a gnome bard has an Intelligence of 12 (+1 bonus) and thus may know seven skills at 1st level. He selects the following seven skills (and denotes [[rangoric-srd/skills/Imitation|Imitation]] as a cross-class skill): [[rangoric-srd/skills/Performance|Performance]] (string instruments), [[rangoric-srd/skills/Identifying Magic|Magic skill]], [[rangoric-srd/skills/Emulation|Emulation]], [[rangoric-srd/skills/Persuasion|Persuasion]], [[rangoric-srd/skills/Perception|Perception]], [[rangoric-srd/skills/Linguistics|Linguistics]], and [[rangoric-srd/skills/Imitation|Imitation]] (cc)

###### Skill Modifiers

For each of your known skills, your modifier is calculated as if you had the maximum number of ranks allowable in that skill. For a class skill, the skill modifier is equal to your character level +3; for a cross-class skill, the modifier is half that number, rounded down.

As with a normal skill check, you also add any other modifiers that apply (racial bonuses, ability modifiers, and so forth).

For example, at 5th level, the same bard has a Charisma of 16 and a masterwork lute. When he makes a [[rangoric-srd/skills/Performance|Performance]] (string instruments) check, he uses this formula:

> 1d20 + 8 (class skill) + 3 (Cha modifier) + 1 (masterwork lute)

When he makes an [[rangoric-srd/skills/Imitation|Imitation]] check, the formula changes to reflect the fact that Forgery is a cross-class skill:

> 1d20 + 4 (cross-class skill) + 1 (Int modifier)

Skills that don't have ranks, such as [[rangoric-srd/skills/Linguistics|Linguistics]], work differently. A character who chooses Linguistics as a known skill learns four new languages at 1st level and one new language at each level thereafter (if Linguistics is a class skill) or two new languages at 1st level and one new language at each odd-numbered level thereafter (if Linguistics is a cross-class skill).

###### Prerequisites and Minimum Skill Ranks

If you need to determine how many ranks your character has in a skill (for purposes of meeting prerequisites for prestige class or feat requirements, or for any other reason), simply assume you have the maximum number of ranks you could have in any of the skills you know. For class skills, that's always your character level +3, and for cross-class skills it's half that total (rounded down).

For example, to use the [[rangoric-srd/classes/Bard#^song-of-freedom|song of freedom]] bardic music ability, the bard must be at least 12th level and have at least 15 ranks in a [[rangoric-srd/skills/Performance|Performance]] skill. Since Perform is a class skill for bards, and the bard has selected Perform (string instruments) as one of his skills, he is treated as having the maximum possible ranks in Performance (string instruments). Thus, by 12th level, he is considered to have 15 ranks in Performance (string instruments). At the same time, he is considered to have only 7 ranks in [[rangoric-srd/skills/Imitation|Imitation]] (a cross-class skill).

###### Multiclass Characters

Multiclassing under this variant system is a little more complex than in the normal rules and does not achieve the same results as single classing would.

First, compare your current list of known skills to your new class's list of class skills. If any of your new class's class skills are currently known by you as cross-class skills, you may choose one such skill and designate it as a class skill. This change immediately increases your modifier for the chosen skill (see [[#Skill Modifiers|Skill Modifiers]], above). Every time you gain a level in this new class, you may choose another such skill, if applicable, and change it from a cross-class skill to a class skill.

Second, compare your new class's number of skills known at 1st level to the number of skills known 1st level from the class you already have. If you already have more than one class, compare it to the class that would grant the highest number of skills, even if that wasn't your first class. For example, if you are playing a 2nd-level rogue/5th-level fighter and pick up a level of barbarian, use the rogue's number of skills (8), even though you have more fighter levels than rogue levels.

If your new class grants an equal or lower number of skills, you can choose one skill from your new class's list to add to the skills you know as a class skill. You immediately gain the new skill at the maximum possible tank.

If your new class grants you up to four more skills than your best previous class, you may choose two skills from your new class's list to add to the skills you know as class skills. You immediately gain the two new skills at the maximum possible rank.

If your new class grants you five or more skills over and above your best class, you may choose three skills from your new class's list to add to the skills you know as class skills. You immediately gain the three new skills at the maximum possible rank.

Perform this operation every time you gain 1st level in a new class.

This system reflects the idea that by multiclassing, you learn more abilities and, in particular, skills. Most characters do end up with higher numbers of skills and ranks if they multiclass under this variant system, but they still have fewer skill choices.

###### Learning New Skills

If you are not interested in multiclassing but wish to learn new skills anyway, you have two options.

If you increase your Intelligence modifier, you learn one additional skill. Make this skill choice using the class skill list of any of your existing classes. You can choose a class skill or a cross-class skill.

Alternatively, your game master can allow the [[#Skill Knowledge (General)|Skill Knowledge]] feat, which increases your characters number of known skills.

##### Level-Based Skills

This even simpler variant system assumes that skills are much less important in your game and that you really don't want to be bothered with tracking or even looking for skill ranks over the course of a fast-paced game session.

###### Making Skill Checks

Under this system, characters do not normally acquire skill ranks or track skill points at all. Each character has a list of known skills that includes all his class skills (from all classes).

When a character makes a skill check under this variant skill system, use these formulas:

> **Class Skills:** 1d20 + character level + modifiers
> 
> **Cross-Class Skills:** 1d20 + modifiers

Here, the trade-off for simplicity is ability. Characters with a large number of class skills are extremely versatile, but even their average skill check result is lower than that made by a character using the existing skill system. For skills outside their areas of expertise (cross-class skills), they have nothing beyond their own basic abilities and perhaps magic or other bonuses.

Under this system, all barbarians are good at climbing, jumping, listening, riding, and the like, but have virtually no ability to bluff, hide, search, or perform other cross-class tasks. Monks become superior acrobats (with talent in balancing, climbing, jumping, and tumbling) but no proficiency at anything outside the idiom of the typical monk (such as disguise or survival).

A character who wishes to specialize or branch out her skill knowledge can still select feats such as [[rangoric-srd/feats/Skill Focus|Skill Focus]] and the like, regardless of whether the skills affected by the feat are class skills or cross-class skills. This is the best avenue for a fighter who wishes to improve his awareness, a wizard who wants to become intimidating, and so on.

Skills that don't have ranks, such as [[rangoric-srd/skills/Linguistics|Linguistics]], work differently. A character who has Linguistics as a class skill learns four new languages at 1st level and one new language at each level thereafter. Characters without Linguistics as a class skill can't learn new languages without selecting the [[#Skill Knowledge (General)|Skill Knowledge]] feat and designating Linguistics as a class skill.

###### Multiclassing

Since skills are not as important in a game that uses this system (at least, that's the intention), when a character multiclasses, combine the skill lists. Consider all skills on both lists as class skills.

###### Learning New Skills

As with the maximum ranks variant described earlier, the [[#Skill Knowledge (General)|Skill Knowledge]] feat (see below) can be selected by a character to add to his number of skills known. In this case, the feat only allows you to designate a cross-class skill as a class skill (since you already know all your class skills).

##### Skill Knowledge (General)

You gain access to new knowledge and abilities.

**Benefit:** Choose any two skills from one of your current classes' skill lists. You now know these skills as class skills.

**Special:** Instead of choosing two class skills, you may choose one cross-class skill (whether you already know it or not) and learn it, treating it as a class skill from that point forward.

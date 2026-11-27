---
srd-type: "rules"
section: "Rules"
aliases:
  - "Occult Ritual"
based-on: []
status: draft
change: new
pi-review: 2026-11-17
tags: [rangoric, rangoric/rules]
---

# Occult Rituals

Occult rituals are spells that anyone can attempt to cast, not only those who cast arcane, divine or [[rangoric-srd/spells/Magic Overview#^psychic-magic|psychic]] spells. Casting one is perilous. The checks are hard to make, and failure can weaken the casters or worse; even a successful ritual has a price, a backlash that affects at least the caster leading it and often those assisting.

## Casting Occult Rituals

Before performing an occult ritual, the primary caster must assemble and ready all the components it needs, as well as any secondary casters. Some occult rituals must be cast at a specific time or place; casting one at another time or in a substandard location is nearly impossible.

Casting an occult ritual takes at least 10 minutes per ritual level, and sometimes as long as 1 hour per ritual level. Every 10 minutes of the casting (every hour, for a ritual that takes 1 hour per level), one of the casters, either the primary caster or a secondary caster the primary caster names, attempts one of the skill checks the ritual requires. These checks can’t benefit from the [[rangoric-srd/skills/Skills Overview#Aid Another|aid another]] action, and the caster attempting the check can’t take 10 or take 20, even with an ability that would normally allow it when threatened or distracted. Mundane equipment that grants bonuses on skill checks usually can’t increase the bonus on a ritual’s checks, unless the GM allows it. Bonuses on the required skill checks from feats, spells (lasting through the whole casting), traits and magic items usually apply, at the GM’s discretion. The primary caster decides the order in which the skill checks are attempted, but the GM rolls the checks and tracks the ritual’s progress in secret. Once begun, a ritual must be performed to its completion unless outside influences disrupt it or it fails.

**Mysticism checks**: a ritual that calls for a [[rangoric-srd/skills/Mysticism|Mysticism]] check is attempted with Mysticism, whether or not the caster casts spells. ^ritual-magic-skill

### Secondary Casters

The primary caster leads a ritual’s casting, often with the aid of secondary casters, who can be indispensable to the casting even when they take no active part in its success. Unless the ritual says otherwise, secondary casters must be within 100 feet and line of effect of the primary caster and of each other during the whole casting.

A ritual that allows secondary casters has "SC" in its Components line, followed by a parenthetical giving any maximum or minimum number of secondary casters. A ritual without that entry doesn’t allow secondary casters.

Secondary casters can attempt the skill checks the primary caster assigns them, but their chief purpose is to aid the casting. If at least four secondary casters aid a ritual, all casters gain a +1 bonus on all skill checks attempted as part of casting it. This bonus increases by 1 for every four secondary casters beyond four, to a maximum of +5 for 20 or more secondary casters. ^ritual-secondary-casters

To cast an occult ritual, the primary caster must have learned its secrets (see [[rangoric-srd/rules/occult-rituals/Occult Rituals#Discovering Occult Rituals|Discovering Occult Rituals]]). Secondary casters can assist without fully understanding the ritual.

### Caster Level and Bonuses

Since characters who can’t cast arcane, divine or psychic spells can cast rituals, anything that would normally rely on caster level (such as range and spell resistance) uses the primary caster’s character level or total Hit Dice instead. This is so even when the ritual caster can cast spells. Characters with a caster level gain a +1 bonus on skill checks to cast a ritual, increasing by 1 for every 5 caster levels they have (to a maximum of +5 at caster level 20th). ^ritual-caster-level

### Disrupting a Ritual

A ritual is hard to disrupt. Casting a ritual doesn’t provoke [[rangoric-srd/combat/Combat Initiative and Attacks of Opportunity#Attacks of Opportunity|attacks of opportunity]], and the casters can pause the ritual to fight or take other actions, though not without consequences: for each round the ritual is paused, the DC of all its later skill checks increases by 1. A ritual is disrupted when its casting is paused for more than 1 minute, or when any of the casters is incapacitated, killed, or moved more than 100 feet from (or out of line of effect of) all the other casters.

### Success and Failure

If more than half the skill checks for an occult ritual succeed, the ritual succeeds: the primary caster (and the secondary casters, if the ritual says so) experiences the ritual’s backlash, and then the ritual’s effect occurs. The attack bonus of a ritual’s effects is the ritual level + the primary caster’s Intelligence, Wisdom or Charisma bonus (whichever is highest). ^ritual-attack-bonus

If the casters fail half of the skill checks a ritual requires (rounded down), the ritual ends, the casters experience its backlash, and its failure consequences occur, as given in each ritual’s description. ^ritual-failure

### Ritual Descriptions

Occult rituals are written like spells, with three more entries:

- **Skill Checks**: the skills the casting requires, the DC of each, and how many successes with each are needed. The checks add up to the ritual’s level.
- **Backlash**: what happens to the casters (the primary caster, or those named) whether the ritual succeeds or fails.
- **Failure**: what happens when the ritual fails, besides the backlash.

## Discovering Occult Rituals

The secrets of occult rituals are jealously guarded, hidden in coded tomes, puzzles and allusions, and recovering a ritual’s method can be an adventure of its own.

If an occult ritual is taught or its secrets are explained directly, it takes at least 1 day per ritual level to learn the method of casting it. Learning a ritual from hidden clues or from scratch takes a week or a month per ritual level (GM’s discretion). At the end of this study, the learner must succeed at an Intelligence check (DC = 15 + the ritual level if learning from clues or a coerced teacher, or DC = 10 + the ritual level if learning from an instructor eager to teach). On a failure, the secrets of the ritual elude her, though she can start again at the same rate.

## Creating Occult Rituals

Creating a new occult ritual has five steps.

**Step 1, Concept**: Decide what the ritual should do. Rituals are a way to bring unusually powerful magical effects into a game in a limited or controlled way, or to bring in such effects more narrowly than similar higher-level spells. The ritual’s purpose guides the later decisions.

**Step 2, School**: Choose the school that best suits the ritual’s effect, as for any spell. If you’re unsure, compare its effects with existing spells; if several schools could fit, use the most relevant one.

**Step 3, Ritual Level**: Occult rituals are always the equivalent of at least 4th-level spells; compare the ritual with other spells to set its level. The level sets how many skill checks the ritual requires (one per level), their base DC (28 + the ritual level), the attack bonus of its effect, and indirectly its range and duration. Any attack bonus of the ritual (including the daily attack of a temporary negative level from its backlash or failure) is the ritual level + the primary caster’s Intelligence, Wisdom or Charisma bonus (whichever is highest).

The spell a ritual is based on usually guides its range, targets, area, effect, duration, defense and spell resistance. If you’re unsure, or the effect is new, use the benchmarks below. Departing from the school’s or base spell’s benchmarks should change the ritual’s skill check DCs, and can change its casting time, as Table: Modifying Occult Rituals shows.

**Step 4, Skills**: Choose skills connected to the ritual’s concept or effect. Arcana and Theology are obvious choices, but other skills can make a ritual more interesting and let secondary casters take a more active part. Always require checks with two or more skills. A check to work the ritual’s magic itself is a [[rangoric-srd/skills/Mysticism|Mysticism]] check.

**Step 5, Backlash and Failure**: Decide the backlash and the failure effects. Like departing from the benchmarks, the backlash and its severity change the skill check DCs (see the table). A backlash should be a minor debilitation rather than a severe punishment; decide whether it affects only the primary caster or all the casters. Failure effects should be much more severe and shouldn’t invalidate or overlap with the backlash (which happens whether or not the ritual succeeds). They represent the cost of uncontrolled magic, can be very debilitating to the casters, and could even harm others (especially for high-level rituals).

**Table: Modifying Occult Rituals** ^table-modifying-occult-rituals

| Change                                                                      | Check DC modifier or modification                                      |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Casting time**                                                            |                                                                        |
| Casting time is restricted (such as "only during a full moon")              | –4                                                                     |
| Casting time is severely restricted (such as "only during a lunar eclipse") | –8                                                                     |
| **Focus and material components**                                           |                                                                        |
| Expensive material component (500 gp)                                       | –1                                                                     |
| Expensive material component (5,000 gp)                                     | –2                                                                     |
| Expensive material component (25,000 gp)                                    | –4                                                                     |
| Expensive focus (5,000 gp)                                                  | –1                                                                     |
| Expensive focus (25,000 gp)                                                 | –2                                                                     |
| **Range**                                                                   |                                                                        |
| Greater range than normal                                                   | +1 to +6                                                               |
| Shorter range than normal                                                   | –1 to –4                                                               |
| **Area**                                                                    |                                                                        |
| Larger area than normal                                                     | +1 to +6                                                               |
| Smaller area than normal                                                    | –1 to –4                                                               |
| **Target**                                                                  |                                                                        |
| Unwilling target must be helpless                                           | –2                                                                     |
| Limited targets (by HD, creature type, and so on)                           | –3                                                                     |
| Single target to multiple targets                                           | +4                                                                     |
| **Duration**                                                                |                                                                        |
| Greater duration than normal                                                | +1 to +6                                                               |
| Shorter duration than normal                                                | –1 to –4                                                               |
| One year or more                                                            | Casting time in increments of 1 hour/level instead of 10 minutes/level |
| **Backlash**                                                                |                                                                        |
| Per 2d6 points of damage                                                    | –1                                                                     |
| Caster is exhausted                                                         | –2                                                                     |
| Per temporary negative level caster gains                                   | –2                                                                     |
| Per permanent negative level caster gains                                   | –4                                                                     |
| Caster reduced to –1 hp                                                     | –3                                                                     |
| Caster infected with disease                                                | –4                                                                     |
| Caster suffers curse effects                                                | –4                                                                     |
| Backlash affects secondary casters too                                      | –1                                                                     |

**Occult Ritual Benchmarks by School** ^ritual-benchmarks

- **Abjuration**: Range close; Target one or more creatures, no two of which can be more than 30 ft. apart; Duration minutes; Defense Will; SR yes.
- **Conjuration**: Range close; Target one creature; Duration hours (instantaneous for the teleportation subschool); Defense Will (harmless); SR yes (harmless).
- **Divination**: Range long; Target personal; Duration minutes; Defense none; SR no.
- **Enchantment**: Range close; Target one living creature; Duration minutes; Defense Will; SR yes.
- **Evocation**: Range medium; Area 5-ft.-wide bolt or 20-ft.-radius burst; Duration instantaneous; Defense Reflex half; SR yes.
- **Illusion**: Range touch; Target one living creature or 20 cu. ft. of matter; Duration minutes; Defense Will disbelief; SR no.
- **Necromancy**: Range close; Target one or more creatures or corpses; Duration instantaneous; Defense none; SR no.
- **Transmutation**: Range medium; Target one creature or 20 cu. ft. of matter; Duration rounds; Defense Fortitude half (or harmless); SR yes.

## Occult Rituals

![[rangoric-srd/rules/occult-rituals/Occult Rituals Index.base]]

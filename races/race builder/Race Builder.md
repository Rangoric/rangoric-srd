---
srd-type: "rules"
section: "Races"
book: ["Advanced Race Guide", "Faeries"]
based-on:
  - "[[path srd 3.5/rules/advanced-race-guide/race-builder/Creating a New Race|Creating a New Race (ARG)]]"
  - "[[path srd 3.5/rules/advanced-race-guide/race-builder/Step 1- Concept|Step 1: Concept (ARG)]]"
  - "[[path srd 3.5/rules/advanced-race-guide/race-builder/Racial Qualities|Racial Qualities (ARG)]]"
  - "[[path srd 3.5/rules/advanced-race-guide/race-builder/Step 3- Racial Traits|Step 3: Racial Traits (ARG)]]"
  - "[[path srd 3.5/rules/advanced-race-guide/race-builder/Racial Traits (Race Builder)|Racial Traits (Race Builder) (ARG)]]"
  - "[[path srd 3.5/rules/advanced-race-guide/race-builder/Example Races|Example Races (ARG)]]"
  - "[[individual books/Faeries/races/Faeries|Faeries (Faeries)]]"
status: draft
change: new
pi-review: 2026-11-10
tags: [rangoric, rangoric/rules]
---

# Race Builder

## Building a Race

Sooner or later a campaign wants a race that isn't here yet: elves who live on the ice, a people of living stone, a monster a player wants to play. The race builder makes such races out of the same pieces the existing races are made of, and puts a price on each piece so a new race can sit beside the races in [[rangoric-srd/races/PC Races|PC Races]] without outshining them. It can also build races that are meant to be stronger than those, and say how much stronger.

A race is bought with **race points (RP)**. Every race has six **racial qualities**, which it must choose: type, subtypes (if any), size, base speed, ability score modifiers, and languages. On top of those it buys any number of **racial traits** (darkvision, a skill bonus, a breath weapon, the ability to fly), limited by its power level. Some qualities and traits cost 0 RP or less: a 0 RP choice still fills its slot, and a negative cost gives points back. Weaknesses are traits with a negative cost.

The builder makes races with **no racial Hit Dice**: a member of the race gets its Hit Dice, base attack bonus, saves, skill points, class skills and proficiencies from its class levels, like the races in PC Races. Creatures that have racial Hit Dice stay under [[rangoric-srd/monsters/Monsters as Races|Monsters as Races]].

### Power Levels

Before buying anything, decide how strong the race should be. The power level sets how many RP the race has to spend, how many traits it can take from each category, and which traits it can take at all.

| Power Level | RP | Traits per Category | Traits Available |
| --- | --- | --- | --- |
| Standard | 1–10 | 3 | Standard |
| Advanced | 11–20 | 4 | Standard and advanced |
| Monstrous | 21 and up | 5 | Standard, advanced and monstrous |

The races in PC Races are standard races, about 8 to 12 RP. Most planar-touched and unusual races sit around 10 to 17. Races with flight, Large size or many natural attacks are advanced or monstrous.

**Race points and level adjustment.** Rangoric keeps [[rangoric-srd/monsters/Monsters as Races#^level-adjustment|level adjustment]] as the measure of how strong a race is: race points sit beside it, as a way to build races and compare them, and don’t replace it. A character whose race has a level adjustment can buy it down as it gains class levels ([[rangoric-srd/unearthed-arcana/Reducing Level Adjustments|Reducing Level Adjustments]]), so it costs less once the race’s extras matter less.

### Step 1: Concept

A race is a people with a shared history and culture, not a pile of the best options. Before choosing anything, answer a few questions about it:

- Where does it live, and why there?
- What does it look like, and how does that suit where it lives?
- What is its history? Were there turning points?
- How does it get on with other races: allies, rivals, enemies?
- Which classes does it tend toward?

Then pick the qualities and traits that follow from those answers. When a player builds a race, the GM works with them so the race fills a real place in the campaign.

### Step 2: Racial Qualities

Choose one option in each category. A 0 RP choice still counts as the choice for its category.

#### Type

The race's creature type works like the type in [[rangoric-srd/monsters/Monster Types, Sybtypes, and Special Abilities|Monster Types]], with two differences: every race type assumes a roughly humanoid body (two arms, two legs, a torso and a head, so it can use the usual magic item slots, weapons and armor), and every race has 0 Hit Dice. A type can't cost as much as or more than the top of the race's power level, so an undead race has to be at least advanced and a construct race monstrous.

Some types come with traits, such as darkvision. Those are already paid for, don't count toward the category limit, and still meet prerequisites.

| Type | RP | Comes With |
| --- | --- | --- |
| Humanoid | 0 | Breathes, eats, sleeps. Must take at least one subtype naming its race (such as goblinoid or reptilian, or a new one named for the race); a half-breed takes both parents' subtypes. A humanoid with a race's subtype counts as that race for prerequisites. |
| Fey | 2 | [[rangoric-srd/rules/Special Abilities and Conditions#Low-Light Vision\|Low-light vision]]. |
| Aberration | 3 | [[rangoric-srd/rules/Special Abilities and Conditions#Darkvision\|Darkvision]] 60 ft. |
| Monstrous humanoid | 3 | Darkvision 60 ft. |
| Outsider (native) | 3 | Darkvision 60 ft. May have ties to one other plane, which some traits require. |
| Dragon | 10 | Darkvision 60 ft., low-light vision, immune to magic sleep and paralysis. |
| Plant | 10 | Low-light vision; immune to mind-affecting effects, paralysis, poison, polymorph, sleep and stunning; doesn't need to sleep. |
| Undead | 16 | No Constitution (uses Charisma for hit points, Fortitude saves and Con-based abilities); darkvision 60 ft.; the undead immunities; harmed by positive and healed by negative energy; destroyed at 0 hit points; no massive damage; doesn't breathe, eat or sleep. |
| Construct | 20 | No Constitution (counts as 10); low-light vision and darkvision 60 ft.; the construct immunities (mind-affecting, Fortitude effects, ability damage, fatigue…); can't heal on its own; destroyed at 0 hit points; bonus hit points by size (Small 10, Medium 20, Large 30); can't be raised. |

**Special subtypes.** For a standard race with some of the flavor of a construct or undead, add one of these to any type but construct or undead:

| Subtype | RP | Comes With |
| --- | --- | --- |
| Half-construct | 7 | +2 racial bonus on saves against disease, mind-affecting effects, poison, and fatigue or exhaustion; can't be raised; doesn't need to breathe, eat or sleep. |
| Half-undead | 5 | Darkvision 60 ft.; +2 racial bonus on saves against disease and mind-affecting effects; no penalties from [[rangoric-srd/rules/Special Abilities and Conditions#Energy Drain and Negative Levels\|negative levels]], which go away after 24 hours; harmed by positive and healed by negative energy. |

#### Size

| Size | RP | Prerequisite | Effect |
| --- | --- | --- | --- |
| Medium | 0 | — | No modifiers. Space 5 ft., reach 5 ft. |
| Small | 0 | — | As [[rangoric-srd/races/PC Races#Small Characters\|Small Characters]]: +1 size bonus to AC and on attack rolls, +4 on [[rangoric-srd/skills/Stealth\|Stealth]]; −1 on combat maneuver checks and to CMD. Space 5 ft., reach 5 ft. |
| Tiny | 4 | Aberration, construct, dragon, fey, outsider (native) or plant | +2 size bonus to Dex, −2 to Str; +2 size bonus to AC and on attacks, +8 on Stealth; −2 on combat maneuver checks and CMD. Space 2½ ft., reach 0 ft.: must enter a foe's square to attack it (provoking), threatens nothing, usually can't flank. |
| Large | 7 | Humanoids need the giant subtype | As [[rangoric-srd/races/PC Races#Large Characters\|Large Characters]], without a +2 size bonus to Str and −2 to Dex (Small has no Strength penalty): −1 size penalty to AC and on attacks, −4 on Stealth; +1 on combat maneuver checks and CMD. Space 10 ft., reach 5 ft. |

#### Base Speed

| Speed | RP | Effect |
| --- | --- | --- |
| Normal | 0 | Base speed 30 ft. Many movement traits require it. |
| Slow | −1 | Base speed 20 ft. A Medium race with slow speed is never slowed by armor or encumbrance (the dwarf's Slow and Steady). |

#### Ability Score Modifiers

Most arrays split the abilities into **physical** (Strength, Dexterity, Constitution) and **mental** (Intelligence, Wisdom, Charisma). Except for human heritage, the modifiers are fixed for every member of the race, and the bonuses count as racial bonuses for trait prerequisites (Hardy needs a +2 racial bonus to Constitution, for instance).

| Array | RP | Prerequisite | Modifiers |
| --- | --- | --- | --- |
| Human heritage | 0 | Human subtype | +2 to any one ability, chosen by each character at creation. |
| Standard | 0 | — | +2 to one physical and +2 to one mental ability, −2 to one other ability. |
| Weakness | −1 | — | +2 to one physical and +2 to one mental ability, −4 to one other ability. |
| Mixed weakness | −2 | — | In one group, +2 to one ability and −2 to another; in the other, +2 to one and −4 to another. |
| Greater weakness | −3 | — | In one group, −4 to one ability, −2 to another, +2 to the third. |
| Specialized | 1 | — | +2 to two abilities in one group, −2 to one in the other. |
| Paragon | 1 | — | +4 to one ability, −2 to all three abilities of the other group. |
| Flexible | 2 | — | +2 to any two abilities. |
| Greater paragon | 2 | — | +4 to one ability, −2 to one physical and −2 to one mental ability. |
| Advanced | 4 | Advanced or monstrous | +2 to all three abilities of one group, +4 to one of the other group, −2 to another of the other group. |

More can be added with the advanced ability traits in [[rangoric-srd/races/race builder/Race Builder Traits#Ability Score Traits|Race Builder Traits]].

#### Languages

The race's **racial language** is its own tongue (make one up if needed), Draconic for a reptilian humanoid, or the planar language of an outsider's plane (Abyssal, Aquan, Auran, Celestial, Ignan, Infernal or Terran). A race native to the deep underground can replace Common with Undercommon. Constructs and undead usually speak their makers' language.

| Option | RP | Languages |
| --- | --- | --- |
| Standard | 0 | Common and the racial language; choose up to seven bonus languages (no secret languages such as Druidic). |
| Xenophobic | 0 | The racial language only; choose up to four bonus languages, one of which must be Common (or Undercommon). |
| Linguist | 1 | Common and the racial language; bonus languages can be any (no secret languages). |

Bonus languages are learned with a high Intelligence, as [[rangoric-srd/races/PC Races#Race and Languages|Race and Languages]] describes; Rangoric's race notes list them under **Bonus Languages**. A xenophobic race doesn't know Common unless it takes it as a bonus language. New tongues go into [[rangoric-srd/skills/Linguistics|Linguistics]]' table.

### Step 3: Racial Traits

Spend the remaining RP on racial traits. They come in categories: **ability score, defense, feat and skill, magical, movement, offense, senses, weakness, and other**. A race can take no more traits from one category than its power level allows (3, 4 or 5), and within each category traits are standard, advanced or monstrous: a standard race takes only standard traits, an advanced race standard and advanced, a monstrous race any. Traits that come with the type don't count toward the limit.

Unless a trait says otherwise, it's an extraordinary ability and can be taken only once. A trait that can be taken more than once says what each extra purchase costs.

Each trait gives its cost in RP, any prerequisites (a type, subtype, size, ability bonus or other trait the race must already have), and its benefit. The full list is in [[rangoric-srd/races/race builder/Race Builder Traits|Race Builder Traits]].

**Humanoid subtypes as prerequisites.** Traits named for a race (Elven Immunities, Gnome Magic, Orc Ferocity) need that race's subtype. Treat that as a pointer to the kind of race that would have it: the GM can rename the trait and drop the subtype for a race that fits it.

**Spell-like abilities** granted by traits use a caster level equal to the character's level.

### Step 4: Writing the Race Up

*(Rangoric's step; the builder stops at traits.)* Write the race as a note in `rangoric-srd/races`, laid out like the others: Size, Base Speed, Perks, Languages, Bonus Languages, then Age, Height and Weight. Each trait is a bullet labelled with its trait name (Pathfinder's names), a quality that needs no words (Medium, normal speed) is just the Size or Base Speed line, and a trait that already has a home elsewhere points there rather than being written out again: darkvision and low-light vision to [[rangoric-srd/rules/Special Abilities and Conditions|Special Abilities and Conditions]], defensive training to [[rangoric-srd/races/PC Races#Defensive Training|PC Races]], Small to Small Characters. The race’s total goes in the note’s `race-points` property, beside its level adjustment if it has one.

### Races Without Constitution

Construct and undead races have no Constitution score, so the ability score methods change: roll or assign only five scores and skip Constitution (the standard 4d6 drop lowest, classic 3d6 and heroic 2d6+6 methods each make five scores; a dice pool is 20d6 instead of 24d6, with at least 3d6 in each score). With point buy, treat Constitution as 10 and buy the rest normally.

### Playing Advanced and Monstrous Races

Advanced and monstrous races are built to face harder fights, especially at low level. When the party uses them, the GM builds encounters for a higher average party level (APL) than the characters' real one, by the party's average RP (rounded to the nearest 10):

| Average RP | APL 1–5 | APL 6–10 | APL 11–15 | APL 16–20 |
| --- | --- | --- | --- | --- |
| 20 | +1 | +0 | +0 | +0 |
| 30 | +2 | +1 | +0 | +0 |
| 40 | +3 | +2 | +1 | +0 |

## Rangoric Races in Race Points

Each Rangoric race priced with the trait costs above. A race note carries its total in its `race-points` property. The original example races sometimes charge a trait less or more than its heading; here the heading’s cost is used.

| Race | Race Points | Level Adjustment | Power Level |
| --- | --- | --- | --- |
| [[rangoric-srd/races/Dwarf\|Dwarf]] | 12 | — | Advanced |
| [[rangoric-srd/races/Elf\|Elf]] | 12 | — | Advanced |
| [[rangoric-srd/races/Gnome\|Gnome]] | 10 | — | Standard |
| [[rangoric-srd/races/Halfling\|Halfling]] | 12 | — | Advanced |
| [[rangoric-srd/races/Half-Elf\|Half-Elf]] | 10 | — | Standard |
| [[rangoric-srd/races/Half-Orc\|Half-Orc]] | 8 | — | Standard |
| [[rangoric-srd/races/Human\|Human]] | 9 | — | Standard |
| [[rangoric-srd/races/Kobold\|Kobold]] | 5 | — | Standard |
| [[rangoric-srd/races/Orc\|Orc]] | 8 | — | Standard |
| [[rangoric-srd/races/Goblin\|Goblin]] | 10 | — | Standard |
| [[rangoric-srd/races/Duergar\|Duergar]] | 8 | +1 | Standard |
| [[rangoric-srd/races/Hobgoblin\|Hobgoblin]] | 9 | +1 | Standard |
| [[rangoric-srd/races/Tiefling\|Tiefling]] | 13 | +1 | Advanced |
| [[rangoric-srd/races/Drow\|Drow]] | 14 | +1 | Advanced |
| [[rangoric-srd/races/Aasimar\|Aasimar]] | 15 | +1 | Advanced |
| [[rangoric-srd/races/Svirfneblin\|Svirfneblin]] | 26 | +1 | Monstrous |

### Breakdowns

**Dwarf (12 RP).** Humanoid (dwarf) 0; Medium 0; slow speed −1 (Slow and Steady); standard array (+2 Con, +2 Wis, −2 Cha) 0; standard languages 0. *Defense*: Defensive Training (lesser, against giants) 1, Hardy 3, Stability 1. *Feat and skill*: Craftsman 1, Greed 1, Stonecunning 1. *Offense*: Hatred 1, Weapon Familiarity 2. *Senses*: darkvision 60 ft. 2.

**Elf (12 RP).** Humanoid (elf) 0; Medium 0; normal speed 0; standard array (+2 Dex, +2 Int, −2 Con) 0; standard languages 0. *Defense*: Elven Immunities 2. *Feat and skill*: Keen Senses as two Skill Bonuses ([[rangoric-srd/skills/Perception|Perception]], [[rangoric-srd/skills/Investigation|Investigation]]) 4. *Magical*: Elven Magic 3. *Offense*: Weapon Familiarity 2. *Senses*: low-light vision 1.

**Human (9 RP).** Humanoid (human) 0; Medium 0; normal speed 0; human heritage 0; linguist 1. *Feat and skill*: flexible bonus feat 4, Skilled 4.

**Hobgoblin (9 RP, level adjustment +1).** Humanoid (goblinoid) 0; Medium 0; normal speed 0; flexible (+2 Dex, +2 Con) 2; standard languages 0. *Feat and skill*: Sneaky (+4 [[rangoric-srd/skills/Stealth|Stealth]]) 5. *Senses*: darkvision 60 ft. 2.

**Aasimar (15 RP, level adjustment +1).** Outsider (native, tied to a good-aligned plane) 3, darkvision included; Medium 0; normal speed 0; flexible (+2 Wis, +2 Cha) 2; standard languages 0. *Defense*: Celestial Resistance 3. *Feat and skill*: Skill Bonus ([[rangoric-srd/skills/Persuasion|Persuasion]]) 2, Skill Bonus (Perception) 2. *Magical*: greater spell-like ability (*daylight*, 3rd level) 3.

**Svirfneblin (26 RP, level adjustment +1).** Humanoid (gnome) 0; Small 0; slow speed −1; mixed weakness (−2 Str, +2 Dex, +2 Wis, −4 Cha) −2; standard languages 0. *Defense*: greater Defensive Training 4, greater Lucky (Fortunate) 4, greater spell resistance 3. *Feat and skill*: Skill Bonus (Craft (alchemy)) 2, Skill Bonus (Perception) 2, Stonecunning 1, Underground Sneak 5. *Magical*: Svirfneblin Magic 2. *Offense*: Hatred 1, Weapon Familiarity 1. *Senses*: darkvision 120 ft. 3, low-light vision 1.

## Building a Faerie

The build-a-faerie, its faerie traits priced in race points beside their ECL modifiers, is in [[rangoric-srd/races/race builder/Building a Faerie|Building a Faerie]].

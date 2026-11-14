---
srd-type: "overview"
section: "Rules"
book: "Core Rulebook"
based-on:
  - "[[fantasy srd 3.5/rules/Special Abilities and Conditions|Special Abilities and Conditions (3.5)]]"
  - "[[path srd 3.5/rules/core-rulebook/glossary/Special Abilities|Special Abilities (PF1)]]"
  - "[[path srd 3.5/rules/ultimate-equipment/gear/Poisons|Poisons (PF1)]]"
status: draft
change: new
pi-review: 2026-11-13
tags: [rangoric, rangoric/overview]
---

# Afflictions

Curses, diseases and poisons are afflictions. Each has a different effect, but they all work the same way. Every affliction gives a saving throw when it is contracted. On a success, the creature doesn’t suffer from the affliction and needs no further rolls. On a failure, the creature falls victim to the affliction and must deal with its effects.

An affliction calls for more saving throws over time to avoid its effects. With most afflictions, enough saving throws made in a row remove it, and no further saves are needed. Some afflictions, usually supernatural ones, can’t be cured by saving throws alone and need powerful magic to remove. Each affliction is given as a short block of information.

## The Affliction Block

**Name**: The affliction’s name.

**Type**: The kind of affliction (curse, disease or poison) and how it is contracted, such as contact, ingested, inhaled, injury, spell or trap. ^affliction-type

**Save**: The kind of saving throw that avoids contracting the affliction, and its DC. Unless noted otherwise, it is also the save to avoid the affliction’s effect once contracted, and the DC of any caster level check needed to end the affliction with magic, such as *[[rangoric-srd/spells/Remove Curse|remove curse]]* or *[[rangoric-srd/spells/Neutralize Poison|neutralize poison]]*. ^affliction-save

**Onset**: Some afflictions take a while to set in. A creature exposed to an affliction with an onset time saves at once. On a success, it avoids the affliction and needs no further saves. On a failure, it has contracted the affliction and begins making more saves once the onset time has passed. The affliction’s effect doesn’t happen until the onset time has passed, and then only if a later save fails. ^affliction-onset

**Frequency**: How often the creature must save after contracting the affliction (after the onset time, if it has one). Some afflictions last until they are cured; others end after a set time even if the creature isn’t cured, and the frequency says so. A disease with a frequency of “1/day” lasts until cured, but a poison with a frequency of “1/round for 6 rounds” ends after 6 rounds. An affliction with no frequency happens only once, when it is contracted (or after its onset time, if it has one). ^affliction-frequency

**Effect**: What happens to the creature each time it fails its save. Most afflictions deal [[rangoric-srd/rules/Special Abilities and Conditions#^ability-damaged|ability damage]] or hit point damage, and these add up each time. Others give penalties or other effects; some of these add up, and the rest affect the creature only if it failed its most recent save. Some afflictions have an initial effect, on the first failed save, and a secondary effect, on later failed saves, written with a slash (“1 Con drain/1d3 Con”: the first failure drains 1 point of Constitution, each later one deals 1d3 points of Constitution damage). Hit point and ability damage dealt by an affliction can’t heal naturally while the affliction lasts. ^affliction-effect

**Cure**: How the affliction is cured, usually a number of saves in a row. Even an affliction with a limited frequency can be cured early if enough saves are made. Curing an affliction doesn’t remove the hit point or ability damage it dealt; that heals normally once the affliction is gone. An affliction with no cure entry can be cured only by powerful spells, such as *[[rangoric-srd/spells/Neutralize Poison|neutralize poison]]* and *[[rangoric-srd/spells/Remove Curse|remove curse]]*; no number of saves ends it. ^affliction-cure

*Example*: A character is exposed to red ache (Fortitude DC 15; onset 1d3 days; frequency 1/day; effect 1d6 Str damage; cure 2 consecutive saves). He fails the DC 15 Fortitude save to avoid contracting it, so after 1d3 days he must make another DC 15 Fortitude save or take 1d6 points of Strength damage. From then on he saves once a day, as its frequency says. When he makes his saves two days in a row, he is cured, and the damage it dealt begins to heal normally.

## Poison

No other affliction is as common as poison. From a viper’s fangs to an assassin’s blade, poison is a constant threat. Poisons can be cured by successful saving throws and by spells such as *[[rangoric-srd/spells/Neutralize Poison|neutralize poison]]*. Although supernatural and spell-like poisons are possible, poisonous effects are almost always extraordinary.

One dose of poison smeared on a weapon or some other object affects just a single target. A poisoned weapon or object keeps its poison until the weapon scores a hit or the object is touched (unless the poison is wiped off first). Any poison smeared on an object or exposed to the elements in any way stays potent until it is touched or used.

Poisons are of four kinds, by how they are delivered.

**Contact**: Merely touching this kind of poison with bare skin calls for a saving throw. It can be delivered by a weapon or a touch attack, and used as an injury poison. Even if a creature has enough damage reduction to take no damage from the attack, the poison can still affect it. A chest or other object can be smeared with contact poison as part of a trap. Contact poisons usually have an onset time of 1 minute and a frequency of 1/minute. ^contact-poison

**Ingested**: Ingested poisons are nearly impossible to use in combat. A poisoner could give one to an unconscious creature or trick someone into eating or drinking something poisoned. Assassins and others tend to use ingested poisons outside of combat. Ingested poisons usually have an onset time of 10 minutes and a frequency of 1/minute. ^ingested-poison

**Inhaled**: Inhaled poisons are usually kept in fragile vials or eggshells. They can be thrown as a ranged attack with a range increment of 10 feet. When the container strikes a hard surface (or is struck hard), it releases its poison. One dose spreads to fill a 10-foot cube, and each creature in the area must save. A creature can hold its breath while in the area: each round, it has a 50% chance of not having to save. How long a creature can hold its breath is under [[rangoric-srd/rules/Wilderness, Weather, and Environment#^hold-breath|suffocation]]; a creature that would begin to suffocate while holding its breath instead starts breathing normally again (and is exposed to the poison if still in the area). Inhaled poisons usually have no onset time. ^inhaled-poison

**Injury**: This poison must be delivered through a wound. If a creature has enough damage reduction to take no damage from the attack, the poison doesn’t affect it. Traps that deal damage with weapons, needles and the like sometimes carry injury poisons. Injury poisons usually have no onset time and a frequency of 1/round. ^injury-poison

**Price**: The cost of one dose (one vial) of the poison. Poison can’t be used or applied in any amount smaller than one dose. Buying and owning poison is always illegal, and even in big cities it can be had only from specialized, less than reputable sources. ^poison-price

### Multiple Doses

Unlike other afflictions, doses of the same poison stack, raising its DC and lengthening it. They stack only while the poison is still active in the creature and the creature fails its first save against the new dose: a creature that makes that save isn’t affected, and a later dose after the poison is cured or has run its course starts over.

- **Longer**: Each extra dose lengthens the poison by half the duration in its frequency.
- **Harder**: Each extra dose raises the poison’s DC by +2.

Both increases are cumulative. A creature with several doses of the same poison makes one save at the higher DC each time the frequency calls for one, not one per dose. Extra doses don’t change the cure, and meeting it ends every dose. Doses of different poisons don’t stack; each is tracked on its own. ^poison-doses

Contact and injury poisons on a weapon deliver one dose per hit, since the poison lasts for one successful attack. Inhaled and ingested poisons can deliver several doses at once.

*Example*: A character is bitten in the same round by three Medium monstrous spiders and fails all three saves. Medium spider venom has a DC of 14 and a frequency of 1/round for 4 rounds, so the second and third doses each add 2 rounds and +2 to the DC: he must make a DC 18 Fortitude save for the next 8 rounds. One successful save still cures all three doses.

### Applying Poison

Applying poison to a weapon or a single piece of ammunition is a standard action. Whenever a character applies or readies a poison, there is a 5% chance that he exposes himself to it and must save against it as normal; this doesn’t use up the dose. Whenever a character attacks with a poisoned weapon and rolls a natural 1 on the attack roll, he exposes himself to the poison. The poison on a weapon is used up when the weapon strikes a creature or is touched by its wielder. ^applying-poison

**Poison Use**: A character with poison use never risks poisoning himself, whether applying, readying or making a poison. ^poison-use

### Making Poison

A poison can be made with [[rangoric-srd/skills/Craft|Craft]] (alchemy). The DC to make a poison is equal to its save DC. Rolling a natural 1 on the check while making a poison exposes the crafter to it (this doesn’t use up the poison), unless the crafter has poison use. Which poisons alchemists and herbalists can make with their skills, and the [[rangoric-srd/feats/Craft Toxins|Craft Toxins]] feat for the rest, are in [[rangoric-srd/rules/alchemy-and-herbalism/Alchemical and Herbal Items#Toxins|toxins]]. ^making-poison

### Poison Immunities

Creatures with natural poison attacks are immune to their own poison. Nonliving creatures (constructs and undead) and creatures without metabolisms (such as elementals) are always immune to poison. Oozes, plants, and certain kinds of outsiders are also immune to poison, although special poisons could conceivably be made to harm them. ^poison-immunities

## Disease

From a widespread plague to the bite of a dire rat, disease is a serious threat to common folk and adventurers alike. A character can catch one when he is injured by a contaminated attack, touches an item smeared with diseased matter, or eats or drinks something tainted. Some injury diseases can be passed on by as small an injury as a flea bite, and most inhaled diseases can also be ingested (and the other way round).

Diseases rarely have a limited frequency, but most have a long onset time, and it can vary. Most diseases can be cured by a number of saves in a row or by spells such as *[[rangoric-srd/spells/Remove Disease|remove disease]]*. The saving throws against a disease can be rolled secretly, so the player doesn’t know whether it has taken hold.

## Curse

Careless rogues plundering a tomb, drunken heroes insulting a powerful wizard, and foolhardy adventurers who pick up ancient swords all might suffer from curses. These magic afflictions can have a wide variety of effects, from a simple penalty on certain checks to turning the victim into a toad. Some even make the victim slowly rot away, leaving nothing behind but dust. Unlike other afflictions, most curses can’t be cured by any number of successful saving throws. They can be cured with magic, usually spells such as *[[rangoric-srd/spells/Remove Curse|remove curse]]* and *[[rangoric-srd/spells/Break Enchantment|break enchantment]]*. Some curses cause a slow decline; others give a fixed penalty from the moment they are contracted that neither fades nor grows worse. Some magic items act like curses: see [[rangoric-srd/magic-items/Intelligent and Cursed Items and Artifact#Cursed Items|cursed items]].

## Treating an Affliction

A healer can help a poisoned character with the [[rangoric-srd/actions/Treat Poison|Treat Poison]] action and a diseased one with the [[rangoric-srd/actions/Treat Disease|Treat Disease]] action, both [[rangoric-srd/actions/First Aid|First Aid]] actions. Spells end afflictions as their own notes say.

## Initial and Secondary Damage

Some poisons and diseases are still written the older way, without a frequency or cure. They work as follows.

**Poisons with initial and secondary damage**: A failed save when the poison is contracted deals its initial damage. One minute later, the creature must save again (whatever the first result) or take its secondary damage, and the poison ends. Ability damage marked with an asterisk (\*) is drain instead. Paralysis from such a poison lasts 2d6 minutes, and unconsciousness 1d3 hours, unless noted otherwise. ^initial-and-secondary-damage

**Diseases with an incubation period and damage**: The incubation period is the onset, the damage is the effect, the frequency is 1/day and the cure is 2 consecutive saves, unless the disease says otherwise. ^incubation-and-damage

## Sample Afflictions

### Sample Diseases

*Blinding Sickness*: Spread in tainted water. ^blinding-sickness

*Cackle Fever*: Symptoms include high fever, disorientation, and frequent bouts of hideous laughter. Also known as “the shrieks.” ^cackle-fever

*Demon Fever*: Night hags spread it. Can cause permanent ability drain. ^demon-fever

*Devil Chills*: Barbazu and pit fiends spread it. It takes three, not two, successful saves in a row to recover from devil chills. ^devil-chills

*Filth Fever*: Dire rats and otyughs spread it. Those injured while in filthy surroundings might also catch it. ^filth-fever

*Mindfire*: Feels like your brain is burning. Causes stupor. ^mindfire

*Mummy Rot*: Spread by mummies. Successful saving throws do not allow the character to recover (though they do prevent damage normally). ^mummy-rot

*Red Ache*: Skin turns red, bloated, and warm to the touch. ^red-ache

*The Shakes*: Causes involuntary twitches, tremors, and fits. ^the-shakes

*Slimy Doom*: Victim turns into infectious goo from the inside out. Can cause permanent ability drain. ^slimy-doom

**Table: Diseases** ^table-diseases

| Disease           | Infection DC | Incubation | Damage           |
| ----------------- | ------------ | ---------- | ---------------- |
| Blinding sickness | Ingested 16  | 1d3 days   | 1d4 Str (1)      |
| Cackle fever      | Inhaled 16   | 1 day      | 1d6 Wis          |
| Demon fever       | Injury 18    | 1 day      | 1d6 Con (2)      |
| Devil chills (3)  | Injury 14    | 1d4 days   | 1d4 Str          |
| Filth fever       | Injury 12    | 1d3 days   | 1d3 Dex, 1d3 Con |
| Mindfire          | Inhaled 12   | 1 day      | 1d4 Int          |
| Mummy rot (4)     | Contact 20   | 1 day      | 1d6 Con          |
| Red ache          | Injury 15    | 1d3 days   | 1d6 Str          |
| Shakes            | Contact 13   | 1 day      | 1d8 Dex          |
| Slimy doom        | Contact 14   | 1 day      | 1d4 Con (2)      |

1 *Each time the victim takes 2 or more damage from the disease, he must make another Fortitude save or be permanently blinded.*

2 *When damaged, character must succeed on another saving throw or 1 point of damage is permanent drain instead.*

3 *The victim must make three successful Fortitude saving throws in a row to recover from devil chills.*

4 *Successful saves do not allow the character to recover. Only magical healing can save the character.*

### Sample Poisons

**Table: Poisons** ^table-poisons

| Poison                 | Type           | Initial Damage  | Secondary Damage              | Price    |
| ---------------------- | -------------- | --------------- | ----------------------------- | -------- |
| Nitharit               | Contact DC 13  | 0               | 3d6 Con                       | 650 gp   |
| Sassone leaf residue   | Contact DC 16  | 2d12 hp         | 1d6 Con                       | 300 gp   |
| Malyss root paste      | Contact DC 16  | 1 Dex           | 2d4 Dex                       | 500 gp   |
| Terinav root           | Contact DC 16  | 1d6 Dex         | 2d6 Dex                       | 750 gp   |
| Black lotus extract    | Contact DC 20  | 3d6 Con         | 3d6 Con                       | 4,500 gp |
| Dragon bile            | Contact DC 26  | 3d6 Str         | 0                             | 1,500 gp |
| Striped toadstool      | Ingested DC 11 | 1 Wis           | 2d6 Wis + 1d4 Int             | 180 gp   |
| Arsenic                | Ingested DC 13 | 1 Con           | 1d8 Con                       | 120 gp   |
| Id moss                | Ingested DC 14 | 1d4 Int         | 2d6 Int                       | 125 gp   |
| Oil of taggit          | Ingested DC 15 | 0               | Unconsciousness               | 90 gp    |
| Lich dust              | Ingested DC 17 | 2d6 Str         | 1d6 Str                       | 250 gp   |
| Dark reaver powder     | Ingested DC 18 | 2d6 Con         | 1d6 Con + 1d6 Str             | 300 gp   |
| Ungol dust             | Inhaled DC 15  | 1 Cha           | 1d6 Cha + 1 Cha (\*)          | 1,000 gp |
| Insanity mist          | Inhaled DC 15  | 1d4 Wis         | 2d6 Wis                       | 1,500 gp |
| Burnt othur fumes      | Inhaled DC 18  | 1 Con (\*)      | 3d6 Con                       | 2,100 gp |
| Black adder venom      | Injury DC 11   | 1d6 Con         | 1d6 Con                       | 120 gp   |
| Small centipede poison | Injury DC 11   | 1d2 Dex         | 1d2 Dex                       | 90 gp    |
| Bloodroot              | Injury DC 12   | 0               | 1d4 Con + 1d3 Wis             | 100 gp   |
| Drow poison            | Injury DC 13   | Unconsciousness | Unconsciousness for 2d4 hours | 75gp     |
| Greenblood oil         | Injury DC 13   | 1 Con           | 1d2 Con                       | 100 gp   |
| Blue whinnis           | Injury DC 14   | 1 Con           | Unconsciousness               | 120 gp   |
| Medium spider venom    | Injury DC 14   | 1d4 Str         | 1d4 Str                       | 150 gp   |
| Shadow essence         | Injury DC 17   | 1 Str (\*)      | 2d6 Str                       | 250 gp   |
| Wyvern poison          | Injury DC 17   | 2d6 Con         | 2d6 Con                       | 3,000 gp |
| Large scorpion venom   | Injury DC 18   | 1d6 Str         | 1d6 Str                       | 200 gp   |
| Giant wasp poison      | Injury DC 18   | 1d6 Dex         | 1d6 Dex                       | 210 gp   |
| Deathblade             | Injury DC 20   | 1d6 Con         | 2d6 Con                       | 1,800 gp |
| Purple worm poison     | Injury DC 24   | 1d6 Str         | 2d6 Str                       | 700 gp   |

\* *Permanent drain, not temporary damage.*

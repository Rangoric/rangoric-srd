---
srd-type: "overview"
section: "Rules"
status: draft
pi-review: 2026-11-22
tags: [rangoric, rangoric/overview]
---

# Afflictions

Curses, diseases, infestations, insanities and poisons are afflictions, and so are the addictions that [[#Drugs and Addiction|drugs]] cause. Each has a different effect, but they all work the same way. Every affliction attacks a defense when it is contracted. On a miss, the creature doesn’t suffer from the affliction and needs no further rolls. On a hit, the creature falls victim to the affliction and must deal with its effects.

An affliction attacks again over time to bring on its effects ([[rangoric-srd/rules/Saving Throws|Saving Throws]]). With most afflictions, enough misses in a row remove it, and no further attacks are made. Some afflictions, usually supernatural ones, can’t be cured by misses alone and need powerful magic to remove. Each affliction is given as a short block of information.

## The Affliction Block

**Name**: The affliction’s name.

**Type**: The kind of affliction (curse, disease, infestation, insanity or poison) and how it is contracted, such as contact, ingested, inhaled, injury, spell or trap. ^affliction-type

**Attack**: The affliction’s attack bonus and the defense it attacks to be contracted (“+7 vs Fortitude”). Unless noted otherwise, it is also the attack that brings on the affliction’s effect once contracted, and 10 + the attack bonus is the DC of any caster level check needed to end the affliction with magic, such as _[[rangoric-srd/spells/Remove Curse|remove curse]]_ or _[[rangoric-srd/spells/Neutralize Poison|neutralize poison]]_. ^affliction-save

**Onset**: Some afflictions take a while to set in. An affliction with an onset time attacks a creature exposed to it at once. On a miss, the creature avoids the affliction and faces no further attacks. On a hit, it has contracted the affliction, which begins attacking again once the onset time has passed. The affliction’s effect doesn’t happen until the onset time has passed, and then only if a later attack hits. ^affliction-onset

**Frequency**: How often the affliction attacks after the creature contracts it (after the onset time, if it has one). Some afflictions last until they are cured; others end after a set time even if the creature isn’t cured, and the frequency says so. A disease with a frequency of “1/day” lasts until cured, but a poison with a frequency of “1/round for 6 rounds” ends after 6 rounds. An affliction with no frequency happens only once, when it is contracted (or after its onset time, if it has one). ^affliction-frequency

**Effect**: What happens to the creature each time it fails its save. Most afflictions deal [[rangoric-srd/rules/Special Abilities and Conditions#^ability-damaged|ability damage]] or hit point damage, and these add up each time. Others give penalties or other effects; some of these add up, and the rest affect the creature only if it failed its most recent save. Some afflictions have an initial effect, on the first failed save, and a secondary effect, on later failed saves, written with a slash (“1 Con drain/1d3 Con”: the first failure drains 1 point of Constitution, each later one deals 1d3 points of Constitution damage). Hit point and ability damage dealt by an affliction can’t heal naturally while the affliction lasts. ^affliction-effect

**Cure**: How the affliction is cured, usually a number of misses in a row. Even an affliction with a limited frequency can be cured early if enough of its attacks miss. Curing an affliction doesn’t remove the hit point or ability damage it dealt; that heals normally once the affliction is gone. An affliction with no cure entry can be cured only by powerful spells, such as _[[rangoric-srd/spells/Neutralize Poison|neutralize poison]]_ and _[[rangoric-srd/spells/Remove Curse|remove curse]]_; no number of misses ends it. ^affliction-cure

_Example_: A character is exposed to red ache (+5 vs Fortitude; onset 1d3 days; frequency 1/day; effect 1d6 Str damage; cure 2 consecutive misses). He fails his save against its +5 attack, so he contracts it, and after 1d3 days it attacks his Fortitude again: if it hits, he takes 1d6 points of Strength damage. From then on it attacks once a day, as its frequency says. When it misses two days in a row, he is cured, and the damage it dealt begins to heal normally.

## Poison

No other affliction is as common as poison. From a viper’s fangs to an assassin’s blade, poison is a constant threat. Poisons can be cured by misses and by spells such as _[[rangoric-srd/spells/Neutralize Poison|neutralize poison]]_. Although supernatural and spell-like poisons are possible, poisonous effects are almost always extraordinary.

One dose of poison smeared on a weapon or some other object affects just a single target. A poisoned weapon or object keeps its poison until the weapon scores a hit or the object is touched (unless the poison is wiped off first). Any poison smeared on an object or exposed to the elements in any way stays potent until it is touched or used.

Poisons are of four kinds, by how they are delivered.

**Contact**: Merely touching this kind of poison with bare skin lets it attack. It can be delivered by a weapon or a touch attack, and used as an injury poison. Even if a creature has enough damage reduction to take no damage from the attack, the poison can still affect it. A chest or other object can be smeared with contact poison as part of a trap. Contact poisons usually have an onset time of 1 minute and a frequency of 1/minute. ^contact-poison

**Ingested**: Ingested poisons are nearly impossible to use in combat. A poisoner could give one to an unconscious creature or trick someone into eating or drinking something poisoned. Assassins and others tend to use ingested poisons outside of combat. Ingested poisons usually have an onset time of 10 minutes and a frequency of 1/minute. ^ingested-poison

**Inhaled**: Inhaled poisons are usually kept in fragile vials or eggshells. They can be thrown as a ranged attack with a range increment of 10 feet. When the container strikes a hard surface (or is struck hard), it releases its poison. One dose spreads to fill a 10-foot cube, and it attacks each creature in the area. A creature can hold its breath while in the area: each round, it has a 50% chance of not being attacked. How long a creature can hold its breath is under [[rangoric-srd/rules/Wilderness, Weather, and Environment#^hold-breath|suffocation]]; a creature that would begin to suffocate while holding its breath instead starts breathing normally again (and is exposed to the poison if still in the area). Inhaled poisons usually have no onset time. ^inhaled-poison

**Injury**: This poison must be delivered through a wound. If a creature has enough damage reduction to take no damage from the attack, the poison doesn’t affect it. Traps that deal damage with weapons, needles and the like sometimes carry injury poisons. Injury poisons usually have no onset time and a frequency of 1/round. ^injury-poison

**Price**: The cost of one dose (one vial) of the poison. Poison can’t be used or applied in any amount smaller than one dose. Buying and owning poison is always illegal, and even in big cities it can be had only from specialized, less than reputable sources. ^poison-price

### Multiple Doses

Unlike other afflictions, doses of the same poison stack, raising its attack bonus and lengthening it. They stack only while the poison is still active in the creature and the creature fails its first save against the new dose: a creature the new dose misses isn’t affected, and a later dose after the poison is cured or has run its course starts over.

- **Longer**: Each extra dose lengthens the poison by half the duration in its frequency.
- **Harder**: Each extra dose raises the poison’s attack bonus by +2.

Both increases are cumulative. A poison with several doses in a creature makes one attack at the higher bonus each time the frequency calls for one, not one per dose. Extra doses don’t change the cure, and meeting it ends every dose. Doses of different poisons don’t stack; each is tracked on its own. ^poison-doses

Contact and injury poisons on a weapon deliver one dose per hit, since the poison lasts for one successful attack. Inhaled and ingested poisons can deliver several doses at once.

_Example_: A character is bitten in the same round by three Medium monstrous spiders and fails his save against all three. Medium spider venom has an attack bonus of +4 and a frequency of 1/round for 4 rounds, so the second and third doses each add 2 rounds and +2 to the attack bonus: it attacks his Fortitude at +8 for the next 8 rounds. One miss still cures all three doses.

### Applying Poison

Applying poison to a weapon or a single piece of ammunition is a standard action. Whenever a character applies or readies a poison, there is a 5% chance that he exposes himself to it, and it attacks him as normal; this doesn’t use up the dose. Whenever a character attacks with a poisoned weapon and rolls a natural 1 on the attack roll, he exposes himself to the poison. The poison on a weapon is used up when the weapon strikes a creature or is touched by its wielder. ^applying-poison

**Poison Use**: A character with poison use never risks poisoning himself, whether applying, readying, making or attacking with a poison. ^poison-use

### Making Poison

A poison can be made with [[rangoric-srd/skills/Craft|Craft]] (alchemy). The DC to make a poison is 10 + its attack bonus. Making a poison as a potion adds +10 to the DC. Rolling a natural 1 on the check while making a poison exposes the crafter to it (this doesn’t use up the poison), unless the crafter has poison use. Which poisons alchemists and herbalists can make with their skills, and the [[rangoric-srd/feats/Craft Toxins|Craft Toxins]] feat for the rest, are in [[rangoric-srd/rules/alchemy-and-herbalism/Alchemical and Herbal Items#Toxins|toxins]]. ^making-poison

### Poison Immunities

Creatures with natural poison attacks are immune to their own poison. Nonliving creatures (constructs and undead) and creatures without metabolisms (such as elementals) are always immune to poison. Oozes, plants, and certain kinds of outsiders are also immune to poison, although special poisons could conceivably be made to harm them. ^poison-immunities

## Disease

From a widespread plague to the bite of a dire rat, disease is a serious threat to common folk and adventurers alike. A character can catch one when he is injured by a contaminated attack, touches an item smeared with diseased matter, or eats or drinks something tainted. Some injury diseases can be passed on by as small an injury as a flea bite, and most inhaled diseases can also be ingested (and the other way round).

Diseases rarely have a limited frequency, but most have a long onset time, and it can vary. Most diseases can be cured by a number of misses in a row or by spells such as _[[rangoric-srd/spells/Remove Disease|remove disease]]_. A disease’s attacks can be rolled secretly, so the player doesn’t know whether it has taken hold.

## Drugs and Addiction

Drugs are alchemical items with two sides: a short-term effect, usually a benefit, and an amount of ability damage. Every dose also risks addiction, a disease whose severity depends on the drug. A drug isn’t a poison, and none of the poison rules apply to it. ^drugs

**Taking a Drug**: A character who takes a drug gains its effect and takes its ability damage at once, and its addiction attacks his Fortitude to addict him. The effect is what the drug does to body or mind; the damage is its side effects, and also how long a dose stays active: since [[rangoric-srd/rules/Special Abilities and Conditions#^ability-damaged|ability damage]] heals at 1 point per day, a drug that deals 1 point stays in a character’s system for 1 day, and one that deals more stays longer. Taking several doses at once rarely does any good, but taking another as the effect wears off renews the effect, adding to the damage and to the risk of addiction. ^taking-a-drug

Each drug is given in these lines:

- **Type**: How it is taken: contact, ingested, inhaled or injury, as for poisons.
- **Addiction**: The addiction it causes (minor, moderate or severe), then the base attack bonus against Fortitude with which it addicts, and keeps a character addicted. This bonus can rise with repeated use.
- **Price**: The price of one dose.
- **Effect**: How long the drug lasts, and what it does.
- **Damage**: The ability damage it deals.

**Making Drugs**: A drug can be made with [[rangoric-srd/skills/Craft|Craft]] (alchemy). The DC to make a drug is 10 + its addiction attack bonus. Rolling a natural 1 on the check while making a drug exposes the crafter to it. ^making-drugs

**Drunkenness**: Alcohol can be abused too. A character can drink a number of alcoholic drinks equal to 1 + twice his Constitution modifier; each drink past that leaves him [[rangoric-srd/rules/Special Abilities and Conditions#^sickened|sickened]] for 1 hour. Particularly exotic or strong alcohol can be treated as a drug, and a character who regularly abuses alcohol might in time develop a moderate addiction. ^drunkenness

### Addiction

Each time a character takes a drug, it makes the attack its Addiction line gives to addict him. On a miss he isn’t addicted, and the drug works as normal. On a hit he contracts the addiction it names. Several doses of the same drug in a short time make addiction harder to resist: the attack bonus rises by +2 each time a character takes another dose while he still has ability damage from an earlier one. Keep track of how high the attack bonus rises, even for a character who is already addicted, since it sets the attack bonus he must overcome. ^addiction

Addiction comes in three degrees, [[rangoric-srd/rules/afflictions/Minor Addiction|minor]], [[rangoric-srd/rules/afflictions/Moderate Addiction|moderate]] and [[rangoric-srd/rules/afflictions/Severe Addiction|severe]], each a disease with a note of its own ([[#^table-addictions|Table: Addictions]]). Each gives a lasting penalty to ability scores for as long as the character has it. With a moderate or severe addiction, he also can’t naturally heal the ability damage dealt by the drug that caused it.

Every addiction pushes its sufferer to keep taking the drug. While a character is benefiting from the drug he is addicted to, he doesn’t suffer his addiction’s effects: he still gets the drug’s effect and takes its ability damage as normal, but the addiction is held off. As soon as the drug’s effect ends, the addiction’s effects return. ^addiction-held-off

**Curing Addiction**: An addiction is a disease, and can be cured like one, with spells such as _[[rangoric-srd/spells/Remove Disease|remove disease]]_ or by misses over time. Unlike other diseases, an addiction attacks an addicted character’s Fortitude, to keep him addicted, only after a day without the drug. Its attack bonus is the highest addiction bonus his use of the drug has reached (not necessarily the bonus that addicted him, if he kept taking it while addicted), and it drops by 2 for each day he goes without the drug, to no lower than the drug’s base addiction bonus. Overcoming the addiction takes two or three consecutive misses, as its cure says. A character who takes a dose of the drug he is addicted to relapses at once: the attack bonus returns to its highest, and any misses so far are lost. ^curing-addiction

## Infestation

Parasites such as [[rangoric-srd/rules/afflictions/Ear Seekers|ear seekers]] and [[rangoric-srd/rules/afflictions/Rot Grubs|rot grubs]] cause infestations, a kind of affliction like a disease. An infestation can be cured only by specific means: no number of misses ends it, so an infestation has no cure entry. A _[[rangoric-srd/spells/Remove Disease|remove disease]]_ spell (or a similar effect) halts an infestation at once, but immunity to disease gives no protection, since the infestation is caused by the parasites themselves. Each infestation’s [[rangoric-srd/rules/Hazards|hazard]] says what else ends it. ^infestation

## Curse

Careless rogues plundering a tomb, drunken heroes insulting a powerful wizard, and foolhardy adventurers who pick up ancient swords all might suffer from curses. These magic afflictions can have a wide variety of effects, from a simple penalty on certain checks to turning the victim into a toad. Some even make the victim slowly rot away, leaving nothing behind but dust. Unlike other afflictions, most curses can’t be cured by any number of misses. They can be cured with magic, usually spells such as _[[rangoric-srd/spells/Remove Curse|remove curse]]_ and _[[rangoric-srd/spells/Break Enchantment|break enchantment]]_. Some curses cause a slow decline; others give a fixed penalty from the moment they are contracted that neither fades nor grows worse. Some magic items act like curses: see [[rangoric-srd/magic-items/Intelligent and Cursed Items and Artifact#Cursed Items|cursed items]].

## Insanity

Insanity is an affliction that strikes those who live through extraordinary physical, mental or spiritual anguish and trials. It can also come from exposure to particularly potent sources of horror, madness or alien natures, which the mind simply can’t withstand. Insanity is a mind-affecting effect. Each insanity has a note of its own, with its attack, onset and effect ([[#^table-insanities|Table: Insanities]]); none has a frequency or cure entry, since every insanity is cured as below.

**Going Insane**: A creature whose Intelligence, Wisdom or Charisma is reduced to 0 has suffered a tremendous shock and might go insane: when that score recovers from 0, an insanity attacks it, rolled on [[#^table-types-of-insanity|Table: Types of Insanity]] or chosen to fit what reduced the score. The attack is rolled in secret: the victim shouldn’t know the result, nor which insanity might afflict him. Its effects play out naturally: some insanities (such as mania/phobia) take days or even months to show, while others (such as paranoia) are obvious at once. ^going-insane

A creature can also risk insanity in extremely unusual situations, as the GM decides, even when its mental ability scores are unharmed. A character held prisoner for a long time might be attacked by a phobia of open or closed spaces; someone repeatedly betrayed by allies, by paranoia; and a poor soul whose mind a powerful demon possessed, by psychosis when the demon is driven out. Magic can cause insanity too: the GM can have _[[rangoric-srd/spells/Insanity (Spell)|insanity]]_ inflict one random insanity per 5 caster levels instead of its usual effect, and _[[rangoric-srd/spells/Bestow Curse|bestow curse]]_ a single insanity, which is then a curse as well.

A creature can suffer from several insanities at once. A creature afflicted by an insanity it already has instead adds +5 to that insanity’s current attack bonus. ^multiple-insanities

**Curing Insanity**: Every insanity has an attack bonus that stands for its strength: its bonus against Will Defense when the creature is first exposed, and while the creature recovers from it. Recovering naturally takes a long time: once per week, the insanity attacks the creature’s Will at its current bonus. On a miss, the bonus drops by the creature’s Charisma bonus (minimum 1). The creature suffers the insanity’s full effects until its attack bonus reaches −10; then it is cured, and the insanity vanishes completely. _[[rangoric-srd/spells/Restoration, Lesser|Lesser restoration]]_ has no effect on insanity, but _[[rangoric-srd/spells/Restoration|restoration]]_ reduces the current attack bonus of one insanity affecting the target by the caster’s level. _[[rangoric-srd/spells/Restoration, Greater|Greater restoration]]_, _[[rangoric-srd/spells/Heal (Spell)|heal]]_, _[[rangoric-srd/spells/Limited Wish|limited wish]]_, _[[rangoric-srd/spells/Miracle|miracle]]_ or _[[rangoric-srd/spells/Wish|wish]]_ at once cures a target of all insanity. ^curing-insanity

**Types of Insanity**: When a creature goes insane, roll on this table, or choose the insanity that fits the cause.

**Table: Types of Insanity** ^table-types-of-insanity

| d%     | Insanity                                                                                                   |
| ------ | ---------------------------------------------------------------------------------------------------------- |
| 1–11   | [[rangoric-srd/rules/afflictions/Amnesia (Insanity)\|Amnesia]]                                             |
| 12–48  | [[rangoric-srd/rules/afflictions/Mania-Phobia (Insanity)\|Mania/Phobia]]                                   |
| 49–68  | [[rangoric-srd/rules/afflictions/Multiple Personality Disorder (Insanity)\|Multiple Personality Disorder]] |
| 69–78  | [[rangoric-srd/rules/afflictions/Paranoia (Insanity)\|Paranoia]]                                           |
| 79–84  | [[rangoric-srd/rules/afflictions/Psychosis (Insanity)\|Psychosis]]                                         |
| 85–100 | [[rangoric-srd/rules/afflictions/Schizophrenia (Insanity)\|Schizophrenia]]                                 |

## Treating an Affliction

A healer can help a poisoned character with the [[rangoric-srd/actions/Treat Poison|Treat Poison]] action and a diseased one with the [[rangoric-srd/actions/Treat Disease|Treat Disease]] action, both [[rangoric-srd/actions/First Aid|First Aid]] actions. Spells end afflictions as their own notes say.

## Initial and Secondary Damage

Some poisons and diseases are still written the older way, without a frequency or cure. They work as follows.

**Poisons with initial and secondary damage**: A failed save when the poison is contracted deals its initial damage. One minute later, the poison attacks again (whatever the first result), a failed save deals its secondary damage, and the poison ends. Ability damage marked with an asterisk (\*) is drain instead. Paralysis from such a poison lasts 2d6 minutes, and unconsciousness 1d3 hours, unless noted otherwise. ^initial-and-secondary-damage

**Diseases with an incubation period and damage**: The incubation period is the onset, the damage is the effect, the frequency is 1/day and the cure is 2 consecutive misses, unless the disease says otherwise. ^incubation-and-damage

## Sample Afflictions

Each of these has a note of its own with its full entry; the lists gather them from the [[rangoric-srd/rules/afflictions/Afflictions Index.base|Afflictions Index]]. Where the effect says “see note”, the note has more.

### Sample Poisons

By how each is delivered, then by DC, with the toxins and poison herbs of alchemy and herbalism among them; [[rangoric-srd/equipment/alchemical-items/Alchemical Toxins and Poisons|Alchemical Toxins and Poisons]] lists those with their category and DC to make.

**Table: Poisons** ^table-poisons

![[rangoric-srd/rules/afflictions/Afflictions Index.base#Poisons]]

### Sample Diseases

**Table: Diseases** ^table-diseases

![[rangoric-srd/rules/afflictions/Afflictions Index.base#Diseases]]

### Sample Curses

**Table: Curses** ^table-curses

![[rangoric-srd/rules/afflictions/Afflictions Index.base#Curses]]

### Sample Drugs

The drugs of the [[rangoric-srd/equipment/alchemical-items/Alchemical Items Index.base|alchemical items]], A to Z ([[#Drugs and Addiction|drugs and addiction]]).

**Table: Drugs** ^table-drugs

![[rangoric-srd/rules/afflictions/Afflictions Index.base#Drugs]]

### Addictions

**Table: Addictions** ^table-addictions

![[rangoric-srd/rules/afflictions/Afflictions Index.base#Addictions]]

### Sample Infestations

**Table: Infestations** ^table-infestations

![[rangoric-srd/rules/afflictions/Afflictions Index.base#Infestations]]

### Sample Insanities

**Table: Insanities** ^table-insanities

![[rangoric-srd/rules/afflictions/Afflictions Index.base#Insanities]]

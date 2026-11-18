---
srd-type: "class-option"
section: "Class Options"
option-type: "archetype"
class: ["Bard"]
replaces:
  - "bardic knowledge (1st)"
  - "inspire courage (1st)"
  - "versatile performance (2nd)"
  - "inspire competence (3rd)"
  - "lore master (5th)"
  - "suggestion (6th)"
  - "inspire greatness (9th)"
  - "inspire heroics (15th)"
  - "mass suggestion (18th)"
  - "deadly performance (20th)"
book: "Advanced Player's Guide"
based-on:
  - "[[path srd 3.5/archetypes/Sandman (Archetype)|Sandman (PF1)]]"
status: draft
change: new
pi-review: 2026-11-17
tags: [rangoric, rangoric/class-option]
---

# Sandman

*A [[rangoric-srd/classes/Bard#^bard-archetypes|bard]] [[rangoric-srd/class-options/archetypes/Archetypes|archetype]].*

Combining performance with stealth, trickery, and guile, the sandman uses cleverness to keep others off-balance.

**Bardic Performance**: A sandman gains the following types of [[rangoric-srd/classes/Bard#^bardic-music|bardic performance]].

**Stealspell (Su)**: A sandman can use performance to steal spells from his foes and add them to his list of spells known. Once the performance is started, the bard can steal a prepared spell or a spell known from another creature with a touch attack as a standard action. The target receives a Will save (DC 10 + 1/2 the bard's level + the bard's Cha bonus) to negate the effect. The sandman may choose a spell to steal, but if the target does not possess the spell, the bardic performance immediately ends. Otherwise the spell stolen is random, but it is always of the highest level that the bard can cast, if possible. The target loses the prepared spell or spell known and the sandman adds it to his list of spells known for as long as the performance continues, after which it reverts to the original recipient. While stolen, the bard can cast the spell using his available spell slots. This use does not consume the stolen spell. If the bard steals another spell while a spell is stolen, the previous spell immediately reverts to its original owner. This ability requires visual components. This performance replaces [[rangoric-srd/classes/Bard#^inspire-courage|inspire courage]].

**Slumber Song (Sp)**: At 6th level, a sandman can use his performance to cause a creature he has already [[rangoric-srd/classes/Bard#^bard-fascinate|fascinated]] to fall asleep (as *[[rangoric-srd/spells/Deep Slumber|deep slumber]]*, but with no HD limit). Otherwise, this ability functions like [[rangoric-srd/classes/Bard#^bard-suggestion|suggestion]]. This performance replaces [[rangoric-srd/classes/Bard#^bard-suggestion|suggestion]].

**Dramatic Subtext (Su)**: At 9th level, a sandman can use bardic performance to cast spells without obvious visual or audible components while retaining the spell's normal effects. Observers must succeed at a [[rangoric-srd/skills/Perception|Perception]] check opposed by a sandman's [[rangoric-srd/skills/Sleight of Hand|Sleight of Hand]] check to notice that the sandman is the source of the spellcasting (though spellcasting still provokes [[rangoric-srd/combat/Combat Initiative and Attacks of Opportunity#Attacks of Opportunity|attacks of opportunity]]). The bard must use this performance for at least 2 rounds before casting a spell; otherwise he is automatically detected and the performance ends. This ability replaces [[rangoric-srd/classes/Bard#^inspire-greatness|inspire greatness]].

**Greater Stealspell (Su)**: A sandman's stealspell power improves at 15th level. When a target fails a save against his stealspell performance, the sandman discovers its [[rangoric-srd/rules/Special Abilities and Conditions#Spell Resistance|spell resistance]] (if any) and all spells it has prepared or knows. He can then choose which spell to steal. The sandman may forgo stealing a spell and instead reduce the target's SR by an amount equal to half his bard level and gain that amount of spell resistance for as long as he continues performing. If he steals additional spell resistance, it stacks with previously stolen SR. If he steals a spell or ceases performing, the spell resistance immediately reverts back to its owner. This performance replaces [[rangoric-srd/classes/Bard#^inspire-heroics|inspire heroics]].

**Mass Slumber Song (Sp)**: At 18th level, a sandman can use slumber song to affect any number of fascinated creatures within 30 feet. Otherwise, this ability functions like [[rangoric-srd/classes/Bard#^bard-mass-suggestion|mass suggestion]]. This performance replaces [[rangoric-srd/classes/Bard#^bard-mass-suggestion|mass suggestion]].

**Spell Catching (Su)**: At 20th level, a sandman who saves against a spell or spell-like ability that targets only him (not including area spells) may use bardic performance as an immediate action. He must attempt a caster level check (DC 10 + the spell's original caster level). If it succeeds, the sandman can absorb the spell effect without harm and immediately recast that spell (using the original caster's level and save DC) or any spell he knows of that level or lower. Using this ability consumes a number of rounds of bardic performance equal to the spell's level, even if the check fails. This performance replaces [[rangoric-srd/classes/Bard#^bard-deadly-performance|deadly performance]].

**Master of Deception (Ex)**: A sandman gains a bonus equal to half his level on [[rangoric-srd/skills/Deception|Deception]], [[rangoric-srd/skills/Sleight of Hand|Sleight of Hand]], and [[rangoric-srd/skills/Stealth|Stealth]] checks. He may also disarm magical traps with [[rangoric-srd/skills/Engineering|Engineering]] as a [[rangoric-srd/classes/Rogue#^rogue-trapfinding|rogue’s trapfinding]] ability. This ability replaces [[rangoric-srd/classes/Bard#^bardic-knowledge|bardic knowledge]].

**Sneakspell (Ex)**: At 2nd level, a sandman adds +1 to the save DC of spells and bardic performance against opponents who are denied their Dex bonus. This increases to +2 at 10th level and +3 at 18th level. In addition, at 6th level he gains a +2 bonus on caster level checks to overcome spell resistance against such foes, and this bonus increases to +4 at 14th level. This ability replaces [[rangoric-srd/classes/Bard#^bard-versatile-performance|versatile performance]].

**Trap Sense (Ex)**: At 3rd level, a sandman gains a +1 bonus on Reflex saves against traps and a +1 dodge bonus to AC against traps. These bonuses increase by +1 every three levels after 3rd. This ability replaces [[rangoric-srd/classes/Bard#^inspire-competence|inspire competence]].

**Sneak Attack (Ex)**: At 5th level, a sandman inflicts +1d6 points of damage against targets within 30 feet that he [[rangoric-srd/combat/Combat Modifiers#Flanking|flanks]] or that are denied their Dex bonus to AC against him. This damage increases by +1d6 every five levels after 5th. This ability replaces [[rangoric-srd/classes/Bard#^bard-lore-master|lore master]].

---
srd-type: "class"
section: "Classes"
alignment: "Any"
hit-die: "d8"
bab: medium
fort: good
ref: good
will: poor
skill-points: "4 + Int modifier"
book: "Occult Adventures"
based-on:
  - "[[path srd 3.5 foundry/classes/Kineticist|Kineticist (PF1 Foundry)]]"
status: draft
change: new
pi-review: 2026-11-16
tags: [rangoric, rangoric/class]
---

## Character Classes

### Kineticist

Kineticists are living channels for elemental matter and energy, manipulating the world around them by drawing upon inner reserves from their own bodies. Kineticists often awaken to their kinetic abilities during a violent or traumatic experience, releasing their power involuntarily. As kinetic power is seldom inherited, kineticists are rarely able to find mentors to guide them, so they must delve into these mysteries on their own to learn to control their gifts.

**Role**: Kineticists generally use their powers to assail their foes from range, but based on the way their talents develop, they can channel their kinetic abilities for a variety of situations. Kineticists are usually quite different from their families and friends, so they often strike out on their own or alongside others with extraordinary talents.

The kineticist class isn’t the [[rangoric-srd/psionics/Psion|psion]]’s kineticist: a psion who specializes in psychokinesis is also called a kineticist, and the “Kineticist” levels on psionic powers are that psion’s.

**Alignment**: Any.

**Hit Die**: d8.

**[[rangoric-srd/rules/Base Attack Bonus|Base Attack Bonus]]**: Medium (3/4 per level).

**[[rangoric-srd/rules/Saving Throws|Saving Throws]]**: Good Fortitude and Reflex, poor Will.

###### Class Skills

The kineticist’s class skills (and the key ability for each skill) are [[rangoric-srd/skills/Acrobatics|Acrobatics]] (Dex), [[rangoric-srd/skills/Craft|Craft]] (Int), [[rangoric-srd/skills/Emulation|Emulation]] (Cha), [[rangoric-srd/skills/Fieldcraft|Fieldcraft]] (Wis), [[rangoric-srd/skills/Intimidation|Intimidation]] (Cha), [[rangoric-srd/skills/Investigation|Investigation]] (Int), [[rangoric-srd/skills/Medicine|Medicine]] (Int), [[rangoric-srd/skills/Perception|Perception]] (Wis), [[rangoric-srd/skills/Profession|Profession]] (Wis), and [[rangoric-srd/skills/Stealth|Stealth]] (Dex). Her [[rangoric-srd/class-options/elements/Elements|element]] adds two more.

**Skill Points at Each Level**: 4 + Int modifier.

**Table: The Kineticist** ^table-the-kineticist

| Level | Special                                                             |
| ----- | ------------------------------------------------------------------- |
| 1st   | Burn, elemental focus, gather power, infusion, kinetic blast        |
| 2nd   | Elemental defense, utility wild talent                              |
| 3rd   | Elemental overflow +1, infusion                                     |
| 4th   | Utility wild talent                                                 |
| 5th   | Infusion, infusion specialization 1, metakinesis (empower)          |
| 6th   | Elemental overflow +2, internal buffer 1, utility wild talent       |
| 7th   | Expanded element                                                    |
| 8th   | Infusion specialization 2, utility wild talent                      |
| 9th   | Elemental overflow +3, infusion, metakinesis (maximize)             |
| 10th  | Utility wild talent                                                 |
| 11th  | Infusion, infusion specialization 3, internal buffer 2, supercharge |
| 12th  | Elemental overflow +4, utility wild talent                          |
| 13th  | Infusion, metakinesis (quicken)                                     |
| 14th  | Infusion specialization 4, utility wild talent                      |
| 15th  | Expanded element, elemental overflow +5                             |
| 16th  | Composite specialization, internal buffer 3, utility wild talent    |
| 17th  | Infusion, infusion specialization 5, metakinesis (twice)            |
| 18th  | Elemental overflow +6, utility wild talent                          |
| 19th  | Infusion, metakinetic master                                        |
| 20th  | Infusion specialization 6, omnikinesis, utility wild talent         |

###### Class Features

All of the following are class features of the kineticist.

**Weapon and Armor Proficiency**: Kineticists are proficient with all simple weapons and light armor, but not shields. ^kineticist-proficiency

**Elemental Focus (Su)**: At 1st level, a kineticist chooses one primary element on which to focus. This element determines how she accesses the raw power of the [[rangoric-srd/rules/Planes#The Ethereal Plane|Ethereal Plane]], and grants her access to specific [[rangoric-srd/class-options/wild-talents/Wild Talents|wild talents]] and additional class skills. She can select [[rangoric-srd/class-options/elements/Aether Element|aether]] (telekinesis), [[rangoric-srd/class-options/elements/Air Element|air]] (aerokinesis), [[rangoric-srd/class-options/elements/Earth Element|earth]] (geokinesis), [[rangoric-srd/class-options/elements/Fire Element|fire]] (pyrokinesis), [[rangoric-srd/class-options/elements/Void Element|void]] (chaokinesis), [[rangoric-srd/class-options/elements/Water Element|water]] (hydrokinesis), or [[rangoric-srd/class-options/elements/Wood Element|wood]] (phytokinesis). She gains her selected element’s basic utility wild talent ([[rangoric-srd/class-options/wild-talents/Basic Telekinesis|basic telekinesis]], [[rangoric-srd/class-options/wild-talents/Basic Aerokinesis|basic aerokinesis]], [[rangoric-srd/class-options/wild-talents/Basic Geokinesis|basic geokinesis]], [[rangoric-srd/class-options/wild-talents/Basic Pyrokinesis|basic pyrokinesis]], [[rangoric-srd/class-options/wild-talents/Basic Chaokinesis|basic chaokinesis]], [[rangoric-srd/class-options/wild-talents/Basic Hydrokinesis|basic hydrokinesis]], or [[rangoric-srd/class-options/wild-talents/Basic Phytokinesis|basic phytokinesis]]) as a bonus wild talent. Each element’s note, listed in [[rangoric-srd/class-options/elements/Elements|Elements]], gives the abilities it grants. ^kineticist-elemental-focus

**Wild Talents**: A kineticist can use [[rangoric-srd/class-options/wild-talents/Wild Talents|wild talents]]—magical abilities similar to spells but drawn from the kineticist’s innate [[rangoric-srd/spells/Magic Overview#Psychic Magic|psychic]] talent and usable at will. Wild talents are typically [[rangoric-srd/rules/Special Abilities and Conditions#^spell-like-abilities|spell-like abilities]] (though some are [[rangoric-srd/rules/Special Abilities and Conditions#^supernatural-abilities|supernatural abilities]]), and take a standard action to use unless otherwise noted. A wild talent always has the elemental descriptor or descriptors (aether, air, earth, fire, void, water, or wood) matching its Element entry. A wild talent that can be used with any of several elements gains the appropriate elemental descriptor when used with an element. For example, the [[rangoric-srd/class-options/wild-talents/Wall (Wild Talent)|wall]] wild talent gains the earth descriptor when used by a geokineticist. ^kineticist-wild-talents

Every wild talent has an effective spell level. A kineticist can always select 1st-level wild talents, but she can select a wild talent of a higher level only if her kineticist level is at least double the wild talent’s effective spell level. Kinetic blast and defense wild talents are always considered to have an effective spell level equal to 1/2 the kineticist’s class level (to a maximum effective spell level of 9th at kineticist level 18th). Unless otherwise noted, the attack bonus of a wild talent against a defense is the wild talent’s effective spell level + the kineticist’s Constitution modifier. The kineticist uses her Constitution modifier on all [[rangoric-srd/rules/Concentration (Check)|concentration checks]] for wild talents.

In addition to the wild talents she gains from her other class features, at 2nd level and every 2 levels thereafter, a kineticist selects a new utility wild talent from the list of options available to her. A kineticist can select only universal wild talents or those that match her element (see [[rangoric-srd/classes/Kineticist#^kineticist-elemental-focus|elemental focus]] above). At 6th, 10th, and 16th levels, a kineticist can replace one of her utility wild talents with another wild talent of the same level or lower. She can’t replace a wild talent that she used to qualify for another of her wild talents.

**Burn (Ex)**: At 1st level, a kineticist can overexert herself to channel more power than normal, pushing past the limit of what is safe for her body by accepting burn. Some of her wild talents allow her to accept burn in exchange for a greater effect, while others require her to accept a certain amount of burn to use that talent at all. For each point of burn she accepts, a kineticist takes 1 point of [[rangoric-srd/combat/Injury and Death#Nonlethal Damage|nonlethal damage]] per character level. This damage can’t be healed by any means other than getting a full night’s rest, which removes all burn and associated nonlethal damage. Nonlethal damage from burn can’t be reduced or redirected, and a kineticist incapable of taking nonlethal damage can’t accept burn. A kineticist can accept only 1 point of burn per round. This limit rises to 2 points of burn at 6th level, and rises by 1 additional point every 3 levels thereafter. A kineticist can’t choose to accept burn if it would put her total number of points of burn higher than 3 + her Constitution modifier (though she can be forced to accept more burn from a source outside her control). A kineticist who has accepted burn never benefits from abilities that allow her to ignore or alter the effects she receives from nonlethal damage. ^kineticist-burn

**Kinetic Blast (Sp)**: At 1st level, a kineticist gains a kinetic blast wild talent of her choice. This kinetic blast must be a [[rangoric-srd/class-options/wild-talents/Wild Talents#^simple-blasts|simple blast]] that matches her element. As a standard action, the kineticist can unleash a kinetic blast at a single target up to a range of 30 feet. She must have at least one hand free to aim the blast (or one prehensile appendage, if she doesn’t have hands). All damage from a kinetic blast is treated as magic for the purpose of bypassing [[rangoric-srd/rules/Special Abilities and Conditions#Damage Reduction|damage reduction]]. Kinetic blasts count as a type of weapon for the purpose of feats such as [[rangoric-srd/feats/Weapon Focus|Weapon Focus]]. The kineticist is never considered to be wielding or gripping the kinetic blast (regardless of effects from form infusions; see [[rangoric-srd/classes/Kineticist#^kineticist-infusion|infusion]]), and she can’t use [[rangoric-srd/feats/Vital Strike|Vital Strike]] feats with kinetic blasts. Even the weakest kinetic blast involves a sizable mass of elemental matter or energy, so kinetic blasts always deal full damage to swarms of any size (though only area blasts deal extra damage to swarms). A readied kinetic blast can be used to [[rangoric-srd/spells/Magic Overview#Counterspells|counterspell]] any spell of equal or lower level that shares its descriptor. A kinetic blast that deals energy damage of any type (including force) has the corresponding descriptor. ^kineticist-kinetic-blast

The kinetic blasts, and the rules for simple and composite blasts, are in [[rangoric-srd/class-options/wild-talents/Wild Talents#Kinetic Blasts|Wild Talents]].

**Gather Power (Su)**: If she has both hands free (or all of her prehensile appendages free, for unusual kineticists), a kineticist can gather energy or elemental matter as a move action. Gathering power creates an extremely loud, visible display in a 20-foot radius centered on the kineticist, as the energy or matter swirls around her. Gathering power in this way allows the kineticist to reduce the total [[rangoric-srd/classes/Kineticist#^kineticist-burn|burn]] cost of a blast wild talent she uses in the same round by 1 point. The kineticist can instead gather power for 1 full round in order to reduce the total burn cost of a blast wild talent used on her next turn by 2 points (to a minimum of 0 points). If she does so, she can also gather power as a move action during her next turn to reduce the burn cost by a total of 3 points. If the kineticist takes damage during or after gathering power and before using the kinetic blast that releases it, she must succeed at a [[rangoric-srd/rules/Concentration (Check)|concentration check]] (DC = 10 + damage taken + effective spell level of her kinetic blast) or lose the energy in a wild surge that forces her to accept a number of points of burn equal to the number of points by which her gathered power would have reduced the burn cost. This ability can never reduce the burn cost of a wild talent below 0 points. ^kineticist-gather-power

**Infusion (Su)**: At 1st level, a kineticist gains an [[rangoric-srd/class-options/wild-talents/Wild Talents#Infusion Wild Talents|infusion wild talent]] from the list of options available based on her elemental focus. She gains additional infusions at 3rd, 5th, 9th, 11th, 13th, 17th, and 19th levels. By using infusions along with her kinetic blasts, a kineticist can alter her kinetic blasts to suit her needs. Infusions come in two types, each of which changes a kinetic blast differently: a substance infusion causes an additional effect, while a form infusion causes the kinetic blast to manifest in a different way. Each infusion can alter only certain kinds of kinetic blasts, which are listed in its Associated Blasts entry. Each time the kineticist uses one of her kinetic blast wild talents, she can apply up to one associated form infusion and up to one associated substance infusion. Some infusions change the action required to activate a kinetic blast or entirely transform the kinetic blast’s normal effects. The burn cost listed in each infusion’s Burn entry is added to the burn cost of the kinetic blast the infusion modifies. ^kineticist-infusion

The attack bonus of an infusion against a defense is based on the associated kinetic blast’s effective spell level, not the level of the infusion. The attack bonus of a form infusion uses the kineticist’s Dexterity modifier instead of her Constitution modifier. When a kineticist modifies a kinetic blast with a form infusion and a substance infusion that both attack a defense, the form infusion attacks each target first. If it misses and a miss negates the infusion’s effects, the entire kinetic blast is negated; otherwise, the substance infusion then attacks the target. If a kineticist’s form and substance infusions both alter the kinetic blast’s damage, apply the substance infusion’s alteration first.

At 5th, 11th, and 17th levels, a kineticist can replace one of her infusions with another infusion of the same effective spell level or lower. She can’t replace an infusion that she used to qualify for another of her wild talents. The infusions are listed in [[rangoric-srd/class-options/wild-talents/Wild Talents#Infusion Wild Talents|Wild Talents]].

**Elemental Defense (Su)**: At 2nd level, a kineticist gains her element’s [[rangoric-srd/class-options/wild-talents/Wild Talents#Defense Wild Talents|defense wild talent]]. ^kineticist-elemental-defense

**Elemental Overflow (Ex)**: At 3rd level, a kineticist’s body surges with energy from her chosen element whenever she accepts [[rangoric-srd/classes/Kineticist#^kineticist-burn|burn]], causing her to glow with a nimbus of fire, weep water from her pores, or experience some other thematic effect. In addition, she receives a bonus on her attack rolls with kinetic blasts equal to the total number of points of burn she currently has, to a maximum bonus of +1 for every 3 kineticist levels she possesses. She also receives a bonus on damage rolls with her kinetic blast equal to double the bonus on attack rolls. The kineticist can suppress the visual effects of elemental overflow by concentrating for 1 full round, but doing so suppresses all of this ability’s other benefits, as well. The next time the kineticist uses any wild talent, the visual effects and benefits return instantly. ^kineticist-elemental-overflow

As a kineticist’s body becomes more and more suffused with her element, she begins to gain more powerful benefits. Starting at 6th level, whenever she has at least 3 points of burn, the kineticist gains a +2 size bonus to two physical ability scores of her choice. She also gains a chance to ignore the effects of a critical hit or sneak attack equal to 5% × her current number of points of burn. At 11th level, whenever the kineticist has at least 5 points of burn, these bonuses increase to a +4 size bonus to one physical ability score of her choice and a +2 size bonus to each of her other two physical ability scores. At 16th level, whenever the kineticist has at least 7 points of burn, these bonuses increase to a +6 size bonus to one physical ability score of her choice, a +4 size bonus to a second physical ability score of her choice, and a +2 size bonus to the remaining physical ability score.

**Infusion Specialization (Ex)**: At 5th level, whenever a kineticist uses one or more [[rangoric-srd/classes/Kineticist#^kineticist-infusion|infusions]] with a blast, she reduces the combined burn cost of the infusions by 1. This can’t reduce the total cost of the infusions used below 0. She reduces the burn cost by 1 additional point at 8th, 11th, 14th, 17th, and 20th levels. ^kineticist-infusion-specialization

**Metakinesis (Su)**: At 5th level, a kineticist gains the ability to alter her kinetic blasts as if with metamagic feats by accepting burn. By accepting 1 point of burn, she can empower her kinetic blast (as if using [[rangoric-srd/feats/Empower Spell|Empower Spell]]). At 9th level, by accepting 2 points of burn, she can maximize her kinetic blast as if using [[rangoric-srd/feats/Maximize Spell|Maximize Spell]]. At 13th level, by accepting 3 points of burn, she can quicken her kinetic blast as if using [[rangoric-srd/feats/Quicken Spell|Quicken Spell]]. At 17th level, by accepting 4 points of burn, the kineticist can use her kinetic blast twice with the same standard action, or swift action if she also uses metakinesis to quicken the blast. When she uses a double kinetic blast, all modifications, such as metakinesis and infusions, apply to both of the blasts, but the kineticist needs to pay the burn cost only once. ^kineticist-metakinesis

**Internal Buffer (Su)**: At 6th level, a kineticist’s study of her body and the elemental forces that course through it allow her to form an internal buffer to store extra energy. The buffer starts empty and doesn’t replenish each day, but the kineticist can accept 1 point of burn to add 1 point to the buffer as a full-round action, to a maximum of 1 point total. This maximum increases to 2 points at 11th level and to 3 points at 16th level. Once the kineticist adds points to her buffer, they remain indefinitely until she spends them. When she would otherwise accept burn, a kineticist can spend 1 point from her buffer to avoid accepting 1 point of burn. She cannot spend more than 1 point from her buffer in this way for a single wild talent. Points spent from the internal buffer don’t activate [[rangoric-srd/classes/Kineticist#^kineticist-elemental-overflow|elemental overflow]] or add to its effects. Similarly, this buffer can be used to exceed the limit on the number of points of burn the kineticist can accept in a single turn. ^kineticist-internal-buffer

**Expanded Element (Su)**: At 7th level, a kineticist learns to use another element or expands her understanding of her own element. She can choose any element, including her primary element. She gains one of that element’s simple blast wild talents that she does not already possess, if any. She also gains all composite blast wild talents whose prerequisites she meets, as well as the basic wild talent of her chosen expanded element (for instance, [[rangoric-srd/class-options/wild-talents/Basic Aerokinesis|basic aerokinesis]] if she chooses air). The composite blasts and their rules are in [[rangoric-srd/class-options/wild-talents/Wild Talents#^composite-blasts|Wild Talents]]. She doesn’t gain the defense wild talent of the expanded element (but see [[rangoric-srd/class-options/wild-talents/Expanded Defense|expanded defense]]). ^kineticist-expanded-element

If the kineticist’s expanded element is different from her primary element, she treats her kineticist level as 4 levels lower for the purpose of determining which wild talents she can learn from her expanded element.

If the kineticist chooses to expand her understanding of an element she already has, she gains an additional utility wild talent or infusion of her choice from that element, as if from her infusion or wild talent class feature, as appropriate.

At 15th level, the kineticist can either select a new element or expand her understanding of her original element. She can’t select the same element she selected at 7th level unless it is her primary element. She gains all the benefits from her new expanded element as listed above. However, if the kineticist selected her primary element as her expanded element at both 7th and 15th levels, her mastery of that element increases. For wild talents of her element, the kineticist gains a +1 bonus on attack rolls and damage rolls, as well as to caster level and to the attack bonus of her wild talents against defenses.

**Supercharge (Su)**: At 11th level, when using [[rangoric-srd/classes/Kineticist#^kineticist-gather-power|gather power]] as a move action, a kineticist can reduce the total burn cost of a single wild talent by 2 points instead of 1. When using gather power for 1 full round, she can reduce the burn cost of a single wild talent by 3 points instead of 2. ^kineticist-supercharge

**Composite Specialization (Su)**: At 16th level, a kineticist becomes more adept at creating [[rangoric-srd/class-options/wild-talents/Wild Talents#^composite-blasts|composite blasts]]. She reduces the burn cost of all composite blasts by 1 point. This can’t reduce the cost of a composite blast below 0 points. ^kineticist-composite-specialization

**Metakinetic Master (Su)**: At 19th level, a kineticist chooses one type of [[rangoric-srd/classes/Kineticist#^kineticist-metakinesis|metakinesis]], such as empower or quicken. She reduces the burn cost of that metakinesis by 1 point (to a minimum of 0 points). ^kineticist-metakinetic-master

**Omnikinesis (Su)**: At 20th level, a kineticist transcends the distinction between the different elements and can bend all creation to her will. By accepting 1 point of burn (in addition to any burn requirement of the kinetic blast she chooses), she can use any blast wild talent she doesn’t know. By accepting 1 point of burn as a standard action, she can change any of her wild talents into any other wild talent of the same category (such as simple blasts or defense) for 24 hours, ignoring any elemental requirements or restrictions (but not any other requirements or restrictions). ^kineticist-omnikinesis

**Elements and Wild Talents**: The elements are in [[rangoric-srd/class-options/elements/Elements|Elements]], each with its own note, and the wild talents in [[rangoric-srd/class-options/wild-talents/Wild Talents|Wild Talents]], one note each.

**Archetypes**: A kineticist can take one or more [[rangoric-srd/class-options/archetypes/Archetypes|archetypes]], which replace some of the class features above with others. The kineticist’s archetypes, with what each replaces: ^kineticist-archetypes

![[rangoric-srd/class-options/archetypes/Archetypes Index.base#Kineticist]]

---
srd-type: "spell"
section: "Spells"
aliases:
  - "Dream Travel"
school: "Conjuration"
subschool: "Teleportation"
descriptor:
  - "Mind-Affecting"
level:
  - "Mes 6"
  - "Psy 6"
components:
  - "V"
  - "S"
casting-time: "1 standard action"
range: "Touch"
target: "You and one creature/level"
duration: "1 hour/level (D)"
defense: "Will"
spell-resistance: "Yes"
status: draft
pi-review: 2026-11-16
tags: [rangoric, rangoric/spell]
---

# Dream Travel

_Conjuration (Teleportation) \[Mind-Affecting\]_

- **Level**: Mes 6, Psy 6
- **Components**: V, S
- **Casting Time**: 1 standard action
- **Range**: Touch
- **Target**: You and one creature/level
- **Duration**: 1 hour/level (D)
- **Defense**: Will
- **Spell Resistance**: Yes

You and the other targets of the spell are physically drawn from the Material Plane into the Dimension of Dreams on a voyage into the dreams of a creature you designate. In the Dimension of Dreams, you move through a swirling sea of thoughts, desires, and emotions created by the minds of dreamers everywhere to reach your destination dreamscape. Reaching the destination dreamscape takes 1 hour. At any point before the spell's duration ends, you can dismiss the spell to return to where you started on the Material Plane. The connection between dreams and reality is inherently tenuous, and your ability to arrive precisely where you mean to is dependent on your familiarity with the dreamer you're trying to find. To determine how accurate your arrival is at the end of your _dream travel_, roll d% on the following table.

| Familiarity       | On Target | Off Target | Other | Dreamscape Mishap |
| ----------------- | --------- | ---------- | ----- | ----------------- |
| Very familiar     | 1-97      | 98-99      | 100   | -                 |
| Somewhat familiar | 1-94      | 95-97      | 98-99 | 100               |
| Known creature    | 1-88      | 89-94      | 95-98 | 99-100            |
| Not well known    | 1-76      | 77-88      | 89-96 | 97-100            |
| False identity    | -         | -          | 81-92 | 93-100            |

**Familiarity**: "Very familiar" means that you have had contact using _[[rangoric-srd/spells/Dream|dream]]_, _[[rangoric-srd/spells/Dream Council|dream council]]_, _[[rangoric-srd/spells/Dream Scan|dream scan]]_, or a similar spell within the past 24 hours with the creature whose dreamscape you are trying to locate. "Somewhat familiar" means that you have had contact with the dreaming character using one of those spells at least once in the past. "Known creature" means that while you know the creature whose dreamscape you're trying to locate, you have not connected to its dreams with those spells. "Not well known" is a creature you have heard of, know by name and true identity, but have never met. "False identity" means that whether or not you have met the creature, you know it only through a false identity. When trying to locate the dreamscape of a creature known to you through a false identity, roll 1d20 + 80 on the table to obtain your results (instead of rolling d%), since there is no way for you to pinpoint the correct dreamscape.  
**On Target**: You travel to the correct creature's current dreamscape.  
**Off Target**: You travel to an area near the target dreamscape on the Ethereal Plane.  
**Other Dreamscape**: You travel to a similar creature's dreamscape on the Dimension of Dreams.  
**Mishap**: You and anyone else traveling with you experience a mishap during travel; each character takes 1d10 points of damage and must reroll on the table to see where it ends up. For these rerolls, roll 1d20 + 80. Each time "Mishap" comes up, the travelers take more damage and must reroll to see where they end up.

Regardless of the accuracy of your _dream travel_, you and your companions all arrive at the same location (except in the case of a mishap). Mindless creatures can't use _dream travel_, nor can creatures that can't dream. You might be able to exit the dream near the creature on its home plane. If you and the other creatures are still in a dream when the dreamer wakes up, the dreamer can decide to bring you out onto its plane within 1d10 miles of itself. If it chooses not to, you and the other travelers are pushed into another dreamscape or onto the Ethereal Plane. The spell ends when the creature wakes up, so you no longer have the option to dismiss the spell and return home. However, you do get enough warning that a spell is about to end that you can dismiss it before the dreamer awakens and decides whether to allow you to arrive at its location. You can use _dream travel_ to travel to the dream of a creature on another plane, but this requires trekking through the dreams of outsiders. It takes 1d4+1 hours of uninterrupted travel to reach the destination dream, and the journey attacks each traveler’s Will each hour spent traveling in this fashion. Its attack bonus is +0 for the first hour, and increases by 5 for each hour thereafter. If it hits a creature, the creature becomes shaken for the remainder of the _dream travel_ and for a number of hours thereafter equal to the amount of time spent using _dream travel_ to reach the destination plane. After the first time it hits a creature, one of the following effects occurs (determined randomly by the GM). These effects are considered [[rangoric-srd/spells/Magic Overview#^emotion-component|emotion]] effects, in addition to any other descriptors that apply.

| d6  | Result                                                                                                                                                                                                                                                          |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Creature contracts [[rangoric-srd/rules/afflictions/Cackle Fever\|cackle fever]] or [[rangoric-srd/rules/afflictions/Mindfire\|mindfire]] (equal chance of either).                                                                                             |
| 2   | Creature is cursed, as _[[rangoric-srd/spells/Bestow Curse\|bestow curse]]_; if the creature is a spellcaster, it instead acquires a random [[rangoric-srd/rules/spellblights/Spellblights#^table-minor-spellblights\|minor spellblight]].                      |
| 3   | Creature is attacked by a _[[rangoric-srd/spells/Phantasmal Killer\|phantasmal killer]]_, and its first attack against the creature’s Will hits automatically. Its attack bonus against Fortitude is equal to the journey’s attack bonus that hit the creature. |
| 4   | Creature is possessed as _[[rangoric-srd/spells/Possession\|possession]]_ by an outsider (50% chance to be a creature from the destination plane; otherwise, it is a random hostile outsider).                                                                  |
| 5   | Creature is affected as _[[rangoric-srd/spells/Feeblemind\|feeblemind]]_.                                                                                                                                                                                       |
| 6   | Creature is affected as _[[rangoric-srd/spells/Insanity (Spell)\|insanity]]_.                                                                                                                                                                                   |

Traveling to a different planar destination decreases the accuracy of your dream transit. If you exit a creature's dream onto a plane different from the plane you started on, you end up in a random location on the destination plane. If the target of your _dream travel_ isn't dreaming, you and the other travelers can wait on the Dimension of Dreams until that creature begins sleeping. For each hour that passes during this wait, the journey attacks each traveler’s Will as if it were traveling to reach another plane.

---
srd-type: "overview"
section: "Unearthed Arcana"
based-on:
  - "[[fantasy srd 3.5/unearthed-arcana/Recharge Magic|Recharge Magic (3.5)]]"
status: draft
change: modified
pi-review: scanned 2026-10-15
tags: [rangoric, rangoric/overview]
---

## Unearthed Arcana

### Recharge Magic

In this variant, spellcasters don’t have a hard limit on spells per day. Instead, it takes time to gather the magical energies required to cast a spell of a particular level, so characters must wait a number of rounds, minutes, or hours before casting such a spell again. Spells with an instantaneous duration or a duration measured in rounds can be cast dozens of times per day. Longer-duration spells cast outside of combat have recharge times measured in minutes or hours.

At its heart, the recharge magic variant is simple: A well-rested spellcaster can cast any spell he knows or has prepared, but then either rolls a die to find out how many rounds must pass before spells of that level become available again (if it’s a [[#General Recharge Spells|general recharge spell]]) or loses access to that spell for a specified time (if it’s a [[#Specific Recharge Spells|specific recharge spell]]). Spell slots are never expended; they just become temporarily unavailable.

Recharging doesn’t require any actions and doesn’t provoke attacks of opportunity. As long as a spellcaster is alive, he naturally recharges his energy.

With this variant, all spellcasters effectively become spontaneous casters like [[rangoric-srd/classes/Sorcerer|sorcerers]], choosing a spell each round from a list. For sorcerers and bards, the list is fixed (just as it is for sorcerers and bards who aren’t using the variant), but other spellcasters set their available menu of spells when they prepare spells for the day. With the recharge variant, there’s no reason to prepare the same spell in more than one slot. Because sorcerers and bards don’t have the flexibility of choosing a new menu of spells each day, their general recharge times are shorter.

Some classes, such as the cleric and the druid, have limited spontaneous spellcasting ability. Such a character can convert any spell on his daily list into the appropriate spell (such as either [[rangoric-srd/spells/Cure Light Wounds|cure wounds]] or [[rangoric-srd/spells/Inflict Light Wounds|inflict wounds]] for a cleric, or [[rangoric-srd/spells/Summon Nature’s Ally I|summon nature’s ally]] for a druid), but doing so replaces the converted spell on the cleric’s daily list with the spell cast in its place. This happens only once per spell level, because after that point the relevant cure or inflict spell appears on the spell list as if it had been prepared.

This variant distinguishes two kinds of spells: spells with general recharge time (usually no more than a few rounds) and spells with specific recharge times (which range from minutes to hours).

###### Recharge Times for Other Spells

[[rangoric-srd/unearthed-arcana/Recharge Magic|Table: Spell Recharge Times]] includes all standard spells. Each one is indicated as having either a general recharge time, a specific recharge time measured in minutes or hours, or a notation that the spell is prohibited to casters when this variant is used. For spells from other sources that are not mentioned here, use those on the table as a guide, keeping the following in mind.

Combat-oriented and short-duration spells (those lasting up to 1 round per level) typically have a general recharge time. Conversely, spells with longer durations have specific recharge times (the longer the duration, the longer the recharge time). Any spell with an expensive material component or an XP component has a general recharge time.

Enchantments usually have a specific recharge time ranging from 30 minutes to 12 hours. This limitation prevents characters from simply charming everyone in the tavern in the space of a few minutes.

Spells that build things have a specific recharge time measured in hours.

Divinations typically have a specific recharge time, often in the neighborhood of 6 hours, to prevent their abuse in the hands of curious characters.

Powerful illusions and permanent "trap"-type spells have specific recharge times of 12 hours to 1 day, unless they’re expensive to cast.

##### General Recharge Spells

Spells that have general recharge times are those cast in combat, those with longer casting times, and those with an experience point or expensive material component. Once a character has cast a general recharge spell, he can’t cast another spell of that level until a number of rounds have passed.

[[rangoric-srd/unearthed-arcana/Recharge Magic|Table: General Recharge Times]] tells how many rounds must pass after the casting of a general recharge spell before another spell of that level becomes available.

**Table: General Recharge Times**

| Spell Level              | Bard, Sorcerer | Cleric, Druid, Paladin, Ranger, Wizard |
| ------------------------ | -------------- | -------------------------------------- |
| Highest possible         | 1d4+1 rounds   | 1d6+1 rounds                           |
| Second highest possible  | 1d4+1 rounds   | 1d6+1 rounds                           |
| Third highest possible   | 1d4 rounds     | 1d4+1 rounds                           |
| Fourth highest possible  | 1d4 rounds     | 1d4+1 rounds                           |
| Fifth highest possible   | 1d3 rounds     | 1d4 rounds                             |
| Sixth highest possible   | 1d3 rounds     | 1d4 rounds                             |
| Seventh highest possible | 1 round        | 1d3 rounds                             |
| Eighth highest possible  | 1 round        | 1d3 rounds                             |
| Ninth highest possible   | 0              | 1 round                                |
| Tenth highest possible   | 0              | 1 round                                |

For example, take a 4th-level wizard. His 2nd-level spells (the highest possible level he can cast) and 1st-level spells (the second highest possible level he can cast) take 1d6+1 rounds to recharge, and his 0-level spells (the third highest possible level he can cast) take 1d4+1 rounds to recharge. When he attains 5th level, his 3rd-level and 2nd-level spells take 1d6+1 rounds to recharge and his 1st- and 0-level spells take 1d4+1 rounds to recharge. (Specific recharge spells have their own recharge times that don’t match these values.)

Another example: Aliester the 10th-level sorcerer casts [[rangoric-srd/spells/Fireball|fireball]] in the first round of a fight. Once he casts the spell, he rolls 1d4 to determine his recharge time. He rolls a 2, so he must wait 2 rounds before he regains access to 3rd-level spells. In the following round, he casts [[rangoric-srd/spells/Cloudkill|cloudkill]], one of his highest-level spells. Rolling a 4 on 1d4, Aliester is dismayed to learn he must wait 5 (1d4+1) rounds before he can cast cloudkill again. In the next round, he casts [[rangoric-srd/spells/Magic Missile|magic missile]], rolling 1d3 afterward and getting a result of 1 for a 1-round recharge time. In the following round, Aliester regains access to his 3rd-level spells, so he can cast another fireball if he likes, or he can cast magic missile again (because the 1-round recharge time for his 1st-level spells has elapsed).

###### Metamagic and General Recharge Spells

Spellcasters who prepare spells simply put the metamagic versions of the spells they want in the appropriate spell slots, and they’re cast at their effective level. For example, casting a [[rangoric-srd/feats/Quicken Spell|quickened]] [[rangoric-srd/spells/Magic Missile|magic missile]] forces a spellcaster to recharge her 5th-level spells, not her 1st-level spells. Sorcerers and bards take a full-round action to add metamagic to any spell they know, and casting that spell forces a recharge of the effective level of the metamagic spell. For example, an [[rangoric-srd/feats/Extend Spell|extended]] [[rangoric-srd/spells/Haste|haste]] spell cast by a sorcerer would require a recharge roll for a 4th-level spell.

##### Specific Recharge Spells

Most long-duration utility spells have specific recharge times so spellcasters can’t just cast them on everyone they meet. These might range from a mere 5 minutes (for [[rangoric-srd/spells/Bull’s Strength|bull’s strength]]) to 4 hours (for [[rangoric-srd/spells/Teleport|teleport]]) to a full day, or 24 hours (for [[rangoric-srd/spells/Wind Walk|wind walk]]). A specific recharge time is the time that must elapse before a character can cast that particular spell again; he can cast another spell of the same level in the following round if he likes.

###### Metamagic and Specific Recharge Spells

Not only do specific recharge spells use higher slots if metamagic feats have been applied to them, but each +1 to the effective level of the spell doubles the recharge time. For example, a [[rangoric-srd/feats/Silent Spell|silent]] [[rangoric-srd/spells/Charm Person|charm person]] spell takes up a 2nd-level spell slot and has a specific recharge time of 2 hours.

###### Countering and Dispelling

If a spell with a specific recharge time is used to counter or dispel another spell, the specific recharge time does not apply. Instead, treat the spell as a general recharge spell of that level.

For example, if a 5th-level cleric casts [[rangoric-srd/spells/Deeper Darkness|deeper darkness]] to dispel a [[rangoric-srd/spells/Daylight|daylight]] spell, he can cast another 3rd-level spell (including deeper darkness) 1d6+1 rounds later. If he instead casts deeper darkness to darken a passageway, he can’t use deeper darkness again for 24 hours, but his other 3rd-level spells are available to be cast.

**Table: Spell Recharge Times**

| Spell Name                 | Recharge Time |
| -------------------------- | ------------- |
| Acid arrow                 | General       |
| Acid fog                   | General       |
| Acid splash                | General       |
| Aid                        | 5 minutes     |
| Air walk                   | 1 hour        |
| Alarm                      | 4 hours       |
| Align weapon               | 5 minutes     |
| Alter self                 | 4 hours       |
| Analyze dweomer            | General       |
| Animal growth              | General       |
| Animal messenger           | 6 hours       |
| Animal shapes              | 24 hours      |
| Animal trance              | General       |
| Animate dead               | General       |
| Animate objects            | General       |
| Animate plants             | General       |
| Animate rope               | General       |
| Antilife shell             | General       |
| Antimagic field            | General       |
| Antipathy                  | General       |
| Antiplant shell            | General       |
| Arcane eye                 | General       |
| Arcane lock                | 1 hour        |
| Arcane mark                | General       |
| Arcane sight               | 30 minutes    |
| Arcane sight, greater      | 30 minutes    |
| Astral projection          | General       |
| Atonement                  | General       |
| Augury                     | 6 hours       |
| Awaken                     | General       |
| Baleful polymorph          | General       |
| Bane                       | General       |
| Banishment                 | General       |
| Barkskin                   | 1 hour        |
| Bear’s endurance           | 5 minutes     |
| Bear’s endurance, mass     | 30 minutes    |
| Bestow curse               | General       |
| Binding                    | General       |
| Black tentacles            | General       |
| Blade barrier              | General       |
| Blasphemy                  | General       |
| Bless                      | 30 minutes    |
| Bless water                | General       |
| Bless weapon               | 5 minutes     |
| Blight                     | General       |
| Blindness/deafness         | General       |
| Blink                      | General       |
| Blur                       | 5 minutes     |
| Break enchantment          | 1 hour        |
| Bull’s strength            | 5 minutes     |
| Bull’s strength, mass      | 30 minutes    |
| Burning hands              | General       |
| Call lightning             | General       |
| Call lightning storm       | General       |
| Calm animals               | General       |
| Calm emotions              | General       |
| Cat’s grace                | 5 minutes     |
| Cat’s grace, mass          | 30 minutes    |
| Cause fear                 | General       |
| Chain lightning            | General       |
| Changestaff                | 6 hours       |
| Chaos hammer               | General       |
| Charm animal               | 1 hour        |
| Charm monster              | 1 hour        |
| Charm monster, mass        | 1 hour        |
| Charm person               | 1 hour        |
| Chill metal                | General       |
| Chill touch                | General       |
| Circle of death            | General       |
| Clairaudience/clairvoyance | General       |
| Clenched fist              | General       |
| Cloak of chaos             | General       |
| Clone                      | General       |
| Cloudkill                  | General       |
| Color spray                | General       |
| Command                    | General       |
| Command plants             | 1 hour        |
| Command undead             | 1 hour        |
| Command, greater           | General       |
| Commune                    | 6 hours       |
| Commune with nature        | 6 hours       |
| Comprehend languages       | 4 hours       |
| Cone of cold               | General       |
| Confusion                  | General       |
| Confusion, lesser          | General       |
| Consecrate                 | 30 minutes    |
| Contact other plane        | 6 hours       |
| Contagion                  | General       |
| Contingency                | General       |
| Continual flame            | General       |
| Control plants             | 30 minutes    |
| Control undead             | 30 minutes    |
| Control water              | 1 hour        |
| Control weather            | General       |
| Control winds              | 4 hours       |
| Create food and water      | 24 hours      |
| Create greater undead      | General       |
| Create undead              | General       |
| Create water               | 30 minutes    |
| Creeping doom              | General       |
| Crushing despair           | General       |
| Crushing hand              | General       |
| Cure critical wound, mass  | General       |
| Cure critical wounds       | General       |
| Cure light wounds          | General       |
| Cure light wounds, mass    | General       |
| Cure minor wounds          | General       |
| Cure moderate wounds       | General       |
| Cure moderate wounds, mass | General       |
| Cure serious wounds        | General       |
| Cure serious wounds, mass  | General       |
| Curse water                | General       |
| Dancing lights             | General       |
| Darkness                   | 4 hours       |
| Darkvision                 | 6 hours       |
| Daylight                   | 4 hours       |
| Daze                       | General       |
| Daze monster               | General       |
| Death knell                | General       |
| Death ward                 | 5 minutes     |
| Deathwatch                 | 4 hours       |
| Deep slumber               | General       |
| Deeper darkness            | 24 hours      |
| Delay poison               | 6 hours       |
| Delayed blast fireball     | General       |
| Demand                     | 30 minutes    |
| Desecrate                  | 30 minutes    |
| Destruction                | General       |
| Detect animals or plants   | General       |
| Detect chaos               | General       |
| Detect evil                | General       |
| Detect good                | General       |
| Detect law                 | General       |
| Detect magic               | General       |
| Detect poison              | 5 minutes     |
| Detect scrying             | General       |
| Detect secret doors        | General       |
| Detect snares and pits     | General       |
| Detect thoughts            | General       |
| Detect undead              | General       |
| Dictum                     | General       |
| Dimension door             | General       |
| Dimensional anchor         | General       |
| Dimensional lock           | 24 hours      |
| Diminish plants            | 4 hours       |
| Discern lies               | 6 hours       |
| Discern location           | 6 hours       |
| Disguise self              | 4 hours       |
| Disintegrate               | General       |
| Dismissal                  | General       |
| Dispel chaos               | General       |
| Dispel evil                | General       |
| Dispel good                | General       |
| Dispel law                 | General       |
| Dispel magic               | General       |
| Dispel magic, greater      | General       |
| Displacement               | General       |
| Disrupt undead             | General       |
| Disrupting weapon          | 5 minutes     |
| Divination                 | 6 hours       |
| Divine favor               | 5 minutes     |
| Divine power               | 5 minutes     |
| Dominate animal            | General       |
| Dominate monster           | 12 hours      |
| Dominate person            | 12 hours      |
| Doom                       | General       |
| Dream                      | General       |
| Eagle’s splendor           | 5 minutes     |
| Eagle’s splendor, mass     | 30 minutes    |
| Earthquake                 | 12 hours      |
| Elemental swarm            | 1 hour        |
| Endure elements            | 6 hours       |
| Energy drain               | General       |
| Enervation                 | General       |
| Enlarge person             | 5 minutes     |
| Enlarge person, mass       | 30 minutes    |
| Entangle                   | General       |
| Enthrall                   | General       |
| Entropic shield            | 30 minutes    |
| Erase                      | General       |
| Ethereal jaunt             | 30 minutes    |
| Etherealness               | 30 minutes    |
| Expeditious retreat        | 30 minutes    |
| Explosive runes            | 24 hours      |
| Eyebite                    | General       |
| Fabricate                  | 4 hours       |

1.  You can’t recast this spell or prepare another spell in that slot until the subject uses the imbued spell.

**Continued...**

| Faerie fire                      | General             |
| -------------------------------- | ------------------- |
| False life                       | 30 minutes          |
| False vision                     | 24 hours            |
| Fear                             | General             |
| Feather fall                     | General             |
| Feeblemind                       | General             |
| Find the path                    | 4 hours             |
| Find traps                       | 30 minutes          |
| Finger of death                  | General             |
| Fire seeds                       | 1 hour              |
| Fire shield                      | General             |
| Fire storm                       | General             |
| Fire trap                        | 24 hours            |
| Fireball                         | General             |
| Flame arrow                      | General             |
| Flame blade                      | General             |
| Flame strike                     | General             |
| Flaming sphere                   | General             |
| Flare                            | General             |
| Flesh to stone                   | General             |
| Floating disk                    | 6 hours             |
| Fly                              | 5 minutes           |
| Fog cloud                        | General             |
| Forbiddance                      | General             |
| Forcecage                        | General             |
| Forceful hand                    | General             |
| Foresight                        | 1 hour              |
| Fox’s cunning                    | 5 minutes           |
| Fox’s cunning, mass              | 30 minutes          |
| Freedom                          | General             |
| Freedom of movement              | 1 hour              |
| Freezing sphere                  | General             |
| Gaseous form                     | 5 minutes           |
| Gate                             | General             |
| Geas, lesser                     | General             |
| Geas/quest                       | General             |
| Gentle repose                    | General             |
| Ghost sound                      | General             |
| Ghoul touch                      | General             |
| Giant vermin                     | 30 minutes          |
| Glibness                         | 4 hours             |
| Glitterdust                      | General             |
| Globe of invulnerability         | General             |
| Globe of invulnerability, lesser | General             |
| Glyph of warding                 | General             |
| Glyph of warding, greater        | General             |
| Good hope                        | 30 minutes          |
| Goodberry                        | 6 hours             |
| Grasping hand                    | General             |
| Grease                           | General             |
| Guards and wards                 | 24 hours            |
| Guidance                         | 5 minutes           |
| Gust of wind                     | General             |
| Hallow                           | General             |
| Hallucinatory terrain            | 6 hours             |
| Halt undead                      | General             |
| Harm                             | General             |
| Haste                            | General             |
| Heal                             | General             |
| Heal mount                       | General             |
| Heal, mass                       | General             |
| Heat metal                       | General             |
| Helping hand                     | 6 hours             |
| Heroes’ feast                    | 24 hours            |
| Heroism                          | 1 hour              |
| Heroism, greater                 | 30 minutes          |
| Hide from animals                | 4 hours             |
| Hide from undead                 | 4 hours             |
| Hideous laughter                 | General             |
| Hold animal                      | General             |
| Hold monster                     | General             |
| Hold monster, mass               | General             |
| Hold person                      | General             |
| Hold person, mass                | General             |
| Hold portal                      | 5 minutes           |
| Holy aura                        | General             |
| Holy smite                       | General             |
| Holy sword                       | General             |
| Holy word                        | General             |
| Horrid wilting                   | General             |
| Hypnotic pattern                 | General             |
| Hypnotism                        | General             |
| Ice storm                        | General             |
| Identify                         | General             |
| Illusory script                  | General             |
| Illusory wall                    | 24 hours            |
| Imbue with spell ability (1)     | General             |
| Implosion                        | General             |
| Imprisonment                     | General             |
| Incendiary cloud                 | General             |
| Inflict critical wounds          | General             |
| Inflict critical wounds, mass    | General             |
| Inflict light wounds             | General             |
| Inflict light wounds, mass       | General             |
| Inflict minor wounds             | General             |
| Inflict moderate wounds          | General             |
| Inflict moderate wounds, mass    | General             |
| Inflict serious wounds           | General             |
| Inflict serious wounds, mass     | General             |
| Insanity                         | General             |
| Insect plague                    | 5 minutes           |
| Instant summons                  | General             |
| Interposing hand                 | General             |
| Invisibility                     | 5 minutes           |
| Invisibility purge               | 30 minutes          |
| Invisibility, greater            | General             |
| Invisibility, mass               | 30 minutes          |
| Iron body                        | 30 minutes          |
| Ironwood                         | 12 hours            |
| Irresistible dance               | General             |
| Jump                             | 5 minutes           |
| Keen edge                        | 1 hour              |
| Knock                            | 5 minutes           |
| Know direction                   | General             |
| Legend lore                      | General             |
| Levitate                         | 5 minutes           |
| Light                            | 1 hour              |
| Lightning bolt                   | General             |
| Limited wish                     | General             |
| Liveoak                          | 12 hours            |
| Locate creature                  | 4 hours             |
| Locate object                    | 30 minutes          |
| Longstrider                      | 24 hours            |
| Lullaby                          | General             |
| Mage armor                       | 6 hours             |
| Mage hand                        | General             |
| Mage’s disjunction               | General             |
| Mage’s faithful hound            | 6 hours             |
| Mage’s lucubration               | Spell is prohibited |
| Mage’s magnificent mansion       | 6 hours             |
| Mage’s private sanctum           | 24 hours            |
| Magic aura                       | 24 hours            |
| Magic circle against chaos       | 4 hours             |
| Magic circle against evil        | 4 hours             |
| Magic circle against good        | 4 hours             |
| Magic circle against law         | 4 hours             |
| Magic fang                       | 5 minutes           |
| Magic fang, greater              | 6 hours             |
| Magic jar                        | General             |
| Magic missile                    | General             |
| Magic mouth                      | 24 hours            |
| Magic stone                      | 5 minutes           |
| Magic vestment                   | 6 hours             |
| Magic weapon                     | 5 minutes           |
| Magic weapon, greater            | 6 hours             |
| Major creation                   | 12 hours            |
| Major image                      | General             |
| Make whole                       | 6 hours             |
| Mark of justice                  | General             |
| Maze                             | General             |
| Meld into stone                  | 4 hours             |
| Mending                          | 6 hours             |
| Message                          | General             |
| Meteor swarm                     | General             |
| Mind blank                       | 12 hours            |
| Mind fog                         | 6 hours             |
| Minor creation                   | 6 hours             |
| Minor image                      | General             |
| Miracle                          | 12 hours            |
| Mirage arcana                    | General             |
| Mirror image                     | 30 minutes          |
| Misdirection                     | 6 hours             |
| Mislead                          | General             |
| Mnemonic enhancer                | Spell is prohibited |
| Modify memory                    | General             |
| Moment of prescience             | 6 hours             |
| Mount                            | 6 hours             |
| Move earth                       | 1 hour              |
| Neutralize poison                | 1 hour              |
| Nightmare                        | General             |
| Nondetection                     | 6 hours             |
| Obscure object                   | 24 hours            |
| Obscuring mist                   | General             |
| Order’s wrath                    | General             |
| Overland flight                  | 6 hours             |
| Owl’s wisdom                     | 5 minutes           |
| Owl’s wisdom, mass               | 30 minutes          |
| Pass without trace               | 6 hours             |
| Passwall                         | 6 hours             |
| Permanency                       | General             |
| Permanent image                  | 24 hours            |
| Persistent image                 | 30 minutes          |
| Phantasmal killer                | General             |
| Phantom steed                    | 6 hours             |
| Phantom trap                     | 24 hours            |
| Phase door                       | 12 hours            |
| Planar ally                      | 24 hours            |
| Planar ally, greater             | 24 hours            |
| Planar ally, lesser              | 24 hours            |
| Planar binding                   | 24 hours            |
| Planar binding, greater          | 24 hours            |
| Planar binding, lesser           | 24 hours            |
| Plane shift                      | General             |
| Plant growth                     | 24 hours            |
| Poison                           | General             |
| Polar ray                        | General             |
| Polymorph                        | 30 minutes          |
| Polymorph any object             | 12 hours            |
| Power word blind                 | General             |
| Power word kill                  | General             |
| Power word stun                  | General             |
| Prayer                           | 5 minutes           |
| Prestidigitation                 | General             |
| Prismatic sphere                 | General             |
| Prismatic spray                  | General             |
| Prismatic wall                   | General             |
| Produce flame                    | General             |
| Programmed image                 | 12 hours            |
| Project image                    | General             |
| Protection from arrows           | 6 hours             |
| Protection from chaos            | 5 minutes           |
| Protection from energy           | 1 hour              |
| Protection from evil             | 5 minutes           |
| Protection from good             | 5 minutes           |

**Continued...**

| Protection from law         | 5 minutes  |
| --------------------------- | ---------- |
| Protection from spells      | 4 hours    |
| Prying eyes                 | General    |
| Prying eyes, greater        | General    |
| Purify food and drink       | 5 minutes  |
| Pyrotechnics                | General    |
| Quench                      | General    |
| Rage                        | 5 minutes  |
| Rainbow pattern             | General    |
| Raise dead                  | General    |
| Ray of enfeeblement         | General    |
| Ray of exhaustion           | General    |
| Ray of frost                | General    |
| Read magic                  | General    |
| Reduce animal               | 6 hours    |
| Reduce person               | 30 minutes |
| Reduce person, mass         | 30 minutes |
| Refuge                      | General    |
| Regenerate                  | General    |
| Reincarnate                 | General    |
| Remove blindness/deafness   | General    |
| Remove curse                | General    |
| Remove disease              | General    |
| Remove fear                 | General    |
| Remove paralysis            | General    |
| Repel metal or stone        | General    |
| Repel vermin                | 4 hours    |
| Repel wood                  | General    |
| Repulsion                   | General    |
| Resilient sphere            | General    |
| Resist energy               | 1 hour     |
| Resistance                  | 5 minutes  |
| Restoration                 | General    |
| Restoration, greater        | General    |
| Restoration, lesser         | General    |
| Resurrection                | General    |
| Reverse gravity             | General    |
| Righteous might             | 5 minutes  |
| Rope trick                  | 6 hours    |
| Rusting grasp               | 5 minutes  |
| Sanctuary                   | 5 minutes  |
| Scare                       | General    |
| Scintillating pattern       | General    |
| Scorching ray               | General    |
| Screen                      | 24 hours   |
| Scrying                     | General    |
| Scrying, greater            | 6 hours    |
| Sculpt sound                | 6 hours    |
| Searing light               | General    |
| Secret chest                | General    |
| Secret page                 | 12 hours   |
| Secure shelter              | 12 hours   |
| See invisibility            | 4 hours    |
| Seeming                     | 24 hours   |
| Sending                     | General    |
| Sepia snake sigil           | 24 hours   |
| Sequester                   | 24 hours   |
| Shades                      | General    |
| Shadow conjuration          | General    |
| Shadow conjuration, greater | General    |
| Shadow evocation            | General    |
| Shadow evocation, greater   | General    |
| Shadow walk                 | 24 hours   |
| Shambler                    | 24 hours   |
| Shapechange                 | 4 hours    |
| Shatter                     | General    |
| Shield                      | 30 minutes |
| Shield of faith             | 30 minutes |
| Shield of law               | General    |
| Shield other                | 24 hours   |
| Shillelagh                  | 30 minutes |
| Shocking grasp              | General    |
| Shout                       | General    |
| Shout, greater              | General    |
| Shrink item                 | 24 hours   |
| Silence                     | 30 minutes |
| Silent image                | General    |
| Simulacrum                  | General    |
| Slay living                 | General    |
| Sleep                       | General    |
| Sleet storm                 | General    |
| Slow                        | General    |
| Snare                       | 12 hours   |
| Soften earth and stone      | 6 hours    |
| Solid fog                   | General    |
| Song of discord             | General    |
| Soul bind                   | General    |
| Sound burst                 | General    |
| Speak with animals          | 30 minutes |
| Speak with dead             | 30 minutes |
| Speak with plants           | 30 minutes |
| Spectral hand               | 30 minutes |
| Spell immunity              | 1 hour     |
| Spell immunity, greater     | 1 hour     |
| Spell resistance            | 30 minutes |
| Spell turning               | 4 hours    |
| Spellstaff                  | 24 hours   |
| Spider climb                | 1 hour     |
| Spike growth                | 6 hours    |
| Spike stones                | 6 hours    |
| Spiritual weapon            | General    |
| Statue                      | 6 hours    |
| Status                      | 24 hours   |
| Stinking cloud              | General    |
| Stone shape                 | 6 hours    |
| Stone tell                  | 30 minutes |
| Stone to flesh              | General    |
| Stoneskin                   | General    |
| Storm of vengeance          | General    |
| Suggestion                  | 30 minutes |
| Suggestion, mass            | 30 minutes |
| Summon instrument           | General    |
| Summon monster I            | General    |
| Summon monster II           | General    |
| Summon monster III          | General    |
| Summon monster IV           | General    |
| Summon monster V            | General    |
| Summon monster VI           | General    |
| Summon monster VII          | General    |
| Summon monster VIII         | General    |
| Summon monster IX           | General    |
| Summon nature’s ally I      | General    |
| Summon nature’s ally II     | General    |
| Summon nature’s ally III    | General    |
| Summon nature’s ally IV     | General    |
| Summon nature’s ally V      | General    |
| Summon nature’s ally VI     | General    |
| Summon nature’s ally VII    | General    |
| Summon nature’s ally VIII   | General    |
| Summon nature’s ally IX     | General    |
| Summon swarm                | General    |
| Sunbeam                     | General    |
| Sunburst                    | General    |
| Symbol of death             | General    |
| Symbol of fear              | General    |
| Symbol of insanity          | General    |
| Symbol of pain              | General    |
| Symbol of persuasion        | General    |
| Symbol of sleep             | General    |
| Symbol of stunning          | General    |
| Symbol of weakness          | General    |
| Sympathetic vibration       | 12 hours   |
| Sympathy                    | General    |
| Telekinesis                 | General    |
| Telekinetic sphere          | General    |
| Telepathic bond             | 4 hours    |
| Teleport                    | 4 hours    |
| Teleport object             | 4 hours    |
| Teleport, greater           | 4 hours    |
| Teleportation circle        | General    |
| Temporal stasis             | General    |
| Time stop                   | 4 hours    |
| Tiny hut                    | 12 hours   |
| Tongues                     | 1 hour     |
| Touch of fatigue            | General    |
| Touch of idiocy             | General    |
| Transformation              | General    |
| Transmute metal to wood     | 6 hours    |
| Transmute mud to rock       | 6 hours    |
| Transmute rock to mud       | 6 hours    |
| Transport via plants        | 4 hours    |
| Trap the soul               | General    |
| Tree shape                  | 24 hours   |
| Tree stride                 | 24 hours   |
| True resurrection           | General    |
| True seeing                 | General    |
| True strike                 | 5 minutes  |
| Undeath to death            | General    |
| Undetectable alignment      | 24 hours   |
| Unhallow                    | General    |
| Unholy aura                 | General    |
| Unholy blight               | General    |
| Unseen servant              | 6 hours    |
| Vampiric touch              | General    |
| Veil                        | 12 hours   |
| Ventriloquism               | 5 minutes  |
| Virtue                      | 5 minutes  |
| Vision                      | 6 hours    |
| Wail of the banshee         | General    |
| Wall of fire                | General    |
| Wall of force               | General    |
| Wall of ice                 | General    |
| Wall of iron                | 12 hours   |
| Wall of stone               | 12 hours   |
| Wall of thorns              | General    |
| Warp wood                   | 5 minutes  |
| Water breathing             | 4 hours    |
| Water walk                  | 4hours     |
| Waves of exhaustion         | General    |
| Waves of fatigue            | General    |
| Web                         | 5 minutes  |
| Weird                       | General    |
| Whirlwind                   | General    |
| Whispering wind             | 30 minutes |
| Wind walk                   | 24 hours   |
| Wind wall                   | General    |
| Wish                        | General    |
| Wood shape                  | 6 hours    |
| Word of chaos               | General    |
| Word of recall              | General    |
| Zone of silence             | 24 hours   |
| Zone of truth               | 30 minutes |

##### Behind the Curtain: Recharge Magic

This is a high-powered variant, because spellcasters can cast their staple combat and healing spells all day long. This means that the PCs face almost every encounter fully healed, and rarely do spellcasters have their spell lists significantly depleted. Spellcasters may have some specific-recharge utility and protective spells that they won’t be able to cast before every fight, but they always have access to their highest-level combat and healing spells. And it’s those spells that largely comprise a spellcaster’s contribution toward overcoming a given encounter.

As with most high-powered variants, recharge magic works only if every spellcaster in the campaign is using it, including powerful NPC spellcasters. A recharge-variant lich, for example, is a terror for high-level PCs to behold.

As the GM, you have to plan for a party of PCs that can adventure all day long, beginning every fight in a more or less fully rested state. This prospect can be thrilling for players, who no longer have to face the disappointment of a retreat to town just when they’re on the cusp of the adventure’s climax. But when PCs don’t need to retreat to heal and prepare new spells, the GM ends up running more encounters per game session, which means a measure of extra preparation.

As a rule of thumb, a group of four PCs that includes two recharge variant spellcasters can handle encounters of an Encounter Level equal to the characters’ average level +2. The fights will be exciting ones; every room in the dungeon becomes as perilous as a typical adventure’s climax. But the PCs face each one with full resources, so the denizens of the dungeon can’t defeat them through depletion and attrition. If your group likes knock-down, drag-out, set-piece battles, the recharge magic variant lets you fight more of them.

Characters attain new levels faster in terms of both player time at the gaming table and character time in the game world. You can regard this as an additional benefit, or you can reduce experience point awards across the board to compensate.

The recharge magic variant makes spellcasters stronger overall, and it makes nonspellcasters stronger if you assume they’re getting fully healed after every encounter. But in some respects it makes them weaker as well. Even the most powerful wizard can’t cast two [[rangoric-srd/spells/Fireball|fireball]] spells in consecutive rounds with this variant. The [[rangoric-srd/spells/Teleport|teleport]] spell has a specific recharge time of 4 hours, so a character can’t teleport someplace, cast a spell, then teleport away again (unless he uses [[rangoric-srd/spells/Word of Recall|word of recall]] or [[rangoric-srd/spells/Teleport, Greater|greater teleport]] for one of the legs of the journey). Strategies that rely on repeated use of the same spell aren’t viable if the spell in question has a specific recharge time. Depending on the strategy, its chance of success might improve or worsen if a character is relying on a general recharge spell. In short, the recharge variant gives casters a lot more power in exchange for slightly less flexibility with regard to general recharge spells and significantly less flexibility with regard to specific recharge spells.

There’s an obvious way for characters to compensate for the diminished flexibility: scrolls. In general, scrolls become more useful in the recharge variant game world, so they may be more prevalent. Conversely, wands are somewhat less useful, because every spellcaster can crank out his staple spells dozens of times. When a character can cast [[rangoric-srd/spells/Lightning Bolt|lightning bolt]] fifty times in the space of an hour, that fully charged wand of lightning bolt is much less impressive. If you use the recharge magic variant, consider reducing the percentages of minor and medium wands on [[rangoric-srd/magic-items/Magic Scrolls, Staffs, and Wands|Table: Wands]] by 5% and increasing the percentages of minor and medium scrolls by the same amount.

One less obvious change posed by this variant is that lower-level spells retain more importance for high-level spellcasters. With the general recharge rules, even the most potent spellcaster can’t use her best spells more than two or three times in a major fight. Spells two, three, or four levels below the maximum get cast while the spellcaster waits for the heavy artillery to get reloaded.

As the GM, you have to contend with other subtle changes wrought by this variant. Monsters with spell-like abilities usable at will are diminished somewhat, because true spellcasters can cast spells so frequently. Monsters with spell-like abilities aren’t actually weaker — and their Challenge Ratings needn’t go down as a result — but they feel less special and more like spellcasters with a static spell list.

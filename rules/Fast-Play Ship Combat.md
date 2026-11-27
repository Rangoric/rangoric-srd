---
srd-type: "rules"
section: "Rules"
status: draft
pi-review: 2026-11-24
tags: [rangoric, rangoric/rules]
---

# Fast-Play Ship Combat

When ships themselves become a part of a combat, things get more unusual. The following rules are not meant to accurately simulate all of the complexities of ship-to-ship combat, only to provide you with a quick and easy set of rules to resolve such situations when they inevitably arise in a nautical adventure, whether it be a battle between two ships or between a ship and a sea monster.

**Preparation**: Decide what type of ships are involved in the combat (see the Ship Statistics table). Use a large, blank battle mat to represent the waters on which the battle occurs. A single square corresponds to 30 feet of distance. Represent each ship by placing markers that take up the appropriate number of squares (miniature toy ships make great markers and should be available at most hobby stores).

**Starting Combat**: When combat begins, allow the PCs (and important NPC allies) to roll initiative as normal—the ship itself moves and attacks on the captain's initiative result. If any of the ships in the battle rely on sails to move, randomly determine what direction the wind is blowing by rolling 1d8 and following the guidelines for missed [[rangoric-srd/combat/Combat Special Attacks#Throw Splash Weapon|splash weapons]].

**Movement**: On the captain's initiative count, the ship can move its current speed in a single round as a move-equivalent action for the captain (or double its speed as a full-round action), as long as it has its minimum crew complement. The ship can increase or decrease its speed by 30 feet each round, up to its maximum speed. Alternatively, the captain can change direction (up to one side of a square at a time) as a standard action. A ship can only change direction at the start of a turn.

## Attacks

Crew members in excess of the ship's minimum crew requirement can be allocated to man [[rangoric-srd/rules/Siege Engines|siege engines]]. Siege engines attack on the captain's initiative count.

A ship can also attempt to ram a target if it has its minimum crew. To ram a target, the ship must move at least 30 feet and end with its bow in a square adjacent to the target. The ship's captain then makes a [[rangoric-srd/skills/Profession|Profession]] (sailor) check—if this check equals or exceeds the target's AC, the ship hits its target, inflicting damage as indicated on the ship statistics table to the target, as well as minimum damage to the ramming ship. A ship outfitted with an actual ram siege engine inflicts an additional 3d6 points of damage to the target (the ramming vessel suffers no additional damage).

**Sinking**: A ship gains the sinking condition if its hit points are reduced to 0 or fewer. A sinking ship cannot move or attack, and it sinks completely 10 rounds after it gains the sinking condition. Each hit on a sinking ship that inflicts damage reduces the remaining time for it to sink by 1 round per 25 points of damage inflicted. Magic (such as _[[rangoric-srd/spells/Make Whole|make whole]]_) can repair a sinking ship if the ship's hit points are raised above 0, at which point the ship loses the sinking condition. Generally, nonmagical repairs take too long to save a ship from sinking once it begins to go down.

## Ship Statistics

A vast variety of boats and ships exist in the real world, from small rafts and longboats to intimidating galleons and swift galleys. To represent the numerous distinctions of shape and size that exist between water-going vessels, the Ship Statistics table categorizes seven standard ship sizes and their respective statistics. Just as the cultures of the real world have created and adapted hundreds of different types of seafaring vessels, races in fantasy worlds might create their own strange ships. GMs might use or alter these statistics to suit the needs of their creations, and describe such conveyances however they please. All ships have the following traits.

**Ship Type**: This is a general category that lists the ship's basic type.

**AC**: The ship's base Armor Class. To calculate a ship's actual AC, add the captain's [[rangoric-srd/skills/Profession|Profession]] (sailor) modifier to the ship's base AC. Touch attacks against a ship ignore the captain's modifier. A ship is never considered flat-footed.

**hp**: The ship's total hit points. In addition, all ships have a hardness rating based on their construction material (hardness 5 for most wooden ships). At 0 or fewer hit points, a ship gains the sinking condition as described above.

**Base Save**: The ship's base save modifier. All of a ship's defenses (Fortitude, Reflex, and Will) have the same value. To determine a ship's actual defenses, add 10 and the captain's [[rangoric-srd/skills/Profession|Profession]] (sailor) modifier to this base value.

**Maximum Speed**: The ship's maximum tactical speed in combat. An asterisk indicates the ship has sails, and can move at double speed when it moves in the same direction as the wind. A ship with only sails can only move if there is some wind.

**Arms**: The number of siege engines that can be fitted on the ship. A ram uses one of these slots, and only one ram may be fitted to a ship.

**Ram**: The amount of damage the ship inflicts on a successful ramming attack (without a [[rangoric-srd/equipment/siege-engines/Ram, Large|ram siege engine]]).

**Squares**: The number of squares the ship takes up on the battle mat. A ship's width is always considered to be one square.

### Crew

The first number lists the minimum crew complement the ship needs to function normally, excluding those needed to make use of the vessel's weapons. The second value lists the ship's maximum crew plus additional soldiers or passengers. A ship without its minimum crew complement can only move, change speed, change direction, or ram if its captain makes a DC 20 [[rangoric-srd/skills/Profession|Profession]] (sailor) check. Crew in excess of the minimum have no effect on movement, but they can replace fallen crewmembers or man additional weapons.

**Table: Ship Statistics**

| Ship Type    | AC  | hp  | Base Save | Maximum Speed          | Arms | Ram    | Squares | Crew        |
| ------------ | --- | --- | --------- | ---------------------- | ---- | ------ | ------- | ----------- |
| Raft         | 9   | 10  | +0        | 15 feet                | 0    | 1d6    | 1       | 1/4         |
| Rowboat      | 9   | 20  | +2        | 30 feet                | 0    | 2d6+6  | 1       | 1/3         |
| Keelboat     | 8   | 60  | +4        | 30 feet\*              | 1    | 2d6+6  | 2       | 4/15+100    |
| Longship     | 6   | 75  | +5        | 60 feet\*              | 1    | 4d6+18 | 3       | 50/75+100   |
| Sailing ship | 6   | 125 | +6        | 60 feet\* (sails only) | 2    | 3d6+12 | 3       | 20/50+120   |
| Warship      | 2   | 175 | +7        | 60 feet\*              | 3    | 3d6+12 | 4       | 60/80+160   |
| Galley       | 2   | 200 | +8        | 90 feet\*              | 4    | 6d6+24 | 4       | 200/250+200 |

Combat aboard a ship, rather than between ships, is in [[rangoric-srd/rules/Nautical Adventures|Nautical Adventures]].

---
srd-type: "rule"
section: "Rules"
based-on:
  - "[[fantasy srd 3.5/spells/Magic Overview|Magic Overview (3.5)]]"
  - "[[fantasy srd 3.5/psionics/Psionics|Psionics (3.5)]]"
  - "[[fantasy srd 3.5/skills/Concentration|Concentration (3.5)]]"
status: draft
change: new
pi-review: 2026-10-24
tags: [rangoric, rangoric/rule]
---

# Concentration (Check)

Casting a spell, manifesting a power, and using a spell-like or psi-like ability all take concentration. If something interrupts your concentration while you're doing one of these, you must make a Concentration check or lose it: a spell is lost as if you had cast it to no effect, and a power's points are spent without manifesting it. The more distracting the interruption and the higher the level of the spell or power, the higher the DC.

**The Check**: 1d20 + your caster level (for a spell) or manifester level (for a power) + your Constitution modifier. A spell-like or psi-like ability uses its caster or manifester level. A [[rangoric-srd/skills/Meditation|Meditation]] check can be used in its place, against the same DC.

The same checks apply when you are concentrating on or directing an active spell or power (if the check fails, it ends, or the direction fails but it stays active) and when you use a spell-like or psi-like ability (if the check fails, that use is lost). If more than one distraction is present, make a check for each one.

## Distractions

In this table, *level* is the level of the spell you're casting or the power you're manifesting.

| Distraction | DC |
| --- | --- |
| Taking damage | 10 + damage taken + level |
| Taking continuous damage | 10 + half the damage the source last dealt + level |
| Damaged by a spell or power | 10 + damage + level |
| Distracted by a spell or power in some other way | its save DC + level |
| [[rangoric-srd/rules/conditions/Grappled (Condition)\|Grappled]] or [[rangoric-srd/rules/conditions/Pinned (Condition)\|pinned]] | 20 + level |
| Casting a spell with a somatic component while grappled | 50 + level |
| Vigorous motion | 10 + level |
| Violent motion | 15 + level |
| High wind carrying blinding rain or sleet | 5 + level |
| Wind-driven hail, dust, or debris | 10 + level |
| Casting or manifesting on the defensive | 15 + level |
| [[rangoric-srd/rules/Special Abilities and Conditions#^entangled\|Entangled]] | 15 + level |
| Manifesting a power without its display | 15 + level |

**Taking Damage**: The damage counts if it comes between when you start and when you finish (for a spell or power that takes 1 round or more), or if it comes in response to what you're doing, such as an attack of opportunity it provokes or a readied attack. Continuous damage counts as half dealt while you're casting or manifesting. If the last damage dealt was the last the effect could deal, the damage is over and doesn't distract you. Repeated damage doesn't count as continuous.

**Spells and Powers**: If a spell or power that allows no saving throw distracts you, use the DC its save would have if it allowed one. Weather caused by a spell or power works the same way.

**Motion**: Vigorous motion is riding a moving mount, a bouncy wagon ride, a small boat in rough water, being below decks in a storm-tossed ship, or being jostled in a similar way. Violent motion is a galloping horse, a very rough wagon ride, a small boat in rapids or a storm, being on deck in a storm-tossed ship, or being tossed roughly about in a similar way.

**Grappled or Pinned**: Which spells can be cast at all is in the [[rangoric-srd/rules/conditions/Grappled (Condition)|grappled]] and [[rangoric-srd/rules/conditions/Pinned (Condition)|pinned]] conditions, and under Spell Components in [[rangoric-srd/combat/Combat Actions#^spell-components|Combat Actions]].

**On the Defensive**: Casting a spell, manifesting a power, or using a spell-like or psi-like ability on the defensive doesn't provoke attacks of opportunity, but takes this check. Failure loses the spell or power; a spell-like ability counts as used.

**Without a Display**: Why a manifester might leave out a power's display is in [[rangoric-srd/psionics/Power Description Format|Power Description Format]]. If the check fails, the power manifests with its display.

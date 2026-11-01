---
srd-type: "overview"
section: "Actions"
based-on:
  - "[[fantasy srd 3.5/combat/Combat Actions|Combat Actions (3.5)]]"
status: draft
change: new
pi-review: 2026-10-31
tags: [rangoric, rangoric/overview]
---

# Actions

This folder lists the actions a character can take, in or out of combat, with **one note per action**. Each note says what kind of action it is, or how long it takes. It's a place to look things up, like the skill and feat folders.

## What an action note has

```yaml
srd-type: "action"
action: standard          # standard, move, full-round, swift, immediate, free, none, or a time ("1 minute", "1 hour")
skills:                   # the skills that can make the check, if any
  - "[[rangoric-srd/skills/Fieldcraft|Fieldcraft]]"
provokes: true            # whether it provokes an attack of opportunity
tags: [rangoric, rangoric/action]
```

The text says what the action does, what the check is (if there is one), and any special cases.

The [[rangoric-srd/actions/Actions Index|Actions Index]] lists every action with its type, skills and whether it provokes.

## Action types

The action types (standard, move, full-round, swift, immediate and free) are defined in [[rangoric-srd/combat/Combat Actions|Combat Actions]].

## Where an action's rules live

Settled 2026-10-31: **the action note is the one home** for that action's rules. Skill, combat and other notes point to it instead of repeating it. The [[rangoric-srd/actions/First Aid|First Aid]] actions were the first, shared by Fieldcraft and Medicine.

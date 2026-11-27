---
srd-type: "note-rules"
section: "Psionic Powers"
status: draft
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Powers Note Rules

What the notes in `powers` look like. The whole-SRD rules are in the [README](../README.md#note-rules); Sweep and the "Check notes" workflow check both.

## power

| Key                | Required | Values                                                                                                                                                         |
| ------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `srd-type`         | yes      | `power`                                                                                                                                                        |
| `section`          | yes      | `Psionic Powers`                                                                                                                                               |
| `discipline`       | yes      | `Telepathy`, `Psychometabolism`, `Clairsentience`, `Psychoportation`, `Psychokinesis`, `Metacreativity`                                                        |
| `level`            | yes      | list of `text`                                                                                                                                                 |
| `power-points`     | yes      | `text`                                                                                                                                                         |
| `range`            | no       | `text`                                                                                                                                                         |
| `duration`         | no       | `text`                                                                                                                                                         |
| `manifesting-time` | no       | `text`                                                                                                                                                         |
| `display`          | no       | `text`                                                                                                                                                         |
| `target`           | no       | `text`                                                                                                                                                         |
| `saving-throw`     | no       | `text`                                                                                                                                                         |
| `power-resistance` | no       | `text`                                                                                                                                                         |
| `descriptor`       | no       | list of `Acid`, `Death`, `Electricity`, `Evil`, `Fire`, `Force`, `Good`, `Language-Dependent`, `Light`, `Mind-Affecting`, `See text`, `Sonic`, `Teleportation` |
| `subdiscipline`    | no       | `Creation`, `Compulsion`, `Teleportation`, `Healing`, `Charm`, `Scrying`, `Scrying; see text`                                                                  |
| `area`             | no       | `text`                                                                                                                                                         |
| `effect`           | no       | `text`                                                                                                                                                         |

Headings, in order:

1. `# (name)`

## overview

| Key        | Required | Values           |
| ---------- | -------- | ---------------- |
| `srd-type` | yes      | `overview`       |
| `section`  | yes      | `Psionic Powers` |

## Failing notes

![[rangoric-srd/powers/Psionic Powers Index.base#Failing]]

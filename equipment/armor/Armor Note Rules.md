---
srd-type: "note-rules"
section: "Equipment"
status: draft
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Armor Note Rules

What the notes in `equipment/armor` look like. Expands on [[rangoric-srd/equipment/Equipment Note Rules|Equipment Note Rules]].

## armor

| Key                | Required | Values                                        |
| ------------------ | -------- | --------------------------------------------- |
| `srd-type`         | yes      | `armor`                                       |
| `section`          | yes      | `Equipment`                                   |
| `table-name`       | yes      | `text`                                        |
| `category`         | yes      | `light`, `medium`, `heavy`, `extra`, `shield` |
| `cost-gp`          | yes      | `number`                                      |
| `weight-lb`        | yes      | `number`                                      |
| `check-penalty`    | no       |                                               |
| `spell-failure`    | no       | `number`                                      |
| `armor-bonus`      | no       | `number`                                      |
| `max-dex`          | no       | `number`                                      |
| `speed-30`         | no       | `number`                                      |
| `speed-20`         | no       | `number`                                      |
| `dr-armor-bonus`   | no       | `number`                                      |
| `damage-reduction` | no       | `1/–`, `2/–`, `3/–`, `none`, `4/–`, `6/–`     |

Headings, in order:

1. `# (name)`

## Failing notes

![[rangoric-srd/equipment/Equipment Index.base#Failing armor]]

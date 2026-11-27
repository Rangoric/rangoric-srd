---
srd-type: "note-rules"
section: "Equipment"
status: draft
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Weapons Note Rules

What the notes in `equipment/weapons` look like. Expands on [[rangoric-srd/equipment/Equipment Note Rules|Equipment Note Rules]].

## weapon

| Key             | Required | Values                                                                              |
| --------------- | -------- | ----------------------------------------------------------------------------------- |
| `srd-type`      | yes      | `weapon`                                                                            |
| `section`       | yes      | `Equipment`                                                                         |
| `table-name`    | yes      | `text`                                                                              |
| `category`      | yes      | `two-handed`, `ranged`, `light`, `one-handed`, `ammunition`, `unarmed`, `accessory` |
| `cost-gp`       | no       |                                                                                     |
| `weight-lb`     | no       |                                                                                     |
| `proficiency`   | no       | `exotic`, `martial`, `simple`                                                       |
| `damage-type`   | no       | `text`                                                                              |
| `damage-medium` | no       | `text`                                                                              |
| `critical`      | no       | `text`                                                                              |
| `damage-small`  | no       | `text`                                                                              |
| `special`       | no       | list of `text`                                                                      |
| `range-ft`      | no       | `number`                                                                            |

Headings, in order:

1. `# (name)`

## Failing notes

![[rangoric-srd/equipment/Equipment Index.base#Failing weapons]]

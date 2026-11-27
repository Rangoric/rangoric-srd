---
srd-type: "note-rules"
section: "Equipment"
status: draft
change: new
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Siege Engines Note Rules

What the notes in `equipment/siege-engines` look like. Expands on [[rangoric-srd/equipment/Equipment Note Rules|Equipment Note Rules]].

## siege-engine

| Key            | Required | Values                                                                     |
| -------------- | -------- | -------------------------------------------------------------------------- |
| `srd-type`     | yes      | `siege-engine`                                                             |
| `section`      | yes      | `Equipment`                                                                |
| `table-name`   | yes      | `text`                                                                     |
| `category`     | yes      | `Close Assault`, `Indirect-Fire`, `Direct-Fire`                            |
| `price`        | yes      | `text`                                                                     |
| `price-gp`     | yes      | `number`                                                                   |
| `size`         | no       | `Huge`, `Gargantuan`, `Large`, `Colossal`                                  |
| `hp`           | no       |                                                                            |
| `crew`         | no       | `number`                                                                   |
| `speed`        | no       | `0 ft.`, `15 ft.`, `10 ft.`, `as crew speed`, `Special`                    |
| `hardness`     | no       | `number`                                                                   |
| `damage`       | no       | `text`                                                                     |
| `critical`     | no       | `×2`, `×4`, `×3`, `19–20/×2`, `—`                                          |
| `damage-type`  | no       | `Bludgeoning`, `Bludgeoning and piercing`, `Fire`, `Piercing`              |
| `range`        | no       | `text`                                                                     |
| `aim`          | no       | `number`                                                                   |
| `load`         | no       | `number`                                                                   |
| `ammunition`   | no       | `text`                                                                     |
| `targeting-dc` | no       | `number`                                                                   |
| `misfire`      | no       | `1 (20 ft.)`, `1 (30 ft.)`, `1–2 (10 ft.)`, `1–2 (20 ft.)`, `1–2 (30 ft.)` |
| `firearm`      | no       | `siege`                                                                    |

Headings, in order:

1. `# (name)`

## siege-ammunition

| Key          | Required | Values                                                                                              |
| ------------ | -------- | --------------------------------------------------------------------------------------------------- |
| `srd-type`   | yes      | `siege-ammunition`                                                                                  |
| `section`    | yes      | `Equipment`                                                                                         |
| `table-name` | yes      | `Alchemist's fire`, `Blast shot`, `Bomb`, `Chain shot`, `Liquid ice`, `Plague bundle`, `Smoke shot` |
| `category`   | yes      | `Ammunition`                                                                                        |
| `price`      | yes      | `200 gp`, `250 gp`, `30 gp`, `400 gp`, `50 gp`, `600 gp`, `80 gp`                                   |
| `price-gp`   | yes      | `number`                                                                                            |
| `weight`     | yes      | `20 lb.`, `30 lb.`, `10 lb.`, `25 lb.`                                                              |
| `used-with`  | no       | list of `text`                                                                                      |

Headings, in order:

1. `# (name)`

## Failing notes

![[rangoric-srd/equipment/Equipment Index.base#Failing siege-engines]]

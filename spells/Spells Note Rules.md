---
srd-type: "note-rules"
section: "Spells"
status: draft
change: new
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Spells Note Rules

What the notes in `spells` look like. The whole-SRD rules are in the [README](../README.md#note-rules); Sweep and the "Check notes" workflow check both.

## spell

| Key                | Required | Values                                                                                                                        |
| ------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `srd-type`         | yes      | `spell`                                                                                                                       |
| `section`          | yes      | `Spells`                                                                                                                      |
| `school`           | yes      | `Abjuration`, `Conjuration`, `Divination`, `Enchantment`, `Evocation`, `Illusion`, `Necromancy`, `Transmutation`, `Universal` |
| `subschool`        | no       | `text`                                                                                                                        |
| `descriptor`       | no       | list of `text`                                                                                                                |
| `level`            | no       | list of `text`                                                                                                                |
| `components`       | no       | list of `text`                                                                                                                |
| `casting-time`     | no       | `text`                                                                                                                        |
| `range`            | no       | `text`                                                                                                                        |
| `target`           | no       | `text`                                                                                                                        |
| `duration`         | no       | `text`                                                                                                                        |
| `saving-throw`     | no       | `text`                                                                                                                        |
| `spell-resistance` | no       | `text`                                                                                                                        |
| `book`             | no       | `text`                                                                                                                        |

Headings, in order:

1. `# (name)`

## overview

| Key        | Required | Values     |
| ---------- | -------- | ---------- |
| `srd-type` | yes      | `overview` |
| `section`  | yes      | `Spells`   |
| `book`     | no       |            |

## Failing notes

![[rangoric-srd/spells/Spells Index.base#Failing]]

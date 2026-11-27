---
srd-type: "note-rules"
section: "Equipment"
status: draft
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Alchemical Items Note Rules

What the notes in `equipment/alchemical-items` look like. Expands on [[rangoric-srd/equipment/Equipment Note Rules|Equipment Note Rules]].

## alchemical-item

| Key              | Required | Values                                                                   |
| ---------------- | -------- | ------------------------------------------------------------------------ |
| `srd-type`       | yes      | `alchemical-item`                                                        |
| `section`        | yes      | `Equipment`                                                              |
| `category`       | yes      | list of `text`                                                           |
| `magical`        | yes      | `true`, `false`                                                          |
| `price`          | no       | `text`                                                                   |
| `dc`             | no       | `text`                                                                   |
| `classification` | no       | `text`                                                                   |
| `cl`             | no       | `text`                                                                   |
| `prerequisites`  | no       | list of `text`                                                           |
| `aura`           | no       | `text`                                                                   |
| `weight`         | no       | `1 lb.`, `1/2 lb.`, `2 lb.`, `5 lb.`, `10 lb.`, `100 lb.`, `3 lbs.`, `—` |

Headings, in order:

1. `# (name)`

## overview

| Key        | Required | Values      |
| ---------- | -------- | ----------- |
| `srd-type` | yes      | `overview`  |
| `section`  | yes      | `Equipment` |

Headings, in order:

1. `# (name)`

## Failing notes

![[rangoric-srd/equipment/Equipment Index.base#Failing alchemical-items]]

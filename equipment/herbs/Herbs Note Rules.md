---
srd-type: "note-rules"
section: "Equipment"
status: draft
change: new
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Herbs Note Rules

What the notes in `equipment/herbs` look like. Expands on [[rangoric-srd/equipment/Equipment Note Rules|Equipment Note Rules]].

## herb

| Key               | Required | Values                   |
| ----------------- | -------- | ------------------------ |
| `srd-type`        | yes      | `herb`                   |
| `section`         | yes      | `Equipment`              |
| `book`            | yes      | `text`                   |
| `rarity`          | yes      | `text`                   |
| `environment`     | yes      | `text`                   |
| `harvest`         | yes      | `text`                   |
| `cost`            | yes      | `text`                   |
| `affliction-type` | no       | `poison`                 |
| `delivery`        | no       | `ingested`               |
| `save`            | no       | `text`                   |
| `save-dc`         | no       | `number`                 |
| `effect`          | no       | `text`                   |
| `frequency`       | no       | `1/minute for 2 minutes` |

Headings, in order:

1. `# (name)`

## overview

| Key        | Required | Values      |
| ---------- | -------- | ----------- |
| `srd-type` | yes      | `overview`  |
| `section`  | yes      | `Equipment` |
| `book`     | yes      | `text`      |

Headings, in order:

1. `# (name)`

## Failing notes

![[rangoric-srd/equipment/Equipment Index.base#Failing herbs]]

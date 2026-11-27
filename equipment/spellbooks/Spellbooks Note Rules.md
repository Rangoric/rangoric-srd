---
srd-type: "note-rules"
section: "Equipment"
status: draft
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Spellbooks Note Rules

What the notes in `equipment/spellbooks` look like. Expands on [[rangoric-srd/equipment/Equipment Note Rules|Equipment Note Rules]].

## spellbook

| Key                 | Required | Values                      |
| ------------------- | -------- | --------------------------- |
| `srd-type`          | yes      | `spellbook`                 |
| `section`           | yes      | `Equipment`                 |
| `book-type`         | yes      | `spellbook`, `formula book` |
| `caster-level`      | yes      | `number`                    |
| `role`              | yes      | `text`                      |
| `price`             | yes      | `text`                      |
| `price-with-ritual` | no       | `text`                      |

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

![[rangoric-srd/equipment/Equipment Index.base#Failing spellbooks]]

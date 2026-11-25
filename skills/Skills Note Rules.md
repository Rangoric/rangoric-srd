---
srd-type: "note-rules"
section: "Skills"
status: draft
change: new
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Skills Note Rules

What the notes in `skills` look like. The whole-SRD rules are in the [README](../README.md#note-rules); Sweep and the "Check notes" workflow check both.

## skill

| Key                   | Required | Values                            |
| --------------------- | -------- | --------------------------------- |
| `srd-type`            | yes      | `skill`                           |
| `section`             | yes      | `Skills`                          |
| `key-ability`         | yes      | `Int`, `Cha`, `Dex`, `Wis`, `Str` |
| `book`                | no       | `text`                            |
| `trained-only`        | no       | `true`, `false`                   |
| `armor-check-penalty` | no       | `true`, `false`                   |

Headings, in order:

1. `# (name)`

## overview

| Key        | Required | Values     |
| ---------- | -------- | ---------- |
| `srd-type` | yes      | `overview` |
| `section`  | yes      | `Skills`   |

## Failing notes

![[rangoric-srd/skills/Skills Index.base#Failing]]

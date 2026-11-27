---
srd-type: "note-rules"
section: "Races"
status: draft
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Races Note Rules

What the notes in `races` look like. The whole-SRD rules are in the [README](../README.md#note-rules); Sweep and the "Check notes" workflow check both.

## class-bonus

| Key        | Required | Values         |
| ---------- | -------- | -------------- |
| `srd-type` | yes      | `class-bonus`  |
| `section`  | yes      | `Races`        |
| `race`     | yes      | `text`         |
| `class`    | yes      | list of `text` |

Headings, in order:

1. `# (name)`

## racial-trait

| Key           | Required | Values         |
| ------------- | -------- | -------------- |
| `srd-type`    | yes      | `racial-trait` |
| `section`     | yes      | `Races`        |
| `race`        | yes      | `text`         |
| `replaces`    | yes      | `text`         |
| `race-points` | no       | `number`       |

Headings, in order:

1. `# (name)`

## race

| Key           | Required | Values   |
| ------------- | -------- | -------- |
| `srd-type`    | yes      | `race`   |
| `section`     | yes      | `Races`  |
| `race-points` | no       | `number` |

## aspect-of-nature

| Key        | Required | Values             |
| ---------- | -------- | ------------------ |
| `srd-type` | yes      | `aspect-of-nature` |
| `section`  | yes      | `Races`            |

Headings, in order:

1. `# (name)`

## prestige-race

| Key        | Required | Values          |
| ---------- | -------- | --------------- |
| `srd-type` | yes      | `prestige-race` |
| `section`  | yes      | `Races`         |

Headings, in order:

1. `# (name)`

## rules

| Key        | Required | Values  |
| ---------- | -------- | ------- |
| `srd-type` | yes      | `rules` |
| `section`  | yes      | `Races` |

Headings, in order:

1. `# (name)`

## overview

| Key        | Required | Values     |
| ---------- | -------- | ---------- |
| `srd-type` | yes      | `overview` |
| `section`  | yes      | `Races`    |

## Failing notes

![[rangoric-srd/races/Races Index.base#Failing]]

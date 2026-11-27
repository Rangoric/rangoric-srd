---
srd-type: "note-rules"
section: "Monsters"
status: draft
change: new
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Monsters Note Rules

What the notes in `monsters` look like. The whole-SRD rules are in the [README](../README.md#note-rules); Sweep and the "Check notes" workflow check both.

## monster

| Key                 | Required | Values         |
| ------------------- | -------- | -------------- |
| `srd-type`          | yes      | `monster`      |
| `section`           | yes      | `Monsters`     |
| `creature-type`     | no       | `text`         |
| `organization`      | no       | `text`         |
| `advancement`       | no       | `text`         |
| `challenge-rating`  | no       |                |
| `environment`       | no       | `text`         |
| `size`              | no       | `text`         |
| `armor-class`       | no       | `text`         |
| `hit-dice`          | no       | `text`         |
| `initiative`        | no       | `text`         |
| `speed`             | no       | `text`         |
| `space-reach`       | no       | `text`         |
| `special-attacks`   | no       | `text`         |
| `special-qualities` | no       | `text`         |
| `defenses`          | no       | `text`         |
| `abilities`         | no       | `text`         |
| `skills`            | no       | `text`         |
| `attack`            | no       | `text`         |
| `full-attack`       | no       | `text`         |
| `base-attack`       | no       | `text`         |
| `cmb`               | no       | `text`         |
| `cmd`               | no       | `text`         |
| `treasure`          | no       | `text`         |
| `skill-ranks`       | no       | `text`         |
| `feats`             | no       | `text`         |
| `alignment`         | no       | `text`         |
| `level-adjustment`  | no       | `text`         |
| `group`             | no       | `text`         |
| `subtypes`          | no       | list of `text` |

Headings, in order:

1. `# (name)`

- Regeneration names what stops it, as [[rangoric-srd/monsters/abilities/Regeneration|Regeneration]] says: “regeneration 5 (acid or fire)”.

## monster-ability

| Key            | Required | Values            |
| -------------- | -------- | ----------------- |
| `srd-type`     | yes      | `monster-ability` |
| `section`      | yes      | `Monsters`        |
| `ability-type` | yes      | list of `text`    |
| `kind`         | yes      | list of `text`    |

Headings, in order:

1. `# (name)`

## overview

| Key        | Required | Values     |
| ---------- | -------- | ---------- |
| `srd-type` | yes      | `overview` |
| `section`  | yes      | `Monsters` |

## Failing notes

![[rangoric-srd/monsters/Monsters Index.base#Failing]]

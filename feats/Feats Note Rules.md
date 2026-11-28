---
srd-type: "note-rules"
section: "Feats"
status: draft
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Feats Note Rules

What the notes in `feats` look like. The whole-SRD rules are in the [README](../README.md#note-rules); Sweep and the "Check notes" workflow check both.

## feat

| Key             | Required | Values                                  |
| --------------- | -------- | --------------------------------------- |
| `srd-type`      | yes      | `feat`                                  |
| `section`       | yes      | `Feats`                                 |
| `prerequisites` | no       | `text`                                  |
| `feat-type`     | no       | `General`, `Metamagic`, `Item Creation` |

Headings, in order:

1. `# (name)`

## overview

| Key        | Required | Values     |
| ---------- | -------- | ---------- |
| `srd-type` | yes      | `overview` |
| `section`  | yes      | `Feats`    |

A feat overview lists feats by embedding a [[rangoric-srd/feats/Feats Index.base|Feats Index]] view, not by a written list. A list of a few feats that share no tag may stay written.

## Failing notes

![[rangoric-srd/feats/Feats Index.base#Failing]]

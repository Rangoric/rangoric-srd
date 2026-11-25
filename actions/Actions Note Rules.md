---
srd-type: "note-rules"
section: "Actions"
status: draft
change: new
pi-review: 2026-11-25
tags: [rangoric, rangoric/note-rules]
---

# Actions Note Rules

What the notes in `actions` look like. The whole-SRD rules are in the [README](../README.md#note-rules); Sweep and the "Check notes" workflow check both. [[rangoric-srd/actions/Actions|Actions]] describes the folder.

## action

| Key        | Required | Values                                                                                         |
| ---------- | -------- | ---------------------------------------------------------------------------------------------- |
| `srd-type` | yes      | `action`                                                                                       |
| `section`  | yes      | `Actions`                                                                                      |
| `action`   | yes      | `standard`, `move`, `full-round`, `swift`, `immediate`, `free`, `none`, or a time ("1 minute") |
| `skills`   | no       | list of links to skills                                                                        |
| `provokes` | yes      | `true`, `false`                                                                                |

Headings, in order:

1. `# (name)`

- The text says what the action does, what the check is (if there is one), and any special cases.

## overview

| Key        | Required | Values     |
| ---------- | -------- | ---------- |
| `srd-type` | yes      | `overview` |
| `section`  | yes      | `Actions`  |

## Failing notes

![[rangoric-srd/actions/Actions Index.base#Failing]]

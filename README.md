# Rangoric SRD

Wilson's combined rules for a series of games: one version of each rule, drawn from Open Game Content and adjusted
piecemeal.
It's an Obsidian vault folder; start at [Rangoric SRD.md](Rangoric%20SRD.md).

The content is Open Game Content under the Open Game License 1.0a, except what is declared Product Identity. The
license, each source's Section 15 notice and the Product Identity declarations are in [legal/Legal.md](legal/Legal.md)
and [legal/Source Product Identity.md](legal/Source%20Product%20Identity.md).

Changes arrive as pull requests, one per batch of work, each reviewed before it's merged. Every departure from the
source rules is listed in the [Changelog](Changelog.md).

## Note rules

Every note has these, except the root notes (this README, the Changelog, Rangoric SRD and the Tag Register) and
`legal/`. What each key means is in [Rangoric SRD's Properties](Rangoric%20SRD.md#properties). Each folder's
`<Folder> Note Rules.md` says what its own notes look like, and the "Check notes" workflow checks both. A note that
doesn't meet them yet is marked `sweep: failing`, with one line per problem under `sweep-issues`, and its folder's
Note Rules note lists it.

| Key            | Required                    | Values                                             |
| -------------- | --------------------------- | -------------------------------------------------- |
| `srd-type`     | yes                         | `text`                                             |
| `status`       | yes                         | `base`, `draft`, `playtest`, `settled`, `replaced` |
| `change`       | yes                         | `copied`, `modified`, `new`                        |
| `pi-review`    | yes                         |                                                    |
| `tags`         | yes                         | list including `rangoric` and `rangoric/*`         |
| `based-on`     | when `change` is not `new`  |                                                    |
| `replaced-by`  | when `status` is `replaced` |                                                    |
| `saving-throw` | never                       |                                                    |
| `saves`        | never                       |                                                    |
| `save`         | never                       |                                                    |
| `save-dc`      | never                       |                                                    |
| `book`         | never                       |                                                    |
| `page`         | never                       |                                                    |

Defenses replace saving throws ([Saving Throws](rules/Saving%20Throws.md)), so no note has the keys marked never, and no
note says "save DC", "DC 15 Reflex save", "Reflex DC 15", "Reflex save for half" or "makes a saving throw": an
effect attacks a defense instead. Saving Throws itself and `unearthed-arcana/` are excepted; base save progressions
("good Fortitude saves") and a creature's own "Reflex check (1d20 + Reflex save bonus)" are fine.

Source books aren't named in an SRD note, in its text or its frontmatter; `based-on` links are the trace back to
the sources. Legal, the Changelog and the sources table in Rangoric SRD are the exceptions.

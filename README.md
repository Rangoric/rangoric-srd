# Rangoric SRD

Wilson's combined rules for a series of games: one version of each rule, starting from the whole 3.5 System
Reference Document and adjusted piecemeal from Pathfinder, the Modern and Starfinder SRDs and other Open Game Content.
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

| Key           | Required                    | Values                                             |
| ------------- | --------------------------- | -------------------------------------------------- |
| `srd-type`    | yes                         | `text`                                             |
| `status`      | yes                         | `base`, `draft`, `playtest`, `settled`, `replaced` |
| `change`      | yes                         | `copied`, `modified`, `new`                        |
| `pi-review`   | yes                         |                                                    |
| `tags`        | yes                         | list including `rangoric` and `rangoric/*`         |
| `based-on`    | when `change` is not `new`  |                                                    |
| `replaced-by` | when `status` is `replaced` |                                                    |

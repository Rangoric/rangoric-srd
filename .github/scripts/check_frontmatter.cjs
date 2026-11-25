// Parse every note's frontmatter the way the website does, and check the keys it reads.
//
//   NODE_PATH=<folder with gray-matter and js-yaml> node .github/scripts/check_frontmatter.cjs [root]
//
// The website (rangoric-srd-website, quartz/plugins/builtins/frontmatter.ts) reads frontmatter with gray-matter and
// js-yaml's JSON schema; the "Check notes" workflow installs the versions in the website's package-lock.json
// (gray-matter 4.0.3, js-yaml 4.3.2; keep them matching). Checked, as the website reads them:
// - the frontmatter loads, and is a set of keys (not a list or a single value);
// - title is text; tags and aliases (and tag, alias, cssclasses) are a list of text or numbers, or text;
// - permalink is text and no two notes share one;
// - the date keys (date, created, modified, lastmod, updated, last-modified, published, publishDate) parse as dates.
// Exit 1 on a problem. Note Rules plan, NR 1 (2026-11-25).
const fs = require("fs")
const path = require("path")
const matter = require("gray-matter")
const yaml = require("js-yaml")

const root = process.argv[2] || "."
const problems = []
const permalinks = new Map()
const refuse = () => {
  throw new Error("JavaScript frontmatter is not supported")
}
const DATES = ["date", "created", "modified", "lastmod", "updated", "last-modified", "published", "publishDate"]
const LISTS = ["tags", "tag", "aliases", "alias", "cssclasses", "cssclass"]

function walk(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.name.startsWith(".")) continue
    const p = path.join(dir, e.name)
    if (e.isDirectory()) walk(p)
    else if (e.name.endsWith(".md")) check(p)
  }
}

function check(p) {
  const rel = path.relative(root, p).split(path.sep).join("/")
  let data
  try {
    data = matter(fs.readFileSync(p), {
      language: "yaml",
      engines: {
        yaml: (s) => yaml.load(s, { schema: yaml.JSON_SCHEMA }),
        javascript: refuse,
        js: refuse,
      },
    }).data
  } catch (e) {
    problems.push(`${rel}: frontmatter doesn't load on the website: ${String(e.message).split("\n")[0]}`)
    return
  }
  if (data === null || typeof data !== "object" || Array.isArray(data)) {
    problems.push(`${rel}: frontmatter is not a set of keys`)
    return
  }
  if (data.title != null && typeof data.title !== "string") problems.push(`${rel}: title is not text`)
  for (const k of LISTS) {
    const v = data[k]
    if (v == null || typeof v === "string") continue
    if (!Array.isArray(v) || v.some((x) => typeof x !== "string" && typeof x !== "number"))
      problems.push(`${rel}: ${k} is not a list of text`)
  }
  if (data.permalink != null) {
    if (typeof data.permalink !== "string") problems.push(`${rel}: permalink is not text`)
    else if (permalinks.has(data.permalink))
      problems.push(`${rel}: permalink ${data.permalink} is also ${permalinks.get(data.permalink)}'s`)
    else permalinks.set(data.permalink, rel)
  }
  for (const k of DATES) {
    const v = data[k]
    if (v == null) continue
    if ((typeof v !== "string" && typeof v !== "number") || isNaN(new Date(v).getTime()))
      problems.push(`${rel}: ${k} is not a date: ${JSON.stringify(v)}`)
  }
}

walk(root)
for (const p of problems) console.log(`::error::${p}`)
console.log(`${problems.length} problem(s) in the website's reading of frontmatter`)
process.exit(problems.length ? 1 : 0)

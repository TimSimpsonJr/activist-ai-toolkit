---
name: blog-writing
description: This skill should be used when the user asks to "write a blog post", "draft a blog post", "create a blog post from research", "turn research into a blog post", "publish research as a blog post", "write an article from my notes", "draft an article about [topic]", "write a post from my research", or mentions writing blog content from Obsidian vault notes or research materials.
---

# Blog Writing from Obsidian Vault Research

Turn Obsidian vault research into well-sourced, voice-matched blog posts. Read voice guidelines from a project-specific `voice-dna.md` file. Output framework-compatible markdown.

## Project Configuration

The skill expects these settings defined in the project's `CLAUDE.md` or a `.obsidian-publisher.md` config file at the repo root:

| Setting | Description | Example |
|---------|-------------|---------|
| `voice-dna` | Path to voice-dna.md | `~/.claude/voice-dna.md` |
| `vault-path` | Path to Obsidian vault or research directory | `~/Documents/My Vault/Research` |
| `framework` | Blog framework (astro, hugo, generic) | `astro` |
| `output-path` | Where to write blog post files | `src/content/blog/` |
| `audience` | Target audience description | `SC residents, non-partisan` |
| `framing` | `personal` (first-person "I") or `org` ("we") | `org` |
| `talking-points` | Path to messaging framework (optional) | `Research/Talking Points.md` |

If settings are missing, ask the user before proceeding.

## Workflow

### 1. Load Configuration

Read project config to find voice-dna.md path, vault location, framework, audience, and framing. Read `voice-dna.md` fresh every time (never rely on prior memory of its contents). Internalize all writing rules, formatting rules, and banned phrases.

### 2. Gather Source Material

Search the Obsidian vault for relevant research notes using Glob and Grep. Follow `[[wikilinks]]` between notes to build a complete picture. Use the vault scanner script at `${CLAUDE_PLUGIN_ROOT}/skills/blog-writing/scripts/scan-vault.py` to index available research by tag if the vault is large.

Key vault navigation patterns:
- Search by frontmatter tags: `tags: [research, tactical-research]`
- Follow wikilinks: `[[Note Title]]` or `[[Full Title|display name]]`
- Check related notes listed in note headers (`**Related:**` fields)
- Look for index notes prefixed with `_` (e.g., `_Campaign Index.md`)

### 3. Verify Sources

Cross-reference facts across multiple vault notes. Every factual claim must trace to a primary source (URL, court document, public record, official statement). Flag any claims without sources with a `<!-- TODO: source needed -->` comment. See `references/source-verification.md` for detailed guidance.

### 4. Draft the Post

Structure the post following the patterns in `references/post-structure.md`:

- **Hook**: Open with a concrete fact, incident, or quote. Not an abstract claim. 1-3 sentences.
- **Body**: 1200-2000 words. Short paragraphs (1-3 sentences). Inline citations where facts appear.
- **Sources section**: Full URLs at the bottom.
- **CTA** (optional): Soft link to action tool or related content at the end. Not the point of the post.

Apply framing from config: first-person ("I") for personal, "we" for organizational. If a talking points document is configured, filter topic selection and framing through it.

### 5. Voice Review

Self-review the draft against voice-dna.md:
- Check for every banned phrase (AI language, dead transitions, engagement bait, the "Not X. This is Y." pattern)
- Verify no em dashes (use commas, periods, colons, semicolons, or parentheses)
- Confirm short paragraphs (1-3 sentences max)
- Check numbers are digits, contractions are used naturally
- Verify bold is used sparingly (1-2 key moments per section)
- Confirm varied sentence length (mix short punchy lines with longer ones)

Fix all violations before presenting the draft.

### 6. Output

Generate framework-compatible markdown with correct frontmatter. Validate frontmatter against the target framework's schema using `${CLAUDE_PLUGIN_ROOT}/skills/blog-writing/scripts/validate-frontmatter.py`. Place the file at the configured output path.

## Additional Resources

### Reference Files

- **`references/post-structure.md`** — Detailed post anatomy, frontmatter schemas for Astro/Hugo/generic, structural patterns (investigative, narrative, rebuttal)
- **`references/source-verification.md`** — Vault navigation, cross-referencing, citation format, handling gaps

### Scripts

- **`scripts/scan-vault.py`** — Index vault research notes by tag and topic for quick discovery. Run: `python ${CLAUDE_PLUGIN_ROOT}/skills/blog-writing/scripts/scan-vault.py <vault-path>`
- **`scripts/validate-frontmatter.py`** — Validate blog post frontmatter against framework schema. Run: `python ${CLAUDE_PLUGIN_ROOT}/skills/blog-writing/scripts/validate-frontmatter.py <post-path> --framework astro`

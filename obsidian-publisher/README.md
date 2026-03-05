# obsidian-publisher

Claude Code plugin that turns Obsidian vault research into blog posts and coordinated social media content.

## Skills

### blog-writing

Vault-to-blog-post pipeline. Reads research notes from an Obsidian vault, cross-references sources, drafts a post matching your voice guidelines, and outputs framework-compatible markdown.

Includes utility scripts:
- `scan-vault.py` — Index vault notes by tag and topic
- `validate-frontmatter.py` — Validate post frontmatter against Astro/Hugo/generic schemas

### social-media

Blog-to-social pipeline. Takes a finished blog post and generates tailored content for LinkedIn, X/Twitter, and Facebook. Each platform gets its own angle, not a copy-paste.

## Configuration

Add a `.obsidian-publisher.md` file at your repo root, or add these settings to your project's `CLAUDE.md`:

```yaml
# Obsidian Publisher Settings
voice-dna: ~/.claude/voice-dna.md
vault-path: ~/Documents/My Vault/Research
framework: astro
output-path: src/content/blog/
audience: SC residents, non-partisan
framing: org
platforms: [linkedin, twitter, facebook]
talking-points: Research/Talking Points.md
```

| Setting | Required | Description |
|---------|----------|-------------|
| `voice-dna` | Yes | Path to your voice-dna.md file |
| `vault-path` | Yes | Path to Obsidian vault or research directory |
| `framework` | Yes | Blog framework: `astro`, `hugo`, or `generic` |
| `output-path` | Yes | Where to write blog post files |
| `audience` | No | Target audience description |
| `framing` | Yes | `personal` (first-person) or `org` ("we" voice) |
| `platforms` | No | Social media platforms (default: linkedin, twitter, facebook) |
| `talking-points` | No | Path to messaging framework document in vault |

## Installation

Test locally:

```bash
claude --plugin-dir /path/to/obsidian-publisher
```

## Usage

Trigger the blog-writing skill:
> "Write a blog post from my research on [topic]"

Trigger the social-media skill:
> "Create social media posts for this blog post"

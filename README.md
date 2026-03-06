# Fieldwork Plugins

Claude Code plugins for deep research and publishing. Two plugins: one turns natural language research prompts into structured Obsidian vault notes, the other turns those notes into blog posts and social media content.

## Quick Start

```bash
# Add the marketplace
/plugin marketplace add TimSimpsonJr/fieldwork-plugins

# Install one or both plugins
/plugin install research-workflow@fieldwork-plugins
/plugin install obsidian-publisher@fieldwork-plugins
```

## Plugins

### Research Workflow (v2.0.0)

An 8-stage research pipeline that searches the web, fetches and summarizes content, classifies it against your vault structure, and writes formatted Obsidian notes with frontmatter, citations, and wikilinks.

**Skills:**

| Skill | Purpose |
|-------|---------|
| `/research` | Run the pipeline. Takes a natural language prompt, returns vault notes. |
| `/research-setup` | First-run wizard. Detects your vault, installs optional tools, builds the search index. |

**Modes:**

- **Single topic** --- `/research "water privatization in Latin America"`
- **Batch** --- `/research "compare water privatization policies across Chile, Bolivia, and Colombia"`
- **Thread pull** --- `/research "pull threads from my notes on PFAS contamination"` (scans existing vault notes for leads)

**Pipeline stages:**

1. **Resolve** --- parse prompt into structured plan (topics, modes, estimates)
2. **Search** --- 1-3 web searches per topic, score and select best 3-7 URLs
3. **Fetch** --- download and clean article content
4. **Media** --- extract images, PDFs, videos; download to vault assets
5. **Summarize** --- ~500-token distillations with key entities, claims, source type
6. **Classify** --- map summaries to vault folders, tags, and wikilinks via FTS5 index
7. **Write** --- create/update vault notes with YAML frontmatter, inline citations, media embeds
8. **Discover** --- scan results for follow-up leads, score by novelty and relevance

Every stage checkpoints to disk. If something crashes, run `/research` again and select "Resume" to pick up where you left off.

**Infrastructure tiers:**

| Tier | What you need | What you get |
|------|--------------|--------------|
| Base | Claude Code | Full pipeline via Haiku subagents and WebSearch |
| Mid | + Ollama | Local summarization (faster, lower cost) |
| Full | + SearXNG (Docker) | Private web search, yt-dlp video downloads, Whisper transcription |

Run `/research-setup` to detect your tier and configure accordingly.

**Subagents** (all Haiku, run in parallel where possible):

- **topic-resolver** --- parses prompts into execution plans
- **search-agent** --- finds and scores web sources
- **classify-agent** --- maps content to vault structure
- **thread-discoverer** --- surfaces follow-up research leads

**Repository:** https://github.com/TimSimpsonJr/research-workflow

---

### Obsidian Publisher (v0.1.0)

Turns vault research into publishable content: blog posts and coordinated social media.

**Skills:**

| Skill | Purpose |
|-------|---------|
| `/blog-writing` | Draft a blog post from vault research. Scans notes by tag/wikilink, verifies sourcing, writes 1200-2000 words. |
| `/social-media` | Generate platform-specific posts (LinkedIn, X, Facebook) from a published blog post. |

**Blog writing process:**

1. Scan vault for relevant research by tag and wikilinks
2. Verify every fact traces to a primary source (flags gaps with `<!-- TODO: source needed -->`)
3. Draft with hook, body, and sources section
4. Self-review against your voice-dna.md style guide
5. Output as framework-compatible markdown (Astro, Hugo, or generic)

**Social media rules:**

- Each post stands alone (reader may not click through)
- Lead with concrete facts, not abstractions
- Platform-specific angles: LinkedIn (professional), X (punchiest fact), Facebook (conversational)
- No engagement bait

**Configuration** (set during first use):

- `voice-dna` --- path to your writing style guide
- `vault-path` --- your Obsidian vault
- `framework` --- astro, hugo, or generic
- `output-path` --- where blog posts land
- `audience` --- target reader description
- `framing` --- personal ("I") or organizational ("we")

**Repository:** https://github.com/TimSimpsonJr/obsidian-publisher

---

## Prerequisites

**Required:**
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) with plugin support
- Python 3.8+
- An [Obsidian](https://obsidian.md/) vault

**Optional (for higher tiers):**
- [Ollama](https://ollama.com/) with 8+ GB RAM or 6+ GB VRAM (mid tier)
- [SearXNG](https://github.com/searxng/searxng) via Docker (full tier)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video downloads (full tier)
- [Whisper](https://github.com/openai/whisper) for audio transcription (full tier)

## Setup

1. Install the marketplace and plugin(s) using the commands in Quick Start above.
2. Run `/research-setup` in your vault's project directory. The wizard will:
   - Detect your vault structure and conventions
   - Check for Ollama, SearXNG, yt-dlp, and Whisper
   - Build a FTS5 search index of your vault
   - Generate `{vault}/.research-workflow/config.json`
3. Run `/research "any topic"` to verify everything works.

For the publisher plugin, `/blog-writing` will prompt for configuration on first use.

## How It Works

No paid API calls. The research pipeline runs entirely through Claude Code's built-in tools:

- **Haiku subagents** handle search, classification, and thread discovery (cheap, parallelizable)
- **Sonnet** orchestrates the pipeline and writes notes
- **Opus** writes synthesis notes when the classify agent determines the content warrants it
- **Ollama** (optional) handles local summarization

State checkpoints after every stage mean you never lose work to a crash or timeout.

## Development

Both plugin source repos accept contributions:

- **Research Workflow:** 211 tests, all offline. Run `pytest tests/ -v` from the repo root.
- **Obsidian Publisher:** Early stage (v0.1.0).

## License

MIT

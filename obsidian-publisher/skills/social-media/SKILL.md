---
name: social-media
description: This skill should be used when the user asks to "create social media posts", "write a LinkedIn post", "write a tweet", "write an X post", "write a Twitter thread", "write a Facebook post", "create social content from a blog post", "share this on social media", "draft social media content", "promote this blog post", or mentions coordinating social media promotion for blog posts or articles.
---

# Social Media Content from Blog Posts

Generate coordinated social media content from blog posts. Each platform gets tailored content (not a copy-paste of the same text). Reads voice from the project's `voice-dna.md`. Matches the blog post's framing and key points to each platform's conventions.

## Project Configuration

Read from the project's `CLAUDE.md` or `.obsidian-publisher.md` config file at the repo root:

| Setting | Description | Example |
|---------|-------------|---------|
| `voice-dna` | Path to voice-dna.md | `~/.claude/voice-dna.md` |
| `platforms` | Target platforms | `[linkedin, twitter, facebook]` |
| `framing` | `personal` (first-person "I") or `org` ("we") | `org` |
| `audience` | Target audience description | `SC residents, non-partisan` |

If no platform list is configured, default to LinkedIn + X/Twitter + Facebook.

## Workflow

### 1. Read the Source Post

Read the blog post being promoted. Identify:
- The title and URL (or slug for constructing the URL)
- The 2-3 most compelling facts (the ones that make people stop scrolling)
- The core argument or narrative
- Any concrete numbers, names, or incidents

### 2. Load Voice

Read `voice-dna.md` and project config. Apply the same voice rules as blog writing: contractions, short paragraphs, varied sentences, no banned phrases, no em dashes. Apply framing (first-person or "we") per config.

### 3. Draft Platform Content

For each target platform, draft content following the patterns in `references/platform-formats.md`. Key principles:

- **Lead with the most concrete, specific fact.** Numbers, names, and incidents stop scrollers. Abstractions don't.
- **Each post stands alone.** The reader may never click through. The post should deliver value on its own.
- **Include a clear link** to the full blog post.
- **Match the blog post's framing.** Don't make the social post more inflammatory than the source material.
- **Never use engagement bait.** No "let that sink in," "read that again," or "you're not ready for this." All banned in voice-dna.md.
- **Tailor the angle per platform.** LinkedIn gets a professional lens. X gets the punchiest single fact. Facebook gets a more conversational take.

### 4. Voice Review

Self-review each draft against voice-dna.md:
- Check for every banned phrase
- Verify no em dashes
- Confirm the tone matches voice-dna.md
- Check platform-specific constraints (character limits, formatting)

### 5. Present for Review

Present all platform drafts to the user in a single message, clearly labeled by platform. Include character counts for platforms with limits. Wait for user approval or edits before any publishing action.

## Content Principles

### What Works

- Specific numbers ("99% of plates scanned belong to people suspected of nothing")
- Named people doing specific things ("Flock's CEO denied federal contracts on camera. Three weeks later, he admitted it.")
- Local relevance ("This happened in Greenville, not some other state")
- Questions that prompt curiosity without being clickbait ("How did a contract get signed with no council vote?")

### What Doesn't

- Abstract claims ("privacy matters")
- Generic calls to action ("take action now!")
- Engagement bait (banned in voice-dna.md)
- Copy-pasting the same text across platforms
- Hashtag spam

## Additional Resources

### Reference Files

- **`references/platform-formats.md`** — Platform-specific formatting, character limits, conventions, and examples for LinkedIn, X/Twitter, and Facebook

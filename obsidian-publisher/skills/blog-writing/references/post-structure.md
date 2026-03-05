# Post Structure Reference

## Post Anatomy

### Hook (1-3 sentences)

Open with a concrete fact, incident, or quote. Never an abstract claim or throat-clearing.

Good hooks:
- A specific number or statistic with a source
- A named person doing a specific thing
- A direct quote that's surprising or damning
- A local incident the reader can picture

Bad hooks:
- "In today's world of..." (banned AI language)
- "Privacy is important because..." (abstract)
- "Have you ever wondered..." (engagement bait)

### Body (1200-2000 words)

Short paragraphs (1-3 sentences max). Varied sentence length. Every factual claim gets an inline citation. Bold sparingly (1-2 key moments per section).

Organize around 3-5 key points. Each point gets its own section or clear paragraph break. Build toward the strongest point, or open with the strongest and support it.

### Sources Section

Full URLs at the bottom, grouped by topic if more than 5 sources. Use markdown link format:

```markdown
## Sources

- [Source Name, Date](https://full-url)
- [Source Name, Date](https://full-url)
```

### CTA (optional)

Soft link at the end. One sentence. Not the point of the post.

```markdown
If you want to do something about this, [find your rep and send a letter](https://example.com/action).
```

## Frontmatter Schemas

### Astro

```yaml
---
title: "Post Title Here"
date: 2026-03-05T00:00:00.000Z
summary: "One sentence summary for meta description and post listings."
tags:
  - topic-tag
  - category-tag
draft: false
---
```

### Hugo

```yaml
---
title: "Post Title Here"
date: 2026-03-05
description: "One sentence summary for meta description."
tags:
  - topic-tag
  - category-tag
draft: false
---
```

### Generic

```yaml
---
title: "Post Title Here"
date: 2026-03-05
summary: "One sentence summary."
tags:
  - topic-tag
---
```

## Structural Patterns

### Investigative

Best for deep, well-sourced posts that build a case.

1. **Hook**: The most surprising or damning single fact
2. **Context**: Brief background (2-3 paragraphs, only what the reader needs)
3. **Evidence**: Multiple angles, each with its own section. Strongest evidence first.
4. **Implications**: What this means for the reader specifically
5. **Soft CTA**: Optional link to action

### Narrative

Best for posts built around a specific incident or person.

1. **Incident**: What happened, to whom, where, when
2. **Expansion**: How this connects to a larger pattern
3. **Why it matters**: What this means for people like the reader
4. **Pattern**: Other incidents that show this isn't isolated
5. **Soft CTA**: Optional link to action

### Rebuttal

Best for countering specific claims from opponents.

1. **Their claim**: State it clearly and fairly (1-2 sentences)
2. **Why it's wrong**: Specific facts that contradict the claim
3. **What's actually true**: The full picture with sources
4. **Why it matters**: What the misleading claim obscures
5. **Soft CTA**: Optional link to action

## Formatting Rules

These are non-negotiable (from voice-dna.md integration):

- Short paragraphs: 1-2 sentences default, 3 max
- Numbers as digits (not spelled out)
- Contractions always
- NO em dashes ever (use commas, periods, colons, semicolons, or parentheses)
- Bold sparingly: 1-2 key moments per section
- Varied sentence length: mix short punchy lines with longer ones
- Physical verbs for abstract processes: "stripped back" not "simplified"
- Parenthetical asides for editorial commentary and honest reactions

## Slug Generation

Derive the filename from the title:
- Lowercase
- Replace spaces with hyphens
- Remove special characters
- Keep it under 60 characters

Example: "SC Has No License Plate Camera Law" -> `sc-has-no-license-plate-camera-law.md`

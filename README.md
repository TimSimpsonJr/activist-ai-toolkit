# Activist AI Toolkit

Claude Code plugins for research and civic engagement.

## Installation

```bash
/plugin marketplace add TimSimpsonJr/activist-ai-toolkit
```

## Available Plugins

### Research Workflow

Deep research pipeline for Obsidian vaults. 8-stage pipeline with batch research, thread-pulling, media capture, and vault-aware classification.

**Install:**
```bash
/plugin install research-workflow@activist-ai-toolkit
```

**What you get:**
- `/research` skill — stateful 8-stage research pipeline
- `/research-setup` skill — interactive vault configuration wizard
- 4 Haiku subagents (topic-resolver, search, classify, thread-discoverer)
- 3-tier infrastructure: base (Claude Code) → mid (+ Ollama) → full (+ SearXNG)

**Repository:** https://github.com/TimSimpsonJr/research-workflow

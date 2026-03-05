# Source Verification Reference

## Vault Navigation

### Finding Relevant Notes

Search the vault research directory using multiple strategies:

1. **Tag search**: Grep for frontmatter tags (`tags: [research, tactical-research]`)
2. **Topic search**: Grep for key terms in note titles and body text
3. **Index notes**: Look for `_`-prefixed files (e.g., `_Campaign Index.md`) that serve as tables of contents
4. **Related fields**: Notes often list related notes in their header: `**Related:** [[Note A]], [[Note B]]`

### Following Wikilinks

Obsidian notes link to each other with `[[wikilinks]]`:

- `[[Note Title]]` links to a note with that exact filename (minus `.md`)
- `[[Full Title|short name]]` links to the full title but displays the short name
- When a wikilink target doesn't exist as a file, it's a stub (topic worth exploring but not yet written)

To follow links:
1. Read the source note
2. Identify all `[[wikilinks]]` in the text
3. Search for matching `.md` files in the vault
4. Read linked notes for additional facts and sources
5. Repeat until you've covered the topic

### Tag Conventions

Common frontmatter tags and what they indicate:

| Tag | Meaning |
|-----|---------|
| `research` | Primary research note |
| `tactical-research` | Research with direct tactical application |
| `strategic-research` | Higher-level strategic analysis |
| `reference` | Reference material (ongoing use) |
| `legislation` | Legislative tracking |
| `campaign` | Campaign strategy or case study |

## Cross-Referencing

### Claim Verification

Every factual claim in a blog post must trace back through this chain:

```
Blog post claim -> Vault note -> Primary source (URL/document)
```

For each claim:
1. Find the vault note containing the fact
2. Check the note cites a primary source (URL, court filing, public record, official statement)
3. If the note cites a secondary source (news article), check if the article cites its own primary source
4. Prefer primary sources in the blog post citation

### Consistency Checks

When multiple vault notes discuss the same fact:
- Compare the specific numbers, dates, and names across notes
- If they disagree, trace each back to its primary source
- Use the version that matches the primary source
- Flag discrepancies for the user to resolve

### Source Hierarchy

Prefer sources in this order:
1. **Court documents, official filings** (most authoritative)
2. **Public records requests, government reports** (FOIA, SCDOT statements)
3. **Official organizational statements** (EFF, ACLU, IJ press releases)
4. **Investigative journalism** (named reporters, established outlets)
5. **News coverage** (general reporting)
6. **Blog posts, opinion pieces** (least authoritative, use only for quotes/positions)

## Citation Format

### Inline Citations

Use natural attribution when possible:

```markdown
According to a 2025 EFF report, the department conducted 261,711 warrantless searches in 14 months.
```

Or parenthetical for less prominent citations:

```markdown
The cameras captured images of 60,000+ vehicles per month (UWCHR, Oct 2025).
```

### Sources Section

Full markdown links with descriptive text:

```markdown
## Sources

- [EFF Lawsuit Press Release, Nov 2025](https://www.eff.org/press/releases/...)
- [9NEWS Investigation, Aug 2025](https://www.9news.com/article/...)
- [UWCHR Report: Leaving the Door Wide Open, Oct 2025](https://jsis.washington.edu/...)
```

Group by topic if more than 5 sources:

```markdown
## Sources

### Federal Data Access
- [Source 1](url)
- [Source 2](url)

### SC-Specific
- [Source 3](url)
- [Source 4](url)
```

## Handling Gaps

### Missing Sources

If a claim in the vault has no cited source:

```html
<!-- TODO: source needed for [specific claim] -->
```

Include the claim in the draft but flag it. Present flagged claims to the user and ask if they can provide sources or if the claim should be removed.

### Dead Links

If a source URL is inaccessible:
- Note the original source and date
- Search for archived versions (Internet Archive)
- Search for other reporting on the same facts
- Flag for the user if no alternative found

### Conflicting Information

If sources disagree:
- Present both versions to the user
- Note which source is more authoritative (per the hierarchy above)
- Recommend using the more authoritative version
- Consider noting the disagreement in the post if relevant

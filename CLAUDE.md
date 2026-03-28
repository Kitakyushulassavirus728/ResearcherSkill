# ResearcherSkill

This repository is the source for the `researcher` skill installed at `~/.claude/skills/researcher/SKILL.md`.

## Sync rule

`researcher.md` and `~/.claude/skills/researcher/SKILL.md` are clones. Any change to one MUST be applied to the other in the same operation. Never leave them out of sync.

## Versioning

This project uses [Semantic Versioning](https://semver.org/) and maintains a [CHANGELOG.md](CHANGELOG.md) following the [Keep a Changelog](https://keepachangelog.com/) format.

When the user says "bump version":
1. Move `[Unreleased]` entries in `CHANGELOG.md` into a new version section with today's date
2. Update the comparison links at the bottom of `CHANGELOG.md`
3. Commit and tag with `v{version}`

Tags are created via the CI pipeline automatically — do not create tags manually.

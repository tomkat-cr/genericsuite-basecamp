---
name: skills-creator
description: Create a new Claude Code skill (slash command) for this project. Use when the user asks to create a new skill, slash command, or automate a recurring workflow.
argument-hint: [skill-name] [brief description]
---

Create a new Claude Code project skill under `.claude/skills/`.

## Steps

1. **Gather requirements** — Ask the user:
   - What should the skill be named? (lowercase, hyphens only, e.g. `my-skill`)
   - What should it do? (one sentence)
   - When should Claude auto-invoke it vs. user-only? (suggest user-only for destructive actions)
   - Does it need arguments? If so, what are they?
   - Should it run any shell commands? Which ones?

2. **Determine invocation mode**:
   - If the skill has side effects (commits, deploys, sends messages, deletes): set `disable-model-invocation: true`
   - If purely informational/generative: omit that flag so Claude can auto-invoke it

3. **Create the skill directory and SKILL.md**:
   ```
   .claude/skills/<skill-name>/SKILL.md
   ```

4. **SKILL.md format**:
   ```markdown
   ---
   name: <skill-name>
   description: <clear description including trigger phrases>
   argument-hint: [optional arg hints]
   disable-model-invocation: true   # only if side effects
   ---

   <Step-by-step instructions for Claude to follow>
   ```

5. **Write the skill content** — the body should be:
   - Step-by-step instructions Claude will follow
   - Use `$ARGUMENTS` if the skill takes arguments
   - Reference project-specific commands from the Makefile or scripts when relevant
   - Include any verification steps or output format expectations

6. **Confirm** — show the user the created file and explain how to invoke it:
   - User invocation: `/<skill-name>` or `/<skill-name> arg1 arg2`
   - Auto-invocation: Claude will trigger it when the description matches the user's request

## Project context

This project uses `.claude/skills/` for project-level skills. Existing skills:
- `translate-docs.md` — translates uncommitted docs
- `release-notes.md` — drafts changelog entries
- `add-doc.md` — scaffolds bilingual doc pages
- `sample-code-update.md` — updates sample code packages
- `skills-creator/` — this skill
- `config-builder/` — builds GenericSuite JSON config files
- `build-agents-md/` — generates AGENTS.md for any project repo

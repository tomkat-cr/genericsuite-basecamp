---
name: add-doc
description: Scaffold a new documentation page in the correct bilingual structure (English + Spanish)
---

Scaffold a new documentation page following the GenericSuite Basecamp bilingual structure.

Steps:
1. Ask the user:
   - What is the page title?
   - Which section does it belong to? (Frontend-Development, Backend-Development, Other, or a new section)
   - What is the filename? (e.g., `my-feature.md`)
   - Brief description of what the page will cover
2. Read one existing page from the target section to match conventions
3. Create the English file at: `docs/en/{section}/{filename}`
4. Create the Spanish stub at: `docs/es/{section}/{filename}` with a placeholder noting translation is pending
5. Show the user the `mkdocs.yml` nav entry they need to add for both language sections
6. Remind the user to run `make serve` to preview the new page locally

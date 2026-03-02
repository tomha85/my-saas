# RULES

## Git workflow
1. Always start from latest main:
   - git checkout main
   - git pull --rebase
2. Create branch:
   - git checkout -b feature/<ticket>-<slug>
3. Commit frequently with clear messages.
4. Push branch:
   - git push -u origin <branch>
5. Create PR with gh:
   - gh pr create --title "<ticket>: <title>" --body-file .factory/SPECS.md

## Never do
- Never commit secrets (.env, tokens, keys).
- Never force push to main.
- Never run rm -rf or destructive commands without explicit instruction.

## Definition of Done
- Spec implemented OR explicitly rejected with reason.
- Tests run (or clearly documented why not).
- PR created with summary + checklist.

## Logging
- Write progress to .factory/STATUS.md
- Update .factory/TASKS.md state transitions

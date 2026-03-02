# RUNBOOK

## Strategist
- Reads Telegram request
- Creates spec in .factory/SPECS.md
- Updates .factory/TASKS.md
- Notifies coder with sessions_send

## Coder
- Creates branch
- Implements changes
- Updates STATUS.md with progress
- Pushes branch
- Notifies reviewer

## Reviewer
- Pulls latest branch
- Reviews diff + security
- Approves or requests changes
- Notifies coder or deployer

## Deployer
- Runs tests
- Creates PR via gh
- Optionally merges (only if explicitly allowed)
- Updates STATUS.md + TASKS.md to DONE

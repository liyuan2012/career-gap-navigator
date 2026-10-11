# Publish or update Career Gap Navigator on GitHub

## Before publication

Review every tracked file for candidate names, CVs, contact details, raw answers,
confidential data and unpublished applications. Start in a **private repository**
if any privacy question remains. This project includes an MIT licence in
the root `LICENSE` file; review the copyright holder attribution before publication.

## New repository

Create an empty repository named `career-gap-navigator` (or your preferred
repository name) in your GitHub account. Keep the hidden `.github/` folder intact.
From the **project root** in the extracted ZIP:

```bash
git init -b main
git add .
git commit -m "Add Career Gap Navigator Skill"
git remote add origin https://github.com/YOUR-ACCOUNT/career-gap-navigator.git
git push -u origin main
```

Replace the example owner URL with **your own repository URL**. If the repository
already exists, do not reinitialize it: clone it, copy/merge the updated
project contents, inspect `git diff`, commit and push on a branch or open a PR.
Never force-push blindly; retain user changes and the repository's license.

Alternative: use GitHub Desktop and publish the extracted project. Ensure hidden
`.github/skills` was included, not accidentally omitted in an upload screen.

## Required files on GitHub

- `.github/skills/career-gap-navigator/SKILL.md`
- `.github/skills/career-gap-navigator/references/opportunity-sourcing.md`
- `.github/skills/career-gap-navigator/references/verification-and-changelog.md`
- `Career Gap Navigator.txt`
- `README.md`
- `.github/workflows/validate.yml`

## Validate before and after upload

```bash
python tests/test_skill_structure.py
python scripts/check_policy_sync.py
python scripts/validate_privacy.py
```

Review GitHub Actions `Validate Career Gap Navigator skill` on pushes/PRs.
These are **static checks**, not AI quality tests. Run the scenarios in
`examples/acceptance-tests.md` with an appropriate agent and accessible real
source documents. Document any failures and remedy them before describing
behavior as validated.

## Activation and limitations

Skills in `.github/skills/` are discovered by **supported** GitHub Copilot or
other agents that read that location. Publishing a repository does NOT
automatically install a Skill in a participant's ChatGPT workspace or guarantee
that every AI will follow each instruction. For plain chat use, copy and paste
`Career Gap Navigator.txt` instead.

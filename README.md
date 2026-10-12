# Career Gap Navigator

**From your CV to an evidence-based career development plan.** Free and open source; no coding required for the standalone prompt.

**[Get started in English, 中文 or Suomi →](QUICKSTART.md)** · [Explore a fictional example](examples/fictional-session.md) · [Read the complete prompt](Career%20Gap%20Navigator.txt)

**README languages:** [English](README.md) | [简体中文](README.zh-CN.md) | [Suomi](README.fi.md)

Compare your CV with **real, attributable career opportunities** when reliable sources are accessible. Distinguish skills that are demonstrated, genuinely unverified, or not evidenced in the CV, then choose specific next actions instead of treating every CV omission as a skills deficit.

### What you can expect

| You provide | Career Gap Navigator helps produce |
|---|---|
| A redacted CV, target occupation, preferred location and career level | A source-linked review of relevant opportunities and their requirements, where web access allows |
| Answers to 3–5 focused verification questions | An updated evidence-based skills and experience assessment, with a change log |
| Your career objective and available constraints | Up to three justified development priorities and a personalized 30/60/90-day action plan |

**Illustrative distinction:** “Helped with a research project” does not, by itself, establish that someone managed the project. The workflow asks what the person actually did and preserves the evidence status until further verification. [See the fictional walkthrough](examples/fictional-session.md).

**Who might use it?** Job seekers, career changers, researchers and other professionals who want a structured starting point for career planning. It is a guidance workflow, not a hiring decision or a guarantee of job outcomes.

> **Pilot status.** A limited same-candidate CV comparison showed improved classification agreement after calibration. That is **not accuracy evidence** or proof of general applicability. The updated end-to-end workflow (including research-funding options and learning recommendations) has not been validated with a broad group of real users.

## Two ways to use it

**Agent Skill:** The repository includes `.github/skills/career-gap-navigator/SKILL.md` and focused references. Open or install it in a compatible skills-aware agent (for example, a supported GitHub Copilot environment). The skill activates when the agent determines the task is relevant. Uploading a repository to GitHub **does not automatically install it in ChatGPT**. See [GitHub's instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) and the [Agent Skills standard](https://agentskills.io/specification).

**Standalone chat prompt:** Open [`Career Gap Navigator.txt`](Career%20Gap%20Navigator.txt), upload a redacted CV in a new chat and paste the prompt in full. This file mirrors the participant-provided updated prompt **verbatim** and is the canonical policy for the packaged skill. No separate test prompt or job dossier is required.

## What the user supplies

| Required (ask only if missing) | Meaning |
|---|---|
| `CV` | Current redacted CV or adequate CV text |
| `Target occupation` | The participant's chosen occupation / career direction |
| `Preferred location` | Country/region and remote scope; relevant host location for funding |
| `Target level` | Entry-level / mid-level / senior / career changer / unsure |

**No advertisement/call is required from the participant** if web browsing is available: search automatically. If browsing is unavailable and there is no readable authentic source, request one actual ad or call and wait. Learning budget, hours, language and preferred course format are optional.

## Opportunity types

Employment vacancies are the **default**. The participant may explicitly request fellowships, research funding, scholarships or other programmes; the workflow then distinguishes each category's **eligibility requirements and selection criteria**. A funding call is not a job advertisement. Never assume research funding is appropriate to every candidate, or use CV keywords to invent a target occupation.

## Two-stage workflow

```text
Participant CV + explicitly chosen occupation, location and level
                              ↓
Real opportunity search (readable sources, checked dates, status)
                              ↓
Preliminary requirement audit (one evidence label for each R-ID)
                              ↓
3–5 high-value questions, each testing ONE coherent fact
                         STOP AND WAIT
                              ↓
Participant replies (SELF-REPORTED unless independently corroborated)
                              ↓
Change Log (changed AND unchanged, answer-addressed R-IDs)
+ full updated audit of every original requirement
                              ↓
Up to 3 priorities; verifiable courses only when justified
                              ↓
30/60/90-day roadmap + 3–12 months + Next 7 days
```

The six exact classifications are `ELIGIBILITY_BARRIER`, `STRENGTH`, `CONFIRMED_SKILL_GAP`, `CV_EVIDENCE_GAP`, `POTENTIAL_EXPERIENCE_GAP` and `UNKNOWN`. **CV silence is never proof of a skills deficit**. Explanations must remain equally substantive in different languages.

## Repository map

```text
.github/skills/career-gap-navigator/
    SKILL.md
    references/
      opportunity-sourcing.md
      evidence-rules.md
      verification-and-changelog.md
      learning-and-roadmap.md
      output-templates.md
Career Gap Navigator.txt          # Exact full standalone prompt
README.md
.github/workflows/validate.yml   # Local structural + policy tests
examples/acceptance-tests.md     # Human behaviour-test plan
examples/fictional-session.md    # Deliberately nonidentifying demo
examples/source-coverage.md      # Mapping from updated policy to Skill
examples/CHANGELOG.md            # Human-readable changes
scripts/check_policy_sync.py     # Consistency check, no network
scripts/validate_privacy.py      # Basic public-content hygiene check
tests/test_skill_structure.py
...
```

## Run local checks

```bash
python tests/test_skill_structure.py
python scripts/check_policy_sync.py
python scripts/validate_privacy.py
```

These verify structure, coverage of critical rules, policy-document sync and basic public-sharing hygiene. They **cannot** prove that the AI obeys the instructions, that the sourced courses exist or that the recommendations improve job outcomes. Run the [human acceptance scenarios](examples/acceptance-tests.md) in isolated chats with synthetic or consented data.

## Privacy and responsible use

- Do not commit actual participant CVs, raw questionnaire answers, names, contact data, grant applications, confidential project evidence or employer data to a public repository.
- Only synthetic examples appear in `examples/`. Scrub names and other identifiers before doing live searches.
- Participant answers remain `SELF-REPORTED` unless independently corroborated.
- Do not fabricate open status, vacancy/funding eligibility, course fees or funding odds. This is guidance, not professional licensing or legal eligibility certification.

## Development and replication

See [Development Guide](docs/Development%20Guide.md) for a general, privacy-safe prompt-design method and [publishing instructions](docs/Publish%20to%20GitHub.md) for GitHub setup.

## Licensing

This project is released under the **MIT License**. See the repository-root [`LICENSE`](LICENSE) file for the full terms. Reuse, modification and redistribution are permitted subject to retaining the copyright and permission notice.

# Updated standalone prompt → Agent Skill coverage map

[`Career Gap Navigator.txt`](../Career%20Gap%20Navigator.txt) is the canonical,
unaltered participant-provided prompt for the current upgrade. The Skill files
translate its workflow to progressive disclosure; they do not replace its
requirements. Where ambiguous, prefer the canonical prompt.

| Updated prompt section | Skill implementation | Review focus |
|---|---|---|
| How a participant uses this prompt | `SKILL.md` intake; `README.md` | CV and 3 target fields; no separate job ad input |
| Non-negotiable principles | `SKILL.md`; `references/evidence-rules.md` | Evidence over CV keywords; language parity; no invented odds |
| Phase 0 — minimum intake | `SKILL.md` | Ask only missing essentials before any search |
| A — career opportunity sourcing | `SKILL.md`; `references/opportunity-sourcing.md` | Employment default; explicitly requested funding; source dates/status; eligibility vs selection |
| B — classification | `SKILL.md`; `references/evidence-rules.md` | One label/R-ID, exact type/level, proof and uncertainty |
| C — Stage 1 | `SKILL.md`; `references/verification-and-changelog.md`; `references/output-templates.md` | Exactly 3–5 coherent questions, then STOP |
| D — Stage 2 | `SKILL.md`; `references/verification-and-changelog.md` | Interpret brief answers narrowly; changes **and retentions**; preserve every R-ID |
| E — training | `SKILL.md`; `references/learning-and-roadmap.md` | Evidence-triggered courses with verified details; no invented providers |
| F — roadmap | `SKILL.md`; `references/learning-and-roadmap.md` | Same <=3 priorities; 30/60/90 days + 3–12 months + Next 7 days |
| G — quality checks | `SKILL.md`; `tests/`; `examples/acceptance-tests.md` | Intakes, scope, source truth, labels, bilingual depth, answer precision |
| Start now | `SKILL.md` intake and Stage 1 gate | Never fill missing participant fields from examples |

## Material improvements compared with the previous Skill

- An opportunity can be an **explicitly requested fellowship or funding programme**, not just a job.
- Opportunity-side `SELECTION CRITERION` remains competitive assessment rather
  than automatically `ELIGIBILITY_BARRIER`.
- Stage 1 questions may ask multiple details about **one activity**, but cannot
  bundle independent competencies into ambiguous yes/no prompts.
- Stage 2 logs each response-addressed R-ID, **including unchanged labels**,
  with provenance and unresolved uncertainties.
- The same evidence depth applies in every output language. The identifiers and
  English labels remain fixed.
- Course searches are conditional, verifiable and integrated into one feasible
  personal development roadmap.

## Validation status

Static file and content checks can demonstrate that these instructions **exist**;
only independent sessions with synthetic/consented cases can demonstrate that
an AI agent consistently **obeys** them. Do not confuse agreement across repeated
or same-candidate cases with ground-truth career advice accuracy.

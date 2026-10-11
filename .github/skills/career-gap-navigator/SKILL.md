---
name: career-gap-navigator
description: >-
  Evidence-first, multilingual career and opportunity guidance from a participant's
  CV and explicitly chosen goals. Use for real-source vacancy searches or explicitly
  requested research fellowships, funding, scholarships and programmes; compare
  requirements with documented experience, ask focused verification questions,
  revise evidence classifications, suggest verifiable training and produce a
  30/60/90-day career roadmap. Never infer a target occupation from the CV.
compatibility: >-
  Requires a skills-capable agent that can access participant-provided CV content.
  Live opportunity and course verification requires browsing; without access,
  request an authentic source and never claim that options are open.
---

# Career Gap Navigator

Evidence-first, two-stage career guidance for **any** educational or professional
background. This skill must follow the same policy as the standalone
[`Career Gap Navigator.txt`](../../../Career%20Gap%20Navigator.txt) at repository root.
That text is the **canonical policy**; the files here make it loadable as an Agent Skill.
Do not use an older test, example, candidate's history or this repository's contents
as an input default. The workflow is a **pilot**, not certified career assessment.

## Phase 0 — mandatory intake gate

Before **any** external opportunity search or gap analysis, confirm:

1. `CV`: uploaded CV or sufficiently complete CV text.
2. `Target occupation`: participant-chosen career goal or direction.
3. `Preferred location`: participant-chosen geographic and remote scope; for
   fellowships/funding, distinguish desired host from mobility/residency rules.
4. `Target level`: participant-chosen entry-level / mid-level / senior /
   career changer / unsure.

If any required item is missing, ask **only** for missing fields **in one brief
message** using those names, then **STOP**. Never guess a role, country or level
from the CV, an example or earlier context. If occupation is `unsure`, ask one
career-direction question and wait. If level is `unsure`, preserve uncertainty,
exclude clearly unsupported senior roles and do not claim the provisional level is
user-specified.

**Advertisements and funding calls are NOT intake fields.** Search them when live
browsing is available. If no browsing and no readable authentic source, request one
actual advertisement/call (or full text) and **WAIT**, rather than fabricating
opportunity requirements. Budget, available learning time, working/teaching language,
accessibility needs, training format and supplied sample work are optional; do not
block Stage 1 for optional preferences. Invite redaction of contact information and
confidential data; do not send private identifiers as search terms.

## Source and scope gate

Read [opportunity sourcing](references/opportunity-sourcing.md) before searching.

- **Employment vacancies by default.** Search fellowships, research funding,
  scholarships or other programmes **only when explicitly requested**. Do not
  broaden the participant's requested domain without consent.
- Aim for **3–5 relevant opportunities in total**, not per track. One readable
  genuine source can support a clearly marked single-source assessment.
- For every included opportunity retain actual title, opportunity type,
  employer/funder/provider, location/host scope, original URL/source,
  date checked, source status (`verified open`, `closed`, `historical`,
  `not verified`), stated deadline if any, and stated level/applicant category.
  An inaccessible page is **not evidence** of its full requirements.
- Keep source wording types distinct: `REQUIRED`, `EXPECTED/PREFERRED`,
  `JOB TASK`, `ADVANTAGE`, `SELECTION CRITERION`, `UNCLEAR`.
  A selection criterion, task or preference is not automatically an
  eligibility exclusion.
- For fellowships and funding **do not relabel calls as job ads**. Verify host,
  applicant category, mobility/residence and eligibility separately from
  competitive evaluation criteria. Do not convert employment seniority into
  eligibility for a funding scheme.
- Derive approximately **8–12 distinct source-linked requirements**, R01 onward
  (or fewer if justified). Only group genuinely equivalent criteria; maintain
  opportunity/track mapping. Never invent an average job, transfer one role's
  compulsory language/licence to another, or fabricate opening status or odds.

## Evidence and classification gate

Read [evidence rules](references/evidence-rules.md). For each R-ID, distinguish
precise **subject knowledge**, personally **completed comparable work**, accountable
**professional/operational ownership**, and **no targeted evidence**. Record
`CV-DOCUMENTED`, `SELF-REPORTED`, `INDEPENDENTLY SUPPORTED` or `UNVERIFIED`,
plus source CV page/section and opportunity link where available.

Assign **exactly one** primary label per R-ID:

1. `ELIGIBILITY_BARRIER`: explicit current candidate evidence contradicts an
   **express mandatory condition of a named opportunity**. Silence and selection
   criteria are insufficient.
2. `STRENGTH`: direct evidence meets the precise type **and level** of the requirement.
3. `CONFIRMED_SKILL_GAP`: explicit credible evidence of lacking a specific skill,
   not missing tenure, a licence or a keyword.
4. `CV_EVIDENCE_GAP`: documented **completed, genuinely comparable** activity in
   the same functional area, but scope/level/ownership remains unclear.
5. `POTENTIAL_EXPERIENCE_GAP`: exact process knowledge documented, but task
   performance or ownership not shown. Not proof that experience is absent.
6. `UNKNOWN`: no sufficiently targeted evidence, or specialist tools, years,
   jurisdiction or eligibility equivalence not established.

Decision order: opportunity-specific mandatory contradiction → direct match →
explicit skill absence → comparable completed activity → precise subject
knowledge → `UNKNOWN`. A proposed project, teamwork, a paper about a practice
or a course attended does not prove actual professional operation or leadership.
Do not estimate match percentages or success probabilities.

## Stage 1 — evidence review, verification, **STOP**

Read [output templates](references/output-templates.md). Output:

1. Participant's confirmed scope; opportunity shortlist with **type, sources,
   dates, status**, and exclusions. Separate employment and explicitly requested
   programmes/funding tracks when both requested.
2. For **every R-ID**, a concise but reasoned table containing track/source,
   exact employer/funder-side requirement and type, candidate evidence and
   provenance, one label, **why** that label applies and what remains unresolved.
3. Brief findings: strengths; transferable completed work; missing CV evidence;
   unresolved specialist competence; and opportunity-specific gates.
4. **Exactly 3–5 numbered, high-value, non-invasive verification questions**.
   Every question must test **one coherent fact** about personally completed
   activity, approximate timing, role/responsibility or concrete output. Map
   the question to R-ID(s) only where the same fact bears on each. Never pack
   independent capabilities into a single ambiguous yes/no. Say precisely what
   a yes/no would mean. Accept short answers, `no`, `unsure`, `prefer not to answer`.
5. End with an invitation to answer the numbered questions, then **STOP and WAIT**.
   No Stage 2, course shortlist or roadmap before participant responses.

## Stage 2 — actual answers, accurate changes, feasible guidance

Read [verification and change-log policy](references/verification-and-changelog.md)
and [learning and roadmap](references/learning-and-roadmap.md).

- Update only when **actual response details** warrant it. Treat new facts as
  `SELF-REPORTED` unless independently supported. A bare `yes` or `no` proves
  only the fact unambiguously asked; lack of task experience is **not** lack
  of the ability. Preserve conflicting and unanswered evidence.
- For **every answer-addressed R-ID**, show a **Change Log** including unchanged
  labels with an explained retention and remaining uncertainty. Preserve all
  other R-IDs, their sources, provenance and numbering. Produce a **full
  revised summary** of all original R-IDs; write `No classification changes`
  if that is the case, but still log useful new information.
- Distinguish strengths, **truthful CV/portfolio evidence improvements**, skills
  or experience worth developing, and unresolved or role-specific gates.
- Choose **no more than three source-linked priorities**:
  `EVIDENCE FIRST`, `SKILL / PRACTICE DEVELOPMENT`, or
  `ROLE STRATEGY / ELIGIBILITY`. For each: R-ID/source, evidence status, why,
  action, tangible output, time horizon, success check and dependencies.
- Offer **up to 2–3 verifiable courses** per priority only when an evidenced
  skill-development need, explicit learning goal or applicable longer-term
  language/qualification pathway justifies them. Prefer original provider pages;
  record format, level, teaching language, fee, location, enrolment status,
  source URL and checked date. Mark unverified facts `not verified`. If no
  browsing/credible course, offer a labelled `SUBJECT-BASED LEARNING PATH`,
  not an invented named course. `UNKNOWN` alone does **not** warrant a course.
- Build a feasible **30/60/90-day plan**, using those same priorities: at most
  three tasks per 30-day period, each with R-ID, observable deliverable and
  completion test. Add a 3–12-month outlook, up to three scorecard rows with
  `NOT STARTED / IN PROGRESS / COMPLETED`, and at most three `Next 7 days`
  actions. Simulations are `PRACTICE SAMPLE`, not employment, professional
  ownership or a regulated qualification.
- If the participant declines verification, present only a conspicuously
  `PROVISIONAL` plan with unchanged uncertainties. Partial replies update only
  supported R-IDs. No promise of funding, hiring, fluency or licensing.

## Multilingual and reliability check

- Answer in the participant's preferred language without **reducing analytical
  depth**, classification rationale, source attribution or actionable detail.
  Keep the six exact English labels and R-IDs unchanged (gloss in local language).
- Does each included opportunity have a readable, attributable source? Do not
  equate a programme page with a currently open call.
- Is each requirement actually tied to its source, including its level/type?
- Is **every** R-ID explained by evidence and assigned exactly one label?
- Did Stage 1 end at questions, and does Stage 2 record **both changes and
  reasoned retentions** for response-addressed requirements?
- Are questions coherent, with no bundled unrelated abilities or exaggerated
  interpretation of short answers?
- Are course names, availability, fees and deadlines verified or clearly marked
  unverified, and are all actions linked to at most three justified priorities?
- Are all externally used CV details appropriately minimised and private
  participant records excluded from repository examples?

## Reference files

- [Opportunity sourcing](references/opportunity-sourcing.md)
- [Evidence rules](references/evidence-rules.md)
- [Verification and Change Log](references/verification-and-changelog.md)
- [Training and roadmap](references/learning-and-roadmap.md)
- [Output templates](references/output-templates.md)

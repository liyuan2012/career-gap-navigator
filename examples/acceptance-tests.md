# Human acceptance test protocol — use isolated fresh conversations

A static check is not an LLM behaviour test. Use participant-consented redacted
CVs or fictional CVs only; save first responses before feedback. For source-
reliability checks, preserve the actual URL, date checked and any accessibility
problem. Run at least one end-to-end **employment** and one explicitly requested
**fellowship/funding** scenario before announcing the upgraded Skill validated.

| Case | Scenario | Pass criterion |
|---|---|---|
| T01 | CV attached, no target/location/level | Ask only missing essentials together and WAIT; no source search |
| T02 | Target, location and level given, no CV | Ask for CV, WAIT |
| T03 | `Target level = unsure` | Mark level provisional; do not infer it as user's stated seniority |
| T04 | Full inputs; employment goal | Real attributable vacancy sources, status/date, 3–5 relevant overall |
| T05 | Full inputs; no browsing / no actual posting | Request authentic source, never create fictional employer requirements |
| T06 | Employment-only goal | Do not insert fellowship, funding, scholarships or extra careers |
| T07 | Funding/fellowship explicitly requested | Separate call from job; verify applicant/host/mobility/eligibility vs selection criteria |
| T08 | Selection criterion but no mandatory contradiction | Do not assign an `ELIGIBILITY_BARRIER` merely from criterion/silence |
| T09 | CV omits software/tool | Classify `UNKNOWN` unless other targeted evidence, no confirmed skill deficit |
| T10 | CV describes research about implementation | Do not infer personal operational implementation or leadership |
| T11 | CV describes completed comparable task | Preserve activity; do not assume senior authority or a full operational role |
| T12 | Stage 1 questions | Exactly 3–5; each tests one coherent fact; stop and wait |
| T13 | One question vaguely bundles two independent abilities | Flag as invalid; rewrite into coherent separate questions |
| T14 | Participant answers bare `yes` | Do not invent tool proficiency, duties, dates or outputs not asked |
| T15 | Participant answers `no` to having performed work | Do not infer underlying skill absence, preserve evidence limits |
| T16 | Stage 2 label should stay unchanged | Change Log still includes reasoned retention and remaining uncertainty |
| T17 | Participant answers questions selectively | Unanswered R-IDs retain original label, sources and provenance; all R-IDs shown in revised summary |
| T18 | Participant declines verification | Only a prominently labelled `PROVISIONAL` plan preserving unresolved evidence |
| T19 | Documented learning need and browsing available | Up to 2–3 actual provider-sourced options per applicable priority; cost/intake verified or `not verified` |
| T20 | No provider sources or browsing | `SUBJECT-BASED LEARNING PATH`, no fabricated named courses |
| T21 | UNKNOWN item only | Do not automatically recommend buying a course |
| T22 | Full revised plan | <=3 priorities, 30/60/90 days + 3–12 months + scorecard + <=3 Next 7 days tasks |
| T23 | Same substantive case tested in two user languages | Keep R-ID labels and comparable evidence analysis, uncertainty, action detail |
| T24 | Synthetic sample exercise | Must be labelled `PRACTICE SAMPLE`, never real professional work |

## Reviewer log (copy once per scenario)

```text
Case ID:
Opportunity type (employment / requested funding / other):
Input information provided:
Tool/browsing availability:
Source URL(s) / date(s) checked:
Actual behaviour:
Pass / Fail / Cannot determine:
Evidence of failure:
Suggested minimal prompt edit:
After-edit repeat result:
```

A 3-CV consistency case is not a representative user sample or measured
accuracy. Publish **no real participant data** in test logs or GitHub issues.

#!/usr/bin/env python3
"""Check canonical prompt release hash and core modular Skill policy coverage.

When deliberately changing the source prompt, revise the modular Skill files,
then run `python scripts/check_policy_sync.py --refresh-baseline` and review
its diff. Hash matching is only a consistency aid, not a behavioural test.
"""
from pathlib import Path
import sys
import hashlib

ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / 'Career Gap Navigator.txt'
BASELINE = ROOT / 'tests' / 'CANONICAL_PROMPT.sha256'
SKILLROOT = ROOT / '.github' / 'skills' / 'career-gap-navigator'
canonical = PROMPT.read_bytes()
actual = hashlib.sha256(canonical).hexdigest()
if '--refresh-baseline' in sys.argv:
    BASELINE.write_text(actual + '  Career Gap Navigator.txt\n', encoding='utf-8')
    print('Updated baseline. Review Skill/references/acceptance-tests manually before commit.')
    sys.exit(0)
assert BASELINE.is_file(), 'Missing canonical source baseline; run with --refresh-baseline'
expected = BASELINE.read_text(encoding='utf-8').split()[0]
assert expected == actual, ('Standalone prompt changed without updating release baseline. '
                            'Review modular skill rules, then --refresh-baseline.')

files = {
    p.name: p.read_text(encoding='utf-8').casefold()
    for p in [SKILLROOT / 'SKILL.md', *(SKILLROOT / 'references').glob('*.md')]
}
def check_anywhere(fragment, required_file=None):
    targets = [files[required_file]] if required_file else files.values()
    assert any(fragment.casefold() in s for s in targets), f'Missing coverage: {fragment}'

for text in [
    'SELECTION CRITERION', 'fellowship', 'scholarships', 'mobility',
    'one coherent', 'SELF-REPORTED', 'Change Log', 'unchanged',
    'SUBJECT-BASED LEARNING PATH', 'Next 7 days',
]:
    check_anywhere(text)
check_anywhere('Stage 1', 'SKILL.md')
check_anywhere('STOP and WAIT', 'SKILL.md')
check_anywhere('Change Log', 'verification-and-changelog.md')
check_anywhere('eligibility', 'opportunity-sourcing.md')
check_anywhere('UNKNOWN', 'evidence-rules.md')
check_anywhere('PRACTICE SAMPLE', 'learning-and-roadmap.md')
print('PASS: Canonical prompt is unchanged and material Skill policy sections are present.')
print('NOTE: Source sync check does not certify policy equivalence or live agent adherence.')

#!/usr/bin/env python3
"""Zero-dependency SKILL.md/README structure and policy-presence smoke tests.

This is NOT a behavioural AI, career-content, job-openings or course-source test.
"""
from pathlib import Path
from urllib.parse import unquote
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / '.github' / 'skills' / 'career-gap-navigator'
SKILL = SKILL_ROOT / 'SKILL.md'
SOURCES = ROOT / 'Career Gap Navigator.txt'

required = [
    SKILL, SOURCES, ROOT / 'LICENSE', ROOT / 'README.md', ROOT / 'README.zh-CN.md', ROOT / 'README.fi.md',
    SKILL_ROOT / 'references' / 'opportunity-sourcing.md',
    SKILL_ROOT / 'references' / 'evidence-rules.md',
    SKILL_ROOT / 'references' / 'verification-and-changelog.md',
    SKILL_ROOT / 'references' / 'learning-and-roadmap.md',
    SKILL_ROOT / 'references' / 'output-templates.md',
    ROOT / 'examples' / 'acceptance-tests.md',
    ROOT / 'examples' / 'fictional-session.md',
    ROOT / 'examples' / 'source-coverage.md',
    ROOT / 'examples' / 'CHANGELOG.md',
    ROOT / 'docs' / 'Development Guide.md',
    ROOT / 'docs' / 'Publish to GitHub.md',
    ROOT / '.github' / 'workflows' / 'validate.yml',
]
for f in required:
    assert f.is_file(), f'Missing {f.relative_to(ROOT)}'

license_text = (ROOT / 'LICENSE').read_text(encoding='utf-8')
assert license_text.startswith('MIT License\n'), 'Root LICENSE is not MIT'
assert 'Permission is hereby granted, free of charge' in license_text
assert 'Copyright (c) 2026 ' in license_text, 'Missing MIT copyright statement'

skill = SKILL.read_text(encoding='utf-8')
assert skill.startswith('---\n'), 'SKILL.md must begin with YAML frontmatter'
parts = skill.split('\n---\n', 1)
assert len(parts) == 2, 'SKILL.md lacks a closing frontmatter delimiter'
frontmatter = parts[0].split('---\n', 1)[1]
assert re.search(r'^name:\s*career-gap-navigator\s*$', frontmatter, re.M), 'Invalid name'
assert re.search(r'^description:\s*>-', frontmatter, re.M), 'Missing description'
assert len(skill.splitlines()) < 500, 'SKILL.md exceeds 500 lines'
assert len(skill.splitlines()) > 50, 'SKILL.md unexpectedly short'

# Validate local SKILL links, including URL-encoded filenames with spaces.
links = re.findall(r'\]\(([^)]+)\)', skill)
assert links, 'No resource links in SKILL.md'
for target in links:
    if target.startswith(('https://', 'http://', '#')):
        continue
    dest = (SKILL_ROOT / unquote(target)).resolve()
    assert dest.is_file(), f'Broken SKILL.md resource link: {target}'
    assert ROOT in dest.parents, f'External file link: {target}'

prompt = SOURCES.read_text(encoding='utf-8')
assert prompt.splitlines()[0] == 'CAREER GAP NAVIGATOR'
assert prompt.count('STAGE 1') >= 2
assert 'PHASE 0' in prompt and 'STAGE 2' in prompt
assert 'START NOW' in prompt

labels = [
    'ELIGIBILITY_BARRIER', 'STRENGTH', 'CONFIRMED_SKILL_GAP',
    'CV_EVIDENCE_GAP', 'POTENTIAL_EXPERIENCE_GAP', 'UNKNOWN',
]
for label in labels:
    assert label in prompt and label in skill, f'Missing label: {label}'

features = {
    'intake': ['Target occupation', 'Preferred location', 'Target level', 'CV', 'STOP'],
    'source breadth': ['employment', 'funding', 'fellowship', 'scholarship', 'SELECTION CRITERION'],
    'verification': ['3–5', 'one coherent', 'yes/no', 'R-ID'],
    'revision': ['Change Log', 'retentions', 'SELF-REPORTED', 'PROVISIONAL'],
    'guidance': ['course', 'not verified', '30/60/90', 'Next 7 days', 'PRACTICE SAMPLE'],
    'language parity': ['Multilingual', 'language', 'depth'],
}
full = '\n'.join(p.read_text(encoding='utf-8') for p in required if p.suffix in {'.md', '.txt'})
for category, expected_terms in features.items():
    for term in expected_terms:
        assert term.casefold() in full.casefold(), f'Missing coverage: {category}/{term}'
        # Core rules must also be visible to the main skill when it is activated.
        if term not in ('yes/no', 'PRACTICE SAMPLE'):
            assert term.casefold() in skill.casefold(), f'Missing main skill rule: {term}'

# Multilingual README documents remain discoverable and point to real local files.
for language_file in ['README.md', 'README.zh-CN.md', 'README.fi.md']:
    document = (ROOT / language_file).read_text(encoding='utf-8')
    assert document.startswith('# Career Gap Navigator\n'), f'Unexpected title: {language_file}'
    for other in ['README.md', 'README.zh-CN.md', 'README.fi.md']:
        assert f']({other})' in document, f'Missing language navigation: {language_file} -> {other}'
    for target in re.findall(r'\]\(([^)]+)\)', document):
        if target.startswith(('https://', 'http://', '#')):
            continue
        destination = (ROOT / unquote(target.split('#', 1)[0])).resolve()
        assert destination.is_file(), f'Broken README link in {language_file}: {target}'
        assert ROOT in destination.parents, f'Unsafe README link: {target}'

assert not (SKILL_ROOT / 'references' / 'job-sourcing.md').exists(), 'Obsolete reference persists'
assert not (ROOT / 'docs' / 'Publish%20to%20GitHub.md').exists(), 'Duplicate encoded filename persists'
print(f'PASS: Skill metadata, {len(required)} required files, links, labels and core policy sections.')
print('NOTE: Static checks do NOT prove real AI behaviour, accuracy or course availability.')

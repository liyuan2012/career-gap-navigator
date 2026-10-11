#!/usr/bin/env python3
"""Basic public-repo hygiene checks (cannot replace human privacy review)."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
ignore_dirs = {'.git', '__pycache__', '.pytest_cache'}
files = [p for p in ROOT.rglob('*') if p.is_file() and not set(p.relative_to(ROOT).parts) & ignore_dirs]
for p in files:
    # Do not search for forbidden tokens inside the validator's own source.
    if p.resolve() == Path(__file__).resolve():
        continue
    rel = p.relative_to(ROOT)
    assert p.suffix.lower() not in {'.pdf', '.docx', '.xlsx', '.pptx', '.jpg', '.png'}, f'Review binary/possibly private file: {rel}'
    # Never bundle an actual candidate CV or raw evaluation transcript.
    assert not re.search(r'(?i)^(cv[0-9 _-]*|.*candidate[_ -]cv.*|raw[_ -]results).*\.(txt|md|pdf)$', p.name), f'Possible private input: {rel}'
    if p.suffix.lower() not in {'.md', '.txt', '.py', '.yml', '.yaml', ''}:
        continue
    txt = p.read_text(encoding='utf8')
    # Do not prohibit public documentation URLs or synthetic email-free examples.
    assert not re.search(r'(?i)\b[A-Z0-9._%+-]+@(?!example\.com\b)[A-Z0-9.-]+\.[A-Z]{2,}\b', txt), f'Possible email address: {rel}'
    # Human review is required for indirect identifiers and public employer names.
    # Do not encode actual pilot-participant identities in this public checker.
print(f'PASS: {len(files)} repository files screened for simple public-sharing hazards.')
print('NOTE: Automated privacy scans miss many indirect identifiers; perform a manual review.')

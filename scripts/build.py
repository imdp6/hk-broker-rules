#!/usr/bin/env python3
"""Build domain-only Surge lists from reviewed, attributed entries."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def build(check=False):
    data = json.loads((ROOT / 'sources.json').read_text())
    expected = {}
    all_rules = []
    seen = set()
    for broker in data['brokers']:
        rules = []
        for entry in broker['rules']:
            kind, host = entry['type'], entry['host']
            assert kind in {'DOMAIN', 'DOMAIN-SUFFIX'}, entry
            assert re.fullmatch(r'(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,}', host), host
            assert entry['source'].startswith('https://') and entry['reason'], entry
            line = f'{kind},{host}'
            assert line not in seen, line
            seen.add(line)
            rules.append(line)
        header = f"# {broker['name']} | Reviewed: {data['reviewed']}\n# Domain-only routing; not a complete endpoint inventory.\n"
        expected[f"rule/Surge/{broker['id']}.list"] = header + '\n'.join(rules) + '\n'
        all_rules.extend([f"# {broker['name']}", *rules, ''])
    expected['rule/Surge/HK-Broker.list'] = f"# HK Broker | Reviewed: {data['reviewed']}\n# Rules: {len(seen)} | Domain-only\n\n" + '\n'.join(all_rules)
    for name, content in expected.items():
        path = ROOT / name
        if check:
            assert path.exists() and path.read_text() == content, f'Stale output: {name}'
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    assert {str(p.relative_to(ROOT)) for p in (ROOT / 'rule/Surge').glob('*.list')} == set(expected), 'Unexpected list file'
    print(f"Validated {len(seen)} domain rules across {len(data['brokers'])} brokers; {len(expected)} lists.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    build(parser.parse_args().check)

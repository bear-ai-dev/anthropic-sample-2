"""Read recorded verifier details without running or changing any grader."""
import json
import re
from pathlib import Path

def failure_checks(directory, reward):
    directory=Path(directory)
    if reward==1: return [],'pass'
    for name in ('report.json','report.txt','reward-detail.json','output.json'):
        path=directory/name
        if not path.exists(): continue
        if name=='report.txt':
            lines=[x.strip() for x in path.read_text().splitlines() if x.strip() and not x.startswith('reward=')]
            if lines: return lines,name
        data=json.loads(path.read_text()) if name.endswith('.json') else {}
        if isinstance(data.get('rules'),list):
            return [r.get('name',r.get('rule',str(r))) for r in data['rules'] if not r.get('passed')],name
        if isinstance(data.get('tests'),list):
            return [r['name'] for r in data['tests'] if r.get('status')!='passed'],name
        detail=data.get('detail')
        if isinstance(detail,str):
            lines=[x.strip()[2:] for x in detail.splitlines() if x.strip().startswith('- ')]
            if lines: return lines,name
        if isinstance(detail,dict) and detail.get('runs'):
            return [f'{k}: {note}' for k,v in detail['runs'].items() if not v.get('ok') for note in v.get('notes',['failed'])],name
    text=(directory/'test-stdout.txt').read_text() if (directory/'test-stdout.txt').exists() else ''
    checks=[f'{name} [{kind}]' for kind,name in re.findall(r'^\s*NOT PASSED \(([\w-]+)\): (.+)$',text,re.M)]
    if checks: return checks,'test-stdout.txt'
    return [],'unparsed'

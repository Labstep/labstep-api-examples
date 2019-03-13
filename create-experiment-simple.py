#!/usr/bin/env python
import json
import requests
headers = {
    'apikey': 'YOUR_API_KEY'
}
data = {
    'name':'My Experiment',
    'description': 'Create an experiment with out a protocol',
}
print(data)

url = 'https://api.labstep.com/api/generic/experiment-workflow'
r = requests.post(
    url,
    json=data,
    headers=headers,
)
parsed = json.loads(r.content)
print(json.dumps(parsed, indent=4, sort_keys=True))

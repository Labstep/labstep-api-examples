#!/usr/bin/env python
import json
import requests
headers = {
    'apikey': 'YOUR_API_KEY'
}
data = {
    'name':'My Experiment',
    'description': 'Creating an experiment associated to an existing protocol',
    'protocol_id': 123,
}
print(data)

url = 'https://api.labstep.com/api/generic/experiment'
r = requests.post(
    url,
    json=data,
    headers=headers,
)
parsed = json.loads(r.content)
print(json.dumps(parsed, indent=4, sort_keys=True))
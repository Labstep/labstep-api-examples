#!/usr/bin/env python

import json
import requests

headers = {
    'apikey': 'YOUR-API-KEY',
}

data = {
    'name': 'Labstep Experiment API example',
    'description': 'Create an experiment with a custom description on your timeline',
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

#!/usr/bin/env python

import json
import requests

headers = {
    'apikey': 'YOUR-API-KEY',
}

data = {
    'name': 'Protocol Step Name',
    'description': 'This is my step',
    'protocol_id': '2522'
}
print(data)
url = 'https://api.labstep.com/api/generic/protocol-step'
r = requests.post(
    url,
    json=data,
    headers=headers,
)

parsed = json.loads(r.content)
print(json.dumps(parsed, indent=4, sort_keys=True))

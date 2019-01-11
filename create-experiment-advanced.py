#!/usr/bin/env python

import json
import requests

headers = {
    'apikey': 'YOUR-API-KEY',
}

data = {
    'name': 'Labstep Experiment API advanced example',
    'description': 'A more advanced example, using a specific protocol',
    'start': "2018-04-10T17:14:11+0100",
    'end': "2018-04-10T17:14:11+0100",
    'protocol_id': '2522',
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

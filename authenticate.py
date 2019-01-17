#!/usr/bin/env python

import json
import requests

data = {
    'username': 'YOUR-USERNAME-HERE',
    'password': 'YOUR-PASSWORD-HERE',
}
print(data)
url = 'https://api.labstep.com/public-api/user/login'
r = requests.post(
    url,
    json=data,
    headers={},
)

parsed = json.loads(r.content)
print(json.dumps(parsed, indent=4, sort_keys=True))

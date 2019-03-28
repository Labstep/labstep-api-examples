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

# From the experiment workflow, get the id – mark as finished
experimentWorkflowId = parsed['id']

# From the experiment workflow, get the thread.id – then use it to create a new comment
threadId = parsed['thread']['id']

data = {
    'ended_at': "2019-03-10T13:47:38+0000",
}
url = 'https://api.labstep.com/api/generic/experiment-workflow/%d' % experimentWorkflowId
r = requests.put(
    url,
    json=data,
    headers=headers,
)
parsed = json.loads(r.content)


data = {
    'body': 'comment body',
    'thread_id': threadId,
}
url = 'https://api.labstep.com/api/generic/comment'
r = requests.post(
    url,
    json=data,
    headers=headers,
)
parsed = json.loads(r.content)

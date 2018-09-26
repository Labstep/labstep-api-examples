#!/usr/bin/env python

import json
import requests

APIKEY = 'YOUR-API-KEY'
APIKEY = 'test@labstep.com'

HOSTNAME = 'https://api.labstep.com'
HOSTNAME = 'http://localhost:8000'

headers = {
    'apikey': APIKEY,
}

def post(url, data = None, files = None):
    response = requests.post(
        url,
        json=data,
        files=files,
        headers=headers,
    )
    assert response.ok, 'response is not ok, there was an error'
    parsed = json.loads(response.content)
    return parsed

def create_protocol(data):
    url = '{0}/api/generic/protocol'.format(HOSTNAME)
    return post(url, data)

def create_step(data):
    url = '{}/api/generic/protocol-step'.format(HOSTNAME)
    return post(url, data)

def create_experiment(data):
    url = '{}/api/generic/experiment'.format(HOSTNAME)
    return post(url, data)

def create_file(files):
    url = '{}/api/generic/file/upload'.format(HOSTNAME)
    return post(url, files=files)

def create_comment(data):
    url = '{}/api/generic/comment'.format(HOSTNAME)
    return post(url, data)

data = {
    'name': 'Advanced Protocol',
}

protocol = create_protocol(data)

data = {
    'name': 'Image Acquisition',
    'description': 'Experiments using this steps will attach a file here',
    'protocol_id': protocol['id']
}

protocol_step = create_step(data)

# We'll create two Experiment entities
for i in range(2):
    data = {
        'protocol_id': protocol['id'],
    }

    experiment = create_experiment(data)

    # Cannot attach files directly to ExperimentStep entity
    experiment_step = experiment['steps'][0]

    # We can attach via a Thread entity
    thread = experiment_step['thread']

    files = {'file': open('IMG_0001.png', 'rb')}

    uploaded = create_file(files)

    data = {
        'body': 'Attached the uploaded files with a new Comment',
        'thread_id': thread['id'],
        'file_id': uploaded.keys(),
    }

    comment = create_comment(data)

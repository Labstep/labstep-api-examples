# Labstep API examples

This repository contains a handful of python scripts using the Labstep API.

Full documentation can be found on Intercom https://help.labstep.com/api/getting-started-with-the-labstep-api, this repository is just the source code backing the documentation.


## Requirements

The only dependency is 'requests' module, which you can install using

    pip install requests

## Examples

### Authentication

Create a file called ‘authenticate.py’

    #!/usr/bin/env python
    import json
    import requests
    data = {
        'username': 'test@labstep.com',
        'password': 'YOUR-PASSWORD',
    }
    print(data)
    url = 'https://api-staging.labstep.com/public-api/user/login'
    r = requests.post(
        url,
        json=data,
        headers={},
    )
    parsed = json.loads(r.content)
    print(json.dumps(parsed, indent=4, sort_keys=True))

Running the script will print all the user information, including your API key

    $ python authenticate.py
    {'username': 'test@labstep.com', 'password': 'YOUR-PASSWORD'}
    {
        "api_key": "YOUR-API-KEY",
        "enabled": true,
        "first_name": "Test", .... further JSON content

### Create a Protocol

Create a new file called ‘create-protocol.py’

    #!/usr/bin/env python
    import json
    import requests
    headers = {
        'apikey': YOUR-API-KEY',
    }
    data = {
        'name': 'Programmatic Protocol',
    }
    print(data)
    url = 'https://api-staging.labstep.com/api/generic/protocol'
    r = requests.post(
        url,
        json=data,
        headers=headers,
    )
    parsed = json.loads(r.content)
    print(json.dumps(parsed, indent=4, sort_keys=True))

Running the script will create an empty protocol on the Labstep database

    $ python create-protocol.py
    {'name': 'Programmatic Protocol'}
    {
        "id": 2522,
        "additional_information": null,
        "author": {
            "id": 2,
            "name": "Test account",
            "username": "test@labstep.com"
        },
        "changes": null,
        "children_protocol_collections": [],
        "collection": {
            "id": 1801,
            "parent_protocol": null,
            "permissions": {
                "edit": true,
                "owner": true, ... further JSON

This creates Protocol with id: 2522


### Create an Experiment

Create a ‘create-experiment.py’ file

    #!/usr/bin/env python
    import json
    import requests
    headers = {
        'apikey': 'YOUR_API_KEY'
    }
    data = {
        'name':'My Experiment',
        'description': 'Testing whether the labstep API works,
        'protocol_id': '2522',

    }
    print(data)

    url = 'https://api-staging.labstep.com/api/generic/experiment'
    r = requests.post(
        url,
        json=data,
        headers=headers,
    )
    parsed = json.loads(r.content)
    print(json.dumps(parsed, indent=4, sort_keys=True))

Running the script will create an Experiment, using the Protocol with id:2522. You can also create an experiment without attaching a protocol.

    $ python create-experiment.py
    {'name':'My Experiment','description': 'Testing whether the labstep API works,'protocol_id': '2522'}
    {
       "id": 124,
       "author": {
            "first_name": "Test",
            "id": 2,
            "last_name": "account",
            "name": "Test account",
            "profile": {
                "id": 2,
	 	    ...
            }
        "deleted_at": null,
        "end": "2018-04-10T17:14:11+0100", …


Learn more To learn how to attach files to your Experiments, see the “Upload Instrument Data” tutorial below.

### Upload Instrument Data

You can attach files / images to your experiment by specifying the experiment_id when uploading a file. For example, our instruments produces files such as IMG_0001.png which we can upload to experiment with id:123 as follows:

    import json
    import requests

    headers = {
        'apikey': 'YOUR_API_KEY'
    }

    files = {'file': open('IMG_0001.png', 'rb')}
    data = {'experiment_id':123}
    print(files)
    url = 'https://api-staging.labstep.com/api/generic/file/upload'
    r = requests.post(
        url,
        headers=headers,
        files=files,
        data=data
    )
    response = json.loads(r.content)

    '''
    response is a long JSON of the shape
    {"2042":{"id":2042,"created_at":"2018-04-   10T13:47:38+0000","name":"IMG_0001.png","path":"2018\/04\/10\/phpPvfO92.png","size":41427,"mime_type":"image\/png","thumbnail"  :"thumbnails\/file_small\/2018\/04\/10\/phpPvfO92.png","thumbnail_medium":"thumbnails\/file_medium\/2018\/04\/10\/phpPvfO92.pn  g","thumbnail_large":"thumbnails\/file_large\/2018\/04\/10\/phpPvfO92.png"}}
    '''

While Labstep has no storage limit per-user at present, we do limit the attachment size to 25 MB on uploading.

### Further details

We use the same API for our web app so anything you can do on the web app you can do via the api! To see how the web app does it, open the developer tools in your browser, go to the network tab and search for network requests sent to `api.labstep.com`

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
    url = 'https://api.labstep.com/public-api/user/login'
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
    url = 'https://api.labstep.com/api/generic/protocol'
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

### Attach a Step to a Protocol

With a blank protocol, like the one created above, not much can be done but steps can be easily attached to build-in interactive features.

Create a file called ‘add-protocol-step.py’

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

To add new Step to Protocol id:2522, run the script

    $ python add-step.py
    {'protocol_id': '2522', 'name': 'Protocol Step Name', 'description': 'This is my step'}
    {
        "description": "This is my step",
        "files": [],
        "id": 9737,
        "indentation": 0,
        "linked_protocols": [],
        "name": "Protocol Step Name",
        "tables": [],
        "timers": [],
        "values": []
    }

You can then add files, timers and other interactive features to the stops. Email info@labstep.com if you’d like to find out more.

### Run a Protocol (create an Experiment)

Create a ‘create-experiment.py’ file

    #!/usr/bin/env python
    import json
    import requests
    headers = {
        'apikey': 'YOUR-API-KEY',
    }
    data = {
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

Running the script will post an experiment on your timeline, using Protocol with id:2522. The experiment will be shared with your groups.

    $ python create-experiment.py
    {'start': '2018-04-10T17:14:11+0100', 'end': '2018-04-10T17:14:11+0100', 'protocol_id': '2522'}
    {
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

### Create a Post
Open a new file called ‘create-post.py’

    #!/usr/bin/env python
    import json
    import requests
    headers = {
     'apikey': 'YOUR-API-KEY',
    }
    data = {
        'name': 'Labstep Post API',
        'description': 'Create post with custom description on your timeline',
    }
    print(data)
    url = 'https://api.labstep.com/api/generic/post'
    r = requests.post(
        url,
        json=data,
        headers=headers,
    )
    parsed = json.loads(r.content)
    print(json.dumps(parsed, indent=4, sort_keys=True))

Running the script will create a new Post on your timeline, shared with your groups

    $ python create-post.py
    {'name': 'Labstep Post API', 'description': 'Create post with custom description on your timeline'}
    {
        "author": {
            "id": 2,
            ...
            "username": "test@labstep.com"
        },
        "created": "2018-04-10T16:29:03+0000",
        "deleted_at": null,
        "description": "Create post with custom description on your timeline",
        "files": [],
        "id": 1489,
        "thread": {
            "comments": [],
            "comments_count": 0,
            "id": 37055
        },
        "title": null,
        "updated": "2018-04-10T16:29:03+0000"
    }

### Upload Instrument Data

Our instruments produces files such as IMG_0001.png

We start by uploading your file to Labstep, the file is saved and and the its database ID is returned

    import json
    import requests

    headers = {
        'apikey': 'YOUR-API-KEY',
    }

    files = {'file': open('IMG_0001.png', 'rb')}
    print(files)
    url = 'https://api.labstep.com/api/generic/file/upload'
    r = requests.post(
        url,
        headers=headers,
        files=files
    )
    response = json.loads(r.content)

    '''
    response is a long JSON of the shape
    {"2042":{"id":2042,"created_at":"2018-04-   10T13:47:38+0000","name":"IMG_0001.png","path":"2018\/04\/10\/phpPvfO92.png","size":41427,"mime_type":"image\/png","thumbnail"  :"thumbnails\/file_small\/2018\/04\/10\/phpPvfO92.png","thumbnail_medium":"thumbnails\/file_medium\/2018\/04\/10\/phpPvfO92.pn  g","thumbnail_large":"thumbnails\/file_large\/2018\/04\/10\/phpPvfO92.png"}}
    '''

The file database IDs can then be used to create a new post

    data = {
        'name': 'My microscopy post',
        'description': 'Automatically created with labstep API test (having fun with attachments)',
        'file_id': response.keys(),
    }
    print(data)
    url = 'https://api.labstep.com/api/generic/post'
    r = requests.post(
        url,
        json=data,
        headers=headers,
    )
    print(r.text)
    print(r.content)

Then, the post with attachments will appear on your timeline in either the web or mobile apps!

Available storage space while Labstep has no storage limit per-user at present, we do limit the attachment size to 25 MB on uploading.


### Further details

Some examples are independent of each other, for example:

- `create-post.py` creates an empty Post on your timeline
- `create-protocol.py` creates an empty Protocol in your library
- `storage-files-attachments.py` uploads some files first, then creates a Post on your timeline and attaches the files to it

Others build on previous examples. For example:

- `attach-file.py` depends on `create-post.py`
- `add-protocol-step.py` depends on `create-protocol.py`
- `create-experiment.py` depends on `create-protocol.py`

## Advanced examples

An `advanced-example.py` outlines how to create a Protocol with an "Image acquisition" step. The protocol is then re-used by multiple experiments, uploading files.

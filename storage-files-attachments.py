
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
{"2042":{"id":2042,"created_at":"2018-04-10T13:47:38+0000","name":"IMG_0001.png","path":"2018\/04\/10\/phpPvfO92.png","size":41427,"mime_type":"image\/png","thumbnail":"thumbnails\/file_small\/2018\/04\/10\/phpPvfO92.png","thumbnail_medium":"thumbnails\/file_medium\/2018\/04\/10\/phpPvfO92.png","thumbnail_large":"thumbnails\/file_large\/2018\/04\/10\/phpPvfO92.png"}}
'''

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

import json
import requests

headers = {
    'apikey': 'YOUR_API_KEY',
}

files = {'file': open('IMG_0001.png', 'rb')}
data = {'experiment_id': 123}
print(files)
url = 'https://api-staging.labstep.com/api/generic/file/upload'
r = requests.post(
    url,
    headers=headers,
    files=files,
    data=data
)
response = json.loads(r.content)
print(json.dumps(response, indent=4, sort_keys=True))

'''
response is a long JSON of the shape
{"2042":{"id":2042,"created_at":"2018-04-   10T13:47:38+0000","name":"IMG_0001.png","path":"2018\/04\/10\/phpPvfO92.png","size":41427,"mime_type":"image\/png","thumbnail"  :"thumbnails\/file_small\/2018\/04\/10\/phpPvfO92.png","thumbnail_medium":"thumbnails\/file_medium\/2018\/04\/10\/phpPvfO92.pn  g","thumbnail_large":"thumbnails\/file_large\/2018\/04\/10\/phpPvfO92.png"}}
'''

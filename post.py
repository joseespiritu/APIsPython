import requests
import json
import pprint

if __name__ == '__main__':
    url = 'https://httpbin.org/post'

    payload = {'nombre': 'Eduardo',
            'curso': 'python',
            'nivel': 'intermedio'}

    response = requests.post(url, data=json.dumps(payload))

    # json post se encarga de serializarlos
    # data entonces nosotros los serializamos
    print(response.url)

    if response.status_code == 200:
        pprint.pprint(response.content)
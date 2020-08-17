import requests
import json
import pprint

if __name__ == '__main__':
    url = 'https://httpbin.org/delete'

    payload = {'nombre': 'Eduardo',
            'curso': 'python',
            'nivel': 'intermedio'}

    headers = {'Content-Type': 'application/json',
               'access-token': '1234'}

    response = requests.delete(url, data=json.dumps(payload), headers=headers)
    """
    GET
    POST
    PUT
    DELETE
    """

    # json post se encarga de serializarlos
    # data entonces nosotros los serializamos
    print(response.url)

    if response.status_code == 200:
        #pprint.pprint(response.content)
        headers_response = response.headers #Dic
        server =  headers_response['Server']
        print(server)
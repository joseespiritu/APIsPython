"""
Descarga de archivos pesados
"""
import requests

if __name__ == '__main__':
    url = 'https://i.imgur.com/wKeyQdr.jpg'

    response = requests.get(url, stream=True)#Realiza la peticion sin descargar el contenido
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content():#Descarga el contenido poco a poco
            file.write(chunk)

    response.close()
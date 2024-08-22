import requests
from dotenv import load_dotenv
import os

class HttpClientEmail:
    def __init__(self):
        load_dotenv()
        self.url  = os.getenv('API_URL')
        self.data = {
            'Recipients': [os.getenv('API_RECIPIENTS')],
            'Subject': 'Nuevo registro',
            'ContentHtml': '<h1>Se creó un nuevo registro</h>'
        }
        self.headers = {
            'Content-Type': 'application/json'
        }

    def sendEmail(self):
        response = requests.post(self.url, json=self.data, headers=self.headers)
        if response.status_code == 200:
            print('Petición exitosa')
            print('Respuesta:', response.json())
        else:
            print('Error en la petición')
            print('Código de estado:', response.status_code)
            print('Respuesta:', response.text)
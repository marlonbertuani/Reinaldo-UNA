import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = 'https://api.hgbrasil.com/finance/quotations?key='
api = os.getenv("APIKEY")

r = requests.get(url + api)

if (r.status_code == 200):
    print()
    print(r.text)
    print()
else:
    print('Nao houve sucesso na requisicao.')
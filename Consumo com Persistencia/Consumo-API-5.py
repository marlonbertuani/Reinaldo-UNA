import requests
from dotenv import load_dotenv
import os
import sqlite3
from datetime import datetime
import json

load_dotenv()

url = 'https://api.hgbrasil.com/finance/quotations?key='
api = os.getenv("APIKEY")

r = requests.get(url + api)

def salvar_dados(dolar, euro):
    conn = sqlite3.connect('bdcotacoes.db')
    cursor = conn.cursor()

    cursor.execute('''
            INSERT INTO moedas (data, dolar, euro)
            VALUES (?, ?, ?)
        ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), dolar, euro))

    conn.commit()
    conn.close()

    print(f"Salvou!!! dolar R$ {dolar}, euro R$ {euro}")

if (r.status_code == 200):
    print("Json identado para trabalhar melhor!")
    print(json.dumps(r.json(), indent=1))
    print()

    dados = r.json()
    dolar = dados['results']['currencies']['USD']['buy']
    euro = dados['results']['currencies']['EUR']['buy']

    salvar_dados(dolar, euro)
else:
    print('Nao houve sucesso na requisicao.')

import requests
rua = 'rua dos aimores'
url = f"https://viacep.com.br/ws/MG/Belo Horizonte/{rua}/"
formato = '/xml/'
print("Como ficou a URL: ", url)
r = requests.get(url + formato)
if (r.status_code == 200):
    print()
    print('XML : ', r.text)
    print()
else:
    print('Nao houve sucesso na requisicao.')
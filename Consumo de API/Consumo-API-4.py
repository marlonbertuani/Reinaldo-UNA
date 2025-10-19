import requests
url = 'https://viacep.com.br/abc/'
formato = '/xml/'

r = requests.get(url + formato)

if (r.status_code == 200):
    print()
    print('XML : ', r.text)
    print()

else:
    print()
    print("Erro na request, codigo do erro:", r.status_code)
    print(r.text)
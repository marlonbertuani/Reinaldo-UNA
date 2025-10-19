import requests
url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/xml/'
consultas = 5

for i in range(consultas):
    novo_cep = str(int(cep) + i)
    
    r = requests.get(url + novo_cep + formato)
    
    if (r.status_code == 200):
        print()
        print('XML : ', r.text)
        print()
    else:
        print('Nao houve sucesso na requisicao.')

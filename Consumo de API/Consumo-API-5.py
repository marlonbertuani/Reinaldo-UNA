import requests
r = requests.get('http://www.google.com/search', params={'q': 'elson de abreu'})
if (r.status_code == 200):
    with open('resposta.txt', 'w') as arquivo:
        arquivo.write(r.text)
    print()
    print("Arquivo salvo com sucesso!")
else:
    print('Nao houve sucesso na requisicao.')
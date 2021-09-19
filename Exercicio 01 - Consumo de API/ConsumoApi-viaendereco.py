import requests

url = 'https://viacep.com.br/ws/'
estado = 'MG/'
cidade = 'Belo Horizonte/'
rua = 'Rua dos Aimores'
formato = '/xml/'

r = requests.get(url + estado + cidade + rua + formato)

if (r.status_code == 200):
    print()
    print('JSON : ', r.text)
    print()
else:
     print('Nao houve sucesso na requisicao.')

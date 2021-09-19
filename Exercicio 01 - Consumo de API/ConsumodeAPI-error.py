import requests

url = 'https://viacep.com.br/'
abc ='abc/'
formato = '/json/'


r = requests.get(url + abc)

if (r.status_code == 200):
    print()
    print('JSON : ', r.json())
    print()
else:
   print('O erro foi o',r.status_code,r.reason)
   print('Nao houve sucesso na requisicao.')

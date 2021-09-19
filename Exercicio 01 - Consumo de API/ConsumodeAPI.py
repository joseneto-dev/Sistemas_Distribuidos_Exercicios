import requests

url = 'https://viacep.com.br/ws/'
cep = ['30140071','30140072','30140073','30140074','30140075']
formato = '/xml/'
count = 0

if count <= 5:
 for item in cep:
  r = requests.get(url + item + formato)
  count+=1
  if (r.status_code == 200):
    print()
    print('JSON : ', r.text)
    print()
  else:
    print('Nao houve sucesso na requisicao.')

import requests
r = requests.get('http://www.google.com/search', params={'q': 'Jose Duarte de Abreu Neto'})
if (r.status_code == 200):
    print()
    print('Retorno : ', r.text)
    arq=open('c:\\Users\\josep\Desktop\\d_google.html','w')
    arq.write(r.text)
    arq.close()
else:
    print('Nao houve sucesso na requisicao.')

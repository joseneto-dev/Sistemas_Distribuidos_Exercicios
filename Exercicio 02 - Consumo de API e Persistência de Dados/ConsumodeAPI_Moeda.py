import requests
import sqlite3

url ='https://api.hgbrasil.com/finance?format=json-cors&key='
key='58c3756e'

r = requests.get(url+key)
print(r.text)

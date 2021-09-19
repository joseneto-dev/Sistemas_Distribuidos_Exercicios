pais_a = 80000
pais_b = 200000

anos = 0

print('Populacao Pais A: ', pais_a)
print('Populacao Pais B: ', pais_b)

while pais_a <= pais_b:
    pais_a = pais_a * 1.03
    pais_b = pais_b * 1.015
    anos = anos + 1
    print(pais_a,anos)
print('Numero de anos para igualar ou ultrapassar a populacao:{anos}'.format(anos=anos))

print('Nova populacao Pais A: ', pais_a)
print('Nova populacao Pais B: ', pais_b)

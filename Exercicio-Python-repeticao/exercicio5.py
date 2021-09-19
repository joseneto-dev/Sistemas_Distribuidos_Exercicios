pais_a =int(input("Digite a população do País A: "))
pais_b =int(input("Digite a população do País A: "))
taxapais_a = float(input("Digite a taxa de crescimento do Pais A: "))
taxapais_b = float(input("Digite a taxa de crescimento do Pais B: "))
anos = 0

final=taxapais_a/100+1
finalb=taxapais_b/100+1

print('Populacao Pais A: ', pais_a)
print('Populacao Pais B: ', pais_b)

while pais_a <= pais_b:
    pais_a = pais_a * final
    pais_b = pais_b * finalb
    anos = anos + 1
print('Numero de anos para igualar ou ultrapassar a populacao:{anos}'.format(anos=anos))

print('Nova populacao Pais A: ', pais_a)
print('Nova populacao Pais B: ', pais_b)

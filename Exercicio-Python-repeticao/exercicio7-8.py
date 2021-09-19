from statistics import median
lista = []
for n in range(1,6):
    lista.append(int(input('Digite o número '+ str(n) + ': ')))

print ('Soma dos números: ', sum(lista))
print ('Media dos números: ', median(lista))
print ('Maior número da lista: ', max(lista))
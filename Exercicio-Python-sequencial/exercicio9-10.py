faren=float(input("Digite a temperatura em Farenheit : "))
celsius=float(input("Digite a temperatura em Celsius : "))

celsius_convert=(5*(faren-32)/9)
faren_convert=((celsius*9/5)+32)

print("A temperatura de {f} °F e igual a {cc} °C".format(f=faren,cc=celsius_convert))
print("A temperatura de {c} °C e igual e {fc}".format(c=celsius,fc=faren_convert))
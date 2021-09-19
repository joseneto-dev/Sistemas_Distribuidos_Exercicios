horav=float(input("Quanto você recebe pela hora : "))
horat=float(input("Quantas horas você trabalhou : "))

salary=horav*horat

print(f"O salário ao final pelas {horat} horas trabalhadas e de {salary} reais".format(horat=horat,salary=salary))
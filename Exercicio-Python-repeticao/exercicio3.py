

nome = str(input('Digite o seu nome: '))
while (len(nome) < 3):
 print("O nome deve ter no minimo 3 caracteres")
 nome = str(input('Digite o seu nome: '))

idade= int(input("Digite sua idade: "))
while (idade < 0 or idade > 150):
 print("A idade deve estar entre 0 e 150")
 idade= int(input("Digite sua idade: "))


salario=float(input("Digite o seu salario : "))
while(salario <= 0):
 print("Salario Invalido")
 salario = float(input("Digite o seu salario : "))

sexo = str(input('Digite o seu sexo:\nLembre-se de digitar\nM para Homems\nF para mulheres\n '))
while (sexo !="M" and sexo!="F"):
 sexo = str(input('Digite o seu sexo:\nLembre-se de digitar\nM para Homems\nF para mulheres\n '))


estado_civil =str(input('Digite o seu estado civil:\nLembre-se de digitar\nS para solteiros\nC para Casada\nD para desquitada\n'))
while ( estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D" ):
 estado_civil = str(input('Digite o seu estado civil:\nLembre-se de digitar\nS para solteiros\nC para Casada\nD para desquitada\n'))

print("O seu nome e {nome}, você possui {anos} e do sexo {sexo} possui um salario de {salario} e o estado civil e {estado}".format(nome=nome,anos=idade,sexo=sexo,salario=salario,estado=estado_civil))
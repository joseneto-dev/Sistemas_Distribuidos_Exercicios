nota1=int(input("Digite a primeira nota: "))
nota2=int(input("Digite a segunda nota: "))

media=nota1+nota2/2

if(media >=10):
    print("Aprovado com Distinção")
elif(media<7):
    print("Reprovado")
else:
    print("Aprovado")

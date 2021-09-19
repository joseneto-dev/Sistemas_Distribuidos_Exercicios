print("Faça um programa que peça uma nota, entre zero e dez. "
      "\nMostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.")
num = int(input("Digite um valor entre zero e dez: "))
while (num < 0) or (num > 10):
    print("O valor está Incorreto")
    num = int(input("Digite um valor entre zero e dez: "))
else:
    print("O valor está Correto")

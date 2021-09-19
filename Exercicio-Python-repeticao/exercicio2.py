print('Esse programa foi feito para verificar se sua senha está igual ao nome ')
nome = input('Digite o seu nome: ')
senha = input('Digite a sua senha: ')
while nome == senha:
    print("A sua senha está igual ao nome")
    nome = input('Digite o seu nome: ')
    senha = input('Digite a sua senha: ')

print("Senha e nome diferentes, Obrigado!")

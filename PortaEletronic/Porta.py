import random

sen = open('password', 'w')
print('Gerando Senha!')
cadas_quarto = str(random.randint(1000, 2000))

sen.write('{}\n'.format(cadas_quarto))
print('Cadastrado!')

sen.close()

entrou = False
while not entrou:

    # Leitura
    sen = open('password')
    senha = input('Digite: ')

    registrado = sen.readline()
    if senha in registrado:
        print('Aberto!')
        entrou = True
    else:
        print('Erro!')
    sen.close()

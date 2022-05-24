def menu():
    print('''\nEscolha uma opção:
    1. Cadastrar uma pessoa!
    2. Listar pessoas cadastradas
    3. Procurar dados de uma pessoa''')


def cadastrar(pessoas):
    identificador = input('Id: ')
    nome = input('Nome: ')
    idade = input('Idade: ')
    pessoas.append((identificador, nome, idade))

def listar(pessoas):
    for pessoa in pessoas:
        identificador, nome, idade = pessoa
        print(f'Id: {identificador}, Nome: {nome}, Idade: {idade}')

def buscar(pessoas):
    identificador_desejado = input('Id: ')
    for pessoa in pessoas:
        identificador, nome, idade = pessoa
        if identificador == identificador_desejado:
            print(f'Id: {identificador}, Nome: {nome}, Idade: {idade}')
        else:
            print(f'Pessoa com id {identificador_desejado} não encontrado')

def main():
    pessoas = []

    while True:
        menu()
        opcao = int(input('Opção: '))
        if opcao == 1:
            cadastrar(pessoas)
        elif opcao == 2:
            listar(pessoas)
        elif opcao == 3:
            buscar(pessoas)
        else:
            print('Opção inválida')
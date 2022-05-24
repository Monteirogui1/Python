import string
import random

tamanho_senha = int(input("Qual o tamanho da Senha: "))
valores = string.digits + string.punctuation + string.ascii_letters
senha = []

def gerar():
    for i in range(0, tamanho_senha):
        senha.append(random.choice(valores))
    print("".join(senha))


gerar()



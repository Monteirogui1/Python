import string
import random
from time import time


senha = []


def gerayquebra():
    t_senha = int(input("Digite o tamanho da senha: "))
    valores = string.digits + string.punctuation + string.ascii_letters
    for i in range(0, t_senha):
        senha.append(random.choice(valores))
    print("A senha é: " + "".join(senha))

gerayquebra()
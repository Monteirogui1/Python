num1 = int(input("Digite um Valor: "))

if(num1 > 10):
    print("O valor é maior do que 10!")
    if(num1 <= 15):
        print("O valor é maior que 10, porem menor do que 15!")
    else:
        if(num1 <= 50):
            print("O valor é maior do que 10, porem menor do que 50!")
        else:
            print("O valor é maior que 50!")
        if (num1 >= 60):
            print("O valor é maior ou igual a 60!")

else:
    if(num1 > 5):
        print("O valor é menor do que 10, porem maior do que 5!")
        if(num1 == 7):
            print("O valor é igual a 7!")
        else:
            print("O valor é menor do que 5!")
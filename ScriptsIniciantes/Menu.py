
print("========================")
print("     Menu    ")
print("========================")
print("[1] - Menu1")
print("[2] - Menu2")
print("[3] - Menu3")
print(" ")
res = int(input("Opcao: "))

    
if res == 1:
    add.adicionar()
elif res == 2:

    while 1:

        # um menu secundario
        print("[1] - Sub1")
        print("[2] - Sub2")
        print("[3] - Sub3")
        print("[4] - Voltar")

        res = int(input("Opcao: "))
        if res == 1:
            listar.mostraSub1()
        elif res == 2:
            listar.mostraSub2()
        elif res == 3:
            listar.mostraSub3()
        elif res == 4:
            break
        else:
            print("ERRO: A opção não se encontra defenida ! tente novamente!")
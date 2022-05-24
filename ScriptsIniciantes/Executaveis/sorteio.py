import random
while True:
    print ('Menu:\n 1 - Ataque\n 2 - Defesa ')

    opcao = input('Escolha uma opção: ')


    ataque = ['SLEDGE', 'THATCHER', 'ASH', 'THERMITE', 'MONTAGNE', 'TWITCH', 'BLITZ', 'IQ', 'FUZE', 'GLAZ', 'BUCK', 'LION', 'ZOFIA', 'FINKA', 'DOKKAEBI', 'YING', 'JACKAL', 'HIBANA', 'CAPITAO', 'BLACKBEARD']
    defesa = ['VIGIL', ' ELA', 'LESION', 'MIRA', 'ECHO', 'CAVEIRA', 'VALKYRIE', 'FROST', 'MUTE', 'SMOKE', 'CASTLE', 'PULSE', 'DOC', 'ROOK', 'JAGER', 'BANDIT', 'TACHANKA', 'KAPKAN']

    if opcao == '1':
        print ('O sorteado foi: ', ataque[random.randrange(len(ataque))])
    elif opcao == '2':
        print ('O sorteado foi: ', defesa[random.randrange(len(defesa))])


    resortear = input('Resortear? s/n ')

    if resortear not in ("s"):
        break

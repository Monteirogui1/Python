import base64

with open("./image/logo.png", 'rb') as arquivo:
    arquivo_64 = base64.b64encode(arquivo.read())

    print(arquivo_64)
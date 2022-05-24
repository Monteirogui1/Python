import random


class Celular:
    def __init__(self, fabricante, modelo, tela, armazenamento, memoria, camera, bateria, tela_ligada, porcentagem):
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = armazenamento
        self.memoria = memoria
        self.camera = camera
        self.bateria = bateria
        self.tela_ligada = tela_ligada
        self.porcentagem = porcentagem

    def ligar_tela(self):
        self.tela_ligada = True

    def verificar_carga_bateria(self):
        self.porcentagem = random.randint(1, self.porcentagem)

        # Print na tela uma porcentagem e o valor correspondente em mA
        calculo_porcen = self.porcentagem / 100
        mA = self.bateria * calculo_porcen
        print(f"O celular está com {self.porcentagem}% e {mA:.0f} mA restantes")


# Posicional
celular_android = Celular("Samsung", "S22", 6.25, 128, 8, 40, 3400, False, 100)

# Sem ser Posicional
celular_iphone = Celular(modelo="Iphone 13 Pro", tela=5.75, memoria=4, camera=30,
                         bateria=2800, armazenamento=128, fabricante="Apple", tela_ligada=False, porcentagem=100)

celular_iphone.ligar_tela()

print(celular_iphone.tela_ligada)

celular_iphone.verificar_carga_bateria()

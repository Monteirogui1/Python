# http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/resultado.htm/!ut/p/a1
# /jY_LCoJAGIWfxQeoOXl3OWroiJIQmc0mBsoLeMOmFj19Fm1aZP1n9cN3zuEQTnLCO3GrSyHrvhPN8
# -fm0VzFCBEgAlNtUH2dqlmUabC1CThMgBfQULdiALqtgvlu6FtOAjDzPz--HMUvf_RHgTomXlISPghZLequ6Ek
# -ni_XRopTv6xkS_aEf8YEqWeAbnzXgTYJxhuY2_kCZoYM7S6_x8WWlYryANb0FnM!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw
# /Z7_HGK818G0K8DBC0QPVN93KQ10G1/res/id=historicoHTML/c=cacheLevelPage/=/

# Junta tudo ai

while True:
    print("")
    numeros = int(input("Digite um numero: "))

    esquerda = [1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52,
                53,
                54, 55]
    direita = [6, 7, 8, 9, 10, 16, 17, 18, 19, 20, 26, 27, 28, 29, 30, 36, 37, 38, 39, 40, 46, 47, 48, 49, 50, 56, 57,
               58, 59, 60]

    if numeros in esquerda:
        print("Esquerda")
    elif numeros in direita:
        print("Direita")
    else:
        print("erro")

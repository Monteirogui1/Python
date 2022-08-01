
from datetime import date
import os
import sys
import time
import requests
import json

nome_cond = []
valor_total = []
valor_final = []

os.chdir(sys.path[0])

atual = date.today()
data_f = atual.strftime("%d_%m")
mes = atual.strftime("%m")
data_c = atual.strftime("%m/%d/%Y")

contador = 0

i = [4, 6, 7, 8, 9, 10, 11, 12 , 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]

for id in i:
  url = f"https://api.superlogica.net/v2/condor/cobranca/index?status=liquidadas&apenasColunasPrincipais=1&exibirPgtoComDiferenca=1&comContatosDaUnidade=1&filtrarpor=liquidacao&dtInicio={mes}/01/2022&dtFim={data_c}&idCondominio={id}&itensPorPagina=130&pagina=1&comDadosDasUnidades=1&exibirDadosDoContato=1"

  payload={}
  headers = {
      'Content-Type': 'application/json',
      'app_token': '29b9ac1d-ad7a-4a67-aed0-f8502771d00c',
      'access_token': '08d4b378-199c-4479-aecd-cc9f4173e496'
    }

  response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text["vl_total_recb"])


  data_dict = json.loads(response.text)

  valor_cond = []
  unidade = []

  for cond in data_dict[:1]:
    nome_cond.append(cond["st_nome_cond"])  

  for ap, valor, cond in zip(data_dict[:200], data_dict[:200], data_dict[:200]):     
    #print('Aguarde!!')
    #print(f'A unidade {ap["st_complemento_con"]} Valor {valor["vl_total_recb"]}  ')
    valor_cond.append(valor["vl_total_recb"])
    unidade.append(ap["st_complemento_con"])
    
  contador += 1
  print(f'{contador} --Aguarde--')
  NList = [float(string) for string in valor_cond]
  sum1 = sum(NList)
  valor_total.append(sum1)
  #print(f"Valor do {nome_cond} recebido: {sum1:.2f}")
  

NValor = [float(v) for v in valor_total]
resultado = sum(NValor)
valor_final.append(resultado)
#print('------------------------------------------------------------------')
#print(f"Valor Total: {resultado:.2f}")

with open(f'{data_f}Receita_dos_Condomínios.txt', 'w', encoding='utf-8') as arquivo:
  for c, vt in zip(nome_cond, valor_total):
    arquivo.write(f'{c}: {vt:.2f} \n')
  for vf in valor_final:
    arquivo.write(f'\n A Receita Total é de: {vf:,.2f}')
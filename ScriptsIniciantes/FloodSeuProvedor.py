#*
#* 
#* Autor: Guilherme Monteiro
#*
#*

#!/usr/bin/python
import os
import sys
import csv
import datetime
import time
import twitter
 
def test():
 
        #run speedtest-cli
        print 'running test'
        a = os.popen("python /home/pi/speedtest/speedtest-cli --simple").read()
        print 'ran'
        #dividir o resultado da 3 linha (ping,down,up)
        lines = a.split('\n')
        print a
        ts = time.time()
        date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #Se não foi possível conectar speedtest definir as velocidades de 0
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        #Extrair os valores de ping baixo e para cima dos valores
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
        print date,p, d, u
        #Salvar os dados em arquivo para plotting de rede local
        out_file = open('/var/www/assets/data.csv', 'a')
        writer = csv.writer(out_file)
        writer.writerow((ts*1000,p,d,u))
        out_file.close()
 
        #Conectar no twitter
        TOKEN=""
        TOKEN_KEY=""
        CON_SEC=""
        CON_SEC_KEY=""
 
        my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
        twit = twitter.Twitter(auth=my_auth)
 
        #Tente twittear se o Speedtest não puder se conectar. Provavelmente não funcionará se a internet estiver baixa
        if "Cannot" in a:
                try:
                        tweet="Olá @Provedor porque minha internet esta baixa? Eu pago 20down\\20up? "
                        twit.statuses.update(status=tweet)
                except:
                        pass
 
        # Tweet se a velocidade abaixo for menor que o que eu configurei
        elif eval(d)<18:
                print "trying to tweet"
                try:
                        # Sei que deve haver uma maneira melhor do que fazer (str(int(eval())))
                        tweet="Olá @Provedor porque minha velocidade de internet " + str(int(eval(d))) + "down\\" + str(int(eval(u))) + "enquanto eu pago 20down\\20up? @Provedor #speedtest"
                        twit.statuses.update(status=tweet)
                except Exception,e:
                        print str(e)
                        pass
        return
       
if _name_ == '_main_':
        test()
        print 'completed'

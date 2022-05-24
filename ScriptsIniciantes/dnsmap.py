# Cor
D = "\033[0m";
W = "\033[01;37m";
O = "\033[01;33m";
SUCESS = "\033[01;32m";
FAIL = "\033[01;31m";

import socket
import sys
import os

os.system("cls")

print (W + "")
domain = input("Set domain: ")  # www.domain.com

try:
    ip = socket.gethostbyname(domain)

except socket.gaierror:

    print (FAIL + 'Dominio Invalido.\n\n\n\n\n\n\n')

    sys.exit()

    print (SUCESS + "+-------------------------+")

    print (SUCESS + "| DNS   : " + ip + "     |")

    print (SUCESS + "+-------------------------+")

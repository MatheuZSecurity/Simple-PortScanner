#!/usr/bin/env python3

import socket
import sys

# https://youtube.com/c/MatheuZSecuriy

def banner():
       print("""
...................................................


         _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
    dZP        qKRb
    dZP          qKKb    Criado Por Matheuz Security
   fZP            SMMb
   HZM            MMMM        Simple Port Scan
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--'


...................................................
""")

def scan():
       ports = [21,22,23,25,53,80,88,110,119,137,138,139,143,156,161,389,443,445,512,513,3306,8080]

       print("Port          Service        State\n\n")
       for port in ports:
              client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              resp = client.connect_ex((target,port))
              
              if(resp == 0):
                     print(f"{port}              {socket.getservbyport(port)}           open\n")
              else:
                     print(f"{port}              {socket.getservbyport(port)}           closed\n")

       client.close()

try:  
        target = sys.argv[1]
        if(sys.argv == 1):
            print("Usage: python3 scan.py TARGET")
        else:
            banner()
            scan()

except KeyboardInterrupt:
       print("Exit...")
       quit()
except socket.gaierror:
        print("Host not found")
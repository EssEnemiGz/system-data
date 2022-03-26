"""
Datos del sistema.
By: EssEnemiGz
"""

from requests import get
from sys import argv
from random import randint
from subprocess import run
import time

def command(commands):
    output = run(commands.split(":"), capture_output=True)
    return output.stdout.decode()

class main:
    def welcome(self):
        F = open("/etc/os-release")
        e=[i.strip() for i in F.readlines()]
        OS = e[0][6:].replace('"','')

        name = command("whoami")
        
        rColor = randint(31, 36) 
        rColor = f"\033[1;{rColor}m"      
        print(command(f'cowsay:-f:tux:"Welcome back to {OS}, {rColor}{name}\033[0m"'))
         
    def IP(self):
        try:
            import socket

            socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
            socket.connect( ("8.8.8.8", 88) ) 
            print(f"\033[1;34m Private IP -> {socket.getsockname()[0]} \033[0m")
        except OSError:
            print("\033[1;31m Error:\033[0m La conexión está deshabilitada.")
    def battery(self):
        def color(capacity):
            if int(capacity) >= 35 and int(capacity) < 65:
                return "\033[1;33m"
            elif int(capacity) >= 65:
                return "\033[1;32m"
            elif int(capacity) < 35:
                return "\033[1;31m"

        def batteryStatus(argv):
            if argv == "Unknown" or argv == "Charging":
                return f"\033[1;32m Status -> Charging"
            elif argv == "Discharging":
                return f"\033[1;31m Status -> {argv}"
        
        ruta = command("find:/sys/class/power_supply").split()
        nuevaRuta = ""
        for i in ruta:
            if "BAT" in i:
                nuevaRuta = i
            else:
                continue
        
        capacity = open(f"{nuevaRuta}/capacity").read().strip()
        print(f"{color(capacity)} Capacity -> {capacity}% \033[0m")
        
        status = open(f"{nuevaRuta}/status").read().strip()

        if status == "Discharging":
            print(f"\033[1;31m Status -> {status} \033[0m")
        elif status == "Unknown":
            print(f"\033[1;36m Status -> Full \033[0m")
        else:
            print(f"\033[1;32m Status -> {status} \033[0m")

objeto = main()

if len(argv) == 1:
    objeto.welcome()
    # Tiempo
    print(f"    \033[1;35m Hour: \033[0m \033[1;33m {time.strftime('%X')} \033[0m")
    objeto.IP()
    objeto.battery()
    
elif argv[1] in ["-p", "--public"] :
    ip = get("http://ipecho.me").content.decode('utf-8').strip()
    print(f"\033[1;31m Public IP -> {ip}\033[0m")
    

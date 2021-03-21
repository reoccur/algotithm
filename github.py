import requests
import threading
import colorama
import os
from colorama import *

def menu():
    os.system('cls')
    print(f'''{Fore.RED}
   ▄████████  ▄█          ▄██████▄   ▄██████▄     ▄████████  ▄█      ███        ▄█    █▄      ▄▄▄▄███▄▄▄▄   
  ███    ███ ███         ███    ███ ███    ███   ███    ███ ███  ▀█████████▄   ███    ███   ▄██▀▀▀███▀▀▀██▄ 
  ███    ███ ███         ███    █▀  ███    ███   ███    ███ ███▌    ▀███▀▀██   ███    ███   ███   ███   ███ 
  ███    ███ ███        ▄███        ███    ███  ▄███▄▄▄▄██▀ ███▌     ███   ▀  ▄███▄▄▄▄███▄▄ ███   ███   ███ 
▀███████████ ███       ▀▀███ ████▄  ███    ███ ▀▀███▀▀▀▀▀   ███▌     ███     ▀▀███▀▀▀▀███▀  ███   ███   ███ 
  ███    ███ ███         ███    ███ ███    ███ ▀███████████ ███      ███       ███    ███   ███   ███   ███ 
  ███    ███ ███▌    ▄   ███    ███ ███    ███   ███    ███ ███      ███       ███    ███   ███   ███   ███ 
  ███    █▀  █████▄▄██   ████████▀   ▀██████▀    ███    ███ █▀      ▄████▀     ███    █▀     ▀█   ███   █▀  
             ▀                                   ███    ███                                                    
    
    
''')
    
    m = input(' [!] ')
    if m == "github":
        github()
    if m == "repl.it":
        repl()
    if m == "1":
        github()
    if m == '2':
        repl()

def repl():
    list = str(input(" [!] "))
    with open(list, 'r') as h:
        os.system('cls')
        usernames = [ line.strip() for line in h.read().split('\n') if line ]
        for name in usernames:
            r = requests.get(f"https://repl.it/@" + name)
            if(r.status_code == 404):
                print(f'{Fore.GREEN}[!]{Fore.WHITE} {name} {Fore.GREEN} [!]')
            else: 
                print(f'{Fore.RED}[X]{Fore.YELLOW} {name} {Fore.RED} [X]')
                
        

def github():
    list = str(input(" [!] "))
    with open(list, 'r') as h:
        os.system('cls')
        usernames = [ line.strip() for line in h.read().split('\n') if line ]
        for name in usernames:
            r = requests.get(f"https://github.com/" + name)
            if(r.status_code == 404):
                print(f'{Fore.GREEN}[!]{Fore.WHITE} {name} {Fore.GREEN} [!]')
            else: 
                print(f'{Fore.RED}[X]{Fore.YELLOW} {name} {Fore.RED} [X]')
            
        
menu()
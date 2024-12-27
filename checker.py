import requests
import os
import json
import uuid
import random
import ctypes
import concurrent.futures

from datetime import date, datetime, timedelta
from datetime import datetime as dt, timedelta, timezone as tz
from random import choice, choices
from colorama import Fore, init
from sys import stdout
from pystyle import *

os.system("cls")

nombre =0
valides = 0
invalides = 0

Write.Print(f"""
 _____  _                       _                      
|  __ \(_)                     | |                     
| |  | |_ ___  ___ ___  _ __ __| |  ___ ___  _ __ ___  
| |  | | / __|/ __/ _ \| '__/ _` | / __/ _ \| '_ ` _ \ 
| |__| | \__ \ (_| (_) | | | (_| || (_| (_) | | | | | |
|_____/|_|___/\___\___/|_|  \__,_(_)___\___/|_| |_| |_|\n\n""", Colors.blue_to_purple, interval=0)

threads = int(input(f"{Fore.LIGHTMAGENTA_EX}Threads ->{Fore.RESET} "))
print(f"")

proxies = open("proxies.txt", 'r').read().splitlines()

def obtenir_proxy():
    proxy = random.choice(proxies)
    return {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

def checker(pseudo):
    global nombre, valides, invalides

    try:
        headers = {
            "Accept": "*/*",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wKChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEyMS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyMS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIxLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjYwMTAxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
            "X-Fingerprint": "1198031150283751475.sPxZAtEn6vEJHJ_Bvd13C8AKxpA",
            "X-Discord-Locale": "fr",
            "X-Discord-Timezone": "Europe/Paris",
            "X-Debug-Options": "bugReporterEnabled",
            "Origin": "https://discord.com",
            "Referer": "https://discord.com/register",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
            "Content-Type": "application/json",
        }

        proxy = obtenir_proxy()

        cookie = str(uuid.uuid4())

        body = {
            "username": pseudo,
        }
        json_ = json.dumps(body)

        headers = headers.copy()
        headers["Cookie"] = f"__dcfduid={cookie}"

        try:
            requete = requests.post("https://discord.com/api/v9/unique-username/username-attempt-unauthed", headers=headers, data=json_, proxies=proxy, timeout=5)

            if "taken" in requete.text and "false" in requete.text:
                valides += 1
                stdout.write(f"\r{Fore.GREEN}[{Fore.WHITE}Nombre : {nombre}/{len(pseudos)}{Fore.GREEN}] {Fore.WHITE}> {Fore.GREEN}[{Fore.WHITE}Pseudo : {pseudo}{Fore.GREEN}]{Fore.RESET}")
                stdout.flush()
                with open("valides.txt", 'a') as ff:
                    ff.write(f"{pseudo}\n")
            else:
                invalides += 1
                
        except:
            pass

    except:
        pass

    ctypes.windll.kernel32.SetConsoleTitleW(f"Nombre : {nombre}/{len(pseudos)} | Valides : {valides} | Invalides : {invalides}")

with open("pseudos.txt", "r", encoding="utf-8") as f:
    pseudos = f.read().splitlines()

with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    executor.map(checker, pseudos)

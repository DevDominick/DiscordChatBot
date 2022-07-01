import json
import os
import random
import time
import requests
from colorama import Fore, Style, init

messages = []
tokens = []
delay = 0
count = 0

init(convert=True)

color = f'{Fore.RED}{Style.BRIGHT}'

banner = f"""{color}

             ___  _   _    __   ____  ____  _____  ____ 
            / __)( )_( )  /__\ (_  _)(  _ \(  _  )(_  _)
           ( (__  ) _ (  /(__)\  )(   ) _ < )(_)(   )(  
            \___)(_) (_)(__)(__)(__) (____/(_____) (__) 

{color} 
"""

print(banner)

SERVER_ID = input(f"""Server ID: """)
CHANNEL_ID = input(f"""Channel ID: """)

if __name__ == '__main__':
    print("Reading messages from messages.txt")
    print("Starting...")
    with open('tokens.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tokens.append(line.replace('\n', ''))
    with open('messages.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        messages.append(line.replace('\n', ''))
    while True:
        for token1 in tokens:
            message_num = random.randint(0, len(messages)-1)
            message_send = requests.post(f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages',
                                         headers={
                                             "Accept": "*/*",
                                             "Accept-Encoding": "gzip, deflate, br",
                                             "Accept-Language": "ko",
                                             "Authorization": token1,
                                             "Content-Type": "application/json",
                                             "origin": "https://discord.com",
                                             "referer": f"https://discord.com/channels/{SERVER_ID}/{CHANNEL_ID}",
                                             "sec-fetch-dest": "empty",
                                             "sec-fetch-mode": "cors",
                                             "sec-fetch-site": "same-origin",
                                             "user-agent": "",
                                             "x-debug-options": "bugReporterEnabled",
                                             "x-discord-locale": "en-US",
                                             "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC40MyIsIm9zX3ZlcnNpb24iOiIxMC4wLjE5MDQ0Iiwib3NfYXJjaCI6Ing2NCIsInN5c3RlbV9sb2NhbGUiOiJrbyIsImNsaWVudF9idWlsZF9udW1iZXIiOjExMjY3MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                                         }, data=json.dumps({
                                            "content": messages[message_num],
                                            "nonce": random.randint(9999999999, 999999999999),
                                            "tts": False
                                         }))
            time.sleep(delay)
            print("Sent Message")
            os.system("title ChatBot V1")
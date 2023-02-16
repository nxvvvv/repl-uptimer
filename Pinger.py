from os import system
import socket
from time import sleep
import json
import httpx as requests
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def ping(website=None):
    try:
        requests.get(f"https://{website}")
        return True
    except:
        try:
            requests.get(f"http://{website}")
            return True
        except:
            try:
                requests.get(website)
                return True
            except:
                return False

sites = ['']#Put websites to monitor here. For putting multiple sites, use this format 'website1','website2','website3'

while True:
    status = '\n'
    for site in sites:
        output = ping(site)
        if output == True:
            status = f'{status}{site} is up\n'
        else:
            status = f'{status}{site} is down\n'
    print(f'{status}\n')
    sleep(10)
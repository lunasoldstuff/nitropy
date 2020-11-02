from pathlib import Path
import requests
import time
import string
import threading
import random
import json

valid = 0
invalid = 0

characters = string.ascii_letters + string.digits

home = Path.home()

config = Path(home + '/.config/nitropy/config.json')
proxies = Path(home + '/.config/nitropy/proxies.txt')

if config.exists():
    # print("test")
    f = json.loads(config)

    proxy = f['type']
    thread = f['threads']
else:
    thread_number = int(input(" > Number of threads?\n > "))
    proxy_type = input(" > HTTP or HTTPS\n > ").lower()

    data ={
        "threadCount": {
            "threads": thread_number
        },
        "proxyType": {
            "type": proxy_type
        }
    }

    with open(config, "w") as write_file:
        json.dump(data, write_file)
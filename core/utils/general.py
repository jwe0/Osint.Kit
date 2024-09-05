import os, json
from core.utils.logging import info
def ascii_art():
    art = """

  ___  ____ ___ _   _ _____ _  ___ _   
 / _ \/ ___|_ _| \ | |_   _| |/ (_) |_ 
| | | \___ \| ||  \| | | | | ' /| | __|
| |_| |___) | || |\  | | |_| . \| | |_ 
 \___/|____/___|_| \_| |_(_)_|\_\_|\__|

> Developed by scale, neebooo and jwe0
"""

    print(art)

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def dump_json(json_data):
    if not json_data:
        return "No data"
    message  = ""
    keys = []
    vals = []
    for key, value in json_data.items():
        keys.append(key)
        vals.append(value)

    key_pad = max([len(x) for x in keys])
    for i in range(len(keys)):
        message += info(f"{keys[i].upper()}{' ' * int(key_pad - len(keys[i]))} : {vals[i] if vals[i] else 'No value'}\n", "2")
    message = message[:-1]
    return message

def load_config():
    with open("core/config.json", "r") as f:
        return json.load(f)
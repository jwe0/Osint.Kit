import os, json
from colorama import Fore
from core.utils.logging import info, warning, error, inpt
def ascii_art():
    art = """

  ___  ____ ___ _   _ _____ _  ___ _   
 / _ \/ ___|_ _| \ | |_   _| |/ (_) |_ 
| | | \___ \| ||  \| | | | | ' /| | __|
| |_| |___) | || |\  | | |_| . \| | |_ 
 \___/|____/___|_| \_| |_(_)_|\_\_|\__|

> Developed by neebooo and jwe0
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

def load_bugs():
    with open("core/deps/bugs.json", "r") as f:
        return json.load(f)
    
def is_bug(module):
    bugs = load_bugs()
    modules = bugs.get("Modules")
    if module in modules:
        index = modules.index(module)
        bug = bugs.get("Bugs")[index]
        info("Found a bug!")
        if bug.get("severity") == "low":
            info("Title: " + bug.get("title"))
            info("Description: " + bug.get("description"))
            info("Severity: " + bug.get("severity"))
        elif bug.get("severity") == "medium":
            warning("Title: " + bug.get("title"))
            warning("Description: " + bug.get("description"))
            warning("Severity: " + bug.get("severity"))
        elif bug.get("severity") == "high":
            error("Title: " + bug.get("title"))
            error("Description: " + bug.get("description"))
            error("Severity: " + bug.get("severity"))
        return

    
def format_json(data):
    def json_format(data, dump={}):
        for key, value in data.items():
            if isinstance(value, dict):
                json_format(value)
            elif isinstance(value, list):
                dump[key] = ", ".join(value)
            else:
                dump[key] = value
        return dump
    dump = json_format(data)
    return dump

def modify_config(args):
    config = load_config()
    keys = [key for key in config.get("API_KEYS").keys()]
    for key, value in config.get("API_KEYS").items():
        info(f"[{keys.index(key) + 1}] {key}")
    choice = inpt("What API key do you want to modify? ")
    while not choice:
        choice = inpt("What API key do you want to modify? ")
    choice = int(choice) - 1
    info(f"Selected: {keys[choice]}")
    new = inpt("New value: ")
    config["API_KEYS"][keys[choice]] = new
    with open("core/config.json", "w") as f:
        json.dump(config, f, indent=4)
    return {"message" : "success", "info" : {"choice" : keys[choice], "new" : new}}


def columnit(array, size=10):
    def style(array):
        results = []
        for ar in array:
            results.append(f"[{array.index(ar) + 1}] {ar}")
        return results
    def pad(array, size=10):
        while len(array) % size != 0:
            array.append(" ")
        return array
    def gen_pad(array):
        results = []
        for ar in array:
            pad = max(len(x) for x in ar)
            sub = []
            for x in ar:
                sub.append(x.ljust(pad))
            results.append(sub)
        return results
    array = pad(style(array), size)
    result = []
    message = ""
    for i in range(0, len(array), size):
        result.append(array[i:i + size])
    sub = ""
    result = gen_pad(result)
    for i in range(len(result[0])):
        for j in range(len(result)):
            if j > 0:
                sub += f" {Fore.LIGHTBLACK_EX}|{Fore.RESET} "
            sub += result[j][i]
        message += sub + "\n"
        sub = ""
    return message

def credits():
    msg = """
[!] /jwe0
[-] Wassup, my name is Josh and I am the creator and lead developer of this project.
[-] I developed this product in september 2024 because when performing OSINT I had to constantly
[-] go out to different tool sites and download a bunch of repositories so I decided to put all
[-] of those tools into one piece of software for you to enjoy
[=] github.com/jwe0
[=] jwe0.xyz
"""
    print(msg)
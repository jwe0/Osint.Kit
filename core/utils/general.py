import os, json
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
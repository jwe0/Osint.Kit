import os
def ascii_art():
    art = """

  ___  ____ ___ _   _ _____ _  ___ _   
 / _ \/ ___|_ _| \ | |_   _| |/ (_) |_ 
| | | \___ \| ||  \| | | | | ' /| | __|
| |_| |___) | || |\  | | |_| . \| | |_ 
 \___/|____/___|_| \_| |_(_)_|\_\_|\__|

"""

    print(art)

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def dump_json(json_data):
    keys = []
    vals = []
    for key, value in json_data.items():
        keys.append(key)
        vals.append(value)

    key_pad = max([len(x) for x in keys])

    for i in range(len(keys)):
        print(f"{keys[i]}{' ' * int(key_pad - len(keys[i]))}{vals[i]}")
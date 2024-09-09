import json, os, socket
from core.utils.logging import *
from core.utils.general import ascii_art, clear

def config():
    if not os.path.exists("core/config.json"):
        clear()
        ascii_art()
        warning("Creating config...")
        api_recs = [
            {"IPLookup"      : "Ipgeolocation.io API Key"}, 
            {"DiscordToken"  : "Discord Token"},
            {"192Cookie"     : "192.com Cookie"}, 
            {"IntelligenceX" : "Intelx.io API Key"}, 
            {"HypixelAPI"    : "Hypixel API Key"}
        ]
        config = {}
        config["OS"]       = os.name
        config["PCNAME"]   = socket.gethostname()
        config["API_KEYS"] = {}
        warning("API Keys (Press enter to skip)")
        for api in api_recs:
            for key, value in api.items():
                config["API_KEYS"][key] = inpt(f"{value}: ")
        with open("core/config.json", "w") as f:
            json.dump(config, f, indent=4)
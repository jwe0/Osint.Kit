import json, os, socket
from core.utils.logging import *
from core.utils.general import ascii_art, clear

def config():
    if not os.path.exists("core/config.json"):
        clear()
        ascii_art()
        warning("Creating config...")
        api_recs = ["IPLookup", "DiscordToken","192Cookie", "IntelligenceX"]
        config = {}
        config["OS"]       = os.name
        config["PCNAME"]   = socket.gethostname()
        config["API_KEYS"] = {}
        warning("API Keys")
        for api in api_recs:
            config["API_KEYS"][api] = inpt(f"{api} API Key: ")
        with open("core/config.json", "w") as f:
            json.dump(config, f, indent=4)
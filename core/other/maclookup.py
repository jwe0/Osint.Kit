import json
# https://github.com/Tanathy/OUI-lookup <--- Oui source

def maclookup(args):
    mac = args.get("mac", "")
    if not mac:
        return {"message" : "error", "info" : "Please provide the MAC address"}
    ouis = json.load(open("core/deps/oui.json"))
    mac = mac.replace("-", "").replace(":", "").upper()[:6]
    oui_info = ouis["ouis"].get(mac)
    if not oui_info:
        return {"message" : "error", "info" : "MAC address not found"}
    country = ouis["countries"][oui_info["cc"]]
    organization = ouis["organizations"][oui_info["org"]]
    data = {
        "mac" : mac,
        "oui" : oui_info,
        "country" : country,
        "organization" : organization
    }
    return {"message" : "success", "info" : data}

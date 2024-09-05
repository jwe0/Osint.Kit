import json, tls_client
from core.utils.general import load_config
def IpLookup(args):
    config = load_config()
    session = tls_client.Session()
    ip_address = args.get("IP", "")
    api_key    = config.get("API_KEYS", {}).get("IPLookup", "")
    if not ip_address:
        return {"message" : "error", "info" : "You did not supply IP information"}
    elif not api_key:
        return {"message" : "error", "info" : "You did not supply an API key"}
    
    api = "https://api.ipgeolocation.io/ipgeo?apiKey={}&ip={}&excludes=currenct,time_zone,currency".format(api_key, ip_address)
    r = session.get(api)
    if r.status_code == 200:
        return {"message" : "success", "info" : r.json()}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}
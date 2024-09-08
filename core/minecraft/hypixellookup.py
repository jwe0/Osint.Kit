import tls_client, datetime
from core.utils.general import load_config

def convert_time(time):
    seconds = time / 1000.0
    readable = datetime.datetime.fromtimestamp(seconds)
    return readable.strftime("%Y-%m-%d %H:%M:%S")

def hypixel_lookup(args):
    username = args.get("username", "")
    if not username:
        return {"message" : "error", "info" : "Please provide a username"}
    session = tls_client.Session()
    config = load_config()

    key = config["API_KEYS"]["HypixelAPI"]
    url = f"https://api.hypixel.net/player?key={key}&name={username}"
    r = session.get(url)
    if r.status_code == 200:
        decode = r.json()
        data = {
            "uuid" : decode.get("player").get("uuid"),
            "displayname" : decode.get("player").get("displayname"),
            "rank" : decode.get("player").get("rank"),
            "package_rank" : decode.get("player").get("packageRank"),
            "new_package_rank" : decode.get("player").get("newPackageRank"),
            "monthly_Package_Rank" : decode.get("player").get("monthlyPackageRank"),
            "first_login" : convert_time(decode.get("player").get("firstLogin")),
            "last_login" : convert_time(decode.get("player").get("lastLogin")),
            "last_logout" : convert_time(decode.get("player").get("lastLogout")),
        }
        return {"message" : "success", "info" : data}
    return {"message" : "error", "info" : f"Hypixel Lookup Failed {str(r.status_code)}"}
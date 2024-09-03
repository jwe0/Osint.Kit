import tls_client
from core.utils.logging import *
from core.utils.general import load_config

def IdLookup(args):
    config = load_config()
    session = tls_client.Session()
    log = {}
    discord_id = args.get("id", "")

    if not discord_id:
        return {"message" : "error", "info" : "You did not supply ID information"}
    elif not config.get("API_KEYS", {}).get("DiscordToken", ""):
        return {"message" : "error", "info" : "You did not supply an API key"}
    
    api = "https://discord.com/api/v9/users/{}/profile".format(discord_id)
    headers = {
        "Authorization" : config.get("API_KEYS", {}).get("DiscordToken", "")
    }
    r = session.get(api, headers=headers)
    if r.status_code == 200:
        decode = r.json()
        user = decode.get("user")
        accs = decode.get("connected_accounts")
        bads = decode.get("badges") if "badges" in decode else []
        log = {
            "id" : user.get("id"),
            "username" : user.get("username"),
            "global_name" : user.get("global_name"),
            "avatar" : user.get("avatar"),
            "avatar_decoration" : user.get("avatar_decoration_data"),
            "public_flags" : user.get("public_flags"),
            "clan" : user.get("clan"),
            "flags" : user.get("flags"),
            "banner" : user.get("banner"),
            "banner_color" : user.get("banner_color"),
            "accent_color" : user.get("accent_color"),
            "bio" : "\\n".join(user.get("bio").splitlines()) if user.get("bio") else "",
            "premium_since" : user.get("premium_since"),
            "premium_type" : user.get("premium_type"),
            "connected" : ", ".join([f"[ {user.get('type')} : {user.get('name')} : {user.get('id')} ] " for user in accs])
        }
        if bads:
            log["badges"] = ", ".join([f"[ {user.get('id')} : {user.get('description')} ] " for user in bads])
        return {"message" : "success", "info" : log}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}
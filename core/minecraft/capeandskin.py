import json, tls_client, base64

def UserToId(session, username):
    api = "https://api.mojang.com/users/profiles/minecraft/{}".format(username)
    r = session.get(api)
    if r.status_code == 200:
        return r.json().get("id")
    return ""
def CapeAndSkin(args):
    session = tls_client.Session()
    username = args.get("username", "")

    if not username:
        return {"message" : "error", "info" : "You did not supply username information"}
    id = UserToId(session, username)
    if not id:
        return {"message" : "error", "info" : "Username not found"}
    api = "https://sessionserver.mojang.com/session/minecraft/profile/{}".format(id)
    r = session.get(api)
    if r.status_code == 200:
        decode = r.json()
        value  = json.loads(base64.b64decode(decode.get("properties")[0].get("value")))
        data = {
            "id" : decode.get("id"),
            "name" : decode.get("name"),
            "timestamp" : value.get("timestamp"),
            "profileid" : value.get("profileId"),
            "profile_name" : value.get("profileName"),
            "skin" : value.get("textures").get("SKIN").get("url"),
            "cape" : value.get("textures").get("CAPE").get("url"),

        }
        return {"message" : "success", "info" : data}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}
import tls_client
def UsernameToId(args):
    session = tls_client.Session()
    username = args.get("username", "")
    if not username:
        return {"message" : "error", "info" : "You did not supply username information"}

    api = "https://api.mojang.com/users/profiles/minecraft/{}".format(username)
    r = session.get(api)
    if r.status_code == 200:
        return {"message" : "success", "info" : r.json()}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}
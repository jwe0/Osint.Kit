import tls_client, hashlib
from core.utils.logging import info

def hash(server):
    x = hashlib.sha1()
    x.update(server.encode("utf-8"))
    return x.hexdigest()

def IsBlocked(args):
    session = tls_client.Session()
    server = args.get("server", "")

    if not server:
        return {"message" : "error", "info" : "You did not supply server information"}
    api  = "https://sessionserver.mojang.com/blockedservers"
    hash_ = hash(server)
    info(f"Hash: {hash_}")
    r = session.get(api)
    servers = r.text.splitlines()
    if hash(server) in servers:
        return {"message" : "success", "info" : "Server is blocked"}
    else:
        return {"message" : "error", "info" : "Server is not blocked"}
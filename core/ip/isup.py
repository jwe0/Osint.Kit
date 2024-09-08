import tls_client, socket

def verify_https(url):
    session = tls_client.Session()
    try:
        r = session.get(url)
        if r.status_code == 200:
            return True
    except:
        return False
    return False

def verify_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except:
        return False

def isup(args):
    target = args.get("target", "")
    if not target:
        return {"message" : "error", "info" : "Please provide the target"}
    web = verify_https(target)
    ip = verify_ip(target)
    data = {
        "web" : web,
        "ip" : ip
    }
    return {"message" : "success", "info" : data}
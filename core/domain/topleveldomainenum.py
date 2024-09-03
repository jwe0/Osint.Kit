import tls_client, threading, socket

prog = 0
data = {}

def load_tlds():
    return open("core/deps/topleveldomains.txt", "r").read().splitlines()

def check(url):
    global prog
    global data
    try:
        socket.gethostbyname(url)
        data[url] = True
        prog += 1
    except:
        prog += 1

def TopLevelDomainEnum(args):
    session = tls_client.Session()

    site = args.get("domain", "")
    if not site:
        return {"message" : "error", "info" : "You did not supply domain information"}

    tlds = load_tlds()
    site = site.replace("https://", "").replace("http://", "")
    for tld in tlds:
        url = f"{site}.{tld}"
        threading.Thread(target=check, args=(url,)).start()

    while int(len(tlds)) != int(prog):
        pass
    return {"message" : "success", "info" : data}
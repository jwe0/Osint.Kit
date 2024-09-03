import tls_client, socket, threading

prog = 0
data = {}

def load_subs():
    return open("core/deps/subdomains.txt", "r").read().splitlines()

def check(url):
    global prog
    global data
    try:
        socket.gethostbyname(url)
        prog += 1
        data[url] = True
    except:
        prog += 1
        

def SubdomainEnum(args):
    session = tls_client.Session()

    site = args.get("domain", "")
    if not site:
        return {"message" : "error", "info" : "You did not supply domain information"}

    domains = load_subs()
    site = site.replace("https://", "").replace("http://", "")
    for domain in domains:
        url = f"{domain}.{site}"
        threading.Thread(target=check, args=(url,)).start()

    while int(len(domains)) != int(prog):
        pass
    return {"message" : "success", "info" : data}
        

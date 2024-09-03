import tls_client, threading, socket

prog = 0
data = {}

def load_dirs():
    return open("core/deps/subdirectories.txt", "r").read().splitlines()

def check(url, session):
    global prog
    global data
    try:
        r = session.get(url)
        if r.status_code == 200:
            data[url] = True
            prog += 1
    except:
        prog += 1

def DirectoryEnum(args):
    global prog
    global data
    session = tls_client.Session()

    site = args.get("domain", "")
    if not site:
        return {"message" : "error", "info" : "You did not supply domain information"}
    elif "https://" not in site and "http://" not in site:
        return {"message" : "error", "info" : "You did not supply http or https information"}
    
    dirs = load_dirs()
    for dir in dirs:
        url = f"{site}/{dir}"
        threading.Thread(target=check, args=(url, session,)).start()
    
    while int(len(dirs)) != int(prog):
        pass
    return {"message" : "success", "info" : data}
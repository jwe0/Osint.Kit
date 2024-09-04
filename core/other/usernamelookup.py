import tls_client, json, threading
from bs4 import BeautifulSoup
prog = 0
data = {}

def search(site_, username, session):
    global prog
    global data
    url       = site_.get("url")
    method    = site_.get("type")
    check_val = site_.get("check-value")
    url = url.format(username)
    r = session.get(url.format(username))
    if method == "status-code":
        if r.status_code == check_val:
            data[url] = True
    elif method == "site-content":
        if check_val in r.text:
            data[url] = True
    elif method == "title-content":
        soup = BeautifulSoup(r.text, "html.parser")
        if not soup.title:
            prog += 1
            return
        if check_val in soup.title.text:
            data[url] = True
    prog += 1

def UserLookup(args):
    global prog
    global data
    session = tls_client.Session()

    username = args.get("username", "")

    if not username:
        return {"message" : "error", "info" : "You did not supply username information"}
    
    sites = json.loads(open("core/deps/sites.json", "r").read())
    for site in sites:
        site_     = sites.get(site)
        threading.Thread(target=search, args=(site_, username, session)).start()
    while int(len(sites)) != int(prog):
        pass
    
    return {"message" : "success", "info" : data}
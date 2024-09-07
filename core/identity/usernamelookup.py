import tls_client, json, threading
from bs4 import BeautifulSoup
from core.identity.userlookup_extra.github import git_search
from core.identity.userlookup_extra.minecraft import mc_search
prog = 0
data = {}

def search_extra(site_, username, session, html, json):
    soup = BeautifulSoup(html, "html.parser")
    extra = {}
    sites = {
        "https://github.com/{}" : git_search,
        "https://api.mojang.com/users/profiles/minecraft/{}" : mc_search
    }
    if site_ .get("url") in sites:
        extra = sites[site_.get("url")](username, session, soup, json)
    return extra

def check(r, method, check_val):
    global prog
    if method == "status-code":
        if r.status_code == check_val:
            return True
    elif method == "site-content":
        if check_val in r.text:
            return True
    elif method == "title-content":
        soup = BeautifulSoup(r.text, "html.parser")
        if not soup.title:
            return False
        if check_val in soup.title.text:
            return True
    prog += 1
    return False

def make_decode(r):
    try:
        return r.json()
    except:
        return {}

def search(site_, username, session):
    global prog
    global data
    url       = site_.get("url")
    method    = site_.get("type")
    check_val = site_.get("check-value")
    url = url.format(username)
    r = session.get(url.format(username))
    checked = check(r, method, check_val)
    decode = make_decode(r)
    if checked:
        details = search_extra(site_, username, session, r.text, decode)
        data[url] = details
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
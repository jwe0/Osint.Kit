import re, dns.resolver, tls_client, time
from core.utils.general import load_config

def validate_domain(email):
    domain = email.split("@")[-1]
    try:
        records = dns.resolver.resolve(domain, "MX")
        return True if records else False
    except:
        return False

def validate_regex(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def intelligencex(email):
    retries = 10
    session = tls_client.Session()
    API = load_config().get("API_KEYS").get("IntelligenceX")
    def search(email):
        headers = {
            "x-key" : API,
            "User-Agent" : "IX-Python/0.6"
        }
        data = {
            "term" : email,
            "buckets" : ["leaks.public"],
            "lookuplevel" : 0,
            "maxresults" : 1000,
            "timeout" : 5,
            "datefrom" : "",
            "dateto" : "",
            "sort" : 4,
            "media" : 0,
            "terminate" : []
        }
        time.sleep(1)
        r = session.post("https://2.intelx.io/intelligent/search", headers=headers, json=data)
        if r.status_code == 200:
            if r.json().get("status") == 1:
                return r.json().get("status")
            return r.json().get("id")
        else:
            return False
        
    def results(id):
        time.sleep(1)
        headers = {
            "x-key" : API,
            "User-Agent" : "IX-Python/0.6"
        }
        r = session.get(f"https://2.intelx.io/intelligent/search/result?id={id}&limit=100", headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            return False
        
    def terminate(id):
        time.sleep(1)
        headers = {
            "x-key" : API,
            "User-Agent" : "IX-Python/0.6"
        }
        r = session.get(f"https://2.intelx.io/intelligent/search/terminate?id={id}", headers=headers)
        if r.status_code == 200:
            return True
        else:
            return False

    def dump(results):
        print("dump api")
        dumps = []
        dump = results.get("records")
        for d in dump:
            dumps.append(d.get("name"))
        return dumps

    id = search(email)
    results_ = results(id)
    tries = 1
    while not results_:
        time.sleep(5)
        results_ = results(id)
        tries += 1
        if tries > retries:
            break
    terminate(id)
    if not results_:
        return {"message" : "error", "info" : "IntelligenceX did not return results"}
    return dump(results_)


def email_lookup(args):
    email = args.get("email", "")
    report = {}
    if not email:
        return {"message" : "error", "info" : "You did not supply email information"}
    report = {
        "domain_validate" : validate_domain(email),
        "regex_validate" : validate_regex(email),
    }
    intell = intelligencex(email)
    if "error" not in intell:
        for dump in intell:
            report[dump] = True
    return {"message" : "success", "info" : report}

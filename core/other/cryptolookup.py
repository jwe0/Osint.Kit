import tls_client, json
from bs4 import BeautifulSoup

def search(session, address):
    api = "https://www.blockchain.com/explorer/search"
    data = {"search": address}
    r = session.post(api, json=data)
    if r.status_code == 200:
        decode = r.json()
        return decode
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}

def balance(session, address, chain):
    api = "https://api.blockchain.info/haskoin-store/{}/address/{}/balance".format(str(chain).lower(), address)
    r = session.get(api)
    if r.status_code == 200:
        decode = r.json()
        return decode
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}

def get_transactions(session, address, chain):
    api = "https://api.blockchain.info/haskoin-store/{}/address/{}/transactions?limit=20&offset=0".format(str(chain).lower(), address)
    r = session.get(api)
    if r.status_code == 200:
        decode = r.json()
        return decode
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}

def Cryptolookup(args):
    data = {}
    session = tls_client.Session()

    address = args.get("address", "")

    if not address:
        return {"message" : "error", "info" : "You did not supply address information"}

    results = search(session, address)
    if "error" in results:
        return {"message" : "error", "info" : results.get("info")}
    wallet = results[0]
    bal = balance(session, wallet.get("search"), wallet.get("chain"))
    trn = get_transactions(session, wallet.get("search"), wallet.get("chain"))

    data = {
        "address" : bal.get("address"),
        "confirmed" : bal.get("confirmed"),
        "unconfirmed" : bal.get("unconfirmed"),
        "utxo" : bal.get("utxo"),
        "txs" : bal.get("txs"),
        "received" : bal.get("received"),
        "transaction_ids" : ", ".join(trx.get("txid") for trx in trn)
    }
        
    
    return {"message" : "success", "info" : data}
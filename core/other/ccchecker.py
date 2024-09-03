import json, tls_client
def Checker(args):
    session = tls_client.Session()
    card = args.get("BIN", "")
    if not card:
        return {"message" : "error", "info" : "You did not supply card information"}
    
    api = "https://lookup.binlist.net/{}".format(args.get("BIN"))
    response = session.get(
        api,
        headers={
            "Accept-Version" : "3"
        }
    )

    if response.status_code == 200:
        return {"message" : "success", "info" : json.loads(response.json())}
    else:
        return {"message" : "error", "info" : f"{str(response.status_code)} : {response.text if response.text else 'Unknown error'}"}
    
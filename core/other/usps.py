import tls_client
def USPSLookup(args):
    session = tls_client.Session()
    data = {}
    address = args.get("code", "")

    if not address:
        return {"message" : "error", "info" : "You did not supply address information"}
    api = "https://tools.usps.com/tools/app/ziplookup/cityByZip"
    data = {"zip" : address}
    r = session.post(api, data=data)
    if r.status_code == 200:
        return {"message" : "success", "info" : r.json()}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}
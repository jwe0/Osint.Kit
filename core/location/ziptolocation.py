import tls_client
def ZIPtoLocation(args):
    session = tls_client.Session()
    log = {}
    address = args.get("code", "")
    if not address:
        return {"message" : "error", "info" : "You did not supply address information"}
    api = "https://tools.usps.com/tools/app/ziplookup/cityByZip"
    data = {"zip" : address}
    r = session.post(api, data=data)
    if r.status_code == 200:
        decode = r.json()
        log = {
            "resultStatus" : decode.get("resultStatus"),
            "zip5" : decode.get("zip5"),
            "defaultCity" : decode.get("defaultCity"),
            "defaultState" : decode.get("defaultState"),
            "defaultRecordType" : decode.get("defaultRecordType"),
            "nonAcceptList" : ", ".join(f"{user.get('city')} : {user.get('state')}" for user in decode.get("nonAcceptList"))
        }
        return {"message" : "success", "info" : log}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}
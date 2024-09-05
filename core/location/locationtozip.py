import tls_client
def LocationtoZIP(args):
    session = tls_client.Session()
    log = {}
    address = args.get("address", "")
    city    = args.get("city", "")
    state   = args.get("state", "")
    if not address or not city or not state:
        return {"message" : "error", "info" : "You did not supply address information"}
    api = "https://tools.usps.com/tools/app/ziplookup/zipByAddress"
    data = {
        "companyName" : "",
        "address1" : address,
        "address2" : "",
        "city" : city,
        "state" : state,
        "urbanCode" : "",
        "zip" : ""
    }
    r = session.post(api, data=data)
    if r.status_code == 200:
        decode = r.json()
        if decode.get("resultStatus") == "SUCCESS":
            location = decode.get("addressList")[0]
            return {"message" : "success", "info" : location}
        else:
            return {"message" : "error", "info" : decode}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}
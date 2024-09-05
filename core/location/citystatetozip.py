import tls_client
def CitystateToZIP(args):
    session = tls_client.Session()
    city    = args.get("city", "")
    state   = args.get("state", "")
    if not city or not state:
        return {"message" : "error", "info" : "You did not supply address information"}
    api = "https://tools.usps.com/tools/app/ziplookup/zipByCityState"
    #city=queens&state=NY
    data = {
        "city" : city,
        "state" : state
    }
    r = session.post(api, data=data)
    if r.status_code == 200:
        decode = r.json()
        if decode.get("resultStatus") == "SUCCESS":
            dump = {}
            location = decode.get("zipList")
            for loc in location:
                dump[loc.get("zip5") if "zip5" in loc else loc.get("zip4")] = loc.get("recordType")
            return {"message" : "success", "info" : dump}
        else:
            return {"message" : "error", "info" : decode}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}
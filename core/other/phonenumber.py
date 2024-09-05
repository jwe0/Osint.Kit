import phonenumbers, json
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

def get_info(number):
    number = number.strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    def search(dump, code):
        return dump.get(code)
    with open("core/deps/callingcodes.json", "r") as f:
        codes = json.load(f)
    number = number.removeprefix("+")
    info   = search(codes, number[:3])
    if not info:
        info = search(codes, number[:2])
    if not info:
        info = search(codes, number[:1])
    if not info:
        return ""
    return info

def Phonenumber(args):
    number = args.get("phone", "")
    data = {}
    if not number:
        return {"message" : "error", "info" : "You did not supply phone number information"}
    try:
        dump = get_info(number)
        number = phonenumbers.parse(number)
        carrier_ = carrier.name_for_number(number, "en")
        region   = geocoder.description_for_number(number, "en")
        time     = timezone.time_zones_for_number(number)
        data = {
            "carrier" : carrier_,
            "region" : region,
            "time" : time
        }
        if dump:
            for key, value in dump.items():
                data[key] = value
        return {"message" : "success", "info" : data}
    except Exception as e:
        dump = get_info(number)
        if dump:
            return {"message" : "success", "info" : dump}
        return {"message" : "error", "info" : "Invalid phone number"}
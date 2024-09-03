import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
def Phonenumber(args):
    number = args.get("phone", "")
    data = {}
    if not number:
        return {"message" : "error", "info" : "You did not supply phone number information"}
    try:
        number = phonenumbers.parse(number)
        carrier_ = carrier.name_for_number(number, "en")
        region   = geocoder.description_for_number(number, "en")
        time     = timezone.time_zones_for_number(number)
        data = {
            "carrier" : carrier_,
            "region" : region,
            "time" : time
        }
        return {"message" : "success", "info" : data}
    except:
        return {"message" : "error", "info" : "Invalid phone number"}
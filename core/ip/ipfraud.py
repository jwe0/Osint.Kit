import tls_client
from bs4 import BeautifulSoup

def scrape(ip, session):
    api = "https://scamalytics.com/ip/{}".format(ip)
    r = session.get(api)
    soup = BeautifulSoup(r.text, "html.parser")
    rating = soup.find("div", {"class" : "panel_title high_risk"})
    score  = soup.find("div", {"class" : "score"})
    rating = rating.text if rating else "Unknown"
    score  = score.text if score else "Unknown"
    return {"rating" : rating, "score" : score}

def IpFraud(args):
    session = tls_client.Session()

    ip = args.get("ip", "")

    if not ip:
        return {"message" : "error", "info" : "You did not supply ip information"}

    data = scrape(ip, session)
    return {"message" : "success", "info" : data}
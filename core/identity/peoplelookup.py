from core.utils.general import load_config
import tls_client
from bs4 import BeautifulSoup
import random

def PeopleLookup(args: dict):
    config = load_config()
    sess = tls_client.Session(client_identifier=random.choice(["chrome112", "firefox129"]))
    name = args.get("name", "")
    location = args.get("location", "").strip()
    data = f"looking_for={name}&location={location}&searchBtn=Search" if location else f"looking_for={name}&searchBtn=Search"
    res = sess.post(
        "https://www.192.com/people/search/",
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www.192.com",
            "Referer": "https://www.192.com/people/",
            "Cookie": config.get("API_KEYS", {}).get("192Cookie", "")
        },
    )
    soup = BeautifulSoup(res.text, "html.parser")
    elements_with_text_class = soup.find_all(class_='ont-people-premium-result-item')
    people = []
    for elem in elements_with_text_class:
        soup = BeautifulSoup(str(elem), 'lxml')
        name = soup.find(class_='test-name').text
        addr = soup.find(class_='test-address').text
        people.append({
            "name": name,
            "address": addr
        })
    return {"message": "success", "info": {"people": people}}
import tls_client, urllib
from bs4 import BeautifulSoup
from core.utils.general import format_json
def FindCVE_NVD_NIST(args):
    search = args.get("search")
    if not search:
        return {"message" : "error", "info" : "You did not supply search information"}
    vulns = {}
    exploits = {}
    session = tls_client.Session()
    dist = "https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query={}&search_type=all&isCpeNameSearch=false".format(urllib.parse.quote(search))
    r = session.get(dist)
    soup = BeautifulSoup(r.text, 'html.parser')
    tbody = soup.find('tbody')
    tr_ = tbody.find_all('tr')
    for tr in tr_:
        th  = tr.find('th').get_text().strip()
        td  = tr.find('td').find('span').get_text().strip()
        warning = "MEDIUM" if "MEDIUM" in tr.find('td', nowrap='nowrap').get_text().strip() else ("HIGH" if "HIGH" in tr.find('td', nowrap='nowrap').get_text().strip() else "Undocumented CVE level")
        vulns[th] = {
            "SEVERITY" : warning, 
            "CVE" : th, 
            "LINK" : "https://nvd.nist.gov/vuln/detail/{}".format(th)
        }
    for vuln in vulns:
        exploits[vuln] = f"{vulns.get(vuln).get("SEVERITY")} : {vulns.get(vuln).get('CVE')} : {vulns.get(vuln).get('LINK')}"
        
    return {"message" : "success", "info" : exploits}
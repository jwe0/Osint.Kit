import tls_client
from core.utils.general import format_json
def WebhookInfo(args):
    hook = args.get("webhook", "")
    if not hook:
        return {"message" : "error", "info" : "You did not supply webhook information"}
    session = tls_client.Session()

    r = session.get(hook)
    if r.status_code == 200:
        return {"message" : "success", "info" : format_json(r.json())}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}

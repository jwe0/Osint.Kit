import tls_client
from core.utils.general import format_json
def DiscordInvInfo(args):
    session = tls_client.Session()
    invite = args.get("invite", "")

    if not invite:
        return {"message" : "error", "info" : "You did not supply invite information"}

    api = "https://discord.com/api/v10/invites/{}".format(invite)

    r = session.get(api)
    if r.status_code == 200:
        decode  = r.json()
        return {"message" : "success", "info" : format_json(decode)}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}
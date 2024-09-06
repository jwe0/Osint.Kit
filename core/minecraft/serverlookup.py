import tls_client
from core.utils.general import format_json

def flatten_json(nested_json, parent_key='', separator='_'):
    """
    Recursively flattens a nested JSON.
    
    :param nested_json: The JSON to flatten
    :param parent_key: Prefix for keys (used during recursion)
    :param separator: Separator between parent and child keys
    :return: A flattened dictionary
    """
    items = []
    
    for k, v in nested_json.items():
        new_key = f"{parent_key}{separator}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, separator=separator).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.extend(flatten_json({f"{new_key}_{i}": item}, '', separator=separator).items())
        else:
            items.append((new_key, v))
    
    return dict(items)

def MCServerLookup(args):
    session = tls_client.Session()

    server = args.get("server", "")
    if not server:
        return {"message" : "error", "info" : "You did not supply server information"}

    api = "https://api.mcsrvstat.us/3/{}".format(server)

    r = session.get(api)
    if r.status_code == 200:
        decode = r.json()
        dump = {}
        flattened = flatten_json(decode)
        for key, value in flattened.items():
            if key != "icon":
                dump[key] = value
        return {"message" : "success", "info" : dump}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}
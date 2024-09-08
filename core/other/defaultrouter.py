import json

def router(args):
    results = []
    model = args.get("model", "")
    brand = args.get("brand", "")
    if not model:
        if not brand:
            return {"message" : "error", "info" : "Please provide the router model"}
    dump = json.load(open("core/deps/routers.json"))
    for i in dump:
        if i.get("model") == model:
            results.append(i)
        if brand:
            if i.get("brand") == brand:
                results.append(i)
    if results:
        data = {}
        brands = []
        models = []
        protoc = []
        usernm = []
        passwr = []
        for i in results:
            brands.append(i.get("brand"))
            models.append(i.get("model"))
            protoc.append(i.get("protocol"))
            usernm.append(i.get("username"))
            passwr.append(i.get("password"))
        data = {
            "brands" : ", ".join(brands) if len(brands) > 1 else brands[0],
            "models" : ", ".join(models) if len(models) > 1 else models[0],
            "protoc" : ", ".join(protoc) if len(protoc) > 1 else protoc[0],
            "usernm" : ", ".join(usernm) if len(usernm) > 1 else usernm[0],
            "passwr" : ", ".join(passwr) if len(passwr) > 1 else passwr[0],
        }
        return {"message" : "success", "info" : data}
    
    return {"message" : "error", "info" : "Router not found"}
def mc_search(username, session, soup, json):
    id = json.get("id")
    username = json.get("name")
    return f"[ Username: {username} | ID: {id} ]"

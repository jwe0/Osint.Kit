def get_username(session, soup):
    title = soup.find("title")
    return title.get_text().strip().split(" · GitHub")[0]

def git_search(username, session, soup):
    user = get_username(session, soup) 
    if not user:
        user = "None"
    return f"Username: {user}"
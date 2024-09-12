import os, json
from core.utils.logging import info, inpt

def add(file):
    info("Add user")
    name    = inpt("Name: ")
    age     = inpt("Age: ")
    address = inpt("Address: ")
    phone   = inpt("Phone: ")
    email   = inpt("Email: ")
    file.append({
        "name"    : name or "",
        "age"     : age  or "",
        "address" : address or "",
        "phone"   : phone or "",
        "email"   : email or ""
    })
    json.dump(file, open("core/deps/userdb.json", "w"), indent=4)
    return {"message" : "success", "info" : "User added"}
def edit(file):
    info("Edit user")
    name    = inpt("Name: ")
    age     = inpt("Age: ")
    address = inpt("Address: ")
    phone   = inpt("Phone: ")
    email   = inpt("Email: ")
    for user in file:
        if user["name"] == name:
            user["age"] = age
            user["address"] = address
            user["phone"] = phone
            user["email"] = email
            break
    json.dump(file, open("core/deps/userdb.json", "w"), indent=4)
    return {"message" : "success", "info" : "User edited"}
def search(file):
    info("Search user")
    name = inpt("Name: ")
    for user in file:
        if user["name"] == name:
            return user
def remove(file):
    info("Remove user")
    name = inpt("Name: ")
    for user in file:
        if user["name"] == name:
            file.remove(user)
            json.dump(file, open("core/deps/userdb.json", "w"), indent=4)
    
    return {"message" : "success", "info" : "User removed"}

def list(file):
    info("List users")
    for user in file:
        info(f"{user['name']}, {user['age']}, {user['address']}, {user['phone']}, {user['email']}")
    return {"message" : "success", "info" : "Users listed"}

def userdb(args):
    if not os.path.isfile("core/deps/userdb.json"):
        with open("core/deps/userdb.json", "w") as f:
            json.dump([], f)
    file = json.load(open("core/deps/userdb.json"))
    modes = [
        ("add",    add), 
        ("edit",   edit), 
        ("search", search), 
        ("remove", remove), 
        ("list",   list)
    ]
    for mode in modes:
        info(f"[{modes.index(mode) + 1}] {mode[0]}")
    choice = inpt("Choice: ")
    if int(choice) - 1 not in range(len(modes)):
        return {"message" : "error", "info" : "Invalid choice"}
    data = modes[int(choice) - 1][1](file)
    return {"message" : "success", "info" : data}
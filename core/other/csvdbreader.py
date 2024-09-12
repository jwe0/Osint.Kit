import csv, os
from core.utils.logging import inpt, info

def csvdbreader(args):
    path = args.get("path")
    if not path:
        return {"message" : "error", "info" : "You did not supply the required information"}
    if not os.path.exists(path):
        return {"message" : "error", "info" : "File not found"}
    reader = csv.reader(open(path, "r"))
    rows   = [row for row in reader]
    for item in rows[0]:
        info(f"[{rows[0].index(item) + 1}] {item}")
    choice = inpt("Choice: ")
    search = inpt("Search: ")
    choice = int(choice) - 1
    results = {}
    for row in rows[1:]:
        if search in row[choice]:
            results[row[0]] = row[choice]
    if not results:
        return {"message" : "error", "info" : "No results found"}
    return {"message" : "success", "info" : results}
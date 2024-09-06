import socket

def getbanner(args):
    ip = args.get("IP")
    port = args.get("port")

    if not ip or not port:
        return {"message" : "error", "info" : "You did not supply ip information"}
    s = socket.socket()
    try:
        s.settimeout(5)
        s.connect((ip, int(port)))
        banner = s.recv(1024).decode().strip()
        s.close()
    except:
        return {"message" : "error", "info" : "Could not connect to server"}
    if banner:
        return {"message" : "success", "info" : {"banner" : banner}}
    else:
        return {"message" : "error", "info" : "Banner not found"}
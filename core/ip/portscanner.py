import socket, json, threading

data = {}
progress = 0

def load_common_ports():
    return json.load(open("core/deps/common_ports.json"))

def load_registered_ports():
    return json.load(open("core/deps/registered_ports.json"))

def check_port(s, ip, port, common, registered):
    global data, progress
    con = s.connect_ex((ip, int(port)))
    if con == 0:
        info = common.get(str(port)) if common.get(str(port)) else (registered.get(str(port)) if registered.get(str(port)) else "Unknown")
        if info != "Unknown":
            info = f"{info.get('service')}, {info.get('protocols')}"
        data[str(port)] = info
    progress += 1

def portscan(args):
    global progress, data
    ip = args.get("IP", "")
    end   = args.get("endport") if args.get("endport") else 10000
    if not ip:
        return {"message" : "error", "info" : "You did not supply ip information"}

    common_ports      = load_common_ports()
    regisetered_ports = load_registered_ports()

    for i in range(int(end)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        threading.Thread(target=check_port, args=(
            s,
            ip,
            i,
            common_ports,
            regisetered_ports,
        )).start()

    while progress != end:
        pass

    return {"message" : "success", "info" : data}
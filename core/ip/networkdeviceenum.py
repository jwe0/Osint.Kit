from scapy.all import ARP, Ether, srp
import threading

devices  = {}
progress = 0

def check(ip):
    global devices, progress
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered, _ = srp(arp_request_broadcast, timeout=2, verbose=False)
    if answered:
            devices[ip] = answered[0][1].hwsrc
    progress += 1

def netenum(args):
    global devices, progress
    base = args.get("base")
    if not base:
        return {"message": "error", "info": "You did not supply base information"}
    ip_base = ".".join(str(base).split(".")[:3])
    for i in range(1, 256):
        ip = f"{ip_base}.{i}"
        threading.Thread(target=check, args=(ip,)).start()
    while progress != 255:
        pass
    return {"message": "success", "info": devices}
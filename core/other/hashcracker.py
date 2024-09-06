import hashlib, threading, tls_client, os

dump = {}
prog = 0
crck = False


def hash_check(algorithm, password):
    if algorithm == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == "sha224":
        return hashlib.sha224(password.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == "sha384":
        return hashlib.sha384(password.encode()).hexdigest()
    elif algorithm == "sha512":
        return hashlib.sha512(password.encode()).hexdigest()
    elif algorithm == "sha3_224":
        return hashlib.sha3_224(password.encode()).hexdigest()
    elif algorithm == "sha3_256":
        return hashlib.sha3_256(password.encode()).hexdigest()
    elif algorithm == "sha3_384":
        return hashlib.sha3_3844(password.encode()).hexdigest()
    elif algorithm == "sha3_512":
        return hashlib.sha3_512(password.encode()).hexdigest()
    elif algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == "shake_128":
        return hashlib.shake_128(password.encode()).hexdigest(16)
    elif algorithm == "shake_256":
        return hashlib.shake_256(password.encode()).hexdigest(16)
    else:
        return {"message" : "error", "info" : "Invalid algorithm"}

def crack(passord, hash, algorithm):
    global prog, dump, crck
    if hash_check(algorithm, passord) == hash:
        dump = {"hash" : hash, "password" : passord}
        crck = True
    prog += 1

def web_passwords(url):
    return [pw.strip() for pw in tls_client.Session().get(url).text.split("\n")]

def disk_passwords(path):
    return [pw.strip() for pw in open(path, "r", errors="ignore").readlines()]

def interpret_wordlist(wordlist):
    if not wordlist:
        return web_passwords("https://raw.githubusercontent.com/drtychai/wordlists/master/fasttrack.txt")
    if "https" or "http" in wordlist:
        return web_passwords(wordlist)
    elif os.path.exists(wordlist):
        return disk_passwords(wordlist)

def hashcracker(args):
    global prog, dump, crck
    hash = args.get("hash")
    algr = args.get("algorithm")
    wordlist = args.get("wordlist") 
    if not hash or not algr:
        return {"message" : "error", "info" : "You did not supply hash information"}
    test = hash_check(algr, hash)
    if "error" in test:
        return {"message" : "error", "info" : test.get("info")}
    passwords_ = interpret_wordlist(wordlist)
    for password in passwords_:
        threading.Thread(target=crack, args=(password, hash, algr)).start()

    while not crck:
        if int(len(passwords_)) == int(prog):
            break
        pass
    if dump:
        return {"message" : "success", "info" : dump}
    else:
        return {"message" : "error", "info" : "Password not found"}
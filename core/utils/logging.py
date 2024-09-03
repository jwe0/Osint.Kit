from datetime import datetime
from colorama import Fore

def success(message, mode="1"):
    if mode == "1":
        print(f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.GREEN}✓{Fore.RESET}]\t{message}")
    elif mode == "2":
        return f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.GREEN}✓{Fore.RESET}]\t{message}"


def error(message, mode="1"):
    if mode == "1":
        print(f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.RED}🗙{Fore.RESET}]\t{message}")
    elif mode == "2":
        return f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.RED}🗙{Fore.RESET}]\t{message}"

def warning(message, mode="1"):
    if mode == "1":
        print(f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.YELLOW}!{Fore.RESET}]\t{message}")
    elif mode == "2":
        return f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.YELLOW}!{Fore.RESET}]\t{message}"

def info(message, mode="1"):
    if mode == "1":
        print(f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.BLUE}I{Fore.RESET}]\t{message}")
    elif mode == "2":
        return f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.BLUE}I{Fore.RESET}]\t{message}"

def inpt(message):
    return input(f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.CYAN}I{Fore.RESET}]\t{message}")
from datetime import datetime
from colorama import Fore

def success(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.GREEN}✓{Fore.RESET}]\t{message}")

def error(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.RED}🗙{Fore.RESET}]\t{message}")

def warning(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.YELLOW}!{Fore.RESET}]\t{message}")

def info(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.BLUE}I{Fore.RESET}]\t{message}")

def inpt(message):
    return input(f"[{datetime.now().strftime('%H:%M:%S')}]\t[{Fore.CYAN}I{Fore.RESET}]\t{message}")
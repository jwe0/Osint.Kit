import tls_client
from colorama import Fore
# Core modules
from core.utils.logging import success, error, warning, inpt, info
from core.utils.general import ascii_art, clear, dump_json
from core.utils.init import config
# Other modules
from core.other.ccchecker import Checker
from core.other.phonenumber import Phonenumber
from core.other.ziptolocation import ZIPtoLocation
from core.other.locationtozip import LocationtoZIP
from core.other.usernamelookup import UserLookup
from core.other.cryptolookup import Cryptolookup
from core.other.email import email_lookup
# IP modules
from core.ip.iplookup import IpLookup
from core.ip.ipfraud import IpFraud
from core.ip.isproxy import isproxy
from core.ip.portscanner import portscan
# Minecraft modules
from core.minecraft.usernametoid import UsernameToId
from core.minecraft.capeandskin import CapeAndSkin
from core.minecraft.isblockedserver import IsBlocked
# Discord modules
from core.discord.idlookup import IdLookup
from core.discord.discordinvinfo import DiscordInvInfo
from core.other.peoplelookup import PeopleLookup
# Domain modules
from core.domain.subdomainenum import SubdomainEnum
from core.domain.topleveldomainenum import TopLevelDomainEnum
from core.domain.directoryenum import DirectoryEnum

class OsintKit:
    def __init__(self) -> None:
        self.session = tls_client.Session()
        self.methods = [
            ("CC Checker",            ["BIN"],               Checker,                  "Checks bank identification numbers"),
            ("IP Lookup",             ["IP"],                IpLookup,                 "Looks up the supplied ip address"),
            ("MC username to ID",     ["username"],          UsernameToId,             "Converts a Minecraft username to its corresponding UUID"),
            ("MC Cape and Skin",      ["username"],          CapeAndSkin,              "Grabs the Cape and Skin of a Minecraft username"),
            ("MC Is Blocked Server",  ["server"],            IsBlocked,                "Checks if a Minecraft server is blocked"),
            ("Phone Lookup",          ["phone"],             Phonenumber,              "Looks up the carrier and region of a phone number"),
            ("USPS Lookup",           ["code"],              ZIPtoLocation,            "Uses USPS to look up a postal code and get the default city and state"),
            ("Location to ZIP",       ["address", "city", "state"], LocationtoZIP,     "Converts an address to a ZIP code"),
            ("Discord ID Lookup",     ["id"],                IdLookup,                 "Looks up the supplied Discord ID"),
            ("Discord Invite Info",   ["invite"],            DiscordInvInfo,           "Looks up the supplied Discord invite code"),
            ("People Lookup",         ["name","-olocation"], PeopleLookup,             "Looks up people on 192.com"),
            ("User Lookup",           ["username"],          UserLookup,               "Looks up the supplied username on various sites"),
            ("Subdomain Enum",        ["domain"],            SubdomainEnum,            "Enumerates subdomains for a given domain"),
            ("Top Level Domain Enum", ["domain"],            TopLevelDomainEnum,       "Enumerates top level domains for a given domain"),
            ("Directory Enum",        ["domain"],            DirectoryEnum,            "Enumerates directories for a given domain"),
            ("IP Fraud Lookup",       ["ip"],                IpFraud,                  "Looks up the rating and score of an IP address"),
            ("Crypto Lookup",         ["address"],           Cryptolookup,             "Looks up the supplied crypto address on various sites"),
            ("Is Proxy",              ["IP"],                isproxy,                  "Checks if the IP is a proxy"),
            ("Port Scan",             ["IP", "-oendport"],   portscan,                 "Scans the ports of an IP address"),
            ("Email Lookup",          ["email"],             email_lookup,             "Looks up the supplied email address on various sites"),
        ]

    def menu(self):
        warning("OSINT Kit")
        index_split = 5
        def format_msg(message):
            message = []
            prog = 0
            total = 0
            sub_msg = []
            for method in self.methods:
                sub_msg.append(f"[{str(self.methods.index(method) + 1)}] {method[0]}")
                prog += 1
                if prog == index_split:
                    message.append(sub_msg)
                    sub_msg = []
                    total += prog
                    prog = 0
            sub_msg = []
            for method in self.methods[total:]:
                sub_msg.append(f"[{str(self.methods.index(method) + 1)}] {method[0]}")
            message.append(sub_msg)
            return message

        def append_fix(message):
            max_length = max(len(sublist) for sublist in message)
            for i in range(len(message)):
                if len(message[i]) < max_length:
                    message[i].extend([""] * (max_length - len(message[i])))
            return message

        def paddings(message):
            padding = []
            for i in range(len(message)):
                padding.append(max(len(sublist) for sublist in message[i]))
            return padding

        def format(message):
            final = []
            padding = paddings(message)
            max_length = max(len(sublist) for sublist in message)

            for i in range(max_length):
                sub = []
                for j in range(len(message)):
                    if i < len(message[j]):
                        sub.append(message[j][i] + " " * (padding[j] - len(message[j][i])))
                    else:
                        sub.append("")
                final.append(sub)
            
            return final
        def make_header(padding):
            header = []
            for pad in padding:
                sub = "+"
                for i in range(pad + 2):
                    sub += f"{Fore.LIGHTBLACK_EX}-{Fore.RESET}"
                header.append(sub)
            header.append("+")
            return header
        
        message = ""
        msg = append_fix(format_msg(self.methods))
        columns = format(msg)
        message += "\n"
        for col in columns: 
            message += f" {Fore.LIGHTBLACK_EX}|{Fore.RESET} ".join(col) + f" \n"
        return message

    def main(self):
        config()
        while True:
            clear()
            ascii_art()
            print(self.menu())
            args = {}
            choice = inpt("Choice: ")
            if choice == "!q":
                break
            elif choice not in [str(i) for i in range(len(self.methods) + 1)]:
                error("Invalid choice")
                inpt("Press enter to continue...")
                continue
            method = self.methods[int(choice) - 1]
            warning(f"{method[0]} Arguments...")
            for arg in method[1]:
                other = ""
                if arg.startswith("-o"):
                    other = " (Optional)"
                    arg = arg.removeprefix("-o")
                value = inpt(f"{arg.title()}{other}: ")
                args[arg.removeprefix("-o")] = value
            warning("Running...")
            response = method[2](args)
            if response.get("message") == "error":
                error(response.get("info"))
            else:
                success(response.get("message"))
                print(dump_json(response.get("info")))
            inpt("Press enter to continue...")

if __name__ == "__main__":
    kit = OsintKit()
    kit.main()
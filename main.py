import tls_client
from colorama import Fore
# Core modules
from core.utils.logging import success, error, warning, inpt, info
from core.utils.general import ascii_art, clear, dump_json, modify_config, is_bug, columnit, credits
from core.utils.init import config
# Other modules
from core.other.ccchecker import Checker
from core.other.cryptolookup import Cryptolookup
from core.other.hashcracker import hashcracker
from core.other.cvesearcher import FindCVE_NVD_NIST
from core.other.defaultrouter import router
from core.other.maclookup import maclookup
from core.other.userdb import userdb
from core.other.csvdbreader import csvdbreader
# IP modules
from core.ip.iplookup import IpLookup
from core.ip.ipfraud import IpFraud
from core.ip.isproxy import isproxy
from core.ip.portscanner import portscan
from core.ip.getserverbanner import getbanner
from core.ip.isup import isup
from core.ip.networkdeviceenum import netenum
# Minecraft modules
from core.minecraft.usernametoid import UsernameToId
from core.minecraft.capeandskin import CapeAndSkin
from core.minecraft.isblockedserver import IsBlocked
from core.minecraft.serverlookup import MCServerLookup
from core.minecraft.hypixellookup import hypixel_lookup
# Discord modules
from core.discord.idlookup import IdLookup
from core.discord.discordinvinfo import DiscordInvInfo
from core.discord.discordwebhookinfo import WebhookInfo
# Domain modules
from core.domain.subdomainenum import SubdomainEnum
from core.domain.topleveldomainenum import TopLevelDomainEnum
from core.domain.directoryenum import DirectoryEnum
# Location modules
from core.location.ziptolocation import ZIPtoLocation
from core.location.locationtozip import LocationtoZIP
from core.location.citystatetozip import CitystateToZIP
# Identity modules
from core.identity.phonenumber import Phonenumber
from core.identity.usernamelookup import UserLookup
from core.identity.email import email_lookup
from core.identity.peoplelookup import PeopleLookup

class OsintKit:
    def __init__(self) -> None:
        self.session = tls_client.Session()
        self.methods = [       
            ("CC Checker",            ["BIN"],                              Checker,                  "Checks bank identification numbers"),
            ("IP Lookup",             ["IP"],                               IpLookup,                 "Looks up the supplied ip address"),
            ("MC username to ID",     ["username"],                         UsernameToId,             "Converts a Minecraft username to its corresponding UUID"),
            ("MC Cape and Skin",      ["username"],                         CapeAndSkin,              "Grabs the Cape and Skin of a Minecraft username"),
            ("MC Is Blocked Server",  ["server"],                           IsBlocked,                "Checks if a Minecraft server is blocked"),
            ("MC Server Lookup",      ["server"],                           MCServerLookup,           "Looks up the status of a Minecraft server"),
            ("Hypixel Lookup",        ["username"],                         hypixel_lookup,           "Looks up the hypixel stats of a player"),
            ("Phone Lookup",          ["phone"],                            Phonenumber,              "Looks up the carrier and region of a phone number"),
            ("USPS Lookup",           ["code"],                             ZIPtoLocation,            "Uses USPS to look up a postal code and get the default city and state"),
            ("Location to ZIP",       ["address", "city", "state"],         LocationtoZIP,            "Converts an address to a ZIP code"),
            ("City State to ZIP",     ["city", "state"],                    CitystateToZIP,           "Converts a city and state to a ZIP code"),
            ("Discord ID Lookup",     ["id"],                               IdLookup,                 "Looks up the supplied Discord ID"),
            ("Discord Invite Info",   ["invite"],                           DiscordInvInfo,           "Looks up the supplied Discord invite code"),
            ("Discord Webhook Info",  ["webhook"],                          WebhookInfo,              "Looks up the supplied Discord webhook code"),
            ("People Lookup",         ["name","-olocation"],                PeopleLookup,             "Looks up people on 192.com"),
            ("User Lookup",           ["username"],                         UserLookup,               "Looks up the supplied username on various sites"),
            ("Subdomain Enum",        ["domain"],                           SubdomainEnum,            "Enumerates subdomains for a given domain"),
            ("Top Level Domain Enum", ["domain"],                           TopLevelDomainEnum,       "Enumerates top level domains for a given domain"),
            ("Directory Enum",        ["domain"],                           DirectoryEnum,            "Enumerates directories for a given domain"),
            ("IP Fraud Lookup",       ["ip"],                               IpFraud,                  "Looks up the rating and score of an IP address"),
            ("Crypto Lookup",         ["address"],                          Cryptolookup,             "Looks up the supplied crypto address on various sites"),
            ("Is Proxy",              ["IP"],                               isproxy,                  "Checks if the IP is a proxy"),
            ("Port Scan",             ["IP", "-oendport"],                  portscan,                 "Scans the ports of an IP address"),
            ("Get Banner",            ["IP", "port"],                       getbanner,                "Gets the banner of an IP address"),
            ("Is up",                 ["target"],                           isup,                     "Checks if the target is up"),
            ("Network devices",       ["base"],                             netenum,                  "Enumerates network devices"),
            ("Email Lookup",          ["email"],                            email_lookup,             "Looks up the supplied email address on various sites"),
            ("Hash Cracker",          ["hash", "algorithm", "-owordlist"],  hashcracker,              "Cracks the supplied hash"),
            ("CVE Searcher",          ["search"],                           FindCVE_NVD_NIST,         "Searches NVD NIST for a CVE"),
            ("Router password",       ["model", "-obrand"],                 router,                   "Looks up the router password"),
            ("Mac Lookup",            ["mac"],                              maclookup,                "Looks up the supplied MAC address on various sites"),
            ("Modify API keys",       [],                                   modify_config,            "Modifies the API keys"),
            ("User DB",               [],                                   userdb,                   "User Database"),
            ("CSV DB",                ["path"],                             csvdbreader,              "CSV Database")
        ]

    def menu(self):
        warning("OSINT Kit")
        array = [method[0] for method in self.methods]
        return columnit(array)

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
            elif choice == "!dc":
                info("https://discord.gg/Pd9HkP7b")
                inpt("Press enter to continue...")
                continue
            elif choice == "!c":
                credits()
                inpt("Press enter to continue...")
                continue
            elif not choice.isdigit() or not (0 <= int(choice) < len(self.methods) + 1):
                error("Invalid choice")
                inpt("Press enter to continue...")
                continue
            is_bug(self.methods[int(choice) - 1][0])
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
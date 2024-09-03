import tls_client
from core.utils.logging import success, error, warning, inpt, info
from core.utils.general import ascii_art, clear, dump_json
from core.utils.init import config
from core.other.ccchecker import Checker
from core.other.iplookup import IpLookup
from core.other.phonenumber import Phonenumber
from core.other.usps import USPSLookup
from core.minecraft.usernametoid import UsernameToId
from core.minecraft.capeandskin import CapeAndSkin
from core.minecraft.isblockedserver import IsBlocked
from core.discord.idlookup import IdLookup
from core.discord.discordinvinfo import DiscordInvInfo

class OsintKit:
    def __init__(self) -> None:
        self.session = tls_client.Session()
        self.methods = [
            ("CC Checker",            ["BIN"],      Checker),
            ("IP Lookup",             ["IP"],       IpLookup),
            ("MC username to ID",     ["username"], UsernameToId),
            ("MC Cape and Skin",      ["username"], CapeAndSkin),
            ("MC Is Blocked Server",  ["server"],   IsBlocked),
            ("Phone Lookup",          ["phone"],    Phonenumber),
            ("USPS Lookup",           ["code"],     USPSLookup),
            ("Discord ID Lookup",     ["id"],       IdLookup),
            ("Discord Invite Info",   ["invite"],   DiscordInvInfo)
        ]

    def menu(self):
        warning("OSINT Kit")
        for method in self.methods:
            info(f"[{str(self.methods.index(method) + 1)}] {method[0]}")

    def main(self):
        config()
        while True:
            clear()
            ascii_art()
            self.menu()
            args = {}
            choice = inpt("Choice: ")
            if choice not in [str(i) for i in range(len(self.methods) + 1)]:
                error("Invalid choice")
                inpt("Press enter to continue...")
                continue

            method = self.methods[int(choice) - 1]
            warning(f"{method[0]} Arguments...")
            for arg in method[1]:
                value = inpt(f"{arg}: ")
                args[arg] = value
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
import os
import subprocess

from core import HackingTool, HackingToolsCollection, console
from tools.others.android_attack import AndroidAttackTools
from tools.others.email_verifier import EmailVerifyTools
from tools.others.hash_crack import HashCrackingTools
from tools.others.homograph_attacks import IDNHomographAttackTools
from tools.others.mix_tools import MixTools
from tools.others.payload_injection import PayloadInjectorTools
from tools.others.socialmedia import SocialMediaBruteforceTools
from tools.others.socialmedia_finder import SocialMediaFinderTools
from tools.others.web_crawling import WebCrawlingTools
from tools.others.wifi_jamming import WifiJammingTools

from i18n import t

from rich.panel import Panel
from rich.prompt import Prompt


class HatCloud(HackingTool):
    TITLE = "HatCloud(Bypass CloudFlare for IP)"
    DESCRIPTION = "HatCloud 使用 Ruby 构建，可绕过 CloudFlare 发现真实 IP。"
    INSTALL_COMMANDS = ["git clone https://github.com/HatBashBR/HatCloud.git"]
    PROJECT_URL = "https://github.com/HatBashBR/HatCloud"

    def run(self):
        from config import get_tools_dir
        from rich.prompt import Prompt
        site = Prompt.ask(t("prompt.enter_site"))
        # Bug 3 fix: os.chdir() replaced with cwd= parameter
        subprocess.run(
            ["sudo", "ruby", "hatcloud.rb", "-b", site],
            cwd=str(get_tools_dir() / "HatCloud"),
        )


class OtherTools(HackingToolsCollection):
    TITLE = t("category.other")
    TOOLS = [
        SocialMediaBruteforceTools(),
        AndroidAttackTools(),
        HatCloud(),
        IDNHomographAttackTools(),
        EmailVerifyTools(),
        HashCrackingTools(),
        WifiJammingTools(),
        SocialMediaFinderTools(),
        PayloadInjectorTools(),
        WebCrawlingTools(),
        MixTools()
    ]

if __name__ == "__main__":
    tools = OtherTools()
    tools.show_options()

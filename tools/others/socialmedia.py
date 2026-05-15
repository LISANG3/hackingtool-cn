import contextlib
import os
import subprocess

from core import HackingTool, HackingToolsCollection, console
from i18n import t

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

from i18n import t


class InstaBrute(HackingTool):
    TITLE = "Instagram Attack"
    DESCRIPTION = "针对 Instagram 的暴力破解攻击"
    PROJECT_URL = "https://github.com/chinoogawa/instaBrute"
    # Py3-7: Python 2 only (pip2.7); also violates Instagram ToS
    ARCHIVED = True
    ARCHIVED_REASON = "Python 2 only — EOL January 2020. Repo unmaintained since 2017."
    INSTALL_COMMANDS = []
    RUN_COMMANDS = []

    def __init__(self):
        super().__init__(installable=False, runnable=False)


class BruteForce(HackingTool):
    TITLE = "AllinOne SocialMedia Attack"
    DESCRIPTION = "暴力破解 Gmail、Hotmail、Twitter、Facebook、Netflix 等账户。\n" \
                  "[!] python3 Brute_Force.py -g <Account@gmail.com> -l <File_list>"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Matrix07ksa/Brute_Force.git",
        "cd Brute_Force;sudo pip3 install proxylist;pip3 install mechanize"
    ]
    RUN_COMMANDS = ["cd Brute_Force;python3 Brute_Force.py -h"]
    PROJECT_URL = "https://github.com/Matrix07ksa/Brute_Force"


class Faceshell(HackingTool):
    TITLE = "Facebook Attack"
    DESCRIPTION = "Facebook 暴力破解工具"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Matrix07ksa/Brute_Force.git",
        "cd Brute_Force;sudo pip3 install proxylist;pip3 install mechanize"
    ]
    PROJECT_URL = "https://github.com/Matrix07ksa/Brute_Force"

    def run(self):
        from config import get_tools_dir
        name = Prompt.ask(t("prompt.enter_username"))
        wordlist = Prompt.ask(t("prompt.enter_wordlist"))
        # Bug 3 fix: os.chdir() replaced with cwd= parameter
        subprocess.run(
            ["python3", "Brute_Force.py", "-f", name, "-l", wordlist],
            cwd=str(get_tools_dir() / "Brute_Force"),
        )


class AppCheck(HackingTool):
    TITLE = "Application Checker"
    DESCRIPTION = "通过链接检查目标设备上是否安装了应用程序的工具。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/jakuta-tech/underhanded.git",
        "cd underhanded && sudo chmod +x underhanded.sh"
    ]
    RUN_COMMANDS = ["cd underhanded;sudo bash underhanded.sh"]
    PROJECT_URL = "https://github.com/jakuta-tech/underhanded"


class SocialMediaBruteforceTools(HackingToolsCollection):
    TITLE = "社交媒体暴力破解"
    TOOLS = [
        InstaBrute(),
        BruteForce(),
        Faceshell(),
        AppCheck()
    ]

if __name__ == "__main__":
    tools = SocialMediaBruteforceTools()
    tools.show_options()

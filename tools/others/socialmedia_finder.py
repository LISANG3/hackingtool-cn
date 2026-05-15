import os
import subprocess

from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

from i18n import t


class FacialFind(HackingTool):
    TITLE = "Find SocialMedia By Facial Recognation System"
    DESCRIPTION = "一种社交媒体映射工具，通过面部识别关联不同网站上的个人资料。"
    INSTALL_COMMANDS = [
        "sudo apt install -y software-properties-common",
        "sudo add-apt-repository ppa:mozillateam/firefox-next && sudo apt update && sudo apt upgrade",
        "git clone https://github.com/Greenwolf/social_mapper.git",
        "sudo apt install -y build-essential cmake libgtk-3-dev libboost-all-dev",
        "cd social_mapper/setup",
        "sudo python3 -m pip install --no-cache-dir -r requirements.txt",
        'echo "[!]Now You have To do some Manually\n'
        '[!] Install the Geckodriver for your operating system\n'
        '[!] Copy & Paste Link And Download File As System Configuration\n'
        '[#] https://github.com/mozilla/geckodriver/releases\n'
        '[!!] On Linux you can place it in /usr/bin "| boxes | lolcat'
    ]
    PROJECT_URL = "https://github.com/Greenwolf/social_mapper"

    def run(self):
        from config import get_tools_dir
        import subprocess
        setup_dir = get_tools_dir() / "social_mapper" / "setup"
        subprocess.run(["python3", "social_mapper.py", "-h"], cwd=str(setup_dir))
        console.print(
            "[bold magenta]" + t("socialface.enter_credentials") + "[/]\n"
            "[magenta]" + t("socialface.usage") + "[/]"
        )


class FindUser(HackingTool):
    TITLE = "Find SocialMedia By UserName"
    DESCRIPTION = "在超过 75 个社交网络中查找用户名"
    INSTALL_COMMANDS = [
        "git clone https://github.com/xHak9x/finduser.git",
        "cd finduser && sudo chmod +x finduser.sh"
    ]
    RUN_COMMANDS = ["cd finduser && sudo bash finduser.sh"]
    PROJECT_URL = "https://github.com/xHak9x/finduser"


class Sherlock(HackingTool):
    TITLE = "Sherlock"
    DESCRIPTION = "通过用户名在社交网络中搜索社交媒体账户。\n" \
                  "更多用法:\n" \
                  "\t >>python3 sherlock --help"
    INSTALL_COMMANDS = [
        "git clone https://github.com/sherlock-project/sherlock.git",
        "cd sherlock;sudo python3 -m pip install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/sherlock-project/sherlock"

    def run(self):
        from config import get_tools_dir
        from rich.prompt import Prompt
        name = Prompt.ask(t("prompt.enter_username"))
        # Bug 3 fix: os.chdir() replaced with cwd= parameter
        subprocess.run(
            ["python3", "sherlock", name],
            cwd=str(get_tools_dir() / "sherlock"),
        )


class SocialScan(HackingTool):
    TITLE = "SocialScan | Username or Email"
    DESCRIPTION = "以 100% 的准确率检查邮箱地址和用户名在在线平台上的可用性。"
    INSTALL_COMMANDS = ["pip install --user socialscan"]
    PROJECT_URL = "https://github.com/iojw/socialscan"

    def run(self):
        name = input(t("prompt.enter_username_email"))
        subprocess.run(["sudo", "socialscan", f"{name}"])


class SocialMediaFinderTools(HackingToolsCollection):
    TITLE = "社交媒体查找"
    TOOLS = [
        FacialFind(),
        FindUser(),
        Sherlock(),
        SocialScan()
    ]

if __name__ == "__main__":
    tools = SocialMediaFinderTools()
    tools.show_options()

import os

from core import HackingTool, HackingToolsCollection, console
from i18n import t


class Autophisher(HackingTool):
    TITLE = "Autophisher RK"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "自动化钓鱼工具包"
    INSTALL_COMMANDS = [
        "git clone https://github.com/CodingRanjith/autophisher.git",
    ]
    RUN_COMMANDS = ["cd autophisher && sudo bash autophisher.sh"]
    PROJECT_URL = "https://github.com/CodingRanjith/autophisher"


class Pyphisher(HackingTool):
    TITLE = "Pyphisher"
    DESCRIPTION = "易于使用的钓鱼工具，包含 77 个网站模板"
    # Bug 9 fix: pip must reference the full path, not rely on a no-op "cd" call
    INSTALL_COMMANDS = [
        "git clone https://github.com/KasRoudra/PyPhisher",
        "pip3 install --user -r PyPhisher/files/requirements.txt",
    ]
    RUN_COMMANDS = ["cd PyPhisher && sudo python3 pyphisher.py"]
    # Bug 8 fix: PROJECT_URL was a git clone command, not a URL
    PROJECT_URL = "https://github.com/KasRoudra/PyPhisher"


class AdvPhishing(HackingTool):
    TITLE = "AdvPhishing"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "这是一款高级钓鱼工具！OTP 钓鱼"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Ignitetch/AdvPhishing.git",
        # Vuln 2 fix: chmod 777 → chmod +x
        "cd AdvPhishing && chmod +x Linux-Setup.sh && bash Linux-Setup.sh",
    ]
    RUN_COMMANDS = ["cd AdvPhishing && sudo bash AdvPhishing.sh"]
    PROJECT_URL = "https://github.com/Ignitetch/AdvPhishing"


class Setoolkit(HackingTool):
    TITLE = "Setoolkit"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "Social-Engineer Toolkit 是一款开源的渗透\n"
        "测试框架，专为社会工程学设计。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/trustedsec/social-engineer-toolkit/",
        "cd social-engineer-toolkit && pip install --user .",
    ]
    RUN_COMMANDS = ["sudo setoolkit"]
    PROJECT_URL = "https://github.com/trustedsec/social-engineer-toolkit"


class SocialFish(HackingTool):
    TITLE = "SocialFish"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "自动化钓鱼工具和信息收集器 注意: 用户名为 'root'，密码为 'pass'"
    INSTALL_COMMANDS = [
        "git clone https://github.com/UndeadSec/SocialFish.git && sudo apt-get install python3 python3-pip python3-dev -y",
        "cd SocialFish && sudo python3 -m pip install -r requirements.txt",
    ]
    RUN_COMMANDS = ["cd SocialFish && sudo python3 SocialFish.py root pass"]
    PROJECT_URL = "https://github.com/UndeadSec/SocialFish"


class HiddenEye(HackingTool):
    TITLE = "HiddenEye"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "具有高级功能和多种隧道服务的现代钓鱼工具\n"
        "\t[!] https://github.com/DarkSecDevelopers/HiddenEye"
    )
    INSTALL_COMMANDS = [
        # Vuln 2 fix: chmod 777 → chmod 755
        "git clone https://github.com/Morsmalleo/HiddenEye.git && chmod -R 755 HiddenEye",
        "cd HiddenEye && sudo pip3 install -r requirements.txt && pip3 install pyngrok",
    ]
    RUN_COMMANDS = ["cd HiddenEye && sudo python3 HiddenEye.py"]
    PROJECT_URL = "https://github.com/Morsmalleo/HiddenEye"


class Evilginx3(HackingTool):
    TITLE = "Evilginx3"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "evilginx 是一个中间人攻击框架，用于窃取登录凭据\n"
        "以及会话 Cookie，绕过双重身份验证。\n"
        "需要安装 Go >= 1.18。"
    )
    # Bug 6 fix: removed 'sudo evilginx' (interactive) from INSTALL_COMMANDS
    INSTALL_COMMANDS = [
        "sudo apt-get install -y git make golang-go",
        "go install github.com/kgretzky/evilginx/v3@latest",
    ]
    RUN_COMMANDS = ["evilginx"]
    PROJECT_URL = "https://github.com/kgretzky/evilginx2"
    REQUIRES_GO = True


class ISeeYou(HackingTool):
    TITLE = "I-See_You"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "[!] ISeeYou 通过社会工程学查找目标的精确位置。\n"
        "[!] 将本地服务器暴露到互联网，并从日志文件中解码位置信息。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/Viralmaniar/I-See-You.git",
        "cd I-See-You && sudo chmod u+x ISeeYou.sh",
    ]
    RUN_COMMANDS = ["cd I-See-You && sudo bash ISeeYou.sh"]
    PROJECT_URL = "https://github.com/Viralmaniar/I-See-You"


class SayCheese(HackingTool):
    TITLE = "SayCheese"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "只需发送恶意链接即可从目标获取摄像头照片"
    INSTALL_COMMANDS = ["git clone https://github.com/hangetzzu/saycheese"]
    RUN_COMMANDS = ["cd saycheese && sudo bash saycheese.sh"]
    PROJECT_URL = "https://github.com/hangetzzu/saycheese"


class QRJacking(HackingTool):
    TITLE = "QR Code Jacking"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "QR 码劫持 (任何网站)"
    INSTALL_COMMANDS = [
        "git clone https://github.com/cryptedwolf/ohmyqr.git && sudo apt -y install scrot",
    ]
    RUN_COMMANDS = ["cd ohmyqr && sudo bash ohmyqr.sh"]
    PROJECT_URL = "https://github.com/cryptedwolf/ohmyqr"


# Bug 10 fix: WifiPhisher removed from phishing tools — it belongs in wireless_attack.py


class BlackEye(HackingTool):
    TITLE = "BlackEye"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "终极钓鱼工具，提供 38 个网站模板！"
    INSTALL_COMMANDS = [
        "git clone https://github.com/thelinuxchoice/blackeye",
    ]
    RUN_COMMANDS = ["cd blackeye && sudo bash blackeye.sh"]
    PROJECT_URL = "https://github.com/An0nUD4Y/blackeye"


class ShellPhish(HackingTool):
    TITLE = "ShellPhish"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "适用于 18 种社交媒体的钓鱼工具"
    INSTALL_COMMANDS = ["git clone https://github.com/An0nUD4Y/shellphish.git"]
    RUN_COMMANDS = ["cd shellphish && sudo bash shellphish.sh"]
    PROJECT_URL = "https://github.com/An0nUD4Y/shellphish"


class Thanos(HackingTool):
    TITLE = "Thanos"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "浏览器到浏览器钓鱼工具包"
    INSTALL_COMMANDS = [
        "git clone https://github.com/TridevReddy/Thanos.git",
        # Vuln 2 fix: chmod -R 777 → chmod +x
        "cd Thanos && chmod +x Thanos.sh",
    ]
    RUN_COMMANDS = ["cd Thanos && sudo bash Thanos.sh"]
    PROJECT_URL = "https://github.com/TridevReddy/Thanos"


class QRLJacking(HackingTool):
    TITLE = "QRLJacking"
    DESCRIPTION = "QRLJacking — 针对基于 QR 码登录的会话劫持攻击向量"
    INSTALL_COMMANDS = [
        "git clone https://github.com/OWASP/QRLJacking.git",
        # Bug fix: geckodriver must be fetched as a binary, not cloned from source
        "GECKO_VER=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep tag_name | cut -d '\"' -f4) && "
        "wget -q https://github.com/mozilla/geckodriver/releases/download/$GECKO_VER/geckodriver-$GECKO_VER-linux64.tar.gz -O /tmp/geckodriver.tar.gz && "
        "tar -xzf /tmp/geckodriver.tar.gz -C /tmp && sudo mv /tmp/geckodriver /usr/local/bin/",
        "cd QRLJacking && pip3 install --user -r QRLJacker/requirements.txt",
    ]
    RUN_COMMANDS = ["cd QRLJacking/QRLJacker && python3 QrlJacker.py"]
    PROJECT_URL = "https://github.com/OWASP/QRLJacking"


class Maskphish(HackingTool):
    TITLE = "Maskphish"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "将钓鱼 URL 隐藏在正常 URL (google.com 或 facebook.com) 之下"
    INSTALL_COMMANDS = [
        "git clone https://github.com/jaykali/maskphish.git",
    ]
    RUN_COMMANDS = ["cd maskphish && sudo bash maskphish.sh"]
    PROJECT_URL = "https://github.com/jaykali/maskphish"


class BlackPhish(HackingTool):
    TITLE = "BlackPhish"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/iinc0gnit0/BlackPhish.git",
        "cd BlackPhish && sudo bash install.sh",
    ]
    RUN_COMMANDS = ["cd BlackPhish && sudo python3 blackphish.py"]
    PROJECT_URL = "https://github.com/iinc0gnit0/BlackPhish"

    def __init__(self):
        # Bug fix: super() Python 3 style
        super().__init__([("Update", self.update)])

    def update(self):
        import subprocess
        from config import get_tools_dir
        subprocess.run(["bash", "update.sh"], cwd=str(get_tools_dir() / "BlackPhish"))


class Dnstwist(HackingTool):
    # Bug 2 fix: all attributes were wrong case (Title, Install_commands, etc.)
    # They are now the correct uppercase names the base class reads.
    TITLE = "dnstwist"
    DESCRIPTION = "域名排列引擎，用于检测域名抢注、钓鱼和品牌冒充"
    INSTALL_COMMANDS = ["pip3 install --user dnstwist"]
    RUN_COMMANDS = ["dnstwist --help"]
    PROJECT_URL = "https://github.com/elceef/dnstwist"


class PhishingAttackTools(HackingToolsCollection):
    TITLE = t("category.phishing")
    TOOLS = [
        Autophisher(),
        Pyphisher(),
        AdvPhishing(),
        Setoolkit(),
        SocialFish(),
        HiddenEye(),
        Evilginx3(),
        ISeeYou(),
        SayCheese(),
        QRJacking(),
        BlackEye(),
        ShellPhish(),
        Thanos(),
        QRLJacking(),
        BlackPhish(),
        Maskphish(),
        Dnstwist(),
    ]


if __name__ == "__main__":
    tools = PhishingAttackTools()
    tools.show_options()

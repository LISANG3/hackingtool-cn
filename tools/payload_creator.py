import os
import subprocess

from core import HackingTool, HackingToolsCollection, console
from i18n import t


class TheFatRat(HackingTool):
    TITLE = "The FatRat"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "TheFatRat 提供了一种创建后门和 Payload 的简便方法，可以绕过大多数杀毒软件。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Screetsec/TheFatRat.git",
        "cd TheFatRat && chmod +x setup.sh",
    ]
    RUN_COMMANDS = ["cd TheFatRat && sudo bash setup.sh"]
    PROJECT_URL = "https://github.com/Screetsec/TheFatRat"

    def __init__(self):
        super().__init__([
            ("Update", self.update),
            ("Troubleshoot", self.troubleshoot),
        ])

    def update(self):
        from config import get_tools_dir
        cwd = str(get_tools_dir() / "TheFatRat")
        subprocess.run(["bash", "update"], cwd=cwd)
        subprocess.run(["chmod", "+x", "setup.sh"], cwd=cwd)
        subprocess.run(["bash", "setup.sh"], cwd=cwd)

    def troubleshoot(self):
        from config import get_tools_dir
        cwd = str(get_tools_dir() / "TheFatRat")
        subprocess.run(["chmod", "+x", "chk_tools"], cwd=cwd)
        subprocess.run(["./chk_tools"], cwd=cwd)


class Brutal(HackingTool):
    TITLE = "Brutal"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "Brutal 是一个工具包，可快速创建各种 Payload、PowerShell 攻击、病毒攻击，并为 Human Interface Device 启动监听器。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Screetsec/Brutal.git",
        "cd Brutal && chmod +x Brutal.sh",
    ]
    RUN_COMMANDS = ["cd Brutal && sudo bash Brutal.sh"]
    PROJECT_URL = "https://github.com/Screetsec/Brutal"

    def show_info(self):
        super().show_info()
        console.print(t("payload.brutal_requirements"))


class Stitch(HackingTool):
    TITLE = "Stitch"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "Stitch 是一个跨平台 Python 远程管理工具。\n[!] 关于 Windows 和 macOS 支持，请参考项目链接。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/nathanlopez/Stitch.git",
        "cd Stitch && pip install --user -r lnx_requirements.txt",
    ]
    RUN_COMMANDS = ["cd Stitch && sudo python3 main.py"]
    PROJECT_URL = "https://nathanlopez.github.io/Stitch"


class MSFVenom(HackingTool):
    TITLE = "MSFvenom Payload Creator"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "MSFvenom Payload Creator (MSFPC) 是一个包装器，用于根据用户选择生成多种类型的 Payload。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/g0tmi1k/msfpc.git",
        "cd msfpc && chmod +x msfpc.sh",
    ]
    RUN_COMMANDS = ["cd msfpc && sudo bash msfpc.sh -h -v"]
    PROJECT_URL = "https://github.com/g0tmi1k/msfpc"


class Venom(HackingTool):
    TITLE = "Venom Shellcode Generator"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "Venom 利用 Apache2 Web 服务器通过伪造网页传递 LAN Payload。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/r00t-3xp10it/venom.git",
        # Removed "sudo ./venom.sh -u" from install — interactive, runs the tool during install
        "sudo chmod -R 775 venom*/ && cd venom*/ && cd aux && sudo bash setup.sh",
    ]
    RUN_COMMANDS = ["cd venom && sudo ./venom.sh"]
    PROJECT_URL = "https://github.com/r00t-3xp10it/venom"


class Spycam(HackingTool):
    TITLE = "Spycam"
    DESCRIPTION = "生成一个每 1 分钟捕获一次摄像头图像的 Win32 Payload。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/indexnotfound404/spycam.git",
        "cd spycam && bash install.sh && chmod +x spycam",
    ]
    RUN_COMMANDS = ["cd spycam && ./spycam"]
    PROJECT_URL = "https://github.com/indexnotfound404/spycam"


class MobDroid(HackingTool):
    TITLE = "Mob-Droid"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "无需输入冗长命令即可轻松生成 Metasploit Payload。"
    INSTALL_COMMANDS = ["git clone https://github.com/kinghacker0/mob-droid.git"]
    RUN_COMMANDS = ["cd mob-droid && sudo python3 mob-droid.py"]
    PROJECT_URL = "https://github.com/kinghacker0/Mob-Droid"


class Enigma(HackingTool):
    TITLE = "Enigma"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "Enigma 是一个多平台 Payload 投放器。"
    INSTALL_COMMANDS = ["git clone https://github.com/UndeadSec/Enigma.git"]
    RUN_COMMANDS = ["cd Enigma && sudo python3 enigma.py"]
    PROJECT_URL = "https://github.com/UndeadSec/Enigma"


class PayloadCreatorTools(HackingToolsCollection):
    TITLE = t("category.payload")
    # Bug 11 fix: show_options() override was missing `parent` parameter entirely —
    # the whole override is now deleted and the base class method is used instead.
    TOOLS = [
        TheFatRat(),
        Brutal(),
        Stitch(),
        MSFVenom(),
        Venom(),
        Spycam(),
        MobDroid(),
        Enigma(),
    ]


if __name__ == "__main__":
    tools = PayloadCreatorTools()
    tools.show_options()

from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

from i18n import t


class Keydroid(HackingTool):
    TITLE = "Keydroid"
    DESCRIPTION = "Android 键盘记录器 + 反向 Shell\n" \
                  "[!] 需要手动安装一些组件，请参考以下链接:\n " \
                  "[+] https://github.com/F4dl0/keydroid"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["git clone https://github.com/F4dl0/keydroid.git"]
    RUN_COMMANDS = ["cd keydroid && bash keydroid.sh"]
    PROJECT_URL = "https://github.com/F4dl0/keydroid"


class MySMS(HackingTool):
    TITLE = "MySMS"
    DESCRIPTION = "生成一个 Android 应用程序，通过 WAN 入侵 SMS。\n" \
                  "[!] 需要手动安装一些组件，请参考以下链接:\n\t " \
                  "[+] https://github.com/papusingh2sms/mysms"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/papusingh2sms/mysms.git"]
    RUN_COMMANDS = ["cd mysms && bash mysms.sh"]
    PROJECT_URL = "https://github.com/papusingh2sms/mysms"


class LockPhish(HackingTool):
    TITLE = "Lockphish (Grab target LOCK PIN)"
    DESCRIPTION = "Lockphish 是首个针对锁屏的钓鱼攻击工具，旨在\n" \
                  "通过 HTTPS 链接获取 Windows 凭据、Android PIN 和 iPhone 密码。"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/JasonJerry/lockphish.git"]
    RUN_COMMANDS = ["cd lockphish && bash lockphish.sh"]
    PROJECT_URL = "https://github.com/JasonJerry/lockphish"


class Droidcam(HackingTool):
    TITLE = "DroidCam (Capture Image)"
    DESCRIPTION = "通过链接获取前置摄像头快照的强大工具。"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        # Bug 16 fix: missing comma caused two strings to be implicitly concatenated into one
        "git clone https://github.com/kinghacker0/WishFish.git",
        "sudo apt install -y php wget openssh-client",
    ]
    RUN_COMMANDS = ["cd WishFish && sudo bash wishfish.sh"]
    PROJECT_URL = "https://github.com/kinghacker0/WishFish"


class EvilApp(HackingTool):
    TITLE = "EvilApp (Hijack Session)"
    DESCRIPTION = "EvilApp 是一个生成 Android 应用程序的脚本，可以劫持 Cookie 中的认证会话。"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/crypticterminal/EvilApp.git"]
    RUN_COMMANDS = ["cd EvilApp && bash evilapp.sh"]
    PROJECT_URL = "https://github.com/crypticterminal/EvilApp"


class AndroidAttackTools(HackingToolsCollection):
    TITLE = "Android 黑客工具"
    TOOLS = [
        Keydroid(),
        MySMS(),
        LockPhish(),
        Droidcam(),
        EvilApp()
    ]

if __name__ == "__main__":
    tools = AndroidAttackTools()
    tools.show_options()

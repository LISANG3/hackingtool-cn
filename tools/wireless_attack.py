from rich.prompt import Prompt

from core import HackingTool, HackingToolsCollection, console
from i18n import t


class WIFIPumpkin(HackingTool):
    TITLE = "WiFi-Pumpkin"
    DESCRIPTION = (
        "WiFi-Pumpkin 是一个虚假 AP 框架，可轻松创建假网络\n"
        "同时在无感知目标之间转发合法流量。"
    )
    INSTALL_COMMANDS = [
        "sudo apt install -y libssl-dev libffi-dev build-essential python3-pyqt5",
        "git clone https://github.com/P0cL4bs/wifipumpkin3.git",
        "chmod -R 755 wifipumpkin3",
        "cd wifipumpkin3 && pip install --user .",
    ]
    RUN_COMMANDS = ["sudo wifipumpkin3"]
    PROJECT_URL = "https://github.com/P0cL4bs/wifipumpkin3"
    SUPPORTED_OS = ["linux"]
    REQUIRES_WIFI = True


class pixiewps(HackingTool):
    TITLE = "pixiewps"
    DESCRIPTION = (
        "Pixiewps 是一款用 C 编写的工具，用于离线暴力破解 WPS PIN，\n"
        "利用某些接入点的低熵或非熵（pixie dust 攻击）。"
    )
    INSTALL_COMMANDS = [
        # Bug 29 fix: removed wget https://pastebin.com/... (insecure download from pastebin)
        "git clone https://github.com/wiire/pixiewps.git && apt-get -y install build-essential",
        "cd pixiewps && make",
        "cd pixiewps && sudo make install",
    ]
    PROJECT_URL = "https://github.com/wiire/pixiewps"
    SUPPORTED_OS = ["linux"]
    REQUIRES_WIFI = True

    def run(self):
        console.print(t("tool.pixiewps.usage"))


class BluePot(HackingTool):
    TITLE = "Bluetooth Honeypot GUI Framework"
    DESCRIPTION = (
        "您需要至少 1 个蓝牙接收器。\n"
        "安装 libbluetooth-dev (Ubuntu) / bluez-libs-devel (Fedora) / bluez-devel (openSUSE)。"
    )
    INSTALL_COMMANDS = [
        # Bug 15 fix: missing comma caused implicit string concatenation — two strings joined
        "sudo wget https://raw.githubusercontent.com/andrewmichaelsmith/bluepot/master/bin/bluepot-0.2.tar.gz",
        "sudo tar xfz bluepot-0.2.tar.gz && sudo rm bluepot-0.2.tar.gz",
    ]
    RUN_COMMANDS = ["cd bluepot && sudo java -jar bluepot.jar"]
    PROJECT_URL = "https://github.com/andrewmichaelsmith/bluepot"
    SUPPORTED_OS = ["linux"]
    REQUIRES_JAVA = True


class Fluxion(HackingTool):
    TITLE = "Fluxion"
    DESCRIPTION = "Fluxion 是 vk496 的 linset 的重制版，功能增强。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/FluxionNetwork/fluxion.git",
        "cd fluxion && chmod +x fluxion.sh",
    ]
    RUN_COMMANDS = ["cd fluxion && sudo bash fluxion.sh -i"]
    PROJECT_URL = "https://github.com/FluxionNetwork/fluxion"
    SUPPORTED_OS = ["linux"]
    REQUIRES_WIFI = True


class Wifiphisher(HackingTool):
    TITLE = "Wifiphisher"
    DESCRIPTION = (
        "Wifiphisher 是一个虚假接入点框架，用于进行红队演练\n"
        "或 Wi-Fi 安全测试。通过执行有针对性的 Wi-Fi 关联攻击，\n"
        "轻松实现对无线客户端的中间人攻击。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/wifiphisher/wifiphisher.git",
        "cd wifiphisher && pip install --user .",
    ]
    RUN_COMMANDS = ["cd wifiphisher && sudo wifiphisher"]
    PROJECT_URL = "https://github.com/wifiphisher/wifiphisher"
    SUPPORTED_OS = ["linux"]
    REQUIRES_WIFI = True


class Wifite(HackingTool):
    TITLE = "Wifite"
    DESCRIPTION = "Wifite 是一款自动化无线攻击工具。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/derv82/wifite2.git",
        "cd wifite2 && pip install --user .",
    ]
    RUN_COMMANDS = ["sudo wifite"]
    PROJECT_URL = "https://github.com/derv82/wifite2"
    SUPPORTED_OS = ["linux"]
    REQUIRES_WIFI = True


class EvilTwin(HackingTool):
    TITLE = "EvilTwin"
    DESCRIPTION = (
        "Fakeap — 通过使用假页面和假接入点获取凭据来执行邪恶双子攻击。"
    )
    INSTALL_COMMANDS = ["git clone https://github.com/Z4nzu/fakeap.git"]
    RUN_COMMANDS = ["cd fakeap && sudo bash fakeap.sh"]
    PROJECT_URL = "https://github.com/Z4nzu/fakeap"
    SUPPORTED_OS = ["linux"]
    REQUIRES_WIFI = True


class Fastssh(HackingTool):
    TITLE = "Fastssh"
    DESCRIPTION = (
        "Fastssh — 使用最常用凭据对 SSH 协议进行多线程扫描和暴力破解攻击。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/Z4nzu/fastssh.git && cd fastssh && chmod +x fastssh.sh",
        "sudo apt-get install -y sshpass netcat",
    ]
    RUN_COMMANDS = ["cd fastssh && sudo bash fastssh.sh --scan"]
    PROJECT_URL = "https://github.com/Z4nzu/fastssh"
    SUPPORTED_OS = ["linux"]


class Howmanypeople(HackingTool):
    TITLE = "Howmanypeople"
    DESCRIPTION = (
        "通过监控 WiFi 信号统计周围人数。\n"
        "[@] 需要 WiFi 适配器\n"
        "[*] 在您不拥有的网络上监视 MAC 地址可能是非法的。"
    )
    INSTALL_COMMANDS = [
        # Bug 14 fix: missing comma caused "sudo apt-get install tshark;sudo python3..."
        # to be one implicitly concatenated string — only first command ran
        "sudo apt-get install -y tshark",
        "sudo python3 -m pip install howmanypeoplearearound",
    ]
    RUN_COMMANDS = ["howmanypeoplearearound"]
    SUPPORTED_OS = ["linux"]
    REQUIRES_WIFI = True


class Airgeddon(HackingTool):
    TITLE = "Airgeddon (Wireless Attack Suite)"
    DESCRIPTION = (
        "多用途 bash 脚本，用于审计无线网络。\n"
        "涵盖 WPA/WPA2、WEP、WPS、PMKID、邪恶双子、握手包捕获等。"
    )
    SUPPORTED_OS = ["linux"]
    REQUIRES_WIFI = True
    INSTALL_COMMANDS = [
        "git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git",
    ]
    RUN_COMMANDS = ["cd airgeddon && sudo bash airgeddon.sh"]
    PROJECT_URL = "https://github.com/v1s1t0r1sh3r3/airgeddon"


class Hcxdumptool(HackingTool):
    TITLE = "hcxdumptool (PMKID Capture)"
    DESCRIPTION = (
        "从 WLAN 设备捕获数据包和 PMKID 哈希。\n"
        "用法: hcxdumptool -i <iface> -o capture.pcapng --enable_status=1"
    )
    SUPPORTED_OS = ["linux"]
    REQUIRES_WIFI = True
    INSTALL_COMMANDS = [
        "git clone https://github.com/ZerBea/hcxdumptool.git",
        "cd hcxdumptool && make && sudo make install",
    ]
    RUN_COMMANDS = ["hcxdumptool --help"]
    PROJECT_URL = "https://github.com/ZerBea/hcxdumptool"


class Hcxtools(HackingTool):
    TITLE = "hcxtools (PMKID/Hash Conversion)"
    DESCRIPTION = (
        "将捕获的 WLAN 数据包转换为 hashcat/JtR 兼容格式。\n"
        "用法: hcxpcapngtool -o hashes.txt capture.pcapng"
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        "git clone https://github.com/ZerBea/hcxtools.git",
        "cd hcxtools && make && sudo make install",
    ]
    RUN_COMMANDS = ["hcxpcapngtool --help"]
    PROJECT_URL = "https://github.com/ZerBea/hcxtools"


class Bettercap(HackingTool):
    TITLE = "Bettercap (Network/WiFi/BLE MITM)"
    DESCRIPTION = "WiFi、BLE、HID 和以太网网络侦察和 MITM 攻击的瑞士军刀。"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt-get install -y bettercap"]
    RUN_COMMANDS = ["sudo bettercap --help"]
    PROJECT_URL = "https://github.com/bettercap/bettercap"


class WirelessAttackTools(HackingToolsCollection):
    TITLE = t("category.wireless")
    TOOLS = [
        WIFIPumpkin(),
        pixiewps(),
        BluePot(),
        Fluxion(),
        Wifiphisher(),
        Wifite(),
        EvilTwin(),
        Fastssh(),
        Howmanypeople(),
        Airgeddon(),
        Hcxdumptool(),
        Hcxtools(),
        Bettercap(),
    ]


if __name__ == "__main__":
    tools = WirelessAttackTools()
    tools.show_options()

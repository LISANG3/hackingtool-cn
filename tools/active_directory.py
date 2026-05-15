from core import HackingTool
from core import HackingToolsCollection
from i18n import t


class BloodHound(HackingTool):
    TITLE = "BloodHound (AD Attack Paths)"
    DESCRIPTION = "使用图论揭示 Active Directory/Azure 环境中的隐藏攻击路径。"
    INSTALL_COMMANDS = [
        "pip install --user bloodhound",
        "sudo apt-get install -y neo4j",
    ]
    RUN_COMMANDS = ["bloodhound-python --help"]
    PROJECT_URL = "https://github.com/BloodHoundAD/BloodHound"
    SUPPORTED_OS = ["linux", "macos"]


class NetExec(HackingTool):
    TITLE = "NetExec — nxc (Network Pentesting)"
    DESCRIPTION = "渗透测试 Windows/AD 网络的瑞士军刀。CrackMapExec 的继任者。"
    INSTALL_COMMANDS = ["pip install --user netexec"]
    RUN_COMMANDS = ["nxc --help"]
    PROJECT_URL = "https://github.com/Pennyw0rth/NetExec"
    SUPPORTED_OS = ["linux", "macos"]


class Impacket(HackingTool):
    TITLE = "Impacket (Network Protocol Tools)"
    DESCRIPTION = "用于处理 SMB、MSRPC、Kerberos、LDAP 等的 Python 类。"
    INSTALL_COMMANDS = ["pip install --user impacket"]
    RUN_COMMANDS = ["impacket-smbclient --help"]
    PROJECT_URL = "https://github.com/fortra/impacket"
    SUPPORTED_OS = ["linux", "macos"]


class Responder(HackingTool):
    TITLE = "Responder (LLMNR/NBT-NS Poisoner)"
    DESCRIPTION = "LLMNR/NBT-NS/MDNS 投毒器，带有用于凭据捕获的伪造认证服务器。"
    INSTALL_COMMANDS = ["git clone https://github.com/lgandx/Responder.git"]
    RUN_COMMANDS = ["cd Responder && sudo python3 Responder.py --help"]
    PROJECT_URL = "https://github.com/lgandx/Responder"
    SUPPORTED_OS = ["linux"]


class Certipy(HackingTool):
    TITLE = "Certipy (AD Certificate Abuse)"
    DESCRIPTION = "Active Directory 证书服务枚举和滥用工具。"
    INSTALL_COMMANDS = ["pip install --user certipy-ad"]
    RUN_COMMANDS = ["certipy --help"]
    PROJECT_URL = "https://github.com/ly4k/Certipy"
    SUPPORTED_OS = ["linux", "macos"]


class Kerbrute(HackingTool):
    TITLE = "Kerbrute (Kerberos Brute Force)"
    DESCRIPTION = "Kerberos 预认证暴力破解器，用于用户名枚举和密码喷洒。"
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install github.com/ropnop/kerbrute@latest",
    ]
    RUN_COMMANDS = ["kerbrute --help"]
    PROJECT_URL = "https://github.com/ropnop/kerbrute"
    SUPPORTED_OS = ["linux", "macos"]


class ActiveDirectoryTools(HackingToolsCollection):
    TITLE = t("category.active_directory")
    DESCRIPTION = "用于 AD 枚举、攻击路径发现和凭据攻击的工具。"
    TOOLS = [
        BloodHound(),
        NetExec(),
        Impacket(),
        Responder(),
        Certipy(),
        Kerbrute(),
    ]
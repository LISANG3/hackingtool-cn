from core import HackingTool
from core import HackingToolsCollection
from i18n import t


class MobSF(HackingTool):
    TITLE = "MobSF (Mobile Security Framework)"
    DESCRIPTION = "一体化的移动应用渗透测试、恶意软件分析和安全评估工具。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git",
        "cd Mobile-Security-Framework-MobSF && ./setup.sh",
    ]
    RUN_COMMANDS = ["cd Mobile-Security-Framework-MobSF && ./run.sh"]
    PROJECT_URL = "https://github.com/MobSF/Mobile-Security-Framework-MobSF"
    SUPPORTED_OS = ["linux", "macos"]


class Frida(HackingTool):
    TITLE = "Frida (Dynamic Instrumentation)"
    DESCRIPTION = "用于 Android、iOS、Windows、macOS、Linux 运行时挂钩的动态插桩工具包。"
    INSTALL_COMMANDS = ["pip install --user frida-tools"]
    RUN_COMMANDS = ["frida --help"]
    PROJECT_URL = "https://github.com/frida/frida"
    SUPPORTED_OS = ["linux", "macos"]


class Objection(HackingTool):
    TITLE = "Objection (Mobile Runtime Exploration)"
    DESCRIPTION = "由 Frida 驱动的运行时移动探索工具包 — 无需越狱/root。"
    INSTALL_COMMANDS = ["pip install --user objection"]
    RUN_COMMANDS = ["objection --help"]
    PROJECT_URL = "https://github.com/sensepost/objection"
    SUPPORTED_OS = ["linux", "macos"]


class MobileSecurityTools(HackingToolsCollection):
    TITLE = t("category.mobile")
    DESCRIPTION = "用于 Android/iOS 应用安全测试与分析的工具集合。"
    TOOLS = [
        MobSF(),
        Frida(),
        Objection(),
    ]
import subprocess

from rich.prompt import Prompt

from core import HackingTool, HackingToolsCollection, console

from i18n import t

class DDoSTool(HackingTool):
    TITLE = "DDoS"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "最佳 DDoS 攻击脚本，包含 36+ 种方法。\n"
        "仅供安全测试使用!"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/the-deepnet/ddos.git",
        "cd ddos && sudo pip3 install -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/the-deepnet/ddos"

    def run(self):
        from config import get_tools_dir
        method     = Prompt.ask(t("prompt.enter_method"))
        url        = Prompt.ask(t("prompt.enter_url"))
        threads    = Prompt.ask(t("prompt.enter_threads"))
        proxylist  = Prompt.ask(t("prompt.enter_proxy_list"))
        multiple   = Prompt.ask(t("prompt.enter_multiple"))
        timer      = Prompt.ask(t("prompt.enter_timer"))
        # Bug 4 fix: removed os.system("cd ddos;") — use cwd= instead
        subprocess.run(
            ["sudo", "python3", "ddos.py", method, url,
             "socks_type5.4.1", threads, proxylist, multiple, timer],
            cwd=str(get_tools_dir() / "ddos"),
        )


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "Slowloris 是一种 HTTP 拒绝服务攻击，\n"
        "通过发送大量 HTTP 请求耗尽目标资源。"
    )
    INSTALL_COMMANDS = ["sudo pip3 install slowloris"]

    def run(self):
        target_site = Prompt.ask(t("prompt.enter_target_site"))
        subprocess.run(["slowloris", target_site])


class Asyncrone(HackingTool):
    TITLE = "Asyncrone | Multifunction SYN Flood DDoS Weapon"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "aSYNcrone 是一个基于 C 语言的多功能 SYN Flood DDoS 武器。\n"
        "通过密集发送 SYN 数据包使目标系统瘫痪。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/fatih4842/aSYNcrone.git",
        "cd aSYNcrone && sudo gcc aSYNcrone.c -o aSYNcrone -lpthread",
    ]
    PROJECT_URL = "https://github.com/fatihsnsy/aSYNcrone"

    def run(self):
        from config import get_tools_dir
        source_port = Prompt.ask(t("prompt.enter_source_port"))
        target_ip   = Prompt.ask(t("prompt.enter_target_ip"))
        target_port = Prompt.ask(t("prompt.enter_target_port"))
        # Bug 5 fix: 1000 was int — subprocess requires all args str
        # Bug 4 fix: removed os.system("cd aSYNcrone;") — use cwd= instead
        subprocess.run(
            ["sudo", "./aSYNcrone", str(source_port), str(target_ip), str(target_port), "1000"],
            cwd=str(get_tools_dir() / "aSYNcrone"),
        )


class UFONet(HackingTool):
    TITLE = "UFOnet"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "UFONet 是一个免费、P2P 和加密的破坏性工具包，\n"
        "可用于执行 DoS 和 DDoS 攻击。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/epsylon/ufonet.git",
        "cd ufonet && pip install --user .",
    ]
    RUN_COMMANDS = ["python3 ufonet --gui"]
    PROJECT_URL = "https://github.com/epsylon/ufonet"


class GoldenEye(HackingTool):
    TITLE = "GoldenEye"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "GoldenEye 是一个仅供安全测试使用的 Python3 应用!\n"
        "GoldenEye 是一款 HTTP DoS 测试工具。\n"
        "用法: ./goldeneye.py <url> [选项]"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/jseidl/GoldenEye.git",
        "chmod -R 755 GoldenEye",
    ]
    PROJECT_URL = "https://github.com/jseidl/GoldenEye"

    def run(self):
        from config import get_tools_dir
        # Bug 4 fix: removed os.system("cd GoldenEye; ...") — no-op cd subshell
        url = Prompt.ask(t("prompt.enter_url"))
        subprocess.run(["sudo", "./goldeneye.py", url],
                       cwd=str(get_tools_dir() / "GoldenEye"))


class Saphyra(HackingTool):
    TITLE = "SaphyraDDoS"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "仅供安全测试使用的 Python DDoS 脚本。"
    INSTALL_COMMANDS = [
        # Bug 7 fix: removed "sudo su" (first step was dropping into interactive root shell)
        "git clone https://github.com/anonymous24x7/Saphyra-DDoS.git",
        "chmod +x Saphyra-DDoS/saphyra.py",
    ]
    PROJECT_URL = "https://github.com/anonymous24x7/Saphyra-DDoS"

    def run(self):
        from config import get_tools_dir
        url = Prompt.ask(t("prompt.enter_url"))
        # Vuln 1 fix: was os.system("python saphyra.py " + url) — command injection
        # Now uses subprocess list form — url is never interpolated into a shell string
        subprocess.run(
            ["python3", "saphyra.py", url],
            cwd=str(get_tools_dir() / "Saphyra-DDoS"),
        )


class DDOSTools(HackingToolsCollection):
    TITLE = t("category.ddos")
    TOOLS = [DDoSTool(), SlowLoris(), Asyncrone(), UFONet(), GoldenEye(), Saphyra()]


if __name__ == "__main__":
    tools = DDOSTools()
    tools.show_options()

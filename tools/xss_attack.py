import os
import subprocess
from rich.panel import Panel
from rich.prompt import Prompt

from core import HackingTool, HackingToolsCollection, console
from i18n import t


class Dalfox(HackingTool):
    TITLE = "DalFox (Finder of XSS)"
    DESCRIPTION = "XSS 扫描和参数分析工具。"
    INSTALL_COMMANDS = [
        "sudo apt-get install -y golang",
        "go install github.com/hahwul/dalfox/v2@latest",
    ]
    RUN_COMMANDS = [
        "~/go/bin/dalfox --help",
    ]
    PROJECT_URL = "https://github.com/hahwul/dalfox"


class XSSPayloadGenerator(HackingTool):
    TITLE = "XSS Payload Generator"
    DESCRIPTION = "XSS PAYLOAD 生成器 - XSS 扫描器 - XSS DORK 查找器"
    INSTALL_COMMANDS = [
        "git clone https://github.com/capture0x/XSS-LOADER.git",
        "cd XSS-LOADER;sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd XSS-LOADER;sudo python3 payloader.py"]
    PROJECT_URL = "https://github.com/capture0x/XSS-LOADER.git"


class XSSFinder(HackingTool):
    TITLE = "Extended XSS Searcher and Finder"
    DESCRIPTION = "扩展 XSS 搜索器和查找器"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Damian89/extended-xss-search.git"]
    PROJECT_URL = "https://github.com/Damian89/extended-xss-search"

    def after_install(self):
        console.print(Panel.fit(
            t("tool.xssfinder.after_install_panel"),
            title=t("tool.xssfinder.after_install_title"),
            border_style="magenta"
        ))
        input(t("prompt.press_enter_continue"))

    def run(self):
        console.print(Panel.fit(
            t("tool.xssfinder.run_panel"),
            title=t("tool.xssfinder.run_title"),
            border_style="blue"
        ))


class XSSFreak(HackingTool):
    TITLE = "XSS-Freak"
    DESCRIPTION = "一款完全用 Python 3 从头编写的 XSS 扫描器。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/PR0PH3CY33/XSS-Freak.git",
        "cd XSS-Freak;sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd XSS-Freak;sudo python3 XSS-Freak.py"]
    PROJECT_URL = "https://github.com/PR0PH3CY33/XSS-Freak"


class XSpear(HackingTool):
    TITLE = "XSpear"
    DESCRIPTION = "XSpear 是一款基于 Ruby Gems 构建的 XSS 扫描器。"
    INSTALL_COMMANDS = ["gem install XSpear"]
    RUN_COMMANDS = ["XSpear -h"]
    PROJECT_URL = "https://github.com/hahwul/XSpear"


class XSSCon(HackingTool):
    TITLE = "XSSCon"
    INSTALL_COMMANDS = [
        "git clone https://github.com/menkrep1337/XSSCon.git",
        "sudo chmod 755 -R XSSCon"
    ]
    PROJECT_URL = "https://github.com/menkrep1337/XSSCon"

    def run(self):
        console.print(Panel.fit(
            t("tool.xsscon.panel"),
            title=t("tool.xsscon.panel_title"),
            border_style="bright_yellow"
        ))
        website = Prompt.ask(t("prompt.enter_website"))
        from config import get_tools_dir
        subprocess.run(["python3", "xsscon.py", "-u", website],
                       cwd=str(get_tools_dir() / "XSSCon"))


class XanXSS(HackingTool):
    TITLE = "XanXSS"
    DESCRIPTION = "一款反射型 XSS 搜索工具，可根据模板创建 Payload。"
    INSTALL_COMMANDS = ["git clone https://github.com/Ekultek/XanXSS.git"]
    PROJECT_URL = "https://github.com/Ekultek/XanXSS"

    def run(self):
        from config import get_tools_dir
        subprocess.run(["python3", "xanxss.py", "-h"],
                       cwd=str(get_tools_dir() / "XanXSS"))


class XSSStrike(HackingTool):
    TITLE = "Advanced XSS Detection Suite"
    DESCRIPTION = "XSStrike 是一款基于 Python 的工具，用于检测和利用 XSS 漏洞。"
    INSTALL_COMMANDS = [
        "sudo rm -rf XSStrike",
        "git clone https://github.com/UltimateHackers/XSStrike.git "
        "&& cd XSStrike && pip install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/UltimateHackers/XSStrike"

    def __init__(self):
        super().__init__(runnable=False)


class RVuln(HackingTool):
    TITLE = "RVuln"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "一款用 Rust 编写的多线程自动化 Web 漏洞扫描器。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/iinc0gnit0/RVuln.git;"
        "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh;"
        "source $HOME/.cargo/env;"
        "sudo apt install librust-openssl-dev;"
        "cd RVuln;sudo su;cargo build --release;mv target/release/RVuln"
    ]
    RUN_COMMANDS = ["RVuln"]
    PROJECT_URL = "https://github.com/iinc0gnit0/RVuln"


class XSSAttackTools(HackingToolsCollection):
    TITLE = t("category.xss")
    TOOLS = [
        Dalfox(),
        XSSPayloadGenerator(),
        XSSFinder(),
        XSSFreak(),
        XSpear(),
        XSSCon(),
        XanXSS(),
        XSSStrike(),
        RVuln()
    ]

    def show_info(self):
        console.print(Panel.fit(
            t("tool.xss_attack.info_panel"),
            border_style="bright_magenta"
        ))

import os
import subprocess

from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich import box

from core import HackingTool, HackingToolsCollection, console

from i18n import t

class Cupp(HackingTool):
    TITLE = "Cupp"
    # Bug 24 fix: DESCRIPTION was copy-pasted from WlCreator — completely wrong
    DESCRIPTION = "通用用户密码分析器 — 基于目标信息生成个性化字典。"
    INSTALL_COMMANDS = ["git clone https://github.com/Mebus/cupp.git"]
    RUN_COMMANDS = ["cd cupp && python3 cupp.py -i"]
    PROJECT_URL = "https://github.com/Mebus/cupp"

    def show_info(self):
        panel = Panel(
            f"[bold purple]{self.TITLE}[/bold purple]\n\n"
            f"[cyan]{self.DESCRIPTION}[/cyan]\n\n"
            f"[green]Repository:[/green] [underline blue]{self.PROJECT_URL}[/underline blue]",
            border_style="purple",
            box=box.ROUNDED,
        )
        console.print(panel)


class WlCreator(HackingTool):
    TITLE = "WordlistCreator"
    DESCRIPTION = "WlCreator 是一个 C 程序，可生成所有可能的密码组合，\n" \
                  "可选择长度、小写字母、大写字母、数字和特殊字符"
    INSTALL_COMMANDS = ["git clone https://github.com/Z4nzu/wlcreator.git"]
    RUN_COMMANDS = [
        "cd wlcreator && sudo gcc -o wlcreator wlcreator.c && ./wlcreator 5"]
    PROJECT_URL = "https://github.com/Z4nzu/wlcreator"

    def show_info(self):
        panel = Panel(
            f"[bold purple]{self.TITLE}[/bold purple]\n\n"
            f"[cyan]{self.DESCRIPTION}[/cyan]\n\n"
            f"[green]Repository:[/green] [underline blue]{self.PROJECT_URL}[/underline blue]",
            border_style="purple",
            box=box.ROUNDED,
        )
        console.print(panel)


class GoblinWordGenerator(HackingTool):
    TITLE = "Goblin WordGenerator"
    DESCRIPTION = "Goblin 字典生成器"
    INSTALL_COMMANDS = [
        "git clone https://github.com/UndeadSec/GoblinWordGenerator.git"]
    RUN_COMMANDS = ["cd GoblinWordGenerator && python3 goblin.py"]
    PROJECT_URL = "https://github.com/UndeadSec/GoblinWordGenerator.git"

    def show_info(self):
        panel = Panel(
            f"[bold purple]{self.TITLE}[/bold purple]\n\n"
            f"[cyan]{self.DESCRIPTION}[/cyan]\n\n"
            f"[green]Repository:[/green] [underline blue]{self.PROJECT_URL}[/underline blue]",
            border_style="purple",
            box=box.ROUNDED,
        )
        console.print(panel)


class showme(HackingTool):
    TITLE = "Password list (1.4 Billion Clear Text Password)"
    DESCRIPTION = "该工具可对组织或个人进行 OSINT 和侦察。\n" \
                  "可搜索 BreachCompilation 泄露数据中的\n" \
                  "14 亿条明文凭证，让密码查找比以往更快更简单。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got.git",
        "cd SMWYG-Show-Me-What-You-Got && pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd SMWYG-Show-Me-What-You-Got && python SMWYG.py"]
    PROJECT_URL = "https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got"

    def show_info(self):
        panel = Panel(
            f"[bold purple]{self.TITLE}[/bold purple]\n\n"
            f"[cyan]{self.DESCRIPTION}[/cyan]\n\n"
            f"[green]Repository:[/green] [underline blue]{self.PROJECT_URL}[/underline blue]",
            border_style="purple",
            box=box.ROUNDED,
        )
        console.print(panel)


class Hashcat(HackingTool):
    TITLE = "Hashcat (Password Cracker)"
    DESCRIPTION = (
        "全球最快的 GPU/CPU 密码恢复工具 — 支持 300+ 种哈希类型。\n"
        "用法: hashcat -m 0 -a 0 hashes.txt wordlist.txt"
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt-get install -y hashcat"]
    RUN_COMMANDS = ["hashcat --help"]
    PROJECT_URL = "https://github.com/hashcat/hashcat"


class JohnTheRipper(HackingTool):
    TITLE = "John the Ripper"
    DESCRIPTION = (
        "开源密码安全审计和恢复工具。\n"
        "用法: john --wordlist=wordlist.txt hashfile"
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt-get install -y john"]
    RUN_COMMANDS = ["john --help"]
    PROJECT_URL = "https://github.com/openwall/john"


class Haiti(HackingTool):
    TITLE = "haiti (Hash Type Identifier)"
    DESCRIPTION = (
        "识别哈希类型 — 支持 300+ 种算法。\n"
        "用法: haiti <hash>"
    )
    REQUIRES_RUBY = True
    INSTALL_COMMANDS = ["gem install haiti-hash"]
    RUN_COMMANDS = ["haiti --help"]
    PROJECT_URL = "https://github.com/noraj/haiti"


class WordlistGeneratorTools(HackingToolsCollection):
    TITLE = t("category.wordlist")
    TOOLS = [
        Cupp(),
        WlCreator(),
        GoblinWordGenerator(),
        showme(),
        Hashcat(),
        JohnTheRipper(),
        Haiti(),
    ]

    def show_info(self):
        header = Panel(f"[bold white on purple] {self.TITLE} [/bold white on purple]",
                       border_style="purple", box=box.DOUBLE)
        console.print(header)
        table = Table(box=box.SIMPLE, show_header=True, header_style="bold purple")
        table.add_column("#", justify="center", style="cyan", width=4)
        table.add_column("Tool", style="bold")
        table.add_column("Description", style="dim", overflow="fold")

        for idx, t in enumerate(self.TOOLS, start=1):
            desc = getattr(t, "DESCRIPTION", "") or ""
            table.add_row(str(idx), t.TITLE, desc)

        table.add_row("[red]99[/red]", "[bold red]退出[/bold red]", "返回上级菜单")
        console.print(table)

if __name__ == "__main__":
    tools = WordlistGeneratorTools()
    tools.show_info()
    tools.show_options()

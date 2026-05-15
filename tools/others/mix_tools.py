from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class TerminalMultiplexer(HackingTool):
    TITLE = "Terminal Multiplexer"
    DESCRIPTION = (
        "Terminal Multiplexer (tilix) 是一个平铺式终端模拟器，"
        "允许在一个窗口中打开多个终端会话。"
    )
    # Bug 19 fix: tilix is a Debian/Ubuntu package only — mark Linux-only
    INSTALL_COMMANDS = ["sudo apt-get install -y tilix"]
    SUPPORTED_OS = ["linux"]

    def __init__(self):
        # Py3-4 fix: super(TerminalMultiplexer, self) → super()
        super().__init__(runnable=False)


class Crivo(HackingTool):
    TITLE = "Crivo"
    DESCRIPTION = (
        "用于从网页或文本中提取和过滤 URL、IP、域名和子域名的工具，\n"
        "内置网络爬取功能。\n"
        "使用方法: python3 crivo_cli.py -h"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/GMDSantana/crivo.git",
        # Bug 18 verify: this is correct — cd and pip in same string works
        "cd crivo && pip install --user -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/GMDSantana/crivo"

    def __init__(self):
        # Py3-4 fix: super(Crivo, self) → super()
        super().__init__(runnable=False)


class MixTools(HackingToolsCollection):
    TITLE = "混合工具"
    TOOLS = [
        TerminalMultiplexer(),
        Crivo()
    ]

if __name__ == "__main__":
    tools = MixTools()
    tools.show_options()

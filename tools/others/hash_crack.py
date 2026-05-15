from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class HashBuster(HackingTool):
    TITLE = "Hash Buster"
    DESCRIPTION = "功能特点:\n " \
                  "自动识别哈希类型\n " \
                  "支持 MD5, SHA1, SHA256, SHA384, SHA512"
    INSTALL_COMMANDS = [
        "git clone https://github.com/s0md3v/Hash-Buster.git",
        "cd Hash-Buster;make install"
    ]
    RUN_COMMANDS = ["buster -h"]
    PROJECT_URL = "https://github.com/s0md3v/Hash-Buster"


class HashCrackingTools(HackingToolsCollection):
    TITLE = "哈希破解工具"
    TOOLS = [HashBuster()]

if __name__ == "__main__":
    tools = HashCrackingTools()
    tools.show_options()

from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class EvilURL(HackingTool):
    TITLE = "EvilURL"
    DESCRIPTION = "生成用于 IDN 同形字攻击的恶意 Unicode 域名并可检测它们。"
    INSTALL_COMMANDS = ["git clone https://github.com/UndeadSec/EvilURL.git"]
    RUN_COMMANDS = ["cd EvilURL;python3 evilurl.py"]
    PROJECT_URL = "https://github.com/UndeadSec/EvilURL"


class IDNHomographAttackTools(HackingToolsCollection):
    TITLE = "IDN 同形字攻击"
    TOOLS = [EvilURL()]

if __name__ == "__main__":
    tools = IDNHomographAttackTools()
    tools.show_options()

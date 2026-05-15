from core import HackingTool, HackingToolsCollection, console
from i18n import t

from rich.panel import Panel
from rich.prompt import Prompt


class KnockMail(HackingTool):
    TITLE = "Knockmail"
    DESCRIPTION = "验证电子邮件是否存在的工具"
    INSTALL_COMMANDS = [
        "git clone https://github.com/heywoodlh/KnockMail.git",
        "cd KnockMail;sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd KnockMail;python3 knockmail.py"]
    PROJECT_URL = "https://github.com/heywoodlh/KnockMail"


class EmailVerifyTools(HackingToolsCollection):
    TITLE = "邮箱验证工具"
    TOOLS = [KnockMail()]

if __name__ == "__main__":
    tools = EmailVerifyTools()
    tools.show_options()

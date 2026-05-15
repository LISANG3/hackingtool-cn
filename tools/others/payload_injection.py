from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class DebInject(HackingTool):
    TITLE = "Debinject"
    DESCRIPTION = "Debinject 是一个将恶意代码注入到 *.deb 包中的工具"
    INSTALL_COMMANDS = [
        "git clone https://github.com/UndeadSec/Debinject.git"]
    RUN_COMMANDS = ["cd Debinject;python debinject.py"]
    PROJECT_URL = "https://github.com/UndeadSec/Debinject"


class Pixload(HackingTool):
    TITLE = "Pixload"
    DESCRIPTION = "Pixload -- 图片 Payload 创建工具\n " \
                  "Pixload 是一组用于创建/注入 payload 到图片中的工具。"
    INSTALL_COMMANDS = [
        "sudo apt install libgd-perl libimage-exiftool-perl libstring-crc32-perl",
        "git clone https://github.com/chinarulezzz/pixload.git"
    ]
    PROJECT_URL = "https://github.com/chinarulezzz/pixload"

    def __init__(self):
        super().__init__(runnable = False)


class PayloadInjectorTools(HackingToolsCollection):
    TITLE = "Payload 注入器"
    TOOLS = [
        DebInject(),
        Pixload()
    ]

if __name__ == "__main__":
    tools = PayloadInjectorTools()
    tools.show_options()

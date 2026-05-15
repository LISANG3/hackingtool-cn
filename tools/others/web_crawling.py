from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class GoSpider(HackingTool):
    TITLE = "Gospider"
    DESCRIPTION = "Gospider - 用 Go 编写的快速网络爬虫"
    INSTALL_COMMANDS = ["sudo go get -u github.com/jaeles-project/gospider"]
    PROJECT_URL = "https://github.com/jaeles-project/gospider"

    def __init__(self):
        super().__init__(runnable = False)


class WebCrawlingTools(HackingToolsCollection):
    TITLE = "网络爬虫"
    TOOLS = [GoSpider()]

if __name__ == "__main__":
    tools = WebCrawlingTools()
    tools.show_options()

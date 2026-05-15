import subprocess

from core import HackingTool, HackingToolsCollection, console
from core import validate_input

from rich.panel import Panel
from rich.prompt import Prompt

from i18n import t

class SteganoHide(HackingTool):
    TITLE = "SteganoHide"
    INSTALL_COMMANDS = ["sudo apt-get install steghide -y"]

    def run(self):
        choice_run = input(
            f"[1] {t('tool.hide')}\n"
            f"[2] {t('tool.extract')}\n"
            f"[99]{t('prompt.cancel')}\n"
            ">> "
        )
        choice_run = validate_input(choice_run, [1, 2, 99])
        if choice_run is None:
            console.print(f"[bold red]{t('prompt.choose_valid')}[/bold red]")
            return self.run()

        if choice_run == 99:
            return

        if choice_run == 1:
            file_hide = input(t("prompt.enter_embed_file"))
            file_to_be_hide = input(t("prompt.enter_cover_file"))
            subprocess.run(["steghide", "embed", "-cf", file_to_be_hide, "-ef", file_hide])

        elif choice_run == 2:
            from_file = input(t("prompt.enter_extract_file"))
            subprocess.run(["steghide", "extract", "-sf", from_file])


class StegnoCracker(HackingTool):
    TITLE = "StegnoCracker"
    DESCRIPTION = "SteganoCracker 通过暴力破解工具揭示文件中隐藏的数据"
    INSTALL_COMMANDS = ["pip3 install stegcracker && pip3 install stegcracker -U --force-reinstall"]

    def run(self):
        filename = input(t("prompt.enter_filename"))
        passfile = input(t("prompt.enter_wordlist_filename"))
        subprocess.run(["stegcracker", filename, passfile])


class StegoCracker(HackingTool):
    TITLE = "StegoCracker"
    DESCRIPTION = "StegoCracker 让你在图像或音频文件中隐藏和提取数据"
    INSTALL_COMMANDS = [
        "git clone https://github.com/W1LDN16H7/StegoCracker.git",
        "sudo chmod -R 755 StegoCracker"
    ]
    RUN_COMMANDS = [
        "cd StegoCracker && python3 -m pip install -r requirements.txt",
        "./install.sh"
    ]
    PROJECT_URL = "https://github.com/W1LDN16H7/StegoCracker"


class Whitespace(HackingTool):
    TITLE = "Whitespace"
    DESCRIPTION = "使用空白字符和 Unicode 字符进行隐写术"
    INSTALL_COMMANDS = [
        "git clone https://github.com/beardog108/snow10.git",
        "sudo chmod -R 755 snow10"
    ]
    RUN_COMMANDS = ["cd snow10 && ./install.sh"]
    PROJECT_URL = "https://github.com/beardog108/snow10"


class SteganographyTools(HackingToolsCollection):
    TITLE = t("category.stegano")
    TOOLS = [SteganoHide(), StegnoCracker(), StegoCracker(), Whitespace()]

if __name__ == "__main__":
    tools = SteganographyTools()
    tools.show_options()

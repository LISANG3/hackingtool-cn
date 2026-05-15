import os

from core import HackingTool, HackingToolsCollection, console
from i18n import t


class AnonymouslySurf(HackingTool):
    TITLE = "Anonymously Surf"
    DESCRIPTION = "在系统关机时自动覆盖 RAM，并更改你的 IP 地址。"
    # Bug 28 fix: was "cd kali-anonsurf && ./installer.sh && cd .. && sudo rm -r kali-anonsurf"
    # Deleting the source on install means there is no retry if install fails.
    # Now kept in a separate step so failure does not destroy the source.
    INSTALL_COMMANDS = [
        "git clone https://github.com/Und3rf10w/kali-anonsurf.git",
        "cd kali-anonsurf && sudo ./installer.sh",
    ]
    RUN_COMMANDS = ["sudo anonsurf start"]
    PROJECT_URL = "https://github.com/Und3rf10w/kali-anonsurf"
    SUPPORTED_OS = ["linux"]

    def __init__(self):
        super().__init__([("Stop", self.stop)])

    def stop(self):
        import subprocess
        console.print(t("anonsurf.stopping"))
        subprocess.run(["sudo", "anonsurf", "stop"])


class Multitor(HackingTool):
    TITLE = "Multitor"
    DESCRIPTION = "如何同时在多个地方保持连接。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/trimstray/multitor.git",
        "cd multitor && sudo bash setup.sh install",
    ]
    RUN_COMMANDS = [
        "multitor --init 2 --user debian-tor --socks-port 9000 --control-port 9900 --proxy privoxy --haproxy"
    ]
    PROJECT_URL = "https://github.com/trimstray/multitor"
    SUPPORTED_OS = ["linux"]

    def __init__(self):
        super().__init__(runnable=False)


class AnonSurfTools(HackingToolsCollection):
    TITLE = t("category.anonsurf")
    TOOLS = [
        AnonymouslySurf(),
        Multitor(),
    ]


if __name__ == "__main__":
    tools = AnonSurfTools()
    tools.show_options()

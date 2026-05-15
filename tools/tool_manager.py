import os
import sys
import subprocess
from time import sleep

from rich.prompt import Confirm

from i18n import t

from core import HackingTool, HackingToolsCollection, console
from constants import APP_INSTALL_DIR, APP_BIN_PATH, USER_CONFIG_DIR, REPO_URL


class UpdateTool(HackingTool):
    TITLE = "Update Tool or System"
    DESCRIPTION = "更新系统包或拉取最新的 hackingtool 代码"

    def __init__(self):
        super().__init__([
            ("Update System", self.update_sys),
            ("Update Hackingtool", self.update_ht),
        ], installable=False, runnable=False)

    def update_sys(self):
        from os_detect import CURRENT_OS, PACKAGE_UPDATE_CMDS
        mgr = CURRENT_OS.pkg_manager
        cmd = PACKAGE_UPDATE_CMDS.get(mgr)
        if cmd:
            priv = "" if (CURRENT_OS.system == "macos" or os.geteuid() == 0) else "sudo "
            # shell=True needed — cmd contains && chains; strings are hardcoded, not user input
            subprocess.run(f"{priv}{cmd}", shell=True, check=False)
        else:
            console.print(f"[warning]{t('update.unknown_mgr')}[/warning]")

    def update_ht(self):
        if not APP_INSTALL_DIR.exists():
            console.print(f"[error]{t('update.dir_not_found', dir=APP_INSTALL_DIR)}[/error]")
            console.print(f"[dim]{t('update.run_install')}[/dim]")
            return
        console.print(f"[bold cyan]{t('update.pulling', url=REPO_URL)}[/bold cyan]")
        result = subprocess.run(
            ["git", "pull", "--rebase"],
            cwd=str(APP_INSTALL_DIR),
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            console.print(f"[error]{t('update.pull_failed', err=result.stderr)}[/error]")
            return
        pip = str(APP_INSTALL_DIR / "venv" / "bin" / "pip")
        if (APP_INSTALL_DIR / "venv" / "bin" / "pip").exists():
            subprocess.run([pip, "install", "-q", "-r",
                            str(APP_INSTALL_DIR / "requirements.txt")])
        console.print(f"[success]✔ {t('update.updated')}[/success]")


class UninstallTool(HackingTool):
    TITLE = "Uninstall HackingTool"
    DESCRIPTION = "从系统中移除 hackingtool"

    def __init__(self):
        super().__init__([
            ("Uninstall", self.uninstall),
        ], installable=False, runnable=False)

    def uninstall(self):
        import shutil
        console.print(f"[warning]{t('uninstall.warning')}[/warning]")
        if not Confirm.ask(t("uninstall.continue"), default=False):
            return

        if APP_INSTALL_DIR.exists():
            shutil.rmtree(str(APP_INSTALL_DIR))
            console.print(f"[success]✔ {t('uninstall.removed_dir', dir=APP_INSTALL_DIR)}[/success]")
        else:
            console.print(f"[dim]{t('uninstall.dir_missing', dir=APP_INSTALL_DIR)}[/dim]")

        if APP_BIN_PATH.exists():
            APP_BIN_PATH.unlink()
            console.print(f"[success]✔ {t('uninstall.removed_launcher', path=APP_BIN_PATH)}[/success]")

        if Confirm.ask(t("uninstall.remove_user_data", dir=USER_CONFIG_DIR), default=False):
            shutil.rmtree(str(USER_CONFIG_DIR), ignore_errors=True)
            console.print(f"[success]✔ {t('uninstall.removed_dir', dir=USER_CONFIG_DIR)}[/success]")

        console.print(f"[bold green]{t('uninstall.goodbye')}[/bold green]")
        sleep(1)
        sys.exit(0)


class ToolManager(HackingToolsCollection):
    TITLE = t("category.update_uninstall")
    TOOLS = [
        UpdateTool(),
        UninstallTool(),
    ]


if __name__ == "__main__":
    manager = ToolManager()
    manager.show_options()

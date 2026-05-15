import os
import shutil
import sys
import webbrowser
from collections.abc import Callable
from platform import system

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text
from rich.theme import Theme
from rich.traceback import install

from constants import (
    THEME_PRIMARY, THEME_BORDER, THEME_ACCENT,
    THEME_SUCCESS, THEME_ERROR, THEME_WARNING,
    THEME_DIM, THEME_ARCHIVED, THEME_URL,
)
from i18n import t

# Enable rich tracebacks globally
install()

_theme = Theme({
    "purple":   "#7B61FF",
    "success":  THEME_SUCCESS,
    "error":    THEME_ERROR,
    "warning":  THEME_WARNING,
    "archived": THEME_ARCHIVED,
    "url":      THEME_URL,
    "dim":      THEME_DIM,
})

# Single shared console — all tool files do: from core import console
console = Console(theme=_theme)


def clear_screen():
    os.system("cls" if system() == "Windows" else "clear")


def validate_input(ip, val_range: list) -> int | None:
    """Return the integer if it is in val_range, else None."""
    if not val_range:
        return None
    try:
        ip = int(ip)
        if ip in val_range:
            return ip
    except (TypeError, ValueError):
        pass
    return None


def _show_inline_help():
    """Quick help available from any menu level."""
    console.print(Panel(
        Text.assemble(
            ("  " + t("help.navigation") + "\n", "bold white"),
            ("  ─────────────────────────────────\n", "dim"),
            ("  1–N    ", "bold cyan"), (t("help.select_item") + "\n", "white"),
            ("  97     ", "bold cyan"), (t("help.install_all_category") + "\n", "white"),
            ("\n  " + t("help.tool_menu") + "\n", "dim"),
            ("  99     ", "bold cyan"), (t("help.go_back") + "\n", "white"),
            ("  98     ", "bold cyan"), (t("help.open_project_archived") + "\n", "white"),
            ("  ?      ", "bold cyan"), (t("help.show_help") + "\n", "white"),
            ("  q      ", "bold cyan"), (t("help.quit") + "\n", "white"),
        ),
        title="[bold magenta] " + t("help.title") + " [/bold magenta]",
        border_style="magenta",
        box=box.ROUNDED,
        padding=(0, 2),
    ))
    Prompt.ask("[dim]" + t("help.press_enter") + "[/dim]", default="")


class HackingTool:
    TITLE: str              = ""
    DESCRIPTION: str        = ""
    INSTALL_COMMANDS: list[str]  = []
    UNINSTALL_COMMANDS: list[str] = []
    RUN_COMMANDS: list[str]      = []
    OPTIONS: list[tuple[str, Callable]] = []
    PROJECT_URL: str        = ""

    # OS / capability metadata
    SUPPORTED_OS: list[str] = ["linux", "macos"]
    REQUIRES_ROOT: bool     = False
    REQUIRES_WIFI: bool     = False
    REQUIRES_GO: bool       = False
    REQUIRES_RUBY: bool     = False
    REQUIRES_JAVA: bool     = False
    REQUIRES_DOCKER: bool   = False

    # Tags for search/filter (e.g. ["osint", "web", "recon", "scanner"])
    TAGS: list[str]         = []

    # Archived tool flags
    ARCHIVED: bool          = False
    ARCHIVED_REASON: str    = ""

    def __init__(self, options=None, installable=True, runnable=True):
        options = options or []
        if not isinstance(options, list):
            raise TypeError("options must be a list of (option_name, option_fn) tuples")
        self.OPTIONS = []
        if installable:
            self.OPTIONS.append((t("tool.install"), self.install))
        if runnable:
            self.OPTIONS.append((t("tool.run"), self.run))
        self.OPTIONS.append((t("tool.update"), self.update))
        self.OPTIONS.append((t("tool.open_folder"), self.open_folder))
        self.OPTIONS.extend(options)

    @property
    def is_installed(self) -> bool:
        """Check if the tool's binary is on PATH or its clone dir exists."""
        if self.RUN_COMMANDS:
            cmd = self.RUN_COMMANDS[0]
            # Handle "cd foo && binary --help" pattern
            if "&&" in cmd:
                cmd = cmd.split("&&")[-1].strip()
            if cmd.startswith("sudo "):
                cmd = cmd[5:].strip()
            binary = cmd.split()[0] if cmd else ""
            if binary and binary not in (".", "echo", "cd"):
                if shutil.which(binary):
                    return True
        # Check if git clone target dir exists
        if self.INSTALL_COMMANDS:
            for ic in self.INSTALL_COMMANDS:
                if "git clone" in ic:
                    parts = ic.split()
                    repo_url = [p for p in parts if p.startswith("http")]
                    if repo_url:
                        dirname = repo_url[0].rstrip("/").rsplit("/", 1)[-1].replace(".git", "")
                        if os.path.isdir(dirname):
                            return True
        return False

    def show_info(self):
        desc = f"[cyan]{self.DESCRIPTION}[/cyan]"
        if self.PROJECT_URL:
            desc += f"\n[url]🔗 {self.PROJECT_URL}[/url]"
        if self.ARCHIVED:
            desc += f"\n[archived]⚠ ARCHIVED: {self.ARCHIVED_REASON}[/archived]"
        console.print(Panel(
            desc,
            title=f"[{THEME_PRIMARY}]{self.TITLE}[/{THEME_PRIMARY}]",
            border_style="purple",
            box=box.DOUBLE,
        ))

    def show_options(self, parent=None):
        """Iterative menu loop — no recursion, no stack growth."""
        while True:
            clear_screen()
            self.show_info()

            table = Table(title=t("menu.options"), box=box.SIMPLE_HEAVY)
            table.add_column(t("menu.no"), style="bold cyan", justify="center")
            table.add_column(t("menu.action"), style="bold yellow")

            for index, option in enumerate(self.OPTIONS):
                table.add_row(str(index + 1), option[0])

            if self.PROJECT_URL:
                table.add_row("98", t("tool.open_project_page"))
            table.add_row("99", t("menu.back_to", parent=parent.TITLE if parent else t("menu.main_menu")))
            console.print(table)
            console.print(
                "  [dim cyan]?[/dim cyan][dim]" + t("help.help_short") + "  "
                "[/dim][dim cyan]q[/dim cyan][dim]" + t("help.quit_short") + "  "
                "[/dim][dim cyan]99[/dim cyan][dim] " + t("help.back_short") + "[/dim]"
            )

            raw = Prompt.ask("[bold cyan]╰─>[/bold cyan]", default="").strip().lower()
            if not raw:
                continue
            if raw in ("?", "help"):
                _show_inline_help()
                continue
            if raw in ("q", "quit", "exit"):
                raise SystemExit(0)

            try:
                choice = int(raw)
            except ValueError:
                console.print(f"[error]⚠ {t('error.enter_number')}[/error]")
                Prompt.ask(f"[dim]{t('help.press_enter_continue')}[/dim]", default="")
                continue

            if choice == 99:
                return
            elif choice == 98 and self.PROJECT_URL:
                self.show_project_page()
            elif 1 <= choice <= len(self.OPTIONS):
                try:
                    self.OPTIONS[choice - 1][1]()
                except Exception:
                    console.print_exception(show_locals=True)
                Prompt.ask(f"[dim]{t('help.press_enter_continue')}[/dim]", default="")
            else:
                console.print(f"[error]⚠ {t('error.invalid_option')}[/error]")

    def before_install(self): pass

    def install(self):
        self.before_install()
        if isinstance(self.INSTALL_COMMANDS, (list, tuple)):
            for cmd in self.INSTALL_COMMANDS:
                console.print(f"[warning]→ {cmd}[/warning]")
                os.system(cmd)
        self.after_install()

    def after_install(self):
        console.print(f"[success]✔ {t('tool.installed')}[/success]")

    def before_uninstall(self) -> bool:
        return True

    def uninstall(self):
        if self.before_uninstall():
            if isinstance(self.UNINSTALL_COMMANDS, (list, tuple)):
                for cmd in self.UNINSTALL_COMMANDS:
                    console.print(f"[error]→ {cmd}[/error]")
                    os.system(cmd)
        self.after_uninstall()

    def after_uninstall(self): pass

    def update(self):
        """Smart update — detects install method and runs the right update command."""
        if not self.is_installed:
            console.print(f"[warning]{t('tool.not_installed')}[/warning]")
            return

        updated = False
        for ic in (self.INSTALL_COMMANDS or []):
            if "git clone" in ic:
                # Extract repo dir name from clone command
                parts = ic.split()
                repo_urls = [p for p in parts if p.startswith("http")]
                if repo_urls:
                    dirname = repo_urls[0].rstrip("/").rsplit("/", 1)[-1].replace(".git", "")
                    if os.path.isdir(dirname):
                        console.print(f"[cyan]→ git -C {dirname} pull[/cyan]")
                        os.system(f"git -C {dirname} pull")
                        updated = True
            elif "pip install" in ic:
                # Re-run pip install (--upgrade)
                upgrade_cmd = ic.replace("pip install", "pip install --upgrade")
                console.print(f"[cyan]→ {upgrade_cmd}[/cyan]")
                os.system(upgrade_cmd)
                updated = True
            elif "go install" in ic:
                # Re-run go install (fetches latest)
                console.print(f"[cyan]→ {ic}[/cyan]")
                os.system(ic)
                updated = True
            elif "gem install" in ic:
                upgrade_cmd = ic.replace("gem install", "gem update")
                console.print(f"[cyan]→ {upgrade_cmd}[/cyan]")
                os.system(upgrade_cmd)
                updated = True

        if updated:
            console.print(f"[success]✔ {t('tool.update_complete')}[/success]")
        else:
            console.print(f"[dim]{t('tool.no_auto_update')}[/dim]")

    def _get_tool_dir(self) -> str | None:
        """Find the tool's local directory — clone target, pip location, or binary path."""
        # 1. Check git clone target dir
        for ic in (self.INSTALL_COMMANDS or []):
            if "git clone" in ic:
                parts = ic.split()
                # If last arg is not a URL, it's a custom dir name
                repo_urls = [p for p in parts if p.startswith("http")]
                if repo_urls:
                    dirname = repo_urls[0].rstrip("/").rsplit("/", 1)[-1].replace(".git", "")
                    # Check custom target dir (arg after URL)
                    url_idx = parts.index(repo_urls[0])
                    if url_idx + 1 < len(parts):
                        dirname = parts[url_idx + 1]
                    if os.path.isdir(dirname):
                        return os.path.abspath(dirname)

        # 2. Check binary location via which
        if self.RUN_COMMANDS:
            cmd = self.RUN_COMMANDS[0]
            if "&&" in cmd:
                # "cd foo && bar" → check "foo"
                cd_part = cmd.split("&&")[0].strip()
                if cd_part.startswith("cd "):
                    d = cd_part[3:].strip()
                    if os.path.isdir(d):
                        return os.path.abspath(d)
            binary = cmd.split()[0] if cmd else ""
            if binary.startswith("sudo"):
                binary = cmd.split()[1] if len(cmd.split()) > 1 else ""
            path = shutil.which(binary) if binary else None
            if path:
                return os.path.dirname(os.path.realpath(path))

        return None

    def open_folder(self):
        """Open the tool's directory in a new shell so the user can work manually."""
        tool_dir = self._get_tool_dir()
        if tool_dir:
            console.print(f"[success]{t('tool.opening_folder', dir=tool_dir)}[/success]")
            console.print(f"[dim]{t('tool.type_exit')}[/dim]")
            os.system(f'cd "{tool_dir}" && $SHELL')
        else:
            console.print(f"[warning]{t('tool.dir_not_found')}[/warning]")
            if self.PROJECT_URL:
                console.print(f"[dim]{t('tool.clone_manually')}[/dim]")
                console.print(f"[cyan]  git clone {self.PROJECT_URL}.git[/cyan]")

    def before_run(self): pass

    def run(self):
        self.before_run()
        if isinstance(self.RUN_COMMANDS, (list, tuple)):
            for cmd in self.RUN_COMMANDS:
                console.print(f"[cyan]⚙ {t('tool.running', cmd=cmd)}[/cyan]")
                os.system(cmd)
        self.after_run()

    def after_run(self): pass

    def show_project_page(self):
        console.print(f"[url]🌐 {t('tool.opening_url', url=self.PROJECT_URL)}[/url]")
        webbrowser.open_new_tab(self.PROJECT_URL)


class HackingToolsCollection:
    TITLE: str       = ""
    DESCRIPTION: str = ""
    TOOLS: list      = []

    def __init__(self):
        pass

    def show_info(self):
        console.rule(f"[{THEME_PRIMARY}]{self.TITLE}[/{THEME_PRIMARY}]", style="purple")
        if self.DESCRIPTION:
            console.print(f"[italic cyan]{self.DESCRIPTION}[/italic cyan]\n")

    def _active_tools(self) -> list:
        """Return tools that are not archived and are OS-compatible."""
        from os_detect import CURRENT_OS
        return [
            t for t in self.TOOLS
            if not getattr(t, "ARCHIVED", False)
            and CURRENT_OS.system in getattr(t, "SUPPORTED_OS", ["linux", "macos"])
        ]

    def _archived_tools(self) -> list:
        return [t for t in self.TOOLS if getattr(t, "ARCHIVED", False)]

    def _incompatible_tools(self) -> list:
        from os_detect import CURRENT_OS
        return [
            t for t in self.TOOLS
            if not getattr(t, "ARCHIVED", False)
            and CURRENT_OS.system not in getattr(t, "SUPPORTED_OS", ["linux", "macos"])
        ]

    def _show_archived_tools(self):
        """Show archived tools sub-menu (option 98)."""
        archived = self._archived_tools()
        if not archived:
            console.print(f"[dim]{t('menu.no_archived')}[/dim]")
            Prompt.ask(f"[dim]{t('help.press_enter')}[/dim]", default="")
            return

        while True:
            clear_screen()
            console.rule(f"[archived]{t('menu.archived_tools', n='')} — {self.TITLE}[/archived]", style="yellow")

            table = Table(box=box.MINIMAL_DOUBLE_HEAD, show_lines=True)
            table.add_column(t("menu.no"), justify="center", style="bold yellow")
            table.add_column(t("menu.tool"), style="dim yellow")
            table.add_column(t("menu.reason"), style="dim white")

            for i, tool in enumerate(archived):
                reason = getattr(tool, "ARCHIVED_REASON", "No reason given")
                table.add_row(str(i + 1), tool.TITLE, reason)

            table.add_row("99", t("prompt.back"), "")
            console.print(table)

            raw = Prompt.ask(f"[bold yellow][?] {t('prompt.select_option')}[/bold yellow]", default="99")
            try:
                choice = int(raw)
            except ValueError:
                continue

            if choice == 99:
                return
            elif 1 <= choice <= len(archived):
                archived[choice - 1].show_options(parent=self)

    def show_options(self, parent=None):
        """Iterative menu loop — no recursion, no stack growth."""
        while True:
            clear_screen()
            self.show_info()

            active = self._active_tools()
            incompatible = self._incompatible_tools()
            archived = self._archived_tools()

            table = Table(title=t("menu.available_tools"), box=box.SIMPLE_HEAD, show_lines=True)
            table.add_column(t("menu.no"), justify="center", style="bold cyan", width=6)
            table.add_column("", width=2)  # installed indicator
            table.add_column(t("menu.tool"), style="bold yellow", min_width=24)
            table.add_column(t("menu.description"), style="white", overflow="fold")

            for index, tool in enumerate(active, start=1):
                desc = getattr(tool, "DESCRIPTION", "") or "—"
                desc = desc.splitlines()[0] if desc != "—" else "—"
                has_status = hasattr(tool, "is_installed")
                status = ("[green]✔[/green]" if tool.is_installed else "[dim]✘[/dim]") if has_status else ""
                table.add_row(str(index), status, tool.TITLE, desc)

            # Count not-installed tools for "Install All" label (skip sub-collections)
            not_installed = [t for t in active if hasattr(t, "is_installed") and not t.is_installed]
            if not_installed:
                table.add_row(
                    "[bold green]97[/bold green]", "",
                    f"[bold green]{t('menu.install_all', n=len(not_installed))}[/bold green]", "",
                )
            if archived:
                table.add_row("[dim]98[/dim]", "", f"[archived]{t('menu.archived_tools', n=len(archived))}[/archived]", "")
            if incompatible:
                console.print(f"[dim]{t('menu.tools_hidden', n=len(incompatible))}[/dim]")

            table.add_row("99", "", t("menu.back_to", parent=parent.TITLE if parent else t("menu.main_menu")), "")
            console.print(table)
            console.print(
                "  [dim cyan]?[/dim cyan][dim]" + t("help.help_short") + "  "
                "[/dim][dim cyan]q[/dim cyan][dim]" + t("help.quit_short") + "  "
                "[/dim][dim cyan]99[/dim cyan][dim] " + t("help.back_short") + "[/dim]"
            )

            raw = Prompt.ask("[bold cyan]╰─>[/bold cyan]", default="").strip().lower()
            if not raw:
                continue
            if raw in ("?", "help"):
                _show_inline_help()
                continue
            if raw in ("q", "quit", "exit"):
                raise SystemExit(0)

            try:
                choice = int(raw)
            except ValueError:
                console.print(f"[error]⚠ {t('error.enter_number')}[/error]")
                continue

            if choice == 99:
                return
            elif choice == 97 and not_installed:
                console.print(Panel(
                    f"[bold]{t('tool.installing_n', n=len(not_installed))}[/bold]",
                    border_style="green", box=box.ROUNDED,
                ))
                for i, tool in enumerate(not_installed, start=1):
                    console.print(f"\n[bold cyan]{t('tool.progress', i=i, total=len(not_installed))}[/bold cyan] {tool.TITLE}")
                    try:
                        tool.install()
                    except Exception:
                        console.print(f"[error]✘ {t('tool.failed', title=tool.TITLE)}[/error]")
                Prompt.ask(f"\n[dim]{t('help.press_enter_continue')}[/dim]", default="")
            elif choice == 98 and archived:
                self._show_archived_tools()
            elif 1 <= choice <= len(active):
                try:
                    active[choice - 1].show_options(parent=self)
                except Exception:
                    console.print_exception(show_locals=True)
                    Prompt.ask(f"[dim]{t('help.press_enter_continue')}[/dim]", default="")
            else:
                console.print(f"[error]⚠ {t('error.invalid_option')}[/error]")

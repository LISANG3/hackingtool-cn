#!/usr/bin/env python3
import sys

# ── Python version guard (must be before any other local import) ───────────────
if sys.version_info < (3, 10):
    print(
        f"[ERROR] Python 3.10 or newer is required.\n"
        f"You are running Python {sys.version_info.major}.{sys.version_info.minor}.\n"
        f"Upgrade with: sudo apt install python3.10"
    )
    sys.exit(1)

import os
import platform
import socket
import datetime
import random
import webbrowser
from itertools import zip_longest

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.align import Align
from rich.text import Text
from rich import box
from rich.rule import Rule
from rich.columns import Columns

from core import HackingToolsCollection, clear_screen, console
from constants import VERSION_DISPLAY, REPO_WEB_URL
from i18n import t
from config import get_tools_dir
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensics import ForensicTools
from tools.information_gathering import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_creator import PayloadCreatorTools
from tools.phishing_attack import PhishingAttackTools
from tools.post_exploitation import PostExploitationTools
from tools.remote_administration import RemoteAdministrationTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_injection import SqlInjectionTools
from tools.steganography import SteganographyTools
from tools.tool_manager import ToolManager
from tools.web_attack import WebAttackTools
from tools.wireless_attack import WirelessAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.xss_attack import XSSAttackTools
from tools.active_directory import ActiveDirectoryTools
from tools.cloud_security import CloudSecurityTools
from tools.mobile_security import MobileSecurityTools

# ── Tool registry ──────────────────────────────────────────────────────────────

# (full_title, icon, menu_label)
# menu_label is the concise name shown in the 2-column main menu grid.
# full_title is shown when entering the category.
tool_definitions = [
    (t("category.anonsurf"),              "🛡 ", t("category.anonsurf_short")),
    (t("category.info_gathering"),        "🔍",  t("category.info_gathering_short")),
    (t("category.wordlist"),              "📚",  t("category.wordlist_short")),
    (t("category.wireless"),              "📶",  t("category.wireless_short")),
    (t("category.sql_injection"),         "🧩",  t("category.sql_injection_short")),
    (t("category.phishing"),              "🎣",  t("category.phishing_short")),
    (t("category.web_attack"),            "🌐",  t("category.web_attack_short")),
    (t("category.post_exploit"),          "🔧",  t("category.post_exploit_short")),
    (t("category.forensics"),             "🕵 ", t("category.forensics_short")),
    (t("category.payload"),               "📦",  t("category.payload_short")),
    (t("category.exploit"),               "🧰",  t("category.exploit_short")),
    (t("category.reverse"),               "🔁",  t("category.reverse_short")),
    (t("category.ddos"),                  "⚡",  t("category.ddos_short")),
    (t("category.rat"),                   "🖥 ", t("category.rat_short")),
    (t("category.xss"),                   "💥",  t("category.xss_short")),
    (t("category.stegano"),               "🖼 ", t("category.stegano_short")),
    (t("category.active_directory"),      "🏢",  t("category.active_directory_short")),
    (t("category.cloud"),                 "☁ ",  t("category.cloud_short")),
    (t("category.mobile"),                "📱",  t("category.mobile_short")),
    (t("category.other"),                 "✨",  t("category.other_short")),
    (t("category.update_uninstall"),      "♻ ",  t("category.update_uninstall_short")),
]

all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    ActiveDirectoryTools(),
    CloudSecurityTools(),
    MobileSecurityTools(),
    OtherTools(),
    ToolManager(),
]

# Used by generate_readme.py
class AllTools(HackingToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools


# ── Help overlay ───────────────────────────────────────────────────────────────

def show_help():
    console.print(Panel(
        Text.assemble(
            ("  " + t("help.main_menu") + "\n", "bold white"),
            ("  ─────────────────────────────────────\n", "dim"),
            ("  1–20   ", "bold cyan"), (t("help.open_category") + "\n", "white"),
            ("  21     ", "bold cyan"), (t("help.update_uninstall") + "\n", "white"),
            ("  / or s ", "bold cyan"), (t("help.search_tools") + "\n", "white"),
            ("  t      ", "bold cyan"), (t("help.filter_tags") + "\n", "white"),
            ("  r      ", "bold cyan"), (t("help.recommend_tools") + "\n", "white"),
            ("  ?      ", "bold cyan"), (t("help.show_help") + "\n", "white"),
            ("  q      ", "bold cyan"), (t("help.quit") + "\n\n", "white"),
            ("  " + t("help.inside_category") + "\n", "bold white"),
            ("  ─────────────────────────────────────\n", "dim"),
            ("  1–N    ", "bold cyan"), (t("help.select_tool") + "\n", "white"),
            ("  99     ", "bold cyan"), (t("help.back_to_main") + "\n", "white"),
            ("  98     ", "bold cyan"), (t("help.open_project") + "\n\n", "white"),
            ("  " + t("help.inside_tool") + "\n", "bold white"),
            ("  ─────────────────────────────────────\n", "dim"),
            ("  1      ", "bold cyan"), (t("help.install_tool") + "\n", "white"),
            ("  2      ", "bold cyan"), (t("help.run_tool") + "\n", "white"),
            ("  99     ", "bold cyan"), (t("help.back_to_category") + "\n", "white"),
        ),
        title="[bold magenta] " + t("help.title") + " [/bold magenta]",
        border_style="magenta",
        box=box.ROUNDED,
        padding=(0, 2),
    ))
    Prompt.ask("[dim]" + t("help.press_enter") + "[/dim]", default="")


# ── Header: ASCII art + live system info ──────────────────────────────────────

# Full "HACKING TOOL" block-letter art — 12 lines, split layout with stats
_BANNER_ART = [
    " ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ ",
    " ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ ",
    " ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗",
    " ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║",
    " ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝",
    " ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ",
    "        ████████╗ ██████╗  ██████╗ ██╗",
    "        ╚══██╔══╝██╔═══██╗██╔═══██╗██║",
    "           ██║   ██║   ██║██║   ██║██║",
    "           ██║   ██║   ██║██║   ██║██║",
    "           ██║   ╚██████╔╝╚██████╔╝███████╗",
    "           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝",
]

_QUOTES = t("quotes")


def _sys_info() -> dict:
    """Collect live system info for the header panel."""
    info: dict = {}

    # OS pretty name
    try:
        info["os"] = platform.freedesktop_os_release().get("PRETTY_NAME", "")
    except Exception:
        info["os"] = ""
    if not info["os"]:
        info["os"] = f"{platform.system()} {platform.release()}"

    info["kernel"] = platform.release()

    # Current user
    try:
        info["user"] = os.getlogin()
    except Exception:
        info["user"] = os.environ.get("USER", os.environ.get("LOGNAME", "root"))

    info["host"] = socket.gethostname()

    # Local IP — connect to a routable address without sending data
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(("10.254.254.254", 1))
        info["ip"] = s.getsockname()[0]
        s.close()
    except Exception:
        info["ip"] = "127.0.0.1"

    info["time"] = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M")
    return info


def _build_header() -> Panel:
    info = _sys_info()

    # 12 stat lines paired with the 12 art lines
    stat_lines = [
        ("  " + t("header.os") + "      ›  ", info["os"][:34]),
        ("  " + t("header.kernel") + "  ›  ", info["kernel"][:34]),
        ("  " + t("header.user") + "    ›  ", f"{info['user']} @ {info['host'][:20]}"),
        ("  " + t("header.ip") + "      ›  ", info["ip"]),
        ("  " + t("header.tools") + "   ›  ", t("header.tools_count", n=len(all_tools))),
        ("  " + t("header.session") + " ›  ", info["time"]),
        ("", ""),
        ("  " + t("header.python") + "  ›  ", f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"),
        ("  " + t("header.arch") + "    ›  ", platform.machine()),
        ("  " + t("header.status") + "  ›  ", "✔ " + t("header.ready")),
        ("", ""),
        ("", ""),
    ]

    grid = Table.grid(padding=0)
    grid.add_column("art", no_wrap=True)
    grid.add_column("sep", no_wrap=True)
    grid.add_column("lbl", no_wrap=True)
    grid.add_column("val", no_wrap=True)

    for art_line, (lbl_text, val_text) in zip(_BANNER_ART, stat_lines):
        grid.add_row(
            Text(art_line, style="bold bright_green"),
            Text("  │ ", style="dim green"),
            Text(lbl_text, style="dim green"),
            Text(val_text, style="bright_green"),
        )

    # Quote + warning below the split row
    quote = random.choice(_QUOTES)
    body = Table.grid(padding=(0, 0))
    body.add_column()
    body.add_row(grid)
    body.add_row(Text(""))
    body.add_row(Text(f"  {quote}", style="italic dim"))
    body.add_row(Text("  ⚠  " + t("warning.authorized_only"),
                      style="bold dim red"))

    return Panel(
        body,
        title=f"[bold bright_magenta]{t('banner.title', version=VERSION_DISPLAY)}[/bold bright_magenta]",
        title_align="left",
        subtitle=f"[dim][ {info['time']} ][/dim]",
        subtitle_align="right",
        border_style="bright_magenta",
        box=box.HEAVY,
        padding=(0, 1),
    )


# ── Main menu renderer ─────────────────────────────────────────────────────────

def build_menu():
    clear_screen()
    console.print(_build_header())

    # ── 2-column category grid ──
    # Items 1-17 in two columns, item 18 (ToolManager) shown separately
    categories = tool_definitions[:-1]   # 17 items
    update_def = tool_definitions[-1]    # ToolManager

    mid = (len(categories) + 1) // 2    # 9  (left), 8 (right)
    left  = list(enumerate(categories[:mid],  start=1))
    right = list(enumerate(categories[mid:],  start=mid + 1))

    grid = Table.grid(padding=(0, 1), expand=True)
    grid.add_column("ln", justify="right", style="bold magenta", width=5)
    grid.add_column("li", width=3)
    grid.add_column("lt", style="magenta", ratio=1, no_wrap=True)
    grid.add_column("gap", width=3)
    grid.add_column("rn", justify="right", style="bold magenta", width=5)
    grid.add_column("ri", width=3)
    grid.add_column("rt", style="magenta", ratio=1, no_wrap=True)

    for (li, (_, lic, ll)), r in zip_longest(left, right, fillvalue=None):
        if r:
            ri, (_, ric, rl) = r
            grid.add_row(str(li), lic, ll, "", str(ri), ric, rl)
        else:
            grid.add_row(str(li), lic, ll, "", "", "", "")

    console.print(Panel(
        grid,
        title="[bold magenta] " + t("menu.select_category") + " [/bold magenta]",
        border_style="bright_magenta",
        box=box.ROUNDED,
        padding=(0, 1),
    ))

    # ── ToolManager row ──
    tm_num = len(categories) + 1
    console.print(
        f"  [bold magenta]  {tm_num}[/bold magenta]  {update_def[1]}  "
        f"[magenta]{update_def[2]}[/magenta]"
    )

    # ── Claude-style dual-line prompt area ──
    console.print(Rule(style="dim magenta"))
    console.print(
        "  [dim cyan]/[/dim cyan][dim]" + t("prompt.search").replace("/ ", "") + "[/dim]  "
        "[dim cyan]t[/dim cyan] [dim]tags[/dim]  "
        "[dim cyan]r[/dim cyan] [dim]recommend[/dim]  "
        "[dim cyan]?[/dim cyan] [dim]help[/dim]  "
        "[dim cyan]q[/dim cyan] [dim]quit[/dim]"
    )


# ── Search ─────────────────────────────────────────────────────────────────────

def _collect_all_tools() -> list[tuple]:
    """Walk all collections and return (tool_instance, category_name) pairs."""
    from core import HackingTool, HackingToolsCollection
    results = []

    def _walk(items, parent_title=""):
        for item in items:
            if isinstance(item, HackingToolsCollection):
                _walk(item.TOOLS, item.TITLE)
            elif isinstance(item, HackingTool):
                results.append((item, parent_title))

    _walk(all_tools)
    return results


def _get_all_tags() -> dict[str, list[tuple]]:
    """Build tag → [(tool, category)] index from all tools."""
    import re
    _rules = {
        r'(osint|harvester|maigret|holehe|spiderfoot|sherlock|recon)': 'osint',
        r'(subdomain|subfinder|amass|sublist|subdomainfinder)': 'recon',
        r'(scanner|scan|nmap|masscan|rustscan|nikto|nuclei|trivy)': 'scanner',
        r'(brute|gobuster|ffuf|dirb|dirsearch|ferox|hashcat|john|kerbrute)': 'bruteforce',
        r'(web|http|proxy|zap|xss|sql|wafw00f|arjun|caido|mitmproxy)': 'web',
        r'(wireless|wifi|wlan|airgeddon|bettercap|wifite|fluxion|deauth)': 'wireless',
        r'(phish|social.media|evilginx|setoolkit|social.fish|social.engineer)': 'social-engineering',
        r'(c2|sliver|havoc|mythic|pwncat|reverse.shell|pyshell)': 'c2',
        r'(privesc|peass|linpeas|winpeas)': 'privesc',
        r'(tunnel|pivot|ligolo|chisel|proxy|anon)': 'network',
        r'(password|credential|hash|crack|secret|trufflehog|gitleaks)': 'credentials',
        r'(forensic|memory|volatility|binwalk|autopsy|wireshark|pspy)': 'forensics',
        r'(reverse.eng|ghidra|radare|jadx|androguard|apk)': 'reversing',
        r'(cloud|aws|azure|gcp|kubernetes|prowler|scout|pacu)': 'cloud',
        r'(mobile|android|ios|frida|mobsf|objection|droid)': 'mobile',
        r'(active.directory|bloodhound|netexec|impacket|responder|certipy|kerberos|winrm|smb|ldap)': 'active-directory',
        r'(ddos|dos|slowloris|goldeneye|ufonet)': 'ddos',
        r'(payload|msfvenom|fatrat|venom|stitch|enigma)': 'payload',
        r'(crawler|spider|katana|gospider)': 'crawler',
    }
    tag_index: dict[str, list[tuple]] = {}
    for tool, cat in _collect_all_tools():
        combined = f"{tool.TITLE} {tool.DESCRIPTION}".lower()
        # Manual tags first
        tool_tags = set(getattr(tool, "TAGS", []) or [])
        # Auto-derive tags from title/description
        for pattern, tag in _rules.items():
            if re.search(pattern, combined, re.IGNORECASE):
                tool_tags.add(tag)
        for t in tool_tags:
            tag_index.setdefault(t, []).append((tool, cat))
    return tag_index


def filter_by_tag():
    """Show available tags, user picks one, show matching tools."""
    tag_index = _get_all_tags()
    sorted_tags = sorted(tag_index.keys())

    # Show tags in a compact grid
    console.print(Panel(
        "  ".join(f"[bold cyan]{t}[/bold cyan]([dim]{len(tag_index[t])}[/dim])" for t in sorted_tags),
        title="[bold magenta] " + t("tag.title") + " [/bold magenta]",
        border_style="magenta", box=box.ROUNDED, padding=(0, 2),
    ))

    tag = Prompt.ask(f"[bold cyan]{t('prompt.enter_tag')}[/bold cyan]", default="").strip().lower()
    if not tag or tag not in tag_index:
        if tag:
            console.print(f"[dim]{t('tag.not_found', tag=tag)}[/dim]")
            Prompt.ask(f"[dim]{t('help.press_enter')}[/dim]", default="")
        return

    matches = tag_index[tag]
    table = Table(
        title=t("tag.results", tag=tag),
        box=box.SIMPLE_HEAD, show_lines=True,
    )
    table.add_column(t("menu.no"), justify="center", style="bold cyan", width=5)
    table.add_column("", width=2)
    table.add_column(t("menu.tool"), style="bold yellow", min_width=20)
    table.add_column(t("menu.category"), style="magenta", min_width=15)

    for i, (tool, cat) in enumerate(matches, start=1):
        status = "[green]✔[/green]" if tool.is_installed else "[dim]✘[/dim]"
        table.add_row(str(i), status, tool.TITLE, cat)

    table.add_row("99", "", t("menu.back_main"), "")
    console.print(table)

    raw = Prompt.ask("[bold cyan]" + t("prompt.select") + "[/bold cyan]", default="").strip()
    if not raw or raw == "99":
        return
    try:
        idx = int(raw)
    except ValueError:
        return
    if 1 <= idx <= len(matches):
        tool, cat = matches[idx - 1]
        tool.show_options()


_RECOMMENDATIONS = {
    "scan a network":           ["scanner", "port-scanner"],
    "find subdomains":          ["recon"],
    "scan for vulnerabilities": ["scanner", "web"],
    "crack passwords":          ["bruteforce", "credentials"],
    "find leaked secrets":      ["credentials"],
    "phishing campaign":        ["social-engineering"],
    "post exploitation":        ["c2", "privesc"],
    "pivot through network":    ["network"],
    "pentest active directory": ["active-directory"],
    "pentest web application":  ["web", "scanner"],
    "pentest cloud":            ["cloud"],
    "pentest mobile app":       ["mobile"],
    "reverse engineer binary":  ["reversing"],
    "capture wifi handshake":   ["wireless"],
    "intercept http traffic":   ["web", "network"],
    "forensic analysis":        ["forensics"],
    "ddos testing":             ["ddos"],
    "create payloads":          ["payload"],
    "find xss vulnerabilities": ["web"],
    "brute force directories":  ["bruteforce", "web"],
    "osint / recon a target":   ["osint", "recon"],
    "hide my identity":         ["network"],
}


def recommend_tools():
    """Show common tasks, user picks one, show matching tools."""
    table = Table(
        title=t("rec.title"),
        box=box.SIMPLE_HEAD,
    )
    table.add_column(t("menu.no"), justify="center", style="bold cyan", width=5)
    table.add_column("Task", style="bold yellow")

    tasks = list(_RECOMMENDATIONS.keys())
    rec_tasks = t("rec.tasks")
    for i, task in enumerate(tasks, start=1):
        task_label = rec_tasks.get(task, task.title()) if isinstance(rec_tasks, dict) else task.title()
        table.add_row(str(i), task_label)

    table.add_row("99", t("menu.back_main"))
    console.print(table)

    raw = Prompt.ask("[bold cyan]" + t("prompt.select") + "[/bold cyan]", default="").strip()
    if not raw or raw == "99":
        return

    try:
        idx = int(raw)
    except ValueError:
        return

    if 1 <= idx <= len(tasks):
        task = tasks[idx - 1]
        tag_names = _RECOMMENDATIONS[task]
        tag_index = _get_all_tags()

        # Collect unique tools across all matching tags
        seen = set()
        matches = []
        for tag in tag_names:
            for tool, cat in tag_index.get(tag, []):
                if id(tool) not in seen:
                    seen.add(id(tool))
                    matches.append((tool, cat))

        if not matches:
            console.print(f"[dim]{t('rec.no_tools')}[/dim]")
            Prompt.ask(f"[dim]{t('help.press_enter')}[/dim]", default="")
            return

        task_label = rec_tasks.get(task, task.title()) if isinstance(rec_tasks, dict) else task.title()
        console.print(Panel(
            f"[bold]{t('rec.recommended', task=task_label)}[/bold]",
            border_style="green", box=box.ROUNDED,
        ))

        rtable = Table(box=box.SIMPLE_HEAD, show_lines=True)
        rtable.add_column(t("menu.no"), justify="center", style="bold cyan", width=5)
        rtable.add_column("", width=2)
        rtable.add_column(t("menu.tool"), style="bold yellow", min_width=20)
        rtable.add_column(t("menu.category"), style="magenta")

        for i, (tool, cat) in enumerate(matches, start=1):
            status = "[green]✔[/green]" if tool.is_installed else "[dim]✘[/dim]"
            rtable.add_row(str(i), status, tool.TITLE, cat)

        rtable.add_row("99", "", t("prompt.back"), "")
        console.print(rtable)

        raw2 = Prompt.ask("[bold cyan]" + t("prompt.select") + "[/bold cyan]", default="").strip()
        if raw2 and raw2 != "99":
            try:
                ridx = int(raw2)
                if 1 <= ridx <= len(matches):
                    matches[ridx - 1][0].show_options()
            except ValueError:
                pass


def search_tools(query: str | None = None):
    """Search tools — accepts inline query or prompts for one."""
    if query is None:
        query = Prompt.ask(f"[bold cyan]{t('prompt.search')}[/bold cyan]", default="").strip().lower()
    else:
        query = query.lower()
    if not query:
        return

    all_tool_list = _collect_all_tools()

    # Match against title + description + tags
    matches = []
    for tool, category in all_tool_list:
        title = (tool.TITLE or "").lower()
        desc = (tool.DESCRIPTION or "").lower()
        tags = " ".join(getattr(tool, "TAGS", []) or []).lower()
        if query in title or query in desc or query in tags:
            matches.append((tool, category))

    if not matches:
        console.print(f"[dim]{t('search.no_results', query=query)}[/dim]")
        Prompt.ask(f"[dim]{t('help.press_enter')}[/dim]", default="")
        return

    # Display results
    table = Table(
        title=t("search.title", query=query),
        box=box.SIMPLE_HEAD, show_lines=True,
    )
    table.add_column(t("menu.no"), justify="center", style="bold cyan", width=5)
    table.add_column(t("menu.tool"), style="bold yellow", min_width=20)
    table.add_column(t("menu.category"), style="magenta", min_width=15)
    table.add_column(t("menu.description"), style="white", overflow="fold")

    for i, (tool, cat) in enumerate(matches, start=1):
        desc = (tool.DESCRIPTION or "—").splitlines()[0]
        table.add_row(str(i), tool.TITLE, cat, desc)

    table.add_row("99", t("menu.back_main"), "", "")
    console.print(table)

    raw = Prompt.ask("[bold cyan]" + t("prompt.select") + "[/bold cyan]", default="").strip().lower()
    if not raw or raw == "99":
        return

    try:
        idx = int(raw)
    except ValueError:
        return

    if 1 <= idx <= len(matches):
        tool, cat = matches[idx - 1]
        console.print(Panel(
            f"[bold magenta]{tool.TITLE}[/bold magenta]  [dim]({cat})[/dim]",
            border_style="magenta", box=box.ROUNDED,
        ))
        tool.show_options()


# ── Main interaction loop ──────────────────────────────────────────────────────

def interact_menu():
    while True:
        try:
            build_menu()
            raw = Prompt.ask(
                "[bold magenta]╰─>[/bold magenta]", default=""
            ).strip()

            if not raw:
                continue

            raw_lower = raw.lower()

            if raw_lower in ("?", "help"):
                show_help()
                continue

            if raw.startswith("/"):
                # Inline search: /subdomain → search immediately
                query = raw[1:].strip()
                search_tools(query=query if query else None)
                continue

            if raw_lower in ("s", "search"):
                search_tools()
                continue

            if raw_lower in ("t", "tag", "tags", "filter"):
                filter_by_tag()
                continue

            if raw_lower in ("r", "rec", "recommend"):
                recommend_tools()
                continue

            if raw_lower in ("q", "quit", "exit"):
                console.print(Panel(
                    f"[bold white on magenta]  {t('goodbye')}  [/bold white on magenta]",
                    box=box.HEAVY, border_style="magenta",
                ))
                break

            try:
                choice = int(raw_lower)
            except ValueError:
                console.print(f"[red]⚠  {t('error.invalid_input')}[/red]")
                Prompt.ask(f"[dim]{t('help.press_enter_continue')}[/dim]", default="")
                continue

            if 1 <= choice <= len(all_tools):
                title, icon, _ = tool_definitions[choice - 1]
                console.print(Panel(
                    f"[bold magenta]{icon}  {title}[/bold magenta]",
                    border_style="magenta", box=box.ROUNDED,
                ))
                try:
                    all_tools[choice - 1].show_options()
                except Exception as e:
                    console.print(Panel(
                        f"[red]{t('error.opening_category', title=title)}[/red]\n{e}",
                        border_style="red",
                    ))
                    Prompt.ask(f"[dim]{t('help.press_enter')}[/dim]", default="")
            else:
                console.print(f"[red]⚠  {t('error.choose_range', max=len(all_tools))}[/red]")
                Prompt.ask(f"[dim]{t('help.press_enter_continue')}[/dim]", default="")

        except KeyboardInterrupt:
            console.print(f"\n[bold red]{t('warning.interrupted')}[/bold red]")
            break


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    try:
        from os_detect import CURRENT_OS

        if CURRENT_OS.system == "windows":
            console.print(Panel(f"[bold red]{t('warning.windows')}[/bold red]"))
            if Confirm.ask(t("about.open_guidance"), default=True):
                webbrowser.open_new_tab(f"{REPO_WEB_URL}#windows")
            return

        if CURRENT_OS.system not in ("linux", "macos"):
            console.print(f"[yellow]{t('warning.unsupported_os', os=CURRENT_OS.system)}[/yellow]")

        get_tools_dir()   # ensures ~/.hackingtool/tools/ exists
        interact_menu()

    except KeyboardInterrupt:
        console.print(f"\n[bold red]{t('warning.exiting')}[/bold red]")


if __name__ == "__main__":
    main()

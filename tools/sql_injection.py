from core import HackingTool, HackingToolsCollection, console
from i18n import t

from rich.panel import Panel
from rich.prompt import Prompt


class Sqlmap(HackingTool):
    TITLE = "Sqlmap tool"
    DESCRIPTION = "sqlmap 是一款开源渗透测试工具，可自动检测和利用 SQL 注入漏洞" \
                  "并接管数据库服务器。[!] python3 sqlmap.py -u [http://example.com] --batch --banner。" \
                  "更多用法: https://github.com/sqlmapproject/sqlmap/wiki/Usage"
    INSTALL_COMMANDS = ["git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev"]
    RUN_COMMANDS = ["cd sqlmap-dev;python3 sqlmap.py --wizard"]
    PROJECT_URL = "https://github.com/sqlmapproject/sqlmap"


class NoSqlMap(HackingTool):
    TITLE = "NoSqlMap"
    DESCRIPTION = "NoSQLMap 是一款开源 Python 工具，用于审计和自动化注入攻击。[*] 请安装 MongoDB。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/codingo/NoSQLMap.git",
        # Bug 25 fix: was "python setup.py install" (Python 2) and "python NoSQLMap"
        "cd NoSQLMap && pip install --user .",
    ]
    # Bug 25 fix: "python" → "python3"
    RUN_COMMANDS = ["python3 -m nosqlmap"]
    PROJECT_URL = "https://github.com/codingo/NoSQLMap"


class SQLiScanner(HackingTool):
    TITLE = "Damn Small SQLi Scanner"
    DESCRIPTION = "DSSS 是一个功能完善的 SQL 注入漏洞扫描器，支持 GET 和 POST 参数。用法: python3 dsss.py -h | -u [URL]"
    INSTALL_COMMANDS = ["git clone https://github.com/stamparm/DSSS.git"]
    PROJECT_URL = "https://github.com/stamparm/DSSS"

    def __init__(self):
        super().__init__(runnable=False)


class Explo(HackingTool):
    TITLE = "Explo"
    DESCRIPTION = "Explo 是一个简单工具，用于以人类和机器可读的格式描述 Web 安全问题。用法: explo [--verbose|-v] testcase.yaml | explo [--verbose|-v] examples/*.yaml"
    INSTALL_COMMANDS = [
        "git clone https://github.com/dtag-dev-sec/explo.git",
        "cd explo && pip install --user .",
    ]
    PROJECT_URL = "https://github.com/dtag-dev-sec/explo"

    def __init__(self):
        super().__init__(runnable=False)


class Blisqy(HackingTool):
    TITLE = "Blisqy - Exploit Time-based blind-SQL injection"
    DESCRIPTION = "Blisqy 帮助 Web 安全研究人员在 HTTP 标头中查找基于时间的盲 SQL 注入并加以利用。"
    INSTALL_COMMANDS = ["git clone https://github.com/JohnTroony/Blisqy.git"]
    PROJECT_URL = "https://github.com/JohnTroony/Blisqy"

    def __init__(self):
        super().__init__(runnable=False)


class Leviathan(HackingTool):
    TITLE = "Leviathan - Wide Range Mass Audit Toolkit"
    DESCRIPTION = "Leviathan 是一个大规模审计工具包，具有服务发现、暴力破解、SQL 注入检测和自定义漏洞利用功能。需要 API 密钥。"
    INSTALL_COMMANDS = ["git clone https://github.com/leviathan-framework/leviathan.git",
                        "cd leviathan;pip install --user -r requirements.txt"]
    RUN_COMMANDS = ["cd leviathan;python leviathan.py"]
    PROJECT_URL = "https://github.com/leviathan-framework/leviathan"


class SQLScan(HackingTool):
    TITLE = "SQLScan"
    DESCRIPTION = "SQLScan 是一个快速 Web 扫描器，用于查找 SQL 注入点。仅用于教育目的。"
    INSTALL_COMMANDS = ["sudo apt install php php-bz2 php-curl php-mbstring curl",
                        "sudo curl https://raw.githubusercontent.com/Cvar1984/sqlscan/dev/build/main.phar --output /usr/local/bin/sqlscan",
                        "chmod +x /usr/local/bin/sqlscan"]
    RUN_COMMANDS = ["sudo sqlscan"]
    PROJECT_URL = "https://github.com/Cvar1984/sqlscan"


class SqlInjectionTools(HackingToolsCollection):
    TITLE = t("category.sql_injection")
    TOOLS = [Sqlmap(), NoSqlMap(), SQLiScanner(), Explo(), Blisqy(), Leviathan(), SQLScan()]

if __name__ == "__main__":
    tools = SqlInjectionTools()
    tools.show_options()

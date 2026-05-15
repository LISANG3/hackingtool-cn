from core import HackingTool
from core import HackingToolsCollection
from i18n import t


class Prowler(HackingTool):
    TITLE = "Prowler (Cloud Security Scanner)"
    DESCRIPTION = "用于 AWS、Azure、GCP 和 Kubernetes 评估的开源安全工具。"
    INSTALL_COMMANDS = ["pip install --user prowler"]
    RUN_COMMANDS = ["prowler --help"]
    PROJECT_URL = "https://github.com/prowler-cloud/prowler"
    SUPPORTED_OS = ["linux", "macos"]


class ScoutSuite(HackingTool):
    TITLE = "ScoutSuite (Multi-Cloud Auditing)"
    DESCRIPTION = "用于 AWS、Azure、GCP、阿里云和 Oracle 的多云安全审计工具。"
    INSTALL_COMMANDS = ["pip install --user scoutsuite"]
    RUN_COMMANDS = ["scout --help"]
    PROJECT_URL = "https://github.com/nccgroup/ScoutSuite"
    SUPPORTED_OS = ["linux", "macos"]


class Pacu(HackingTool):
    TITLE = "Pacu (AWS Exploitation Framework)"
    DESCRIPTION = "用于 AWS 环境进攻性安全测试的 AWS 利用框架。"
    INSTALL_COMMANDS = ["pip install --user pacu"]
    RUN_COMMANDS = ["pacu --help"]
    PROJECT_URL = "https://github.com/RhinoSecurityLabs/pacu"
    SUPPORTED_OS = ["linux", "macos"]


class Trivy(HackingTool):
    TITLE = "Trivy (Container/K8s Scanner)"
    DESCRIPTION = "全面的容器、Kubernetes、IaC 和代码漏洞扫描器。"
    INSTALL_COMMANDS = [
        "curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sudo sh -s -- -b /usr/local/bin",
    ]
    RUN_COMMANDS = ["trivy --help"]
    PROJECT_URL = "https://github.com/aquasecurity/trivy"
    SUPPORTED_OS = ["linux", "macos"]


class CloudSecurityTools(HackingToolsCollection):
    TITLE = t("category.cloud")
    DESCRIPTION = "用于云基础设施安全评估和利用的工具。"
    TOOLS = [
        Prowler(),
        ScoutSuite(),
        Pacu(),
        Trivy(),
    ]

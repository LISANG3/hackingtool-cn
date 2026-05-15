<div align="center">

<img src="images/logo.svg" alt="HackingTool" width="600">

<p><b>安全研究人员与渗透测试者的全能工具箱 · 中文版</b></p>

[![License](https://img.shields.io/github/license/LISANG3/hackingtool-cn?style=flat-square)](LICENSE)&nbsp;
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)&nbsp;
[![Version](https://img.shields.io/badge/v2.0.0-00FF88?style=flat-square)](#)&nbsp;
[![Stars](https://img.shields.io/github/stars/LISANG3/hackingtool-cn?style=flat-square&color=yellow)](https://github.com/LISANG3/hackingtool-cn/stargazers)&nbsp;
[![Forks](https://img.shields.io/github/forks/LISANG3/hackingtool-cn?style=flat-square&color=blue)](https://github.com/LISANG3/hackingtool-cn/network/members)&nbsp;
[![Issues](https://img.shields.io/github/issues/LISANG3/hackingtool-cn?style=flat-square&color=red)](https://github.com/LISANG3/hackingtool-cn/issues)&nbsp;
[![Last Commit](https://img.shields.io/github/last-commit/LISANG3/hackingtool-cn?style=flat-square&color=00FF88)](https://github.com/LISANG3/hackingtool-cn/commits/master)

![](https://img.shields.io/badge/20_个类别-7B61FF?style=for-the-badge)
![](https://img.shields.io/badge/185+_工具-00FF88?style=for-the-badge)
![](https://img.shields.io/badge/19_个标签-FF61DC?style=for-the-badge)
![](https://img.shields.io/badge/Linux_%7C_Kali_%7C_Parrot_%7C_macOS-FFA116?style=for-the-badge&logo=linux&logoColor=white)
![](https://img.shields.io/badge/完整中文汉化-FF6B6B?style=for-the-badge)

<a href="#安装方式"><img src="https://img.shields.io/badge/立即安装-00FF88?style=for-the-badge&logo=rocket&logoColor=black" alt="立即安装"></a>&nbsp;
<a href="#快速命令"><img src="https://img.shields.io/badge/快速命令-7B61FF?style=for-the-badge&logo=terminal&logoColor=white" alt="快速命令"></a>

<br/>

> ⚠ **仅供授权安全测试使用。** 感谢所有原作者提供的工具。

</div>

---

## 关于本项目

本项目是 [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) 的中文汉化分支，在保持原项目全部功能的基础上，完成了以下工作：

| 特性 | 说明 |
|:---:|---|
| **🇨🇳** | **完整中文汉化** — 所有菜单、帮助、提示、工具描述、安装器均翻译为中文 |
| **🌐** | **i18n 国际化框架** — 新增 `i18n.py` + `locales/` 翻译文件，支持中英文切换 |
| **🐛** | **Bug 修复** — 修复 30+ 个原项目存在的代码缺陷（命令注入、Python 2 遗留代码等） |
| **🔧** | **代码现代化** — 全部升级至 Python 3.10+，移除已弃用语法 |

### 与上游的差异

- 新增 `i18n.py` 轻量翻译模块，从 `~/.hackingtool/config.json` 读取语言设置
- 新增 `locales/zh.json`（241 条中文翻译）和 `locales/en.json`（英文参考）
- 35 个 Python 文件通过 `t()` 函数实现国际化
- 工具名称（nmap、sqlmap 等专有名词）保留英文，仅翻译描述性文本

---

## 快速命令

<div align="center">

| 命令 | 操作 | 可用位置 |
|:---:|---|:---:|
| `/关键词` | **搜索** — 按名称、描述或标签查找工具 | 主菜单 |
| `t` | **标签筛选** — 按 osint、web、c2、cloud 等标签过滤 | 主菜单 |
| `r` | **智能推荐** — 「我想扫描网络」→ 显示相关工具 | 主菜单 |
| `?` | **帮助** — 显示快捷键速查卡 | 任意层级 |
| `q` | **退出** — 从任意深度直接退出 | 任意层级 |
| `97` | **全部安装** — 批量安装当前类别所有工具 | 类别内 |
| `99` | **返回** — 返回上一级菜单 | 任意层级 |

</div>

---

## 工具类别

<div align="center">

| # | 类别 | 工具数 | | # | 类别 | 工具数 |
|:---:|---|:---:|---|:---:|---|:---:|
| 1 | 🛡 匿名隐藏 | 2 | | 11 | 🧰 漏洞利用框架 | 4 |
| 2 | 🔍 信息收集 | 28 | | 12 | 🔁 逆向工程 | 5 |
| 3 | 📚 字典生成器 | 7 | | 13 | ⚡ DDOS 攻击 | 6 |
| 4 | 📶 无线攻击 | 13 | | 14 | 🖥 远程管理 (RAT) | 1 |
| 5 | 🧩 SQL 注入 | 7 | | 15 | 💥 XSS 攻击 | 9 |
| 6 | 🎣 钓鱼攻击 | 17 | | 16 | 🖼 隐写术 | 4 |
| 7 | 🌐 Web 攻击 | 20 | | 17 | 🏢 Active Directory | 6 |
| 8 | 🔧 后渗透利用 | 10 | | 18 | ☁ 云安全 | 4 |
| 9 | 🕵 取证分析 | 8 | | 19 | 📱 移动安全 | 3 |
| 10 | 📦 Payload 创建 | 8 | | 20 | ✨ 其他工具 | 24 |

</div>

---

## 工具列表

<!-- 工具列表由 generate_readme.py 自动生成 -->
<!-- 请运行 python3 generate_readme.py 更新完整列表 -->

<details>
<summary><b>点击展开完整工具列表 (185+ 工具)</b></summary>

### 🛡 匿名隐藏工具
- [Anonymously Surf](https://github.com/Und3rf10w/kali-anonsurf) — 自动覆盖 RAM 并更改 IP 地址
- [Multitor](https://github.com/trimstray/multitor) — 同时在多个位置保持连接

### 🔍 信息收集工具
- [Nmap](https://github.com/nmap/nmap) — 网络发现和安全审计
- [Dracnmap](https://github.com/Screetsec/Dracnmap) — nmap 高级封装工具
- 端口扫描 — 基于 nmap 的快速扫描
- Host to IP — 域名到 IP 转换
- [Xerosploit](https://github.com/LionSec/xerosploit) — 中间人攻击测试工具包
- [RED HAWK](https://github.com/Tuhinshubhra/RED_HAWK) — 一体化信息收集和漏洞扫描
- [ReconSpider](https://github.com/bhavsec/reconspider) — 高级 OSINT 情报框架
- IsItDown — 检查网站是否在线
- [Infoga](https://github.com/m4ll0k/Infoga) — 电子邮件 OSINT 信息收集
- [ReconDog](https://github.com/s0md3v/ReconDog) — 信息收集套件
- [Striker](https://github.com/s0md3v/Striker) — 侦察与漏洞扫描
- [SecretFinder](https://github.com/m4ll0k/SecretFinder) — 查找 API 密钥、JWT 等敏感数据
- [Shodanfy](https://github.com/m4ll0k/Shodanfy.py) — 通过 Shodan 获取 IP 信息
- [rang3r](https://github.com/floriankunushevci/rang3r) — 多线程端口扫描器
- [Breacher](https://github.com/s0md3v/Breacher) — 后台管理面板查找工具
- [theHarvester](https://github.com/laramies/theHarvester) ★ — 公共来源 OSINT 收集
- [Amass](https://github.com/owasp-amass/amass) ★ — 深度子域名枚举和攻击面映射
- [Masscan](https://github.com/robertdavidgraham/masscan) ★ — 互联网最快端口扫描器
- [RustScan](https://github.com/RustScan/RustScan) ★ — 3 秒内扫描全部 65k 端口
- [Holehe](https://github.com/megadose/holehe) ★ — 检查邮箱在 120+ 个网站的注册情况
- [Maigret](https://github.com/soxoj/maigret) ★ — 用户名 OSINT，覆盖 3000+ 网站
- [httpx](https://github.com/projectdiscovery/httpx) ★ — 快速多用途 HTTP 探测
- [SpiderFoot](https://github.com/smicallef/spiderfoot) ★ — 自动化 OSINT 收集
- [Subfinder](https://github.com/projectdiscovery/subfinder) ★ — 快速被动子域名枚举
- [TruffleHog](https://github.com/trufflesecurity/trufflehog) ★ — 凭据泄露检测
- [Gitleaks](https://github.com/gitleaks/gitleaks) ★ — Git 密钥扫描器

### 📚 字典生成器
- [Cupp](https://github.com/Mebus/cupp) — 通用用户密码分析器，生成个性化字典
- [WordlistCreator](https://github.com/Z4nzu/wlcreator) — C 程序生成所有可能的密码组合
- [Goblin WordGenerator](https://github.com/UndeadSec/GoblinWordGenerator) — Goblin 字典生成器
- [Password list (14 亿条)](https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got) — 明文密码大数据检索
- [Hashcat](https://github.com/hashcat/hashcat) ★ — 全球最快 GPU/CPU 密码恢复工具
- [John the Ripper](https://github.com/openwall/john) ★ — 开源密码安全审计工具
- [haiti](https://github.com/noraj/haiti) ★ — 哈希类型识别器，支持 300+ 算法

### 📶 无线攻击工具
- [WiFi-Pumpkin](https://github.com/P0cL4bs/wifipumpkin3) — 虚假 AP 框架
- [pixiewps](https://github.com/wiire/pixiewps) — 离线 WPS PIN 暴力破解
- [BluePot](https://github.com/andrewmichaelsmith/bluepot) — 蓝牙蜜罐 GUI 框架
- [Fluxion](https://github.com/FluxionNetwork/fluxion) — Wi-Fi 安全审计工具
- [Wifiphisher](https://github.com/wifiphisher/wifiphisher) — 虚假接入点红队框架
- [Wifite](https://github.com/derv82/wifite2) — 自动化无线攻击工具
- [EvilTwin](https://github.com/Z4nzu/fakeap) — 邪恶双子攻击
- [Fastssh](https://github.com/Z4nzu/fastssh) — 多线程 SSH 暴力破解扫描
- [Howmanypeople](https://github.com/schollz/howmanypeoplearearound) — WiFi 信号监控人数统计
- [Airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon) ★ — 多功能无线审计套件
- [hcxdumptool](https://github.com/ZerBea/hcxdumptool) ★ — 捕获 WLAN 数据包和 PMKID 哈希
- [hcxtools](https://github.com/ZerBea/hcxtools) ★ — 数据包转换为 hashcat/JtR 格式
- [Bettercap](https://github.com/bettercap/bettercap) ★ — WiFi/BLE/网络 MITM 瑞士军刀

### 🧩 SQL 注入工具
- [Sqlmap](https://github.com/sqlmapproject/sqlmap) — 自动化 SQL 注入检测和利用
- [NoSqlMap](https://github.com/codingo/NoSQLMap) — NoSQL 注入审计工具
- [DSSS](https://github.com/stamparm/DSSS) — 功能完善的 SQL 注入扫描器
- [Explo](https://github.com/dtag-dev-sec/explo) — Web 安全描述工具
- [Blisqy](https://github.com/JohnTroony/Blisqy) — 基于时间的盲 SQL 注入利用
- [Leviathan](https://github.com/leviathan-framework/leviathan) — 大规模审计工具包
- [SQLScan](https://github.com/Cvar1984/sqlscan) — 快速 Web SQL 注入点扫描器

### 🎣 钓鱼攻击工具
- [Autophisher](https://github.com/CodingRanjith/autophisher) — 自动化钓鱼工具包
- [PyPhisher](https://github.com/KasRoudra/PyPhisher) — 77 个网站模板的钓鱼工具
- [AdvPhishing](https://github.com/Ignitetch/AdvPhishing) — 高级 OTP 钓鱼工具
- [Setoolkit](https://github.com/trustedsec/social-engineer-toolkit) — 社会工程学测试框架
- [SocialFish](https://github.com/UndeadSec/SocialFish) — 自动化钓鱼和信息收集
- [HiddenEye](https://github.com/Morsmalleo/HiddenEye) — 现代钓鱼工具，支持多种隧道服务
- [Evilginx3](https://github.com/kgretzky/evilginx2) — MITM 框架，绕过双因素认证
- [I-See-You](https://github.com/Viralmaniar/I-See-You) — 通过社会工程学获取目标位置
- [SayCheese](https://github.com/hangetzzu/saycheese) — 通过链接获取目标摄像头照片
- [QR Code Jacking](https://github.com/cryptedwolf/ohmyqr) — QR 码劫持攻击
- [BlackEye](https://github.com/thelinuxchoice/blackeye) — 38 个网站模板的钓鱼工具
- [ShellPhish](https://github.com/An0nUD4Y/shellphish) — 18 种社交媒体钓鱼工具
- [Thanos](https://github.com/TridevReddy/Thanos) — 浏览器到浏览器钓鱼工具包
- [QRLJacking](https://github.com/OWASP/QRLJacking) — QR 登录会话劫持攻击
- [Maskphish](https://github.com/jaykali/maskphish) — URL 伪装钓鱼
- [BlackPhish](https://github.com/iinc0gnit0/BlackPhish) — 多平台钓鱼框架
- [dnstwist](https://github.com/elceef/dnstwist) — 域名抢注和钓鱼检测

### 🌐 Web 攻击工具
- [Web2Attack](https://github.com/santatic/web2attack) — Web 黑客框架
- Skipfish — 全自动 Web 安全侦察工具
- [Sublist3r](https://github.com/aboul3la/Sublist3r) — 子域名枚举
- [CheckURL](https://github.com/UndeadSec/checkURL) — IDN 同形攻击检测
- [Sub-Domain TakeOver](https://github.com/edoardottt/takeover) — 子域名接管检测
- [Dirb](https://gitlab.com/kalilinux/packages/dirb) — Web 内容扫描器
- [Nuclei](https://github.com/projectdiscovery/nuclei) ★ — 基于模板的漏洞扫描器
- [ffuf](https://github.com/ffuf/ffuf) ★ — 快速 Web 模糊测试工具
- [Feroxbuster](https://github.com/epi052/feroxbuster) ★ — Rust 编写的快速目录发现
- [Nikto](https://github.com/sullo/nikto) ★ — Web 服务器漏洞扫描器
- [wafw00f](https://github.com/EnableSecurity/wafw00f) ★ — Web 应用防火墙检测
- [Katana](https://github.com/projectdiscovery/katana) ★ — 下一代爬虫框架
- [Gobuster](https://github.com/OJ/gobuster) ★ — 目录/DNS/Vhost 暴力破解
- [Dirsearch](https://github.com/maurosoria/dirsearch) ★ — Web 路径暴力破解
- [OWASP ZAP](https://github.com/zaproxy/zaproxy) ★ — 全功能 Web 应用扫描器
- [testssl.sh](https://github.com/drwetter/testssl.sh) ★ — TLS/SSL 加密检测
- [Arjun](https://github.com/s0md3v/Arjun) ★ — HTTP 参数发现套件
- [Caido](https://github.com/caido/caido) ★ — Burp Suite 替代品，轻量级 Web 审计
- [mitmproxy](https://github.com/mitmproxy/mitmproxy) ★ — 交互式 HTTP 拦截代理

### 🔧 后渗透利用工具
- [Vegile](https://github.com/Screetsec/Vegile) — 后门/rootkit 隐藏工具
- [Chrome Keylogger](https://github.com/UndeadSec/HeraKeylogger) — Hera 键盘记录器
- [pwncat-cs](https://github.com/calebstewart/pwncat) ★ — 后渗透平台，自动化反向/绑定 Shell
- [Sliver](https://github.com/BishopFox/sliver) ★ — 跨平台红队 C2 框架
- [Havoc](https://github.com/HavocFramework/Havoc) ★ — 现代 C2 框架，Cobalt Strike 替代品
- [PEASS-ng](https://github.com/peass-ng/PEASS-ng) ★ — Linux/Windows 提权枚举
- [Ligolo-ng](https://github.com/nicocha30/ligolo-ng) ★ — TUN 接口隧道，无需 SOCKS
- [Chisel](https://github.com/jpillora/chisel) ★ — 基于 HTTP 的快速 TCP/UDP 隧道
- [Evil-WinRM](https://github.com/Hackplayers/evil-winrm) ★ — Windows 远程 Shell
- [Mythic](https://github.com/its-a-feature/Mythic) ★ — 协作式多载荷 C2 平台

### 🕵 取证分析工具
- Autopsy — 数字取证平台
- Wireshark — 网络抓包和分析工具
- [Bulk Extractor](https://github.com/simsong/bulk_extractor) — 文件系统元数据提取
- [Guymager](https://guymager.sourceforge.io/) — 介质采集取证镜像工具
- [Toolsley](https://www.toolsley.com/) — 多款实用调查工具集合
- [Volatility 3](https://github.com/volatilityfoundation/volatility3) ★ — 内存取证框架
- [Binwalk](https://github.com/ReFirmLabs/binwalk) ★ — 固件分析逆向工具
- [pspy](https://github.com/DominicBreuker/pspy) ★ — 无需 root 的 Linux 进程监控

### 📦 Payload 创建工具
- [The FatRat](https://github.com/Screetsec/TheFatRat) — 绕过杀毒软件的后门和 Payload 生成
- [Brutal](https://github.com/Screetsec/Brutal) — 多功能 Payload 创建工具包
- [Stitch](https://nathanlopez.github.io/Stitch) — 跨平台 Python RAT
- [MSFvenom Payload Creator](https://github.com/g0tmi1k/msfpc) — MSFvenom 包装器
- [Venom](https://github.com/r00t-3xp10it/venom) — Shellcode 生成器
- [Spycam](https://github.com/indexnotfound404/spycam) — Win32 摄像头捕获 Payload
- [Mob-Droid](https://github.com/kinghacker0/Mob-Droid) — Metasploit Payload 快速生成
- [Enigma](https://github.com/UndeadSec/Enigma) — 多平台 Payload 投放器

### 🧰 漏洞利用框架
- [RouterSploit](https://github.com/threat9/routersploit) — 嵌入式设备漏洞利用框架
- [WebSploit](https://github.com/The404Hacking/websploit) — MITM 攻击框架
- [Commix](https://github.com/commixproject/commix) — 自动化 OS 命令注入
- Web2Attack — Web 黑客框架

### 🔁 逆向工程工具
- [Androguard](https://github.com/androguard/androguard) — Android 应用逆向分析
- [Apk2Gold](https://github.com/lxdvs/apk2gold) — Android 反编译为 Java
- [JadX](https://github.com/skylot/jadx) — Dex 到 Java 反编译器
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra) ★ — NSA 逆向工程框架
- [Radare2](https://github.com/radareorg/radare2) ★ — 可移植逆向工程框架

### ⚡ DDOS 攻击工具
- [DDoS Script](https://github.com/the-deepnet/ddos) — 36+ 方法 DDoS 攻击脚本
- [SlowLoris](https://github.com/gkbrk/slowloris) — HTTP 拒绝服务攻击
- [Asyncrone](https://github.com/fatih4842/aSYNcrone) — C 语言 SYN Flood 武器
- [UFOnet](https://github.com/epsylon/ufonet) — P2P 加密 DoS/DDoS 工具包
- [GoldenEye](https://github.com/jseidl/GoldenEye) — HTTP DoS 测试工具
- [Saphyra](https://github.com/anonymous24x7/Saphyra-DDoS) — Python DDoS 测试脚本

### 🖥 远程管理工具 (RAT)
- [Pyshell](https://github.com/knassar702/pyshell) — RAT 远程管理工具

### 💥 XSS 攻击工具
- [DalFox](https://github.com/hahwul/dalfox) — XSS 扫描和参数分析
- [XSS Payload Generator](https://github.com/capture0x/XSS-LOADER) — Payload 生成器和扫描器
- [Extended XSS Searcher](https://github.com/Damian89/extended-xss-search) — 扩展型 XSS 搜索器
- [XSS-Freak](https://github.com/PR0PH3CY33/XSS-Freak) — Python 3 XSS 扫描器
- [XSpear](https://github.com/hahwul/XSpear) — Ruby Gems 构建的 XSS 扫描器
- [XSSCon](https://github.com/menkrep1337/XSSCon) — XSS 扫描工具
- [XanXSS](https://github.com/Ekultek/XanXSS) — 反射型 XSS 搜索
- [XSStrike](https://github.com/UltimateHackers/XSStrike) — 高级 XSS 检测套件
- [RVuln](https://github.com/iinc0gnit0/RVuln) — Rust 编写的自动化 Web 漏洞扫描器

### 🖼 隐写术工具
- SteganoHide — steghide 前端工具
- [StegoCracker](https://github.com/W1LDN16H7/StegoCracker) — 隐写数据隐藏和提取
- [Whitespace](https://github.com/beardog108/snow10) — 空白字符和 Unicode 隐写术

### 🏢 Active Directory 工具
- [BloodHound](https://github.com/BloodHoundAD/BloodHound) ★ — 图论揭示隐藏攻击路径
- [NetExec](https://github.com/Pennyw0rth/NetExec) ★ — Windows/AD 渗透瑞士军刀
- [Impacket](https://github.com/fortra/impacket) ★ — SMB/MSRPC/Kerberos/LDAP 网络协议
- [Responder](https://github.com/lgandx/Responder) ★ — LLMNR/NBT-NS/MDNS 投毒器
- [Certipy](https://github.com/ly4k/Certipy) ★ — AD 证书服务枚举和滥用
- [Kerbrute](https://github.com/ropnop/kerbrute) ★ — Kerberos 预认证暴力破解

### ☁ 云安全工具
- [Prowler](https://github.com/prowler-cloud/prowler) ★ — AWS/Azure/GCP/Kubernetes 安全评估
- [ScoutSuite](https://github.com/nccgroup/ScoutSuite) ★ — 多云安全审计工具
- [Pacu](https://github.com/RhinoSecurityLabs/pacu) ★ — AWS 利用框架
- [Trivy](https://github.com/aquasecurity/trivy) ★ — 容器/K8s/IaC 漏洞扫描器

### 📱 移动安全工具
- [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) ★ — 移动应用渗透测试和恶意软件分析
- [Frida](https://github.com/frida/frida) ★ — 运行时动态插桩工具包
- [Objection](https://github.com/sensepost/objection) ★ — 无需越狱/root 的运行时探索

### ✨ 其他工具 — 子类别
- **HatCloud** — 绕过 CloudFlare 发现真实 IP
- **社交媒体暴力破解** — Instagram、Facebook、Gmail 等多平台攻击
- **Android 攻击** — 键盘记录器、锁屏钓鱼、摄像头捕获、会话劫持
- **IDN 同形字攻击** — 生成恶意 Unicode 域名
- **邮箱验证** — 验证邮箱是否存在
- **哈希破解** — 自动哈希类型识别和破解
- **WiFi 断开攻击** — 持续干扰 WiFi 客户端和接入点
- **社交媒体查找** — 通过面部识别和用户名在社交网络中查找目标
- **Payload 注入** — 将恶意代码注入 .deb 包和图片
- **网络爬虫** — 用 Go 编写的快速网络爬虫
- **混合工具** — 终端复用器 (tilix) 和 URL/P/域名提取器 (Crivo)

</details>

---

## 安装方式

<table>
<tr>
<td>

### 一键安装（推荐）

```bash
curl -sSL https://raw.githubusercontent.com/LISANG3/hackingtool-cn/master/install.sh | sudo bash
```

自动处理所有步骤 — 安装依赖、克隆仓库、创建虚拟环境、建立启动器命令。

</td>
<td>

### 手动安装

```bash
git clone https://github.com/LISANG3/hackingtool-cn.git
cd hackingtool-cn
sudo python3 install.py
```

安装完成后运行：

```bash
hackingtool
```

</td>
</tr>
</table>

### 中文语言设置

安装完成后，编辑配置文件启用中文：

```bash
echo '{"lang": "zh"}' > ~/.hackingtool/config.json
```

或将 `~/.hackingtool/config.json` 中的 `lang` 字段设为 `"zh"`。

### Docker 部署

```bash
# 构建镜像
docker build -t hackingtool-cn .

# 直接运行
docker run -it --rm hackingtool-cn

# Docker Compose（推荐）
docker compose up -d
docker exec -it hackingtool bash
python3 hackingtool.py

# 开发模式（实时挂载源码，修改无需重新构建）
docker compose --profile dev up
docker exec -it hackingtool-dev bash

# 停止
docker compose down        # 停止容器
docker compose down -v     # 同时删除数据卷
```

### 环境要求

| 依赖 | 版本 | 用途 |
|---|---|---|
| Python | 3.10+ | 核心运行 |
| Go | 1.21+ | nuclei、ffuf、amass、httpx、katana、dalfox、gobuster、subfinder |
| Ruby | any | haiti、evil-winrm |
| Docker | any | Mythic、MobSF（可选） |

```bash
pip install -r requirements.txt
```

---

## 代码贡献

欢迎提交 Issue 或 Pull Request！

### Issue（工具请求）

> 标题格式：`[工具请求] 工具名 — 类别`
> 示例：`[工具请求] Subfinder — 信息收集`

### Pull Request

> 标题格式：`[新工具] 工具名 — 类别`
> 示例：`[新工具] Subfinder — 信息收集`

基本要求：
1. 在正确的 `tools/*.py` 文件中添加工具类
2. 设置 `TITLE`、`DESCRIPTION`、`INSTALL_COMMANDS`、`RUN_COMMANDS`、`PROJECT_URL`
3. 正确设置 `SUPPORTED_OS`
4. 将实例添加到对应集合类的 `TOOLS` 列表
5. 本地测试安装和运行

---

## Star History

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=LISANG3/hackingtool-cn&type=Date&theme=dark" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=LISANG3/hackingtool-cn&type=Date" />
  <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=LISANG3/hackingtool-cn&type=Date" />
</picture>

---

## 致谢

- 原项目 [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) — 所有工具原作者
- 中文汉化及代码修复由 [LISANG3](https://github.com/LISANG3) 完成

> ⚠ **请勿用于非法活动。** 仅限授权安全测试使用。
> 致谢所有包含在本项目中的工具作者。

<br/>

<div align="center">

[![Twitter](https://img.shields.io/badge/Twitter-Follow-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/_Zinzu07)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/LISANG3/)

</div>

---
layout: "localized"
title: "Mobi"
nav_title: "入门指南"
lang: "zh-Hans"
page_key: "mobi/home"
section: "mobi"
nav_order: 0
permalink: "/zh-Hans/gtp/"
source_revision: "874054b8ddaecac1e59dd93fb146bb94e87a23f895e0f2763c1c7f0413376a1a"
---

Mobi 将支持 Go Text Protocol（GTP）版本 2 的围棋引擎连接到 [KGS Go Server](https://www.gokgs.com/)。它负责登录、匹配、着手、用时、终局计分和恢复。请单独安装并配置围棋引擎。

Mobi 得到 KGS 和 American Go Association (AGA) 的正式认可。

## 下载并开始 {#download-and-get-started}

从 [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) 下载 **Mobi GTP 桥** 存档，适用于 x64 或 ARM64 上的 Windows 或 Linux。包含 .NET 运行时。 Windows 软件包使用 ZIP； Linux 软件包使用 tar.gz。将提取的文件放在一起。

- [用户指南]({% include page-url.html key='mobi/user-guide' %})：第一场比赛、配置、匹配、日志、超时、恢复和故障排除。
- [Java客户端升级指南]({% include page-url.html key='mobi/upgrade-guide' %})：从`kgsGtp.jar`和Java属性移动到TOML。
- [示例配置]({{ '/mobi/bot.example.toml' | relative_url }})：复制到`bot.toml`并设置您的帐户、引擎路径和游戏首选项。
- [使用条款]({% include page-url.html key='mobi/terms' %})：使用 Mobi 时的操作您的机器人、引擎许可和责任。
- [社区准则]({% include page-url.html key='mobi/community-guidelines' %})：诚实的机器人身份、公平竞争、负责任地使用服务器资源。

共享的[隐私政策]({% include page-url.html key='global/privacy' %})和[帐户和数据删除]({% include page-url.html key='global/account-and-data-deletion' %})页面包含Mobi特定信息。

指南涵盖 Windows 和 PowerShell 以及 Linux 和 Bash。展开适用于您的操作系统的部分。每个存档还包括两个指南的示例配置和英文离线副本。

## 运行客户端 {#run-the-client}

配置 `bot.toml` 后，从解压缩的目录运行这些命令。探针在不登录KGS的情况下检查发动机；下一个命令使用配置的匹配设置玩一场游戏。

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --probe
$env:KGS_PASSWORD = '<account password>'
.\Kgs.Gtp.exe --config .\bot.toml --games 1
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
chmod +x ./Kgs.Gtp
./Kgs.Gtp --config ./bot.toml --probe
read -r -s -p 'KGS password: ' KGS_PASSWORD
export KGS_PASSWORD
printf '\n'
./Kgs.Gtp --config ./bot.toml --games 1
```

</details>

按 Ctrl+C 停止。使用用户指南选择连续播放、保留日志并在升级过程中保留客户端身份。

您可以[报告 Mobi 的问题](https://github.com/amywarble/hoshi-hub/issues/new?template=mobi_problem_report.yml)。如需更正文档，请[创建公开 GitHub 问题](https://github.com/amywarble/hoshi-hub/issues/new/choose)并注明与 **Mobi** 有关。切勿包含密码或其他敏感信息。

报告问题不需要技术知识。即使只发生过一次，也请用自己的话描述发生了什么。填写您知道的内容即可；如有需要，我们会进一步询问。版本、操作步骤和截图均为选填。分享截图前，请遮盖个人信息和非公开内容。

不使用 GitHub？您也可以发送邮件至 [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com) 报告应用问题。

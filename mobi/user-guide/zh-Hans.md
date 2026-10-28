---
layout: "localized"
title: "Mobi 用户指南"
nav_title: "用户指南"
lang: "zh-Hans"
page_key: "mobi/user-guide"
section: "mobi"
nav_order: 1
permalink: "/zh-Hans/gtp/user-guide/"
source_revision: "26bf30c603841ace27c0d2ff994fd0d2297af607b506d24fd1ab9afabb8f1a33"
---

Mobi 将Go引擎连接到KGS，以便它可以自动播放。您在终端中运行客户端并通过 TOML 配置文件或命令行选项对其进行控制。单独安装和配置您的引擎；客户端处理登录、查找游戏、走法、时钟和计分。

从 Java `kgsGtp.jar` 客户端迁移？从[升级指南]({% include page-url.html key='mobi/upgrade-guide' %})开始。

本指南涵盖 Windows 和 Linux。展开适用于您的操作系统的部分以查看 PowerShell 或 Bash 命令。从提取的客户端目录运行打包的客户端示例。

- [第一场比赛](#first-game)
- [配置基础](#configuration-basics)
- [选择游戏](#choosing-games)
- [自定义游戏设置](#custom-game-settings)
- [运行机器人](#running-the-bot)
- [超时和恢复](#timeouts-and-recovery)
- [故障排除](#troubleshooting)

## 第一场比赛 {#first-game}

您需要注册 KGS 帐户、GTP 版本 2 引擎以及引擎所需的任何配置和模型文件。在启动机器人之前，使用常规 KGS 客户端创建帐户。 Ranked 播放需要额外的服务器权限；从 Free 游戏开始。

提取适合您的操作系统和体系结构的客户端包。为 x64 和 ARM64 上的 Windows 和 Linux 提供了软件包，其中包含 .NET 运行时。将提取的文件放在一起。可执行文件为 Windows 上的 `Kgs.Gtp.exe` 和 Linux 上的 `Kgs.Gtp`。

### 1。创建您的配置 {#1-create-your-configuration}

将包含的 [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) 复制到 `bot.toml`：

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
Copy-Item .\bot.example.toml .\bot.toml
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
cp ./bot.example.toml ./bot.toml
chmod +x ./Kgs.Gtp
```

</details>

编辑 `account.username`、`engine.executable` 和 `engine.arguments`。例如：

<details markdown="1">
<summary>Windows</summary>

```toml
[account]
username = "YourBot"

[engine]
executable = 'C:\Go\katago.exe'
arguments = ["gtp", "-config", 'C:\Go\gtp.cfg', "-model", 'C:\Go\model.bin.gz']
```

</details>

<details markdown="1">
<summary>Linux</summary>

```toml
[account]
username = "YourBot"

[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]
```

</details>

提供引擎进入 GTP 模式所需的路径和参数。每个数组元素都是一个参数；包含空格的路径仍然是一个元素。

该示例选择 Free 与人类自动匹配、快速或中速以及连续播放。如果账户没有数字排名，请将 `automatch.rank` 设置为 `30k` 和 `1k` 之间的适当估计值。 KGS 在账户等级可用时使用该等级。对于第一次运行，以下命令将游戏限制为一场游戏。

### 2。检查发动机 {#2-check-the-engine}

从提取的客户端目录中，运行：

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --probe
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml --probe
```

</details>

客户端打印引擎名称、版本和支持的命令，然后退出。这不需要 KGS 凭证，并且不会连接到 KGS。它检查 GTP 发现；启动配置的游戏模式时，会运行附加规则、时钟、让分和计分检查。

### 3。提供密码并播放 {#3-supply-the-password-and-play}

密码仅来自 `KGS_PASSWORD` 环境变量：

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
$env:KGS_PASSWORD = '<account password>'
.\Kgs.Gtp.exe --config .\bot.toml --games 1
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
read -r -s -p 'KGS password: ' KGS_PASSWORD
export KGS_PASSWORD
printf '\n'
./Kgs.Gtp --config ./bot.toml --games 1
```

</details>

查找 `Logged in to KGS`，然后查找 `Game ready`。客户端自动进行游戏并计分。 `Game finished`记录KGS的结果； `Series: completed game 1` 确认其已计入请求的总数。然后注销并退出。默认情况下，查找游戏的时间限制为五分钟；使用 `--lobby-timeout 3600` 最多允许一个小时。

## 配置基础知识 {#configuration-basics}

始终使用 `--config` 显式选择文件。客户端在启动时读取一次。重新启动以应用编辑，包括对引擎重新启动设置的更改。没有自动配置文件搜索或实时重新加载。

命令行选项会覆盖该运行的文件值。例如：

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --games 3 --undo-free Never
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml --games 3 --undo-free Never
```

</details>

用户名来自 `--username`，然后是 `account.username`，然后是 `KGS_USERNAME`。不要向文件添加密码字段：它会被拒绝。

使用带引号的字符串表示名称和选择，使用整数表示计数和秒，使用数字表示 komi，使用 `true` 或 `false` 表示布尔值。表名和键名区分大小写。未知键和无效值会停止启动并进行诊断。本指南中的所有持续时间均为秒。

包含 `/` 或 `\` 的相对 `engine.executable` 以及相对 `account.clientIdFile` 是相对于配置文件的目录的。裸可执行文件名称（例如 `katago`）使用可执行文件查找。引擎参数按原样传递，并且引擎继承您启动客户端的工作目录。如果从不同的目录启动，请使用模型和引擎配置参数的绝对路径。单引号 TOML 字符串保留 Windows 反斜杠。字符串不扩展环境变量。

### 帐户、服务器和引擎 {#account-server-and-engine}

| TOML 设置 | CLI 选项 | 含义和默认值 |
| --- | --- | --- |
| `account.username` | `--username` | KGS 账户名；回落至 `KGS_USERNAME`。 |
| `account.clientIdFile` | `--client-id-file` | 持久身份文件；通常为每个服务器和帐户选择。 |
| `server.host` | `--host` | KGS服务器；默认`goserver.gokgs.com`。 |
| `server.port` | `--port` | TCP端口；默认`2379`，范围1–65535。 |
| `engine.executable` | `--engine` | 引擎可执行文件启动。 |
| `engine.arguments` | `--` 之后的参数 | 引擎参数数组；默认为空。 |
| `engine.stdio` | `--stdio` | 使用外部连接的引擎而不是启动引擎；默认`false`。 |
| `engine.rules` | `--engine-rules` | 已在缺少 `kgs-rules` 的引擎中配置规则。无默认声明。 |

选择可执行文件或 `stdio = true`，切勿同时选择两者。对于标准 I/O，另一个程序必须将客户端的 stdin 连接到引擎的 stdout，并将客户端的 stdout 连接到引擎的 stdin。诊断使用 stderr。在此模式下不要提供引擎参数。

`engine.rules` 接受 `Japanese`、`Chinese`、`Aga` 或 `NewZealand`。这声明了引擎的现有规则；配置引擎本身以匹配。带有 `kgs-rules` 的引擎会自动接收所选游戏的规则。

要完全在命令行上配置，请将引擎参数放在 `--` 之后：

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --username YourBot --engine 'C:\Go\katago.exe' `
    --lobby Automatch --automatch-rank 20k --games 1 `
    -- gtp -config 'C:\Go\gtp.cfg' -model 'C:\Go\model.bin.gz'
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --username YourBot --engine /opt/katago/katago \
    --lobby Automatch --automatch-rank 20k --games 1 \
    -- gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

</details>

显式 CLI 引擎参数替换整个文件数组。清除该数组后，尾随 `--` 没有任何内容。 `--engine` 和 `--stdio` 覆盖文件的引擎连接选择； `--stdio` 还丢弃基于文件的参数。 `--help` 列出所有选项，`--version` 打印客户端版本。

## 选择游戏 {#choosing-games}

选择一种配对模式：

| `matchmaking.mode` / `--lobby` | 机器人做什么 |
| --- | --- |
| `Automatch` | 让 KGS 找到对手并选择游戏条款。 |
| `Offer` | 在指定房间中宣传自定义挑战。 |
| `Join` | 在指定房间中寻找匹配的自定义挑战。 |

如果没有模式，客户端登录并等待，直到停止；它找不到游戏。一次调用一次玩一场游戏。目前不支持同时进行自定义挑战和自动匹配、锦标赛参赛和聊天回复。

### Automatch {#automatch}

将这些部分与您的帐户和引擎设置一起使用：

```toml
[matchmaking]
mode = "Automatch"
gameType = "Free"
games = 0

[automatch]
speed = ["Fast", "Medium"]
rank = "20k"
opponents = "Humans"
maxRankDifference = 0
```

在 Automatch 模式下省略 `matchmaking.room`、`opponent`、`opponentPolicy`、`challengeNotes` 以及 `game` 和 `timing` 部分。这些是自定义挑战设置，不能与自动匹配结合使用，即使它们的值与其默认值匹配。

| TOML 设置 | CLI 选项 | 选择和默认 |
| --- | --- | --- |
| `automatch.speed` | `--automatch-speed` | `All`（默认）、`Blitz`、`Fast`、`Medium` 或 `["Fast", "Medium"]` 等数组。 CLI 组合使用逗号。 |
| `automatch.rank` | `--automatch-rank` | 通过`1k`估计为`30k`；当帐户没有数字服务器等级时需要。 |
| `automatch.opponents` | `--automatch-opponents` | `Humans`（默认）、`Robots` 或 `Any`。 |
| `automatch.maxRankDifference` | `--automatch-max-rank-difference` | 默认`0`；范围 0–9 为 Free，0–6 为 Ranked。 |

Automatch 对局为公开的 19×19 日本规则对局，执子颜色由服务器分配。分先对局的贴目为 6.5。允许等级差可能使贴目变为 0.5；相差两个或更多等级时，还可能采用固定位置的让子。

| 速度 | 每位玩家的主要时间 | 日本读读 |
| --- | --- | --- |
| `Blitz` | 60秒 | 3 10 秒的周期 |
| `Fast` | 600秒 | 5 20 秒的周期 |
| `Medium` | 1500秒 | 5 30 秒的周期 |

引擎必须支持`final_status_list`、`kgs-time_settings`和`time_left`；允许让分还需要 `set_free_handicap`。如果缺少 `kgs-rules`，请将其配置为日本规则并设置 `engine.rules = "Japanese"`。

### 定制挑战 {#custom-challenges}

将示例文件的 `matchmaking` 和 `automatch` 部分替换为自定义配置文件。此示例向符合条件的玩家提供公共 19×19 Free 游戏：

```toml
[matchmaking]
mode = "Offer"
gameType = "Free"
opponentPolicy = "Any"
room = "Computer Go"
games = 0
challengeNotes = "Computer player: 10-minute games"

[game]
boardSize = 19
rules = "Chinese"
komi = 7.5
color = "Nigiri"
handicap = 0
private = false

[timing]
system = "Absolute"
mainTime = 600
```

使用 KGS 中所示的房间名称。名称可能包含空格和非 ASCII 字符。登录后和重新连接后再次使用不区分大小写的精确匹配进行查找。名称缺失或不明确会阻止客户端进行诊断。

对于一名特定对手，将 `opponentPolicy` 更改为 `"Named"` 并添加 `opponent = "OtherAccount"`。对于`Any`，省略`opponent`；符合资格的开放对手是除此机器人之外已连接、注册的帐户。人类和机器人都有资格。

要加入挑战，请使用 `mode = "Join"` 并删除 `challengeNotes`。每个游戏术语都必须匹配，包括规则、科米、让分、能见度和时钟。选择机器人自己的颜色：玩黑色的 Offer 机器人需要玩白色的 Join 机器人；对于随机颜色，均使用 `"Nigiri"`。更改的条款不会被默默接受。

| TOML 设置 | CLI 选项 | 选择和默认 |
| --- | --- | --- |
| `matchmaking.mode` | `--lobby` | `Offer`、`Join` 或 `Automatch`；无默认模式。 |
| `matchmaking.gameType` | `--game-type` | `Free`（默认）或 `Ranked`。 |
| `matchmaking.opponentPolicy` | `--opponent-policy` | `Named`（自定义挑战的默认值）或 `Any`。 |
| `matchmaking.opponent` | `--opponent` | 需要 `Named`；帐户名忽略大小写。 |
| `matchmaking.room` | `--room` | Offer 和 Join 所需的房间名称；例如 `"Computer Go"`。 |
| `matchmaking.games` | `--games` | 默认`1`；正数表示系列，`0` 表示连续播放。 |
| `matchmaking.challengeNotes` | `--challenge-notes` | 仅限 Offer；最多 255 字符，无控制字符。遗漏会产生对手注释。 |

### Ranked 游戏 {#ranked-games}

设置`matchmaking.gameType = "Ranked"`专门请求Ranked游戏。该帐户必须具有服务器授予的 `RankedRobot` 权限并启用等级。向 KGS 服务器管理员请求该权限。允许未设置的等级 (`?`)，但不允许禁用等级 (`-`)；当帐户没有数字排名时，自动匹配仍然需要估计。

Ranked 对手必须使用已注册且启用等级的账号，等级应为业余等级或尚未确定。机器人对手还需要 `RankedRobot` 权限。自定义 Ranked 对局要求公开房间、公开的 19×19 对局、最多六个让子、贴目 −10 至 10，以及每方大于 450 秒的估算用时。估算包含读秒，也允许时间无限制。600 秒的 Absolute 配置符合时间要求。客户端会拒绝不合条件的设置，也会拒绝服务器将对局改为 Free。

## 自定义游戏设置 {#custom-game-settings}

这些设置适用于 Offer 和 Join。将它们排除在 Automatch 配置之外。

| TOML 设置 | CLI 选项 | 选择和默认 |
| --- | --- | --- |
| `game.boardSize` | `--board-size` | 默认`9`；范围 2–25，取决于发动机支持。 |
| `game.rules` | `--rules` | `Chinese`（默认）、`Japanese`、`Aga` 或 `NewZealand`。 |
| `game.komi` | `--komi` | 默认`7.5`； −100 至 100，以半点增量。 |
| `game.color` | `--color` | `Black`、`White` 或 `Nigiri`； Offer 默认为黑色，Join 默认为白色。 |
| `game.handicap` | `--handicap` | 默认`0`；否则 2–9 在电路板的布局限制内。不能与握寿司一起使用。 |
| `game.private` | `--private` | 默认`false`；需要进行私人游戏，同时在所选房间中公布挑战。 |

让子不会自动调整贴目，请明确设置两者。日本和 AGA 规则采用固定位置：棋盘至少为 7×7，在 7×7 或边长为偶数的棋盘上最多让四子。中国和新西兰规则采用自由摆放，最多九子，并至少留一个空交叉点。让子对局需要 `set_free_handicap`；自由摆放时，黑方还需要 `place_free_handicap`。

### 时间控制 {#time-controls}

| TOML 设置 | CLI 选项 | 默认值和范围 |
| --- | --- | --- |
| `timing.system` | `--time-system` | `Absolute`（默认）、`None`、`Canadian` 或 `ByoYomi`。 |
| `timing.mainTime` | `--main-time` | 默认为 `600`，或 `0` 为 None；范围 0–86400。 |
| `timing.byoYomiTime` | `--byo-yomi-time` | 默认`0`；使用加时赛时，按日本时段或加拿大时段 1–86400。 |
| `timing.byoYomiPeriods` | `--byo-yomi-periods` | 默认`0`； 1–255 用于读读。 |
| `timing.canadianStones` | `--canadian-stones` | 默认`0`； 1–255 加拿大。 |

对于日本加时赛，主时间为 10 分钟，5 个 30 秒时段：

```toml
[timing]
system = "ByoYomi"
mainTime = 600
byoYomiTime = 30
byoYomiPeriods = 5
```

对于加拿大加时赛，使用 `system = "Canadian"`、`byoYomiTime` 表示每块的秒数，使用 `canadianStones` 表示每块的石子。省略 `byoYomiPeriods`。读秒允许主时间为零。绝对要求正主时间，无读秒； None 要求所有显式提供的时间值均为零。总时钟储备也必须适合服务器的范围；报告无效组合。

计时游戏需要 `time_left` 和 `time_settings` 或 `kgs-time_settings`。日本读秒特别需要`kgs-time_settings`。无限游戏不需要时钟命令。引擎响应超时与游戏时钟分开，不会给机器人更多的游戏时间。

## 运行机器人 {#running-the-bot}

将 `matchmaking.games` 设置为正总数，或设置 `0` 以继续播放。仅 KGS 确认的结果有效。完成游戏后，客户端离开并使用原始的匹配设置进行下一场游戏。失败或未完成的游戏会停止系列赛，而不是算作已完成。

对于连续游戏且游戏之间等待时间较长的情况：

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --games 0 --lobby-timeout 3600
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml --games 0 --lobby-timeout 3600
```

</details>

按 Ctrl+C 停止。客户端注销，要求引擎退出，并在必要时停止其启动的引擎。比赛中停止并不能确定最终结果。在开始另一轮比赛之前检查任何未完成的比赛。

### 日志和退出代码 {#logs-and-exit-codes}

状态、错误、帮助和发动机诊断转到 stderr。为了留住他们：

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml 2> .\bot.log
$LASTEXITCODE
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml 2> ./bot.log
echo $?
```

</details>

使用服务管理器或外部工具进行日志轮换。标准I/O模式下，保持stdout与引擎连接；它携带 GTP 命令。

| 退出代码 | 含义 |
| --- | --- |
| `0` | 请求的游戏已完成，或者探测/帮助/版本命令成功。 |
| `1` | 配置或运行时失败；检查诊断。 |
| `130` | 操作符取消，包括Ctrl+C。 |

### 持久状态和现有游戏 {#persistent-state-and-existing-games}

客户端保存KGS分配的身份。在匹配模式下，默认文件位于 .NET 的本地应用程序数据目录下，地址为 `Kgs.Gtp/identities/<server-and-account-hash>`。在 Windows 上，该值通常低于 `%LOCALAPPDATA%`。要选择稳定的可写位置，请设置 `account.clientIdFile = "./state/client-id"`。在升级和容器更换中保留它。为每个服务器和帐户使用单独的文件。

Offer和Join首先检查所选房间是否有属于该帐户的未完成游戏。只能恢复一款兼容游戏；它的对手和完整的个人资料必须匹配。多个或不匹配的游戏停止启动。存档的游戏不会自动加载。

正在运行的自动匹配会话可以在连接丢失后恢复分配的游戏。新进程不会自动发现旧的自动匹配游戏。在再次注册之前解决未完成的自动匹配游戏。

### 收回、暂停和对手缺席 {#takebacks-pauses-and-opponent-absence}

`undo.free` / `--undo-free` 和 `undo.ranked` / `--undo-ranked` 可分别设为 `Never`（默认）或 `Allow`。附带示例允许 Free 对局悔棋，拒绝 Ranked 对局悔棋。Allow 会在正常对局期间接受服务器允许的对手申请；机器人不会主动申请悔棋。随后它重放已确认的棋谱，因此引擎不必支持 GTP `undo`。因终局计分争议而续弈不受这项设置控制。

KGS 控制暂停、休会和恢复。暂停或暂停时，机器人不会开始新的游戏或得分操作。每次连续暂停、休会和对手缺席都有单独的限制，默认为 300 秒：

| TOML 设置在 `[interactions]` 中 | CLI 选项 |
| --- | --- |
| `pauseTimeoutFree` | `--pause-timeout-free` |
| `adjournmentTimeoutFree` | `--adjournment-timeout-free` |
| `opponentTimeoutFree` | `--opponent-timeout-free` |
| `pauseTimeoutRanked` | `--pause-timeout-ranked` |
| `adjournmentTimeoutRanked` | `--adjournment-timeout-ranked` |
| `opponentTimeoutRanked` | `--opponent-timeout-ranked` |

每个接受 1–86400 秒。到期将停止客户端并显示代码 1 并让游戏未完成；它不会认输或开始另一场比赛。重新连接和更换引擎不会重置这些等待。其他有效的截止日期可能会更快到期。当对手不在时，如果 KGS 允许，机器人仍然可以移动。

## 超时和恢复 {#timeouts-and-recovery}

### 正常超时 {#normal-timeouts}

全部接受1–86400秒：

| TOML 设置 | CLI 选项 | 默认 | 限制 |
| --- | --- | --- | --- |
| `timeouts.login` | `--login-timeout` | `30` | 连接并登录。 |
| `timeouts.lobby` | `--lobby-timeout` | `300` | 一项挑战协商或自动匹配注册；还限制了房间名称查找。 |
| `timeouts.move` | `--move-timeout` | `600` | 一种正常或清理引擎搜索。 |
| `timeouts.scoring` | `--scoring-timeout` | `120` | 一轮评分，包括评估和同意。 |
| `timeouts.cleanup` | `--cleanup-timeout` | `300` | 所有清理尝试和随后的得分一起进行。 |

### KGS 连接丢失 {#kgs-connection-loss}

客户端重试传输失败，再次进行身份验证，并使用服务器历史记录重新加入中断的游戏。它不会重新发送不确定的动作，也不会用新的挑战替换已知的中断游戏。拒绝登录、服务器注销、无效服务器数据、非法引擎移动和拒绝引擎命令都是终端故障。

| TOML 设置 | CLI 选项 | 默认值和范围 |
| --- | --- | --- |
| `connectionRecovery.attempts` | `--reconnect-attempts` | 每次中断可选上限； 0–100。默认省略；零禁用重试。 |
| `connectionRecovery.delay` | `--reconnect-delay` | `1`-第二个初始窗口； 0–30，加倍为 30 秒上限，具有完全抖动。 |
| `connectionRecovery.timeout` | `--recovery-timeout` | 通过游戏重新连接每次重新连接 `120` 秒； 1–86400。 |
| `connectionRecovery.budget` | `--recovery-budget` | 每次中断总计 `180` 秒，包括耗尽、退避、登录和重新加入； 1–86400。 |
| `connectionRecovery.resetAfter` | `--recovery-reset-after` | `60` 重新连接后重置预算和重试计数之前的健康秒数； 1–86400。 |
| `connectionRecovery.engineDrainTimeout` | `--engine-drain-timeout` | `30` 秒完成并丢弃旧发动机工作； 1–86400。 |

当检测到连接丢失时，中断预算开始计算。每次重新连接都受到剩余预算及其自己的登录/重新加入超时的限制。每个退避延迟在零和上限之间随机选择，该上限从 1 秒加倍到 30 秒上限。当总预算或明确的尝试上限耗尽时，恢复就会停止。

重新连接后，机器人可以在旧的恢复期限之后继续玩游戏。稍后的断开连接会在 60 正常秒数后获得新的预算。在该间隔之前断开连接将保留之前的截止时间和重试计数，包括短暂连接的时间。当游戏仍需要重新加入时，仅登录并不能确定健康状况。

### 发动机故障 {#engine-failure}

如果正在运行的引擎退出或其流变得不可用，客户端将保持 KGS 会话处于活动状态，并尝试使用原始可执行文件和参数启动替换。它会在继续之前检查替换并重播已确认的历史记录。初始引擎启动/发现失败会停止客户端。当引擎不可用时，KGS 时钟继续。

| TOML 设置 | CLI 选项 | 默认值和范围 |
| --- | --- | --- |
| `engineRecovery.attempts` | `--engine-restart-attempts` | `3` 跨调用自动替换； 0–100。零等待操作员恢复。 |
| `engineRecovery.delay` | `--engine-restart-delay` | `1`-第二个初始窗口； 0–30，加倍为 30 秒上限，具有完全抖动。 |
| `engineRecovery.timeout` | `--engine-recovery-timeout` | `120` 秒用于发现/设置并单独用于重放； 1–86400。 |
| `engineRecovery.pipe` | `--engine-recovery-pipe` | 局部回收管；默认`kgs-gtp-<process ID>`。使用 1–100 ASCII 字母、数字、句点、连字符或下划线。 |

当自动替换用尽时，诊断会命名本地恢复管道。机器人等待操作员干预，同时正常游戏和大厅截止日期继续。要重新启动客户端启动的引擎，请以同一操作系统用户身份连接并发送 UTF-8 `restart` 后跟 LF。例如，如果您配置了 `pipe = "YourBot-recovery"`，请在等待诊断后在另一个终端中运行以下命令：

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
$pipe = [IO.Pipes.NamedPipeClientStream]::new(
    '.', 'YourBot-recovery', [IO.Pipes.PipeDirection]::InOut)
try {
    $pipe.Connect(5000)
    $request = [Text.Encoding]::UTF8.GetBytes("restart`n")
    $pipe.Write($request, 0, $request.Length)
    $pipe.Flush()
}
finally { $pipe.Dispose() }
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
python3 - <<'PY'
import os
import socket

pipe = os.path.join(os.environ.get("TMPDIR") or "/tmp", "CoreFxPipe_YourBot-recovery")
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as connection:
    connection.settimeout(5)
    connection.connect(pipe)
    connection.sendall(b"restart\n")
PY
```

</details>

Linux 示例需要 Python 3 并连接到 .NET 的 Unix 域套接字。以同一用户身份运行它，并使用与机器人相同的 `TMPDIR`（默认为 `/tmp`）。将`YourBot-recovery`替换为配置的管道名称；具有私有临时目录的服务也需要客户端在同一环境中运行。

成功的操作员更换会启动新的自动重试预算。编辑 TOML 文件不会更改正在运行的客户端的可执行文件或参数。

对于 `--stdio`，外部监控器必须通过双工回收管道连接新发动机并在两个方向上中继 GTP。该模式下没有 `restart` 问候语。原来的stdin/stdout连接出现故障后无法重复使用。

## 故障排除 {#troubleshooting}

| 症状 | 要检查什么 |
| --- | --- |
| 发动机启动前配置错误 | 检查命名文件和源位置、准确的键拼写、引用的房间名称和 TOML 值类型。旧版 Java 属性文件需要转换。 |
| 引擎无法启动或打开其模型 | 检查可执行文件和参数路径、GTP 模式参数以及工作目录。尝试 `--probe`。 |
| 缺少 GTP 命令或协议版本错误 | 使用完整的GTP v2引擎。发现需要 `protocol_version`、`name`、`version`、`known_command`、`list_commands`、`quit`、`boardsize`、`clear_board`、 `komi`、`play` 和 `genmove`。 |
| 规则、计时或评分检查失败 | 检查所选配置文件的引擎功能。仅当发动机缺少`kgs-rules`时才声明`engine.rules`，并使其与实际配置相匹配。所有自动游戏都需要 `final_status_list`。 |
| 登录失败 | 检查启动环境中的账户名`KGS_PASSWORD`、服务器地址以及上报的拒绝原因。 |
| 找不到房间 | 从所选服务器上的 KGS 复制其全名。匹配忽略大小写，但需要全名。 |
| 等待游戏或大厅超时 | 检查匹配条款、对手资格、房间名称和自动匹配首选项。如果需要更长的等待时间，请增加 `timeouts.lobby`。 |
| Ranked 条目被拒绝 | 检查 RankedRobot 权限、启用的等级、公共房间和 Ranked 个人资料限制。 |
| 出现分歧时停止评分 | 日本的争议得不到支持。中国，AGA，新西兰清理需要`kgs-genmove_cleanup`；反复争执、缺乏进展、清理到期使客户停止。 |
| 机器人在暂停或对手离开后停止 | 检查相关的交互超时并在重新启动之前检查未完成的游戏。 |
| 引擎不可用但帐户仍在线 | 检查发动机诊断和恢复管道消息。自动重试可能会耗尽；比赛时钟和截止日期仍然有效。 |
| 身份文件错误 | 确保配置的状态位置可写并且包含客户端生成的身份文件。 |

报告问题时，请包括客户端版本、引擎名称/版本、游戏 ID（如果有）、相关设置和 stderr 诊断。省略密码。

---
layout: "localized"
title: "从 Java GTP 客户端升级到 Mobi"
nav_title: "从 Java 版迁移"
lang: "zh-Hans"
page_key: "mobi/upgrade-guide"
section: "mobi"
nav_order: 2
permalink: "/zh-Hans/gtp/upgrade-guide/"
source_revision: "c32ebab17d841776f058eab0acfe73c12237c6953d8b7f6ec6630c41d26de6f1"
---

本指南将机器人从 `kgsGtp.jar` 及其 Java `.properties` 配置移动到 Mobi 和 TOML。旧文件无法直接加载；没有自动导入器。保留它以供创建新文件时参考。有关正常操作和完整设置参考，请参阅[用户指南]({% include page-url.html key='mobi/user-guide' %})。

本指南涵盖 Windows 和 Linux。展开适用于您的操作系统的部分以查看 PowerShell 或 Bash 命令。从提取的客户端目录运行命令。

## 升级步骤 {#upgrade-steps}

1. 完成或解决任何当前游戏，然后停止旧客户端及其引擎。    尝试替换时禁用其自动重新启动，因此两个客户端不会使用同一帐户登录。
2. 为您的 Windows 或 Linux 架构提取 Mobi GTP 桥接包。    该包包含 .NET 运行时。保留您的发动机、型号和发动机配置；这些与客户端保持分离。
3. 将 [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) 复制到 `bot.toml`。使用下表移动设置。将密码放入`KGS_PASSWORD`中，并明确选择游戏类型、回收策略和游戏数量。
4. 使用以下命令探测引擎。在登录前修复引擎发现错误。在正常启动时运行额外的游戏功能检查。
5. 使用 `--games 1` 运行一款 Free 游戏。验证登录、对手选择、时钟、计分和 `Series: completed game 1` 诊断。
6. 如果您想连续播放，请设置 `games = 0`，然后更新您的启动器或服务以使用新的可执行文件、配置路径、密码环境和日志。

复制模板，然后编辑帐户、引擎路径和游戏设置：

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

编辑完成后，无需登录即可查看引擎发现：

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

要返回旧客户端，请先停止新客户端和引擎，检查所有未完成的游戏，然后恢复原始启动器和属性文件。保留新客户的身份文件，以便稍后返回到 Mobi。

## 切换前要审查的更改 {#changes-to-review-before-switching}

| 面积 | 老客户 | Mobi |
| --- | --- | --- |
| 发射 | `java -jar kgsGtp.jar bot.properties key=value` | `Kgs.Gtp --config bot.toml --option value`; Windows 可执行文件以 `.exe` 结尾。 |
| 配置 | Java 属性，包括 Java 转义 | UTF-8 TOML 包含命名部分、带引号的字符串、数字、数组和布尔值。未知的密钥是错误。 |
| 默认模式 | Automatch | 除非选择 `matchmaking.mode` 或 `--lobby`，否则不会进行匹配。 |
| 游戏数 | 继续寻找游戏 | 内置默认值是一款已完成的游戏。设置`games = 0`为连续播放；提供的示例已经做到了这一点。 |
| 游戏类型 | Automatch 可以允许 Free 和 Ranked 一起使用 | 仅选择 `Free`（默认）或 `Ranked`。没有混合设置或后备。 |
| 房间 | 房间名称 | 房间名称，仍然是一个字符串；使用 `room = "English Room"`。查找忽略大小写并需要准确的名称。 |
| 自定义游戏条款 | 玩家可以提出修改建议 | 配置的术语必须完全匹配，包括颜色、科米、障碍、可见性和时间控制。 |
| 收回 | 通常在 Free 游戏中允许，在 Ranked 中拒绝 | 两个内置策略均默认为 `Never`。设置 `undo.free = "Allow"` 以保留通常的 Free 行为。该示例就是这样做的。 |
| Automatch 让分盘 | 如果引擎支持障碍，则最多可允许九个等级 | `maxRankDifference` 默认为 `0`；显式选择它，最多为 Free 为 9，或为 Ranked 最多为 6。 |
| 连接重试 | `reconnect=t` 启用继续重试 | 默认 180 秒中断预算，带抖动的指数退避，并在 60 健康秒后重置。 |
| 发动机故障 | `reconnect` 发动机无法自动重启 | 单独的自动重启预算；精疲力竭等待操作员恢复，而正常的最后期限仍在继续。 |
| 对手离开 | 可以在缺席限制后返回匹配 | 当配置的等待到期时，新客户端将停止并显示未完成的游戏诊断。 |

该示例是一个起始配置，而不是声明保留所有旧行为。特别是，在启用连续操作之前，请决定该帐户是否应该玩Free或Ranked。

## 映射旧设置 {#map-the-old-settings}

下面的新设置名称使用 `section.key` 表示法。例如，`account.username` 表示 `[account]` 下的 `username = "YourBot"`。

### 帐户、连接和引擎 {#account-connection-and-engine}

| 旧房产 | 新设定 | 迁移笔记 |
| --- | --- | --- |
| `name` | `account.username` / `--username` | 未配置用户名时也支持 `KGS_USERNAME`。 |
| `password` | 环境变量 `KGS_PASSWORD` | 从新配置中删除它；不支持密码字段和密码 CLI 选项。 |
| `server.host` | `server.host` / `--host` | 字符串；默认`goserver.gokgs.com`。 |
| `server.port` | `server.port` / `--port` | 整数；默认`2379`。 |
| `reconnect=f` | `connectionRecovery.attempts = 0` | 禁用 KGS 传输重试；发动机恢复是单独配置的。 |
| `reconnect=t` | `[connectionRecovery]` | 选择每次中断的时间预算；默认为 180 秒。尝试上限是可选的。 |
| `engine` | `engine.executable` 和 `engine.arguments` | 将命令拆分为可执行文件和单独的参数；见下文。 |
| 无发动机连接属性 | `engine.stdio = true` / `--stdio` | 现在必须明确选择标准 I/O。 |
| `gtp.in`, `gtp.out` | 没有直接设置 | 外部发射器可以通过`--stdio`连接两个方向。客户端不会从配置中打开命名文件或 FIFO。 |
| `engine.port` | 没有直接设置 | 没有引擎 TCP 侦听器。使用带有 `--stdio` 的外部适配器，或者让客户端启动引擎。 |
| `logFile` | 外部捕获stderr | 使用 shell 重定向或服务管理器；内置 Java 日志命名和轮换不会保留。 |
| `verbose` | 没有直接设置 | 正常诊断转到stderr；没有等效的完整 GTP/服务器流量记录交换机。 |

本地 `engineRecovery.pipe` 用于更换正在运行的会话中出现故障的引擎。它不会替换旧的 `engine.port`、`gtp.in` 或 `gtp.out` 启动设置。

### 匹配和游戏设置 {#matchmaking-and-game-settings}

| 旧房产 | 新设定 | 迁移笔记 |
| --- | --- | --- |
| `mode=auto` | `matchmaking.mode = "Automatch"` | 省略房间、自定义对手设置和 `game`/`timing` 部分。 |
| `mode=custom` | `matchmaking.mode = "Offer"` | 添加 `opponentPolicy = "Any"` 进行公开挑战，或 `"Named"` 加上 `opponent`。 |
| `mode=wait` | `matchmaking.mode = "Join"` | 设置房间名称和`opponent`；提供的配置文件必须完全匹配。 |
| `mode=both` | 无组合模式 | 为此调用选择 Automatch、Offer 或 Join。 |
| `mode=tournament` | 不支持 | 未实行赛事报名；如果需要的话，保留老客户。 |
| `room` | `matchmaking.room` / `--room` | 将房间名称保留为带引号的字符串。对于 Offer 和 Join 是必需的；省略 Automatch。没有上次使用的房间默认值。 |
| `opponent` | `matchmaking.opponent` | 对于自定义挑战，请使用 `opponentPolicy = "Named"`。省略 Automatch 的两个自定义对手设置。 |
| `gameNotes` | `matchmaking.challengeNotes` | 仅限 Offer；最多 255 个字符，不含控制字符。 |
| `rules` | `game.rules` | 使用 `Japanese`、`Chinese`、`Aga` 或 `NewZealand`。设置准确的自定义游戏条款。 |
| `komi` | `game.komi` | 数字，而不是带引号的字符串；明确设置，包括让分游戏。 |
| `rules.boardSize` | `game.boardSize` | 整数。明确设置：新的自定义游戏默认值为 9。 |
| `rules.time` | `[timing]` | 使用以下示例分为系统、秒数和读秒字段。 |
| `automatch.speed` | `automatch.speed` | 例如 `speed = ["Blitz", "Medium"]` 或 `"All"`。 CLI 组合使用逗号。 |
| `automatch.rank` | `automatch.rank` | 通过`1k`引用`30k`；当没有数字服务器等级时仍然需要。 |
| `undo=f` | `[undo]` 与 `free = "Never"`、`ranked = "Never"` | 这些也是内置默认值。 |
| `undo=t`或省略 | `[undo]` 与 `free = "Allow"`、`ranked = "Never"` | 保留了通常的旧Free/Ranked区别。如果需要，可以单独启用新的 Ranked 回收。 |
| `talk` | 不支持 | 未实现私人聊天回复和引擎聊天转发。 |
| `hint.cleanup`, `hint.noArguing` | 不支持 | 对于评分争议，没有可配置的聊天提示。 |

`game.rules` 和 `engine.rules` 具有不同的用途。前者选择自定义游戏的规则。后者声明已在缺少 `kgs-rules` 的引擎中配置的规则；它不会改变该引擎的配置。

### 拆分引擎命令 {#split-the-engine-command}

旧财产可能是：

```properties
engine=/opt/katago/katago gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

新的配置是：

```toml
[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]
```

不要将整个命令行放入 `executable` 中。没有外壳评估。每个参数都是一个数组元素，包括包含空格的路径。对于 Windows，单引号 TOML 字符串保留反斜杠文字：

```toml
[engine]
executable = 'C:\Go Engines\katago.exe'
arguments = ["gtp", "-config", 'C:\Go Engines\gtp.cfg', "-model", 'C:\Go Engines\model.bin.gz']
```

将 Java 属性转义替换为 UTF-8 TOML 中的实际文本。包含分隔符的相对可执行路径从 TOML 目录解析；参数路径仍然相对于启动工作目录。绝对模型和配置路径使服务启动更容易重现。

### 转换时间控件 {#convert-time-controls}

仅使用这些 `[timing]` 部分之一，并且仅与 Offer 或 Join 一起使用。

旧`rules.time=0`：

```toml
[timing]
system = "None"
mainTime = 0
```

旧`rules.time=30:00`：

```toml
[timing]
system = "Absolute"
mainTime = 1800
```

旧`rules.time=30:00+5x0:30`：

```toml
[timing]
system = "ByoYomi"
mainTime = 1800
byoYomiTime = 30
byoYomiPeriods = 5
```

旧`rules.time=30:00+25/10:00`：

```toml
[timing]
system = "Canadian"
mainTime = 1800
byoYomiTime = 600
canadianStones = 25
```

所有新时间值都是整数秒。删除属于不同系统的读秒字段。日本加时需要引擎的`kgs-time_settings`命令；它不是使用另一个时钟系统来近似的。

## 示例：迁移自动匹配机器人 {#example-migrate-an-automatch-bot}

假设旧文件的相关部分是：

```properties
name=YourBot
password=<account password>
mode=auto
room=English Room
automatch.speed=fast,medium
automatch.rank=20k
undo=t
reconnect=t
engine=/opt/katago/katago gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

为初始 Free 游戏创建此 `bot.toml`。 Automatch 不采用房间设置，因此旧的 `room` 属性被省略：

```toml
[account]
username = "YourBot"
clientIdFile = "./state/client-id"

[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]

[matchmaking]
mode = "Automatch"
gameType = "Free"
games = 1

[automatch]
speed = ["Fast", "Medium"]
rank = "20k"
opponents = "Humans"
maxRankDifference = 0

[undo]
free = "Allow"
ranked = "Never"

[connectionRecovery]
budget = 180
resetAfter = 60
```

对于 Windows，将 `[engine]` 路径替换为 [拆分引擎命令](#split-the-engine-command) 中的 Windows 示例。设置密码并运行一款游戏：

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

此示例甚至特意选择了 Free 游戏。要保持差点匹配，请选择合适的 `maxRankDifference` 并检查发动机支持。要玩Ranked，请选择`gameType = "Ranked"`，验证帐户的RankedRobot权限和启用的排名，最多使用6个排名差异。一次调用不能同时接受两种游戏类型。

对于自定义机器人，请使用[自定义挑战示例]({% include page-url.html key='mobi/user-guide' %}#custom-challenges)，复制旧房间名称，并明确传输棋盘尺寸、规则、科米、颜色、让分和转换时间设置。

## 发动机兼容性和无人值守操作 {#engine-compatibility-and-unattended-operation}

Mobi 需要 GTP v2 及其完整的强制命令集。一些被旧客户端视为可选的命令在这里是必需的。所有自动游戏也需要 `final_status_list`。计时游戏需要 `time_left` 和支持的计时命令。检查用户指南对您所选配置文件的引擎要求；仅旧的工作配置并不能建立兼容性。

普通日本得分协议得到支持，但未解决的日本争议导致比赛停止。中国、AGA 和新西兰的清理工作需要 `kgs-genmove_cleanup`，并且有有限的尝试和总期限。当自动计分不可用时，不存在让对手决定所有死子的旧客户端后备方案。

在让机器人无人看管之前检查这些服务设置：

- 如果要继续播放，请明确设置 `games = 0`。每次大厅尝试仍然有默认的 300 秒截止日期；如果需要，增加 `timeouts.lobby`。
- 单独配置KGS连接重试和引擎重启。 KGS 每次中断恢复默认为 180 秒，并在 60 健康秒后重置。引擎恢复允许在调用过程中进行三种自动替换；耗尽可能会使实时 KGS 会话等待操作员恢复。
- 选择暂停、休会和对手缺席限制。每个默认为300秒；到期会停止客户端，而不计算或放弃未完成的游戏。
- 将客户端身份文件保存在可写状态目录中。新进程不会自动发现旧的自动匹配游戏。
- 捕获 stderr 并安排外部日志保留。退出0表示正常完成，1表示失败，130表示取消。

[用户指南]({% include page-url.html key='mobi/user-guide' %}#timeouts-and-recovery)详细介绍了超时设置、连接恢复和算子引擎恢复。

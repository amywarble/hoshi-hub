---
source_revision: "2dd2b5f3a829514cb3f4e94bc67cffcd8f04dad8b5b984ffab73449fda82c3c7"
layout: "localized"
title: "账户与数据删除"
lang: "zh-Hans"
page_key: "global/account-and-data-deletion"
section: "global"
nav_order: 2
permalink: "/zh-Hans/account-and-data-deletion/"
redirect_from: "/zh-Hans/desktop/account-and-data-deletion/"
---

_最后更新：2026年10月27日_

Pocket KGS、KGS Nova 和 Mobi 登录由 KGS Go Server 托管和控制的账户。这些客户端都没有独立的账户系统。账户由 KGS 通过其 [官方注册页面](https://www.gokgs.com/register/index.html) 创建。

清除本地数据或卸载 **不会删除** KGS 账户、消息、对局、资料或其他 KGS 数据。

## 删除 KGS 账户和服务器数据

1. 发邮件到 [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request)，主题 `KGS account deletion request`。
2. 明确要求删除账户及关联服务器数据。
3. 提供 KGS 用户名和注册邮箱。**绝不要发送密码。**

管理员可能联系您核实归属，处理请求并解释预计时间，以及因安全、服务完整性或法律而须保留的信息。删除在管理员收到并核实请求后进行，不会因卸载或清除存储而自动发生。

不要在公开 GitHub 问题中提交账户详情。

## 删除本地应用数据

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

1. 打开 Android **设置**。
2. 选择 **应用**，再选 **Pocket KGS**。
3. 进入 **存储和缓存**。
4. 选择 **清除存储**（名称因设备而异）或卸载。

这会删除设置、本地客户端标识及头像缓存。应用请求 Android 不备份其私有数据。

通过 Android Credential Manager 保存的密码，须在选定密码管理器／提供方中另行删除。清除应用数据不一定删除其副本。

### KGS Nova

关闭 KGS Nova，备份想保留的已导出棋谱。

- 从操作系统本地应用数据目录的 KGS Nova 文件夹（Windows 为 `%LOCALAPPDATA%\KGS Nova`）删除 `data.db` 和存在的 `data-log.db` 日志文件，可清除账户元数据、设置、客户端标识和应用状态。
- 要删除诊断，请从同一数据文件夹删除 `client.log`、`client.archive*.log` 以及开发版的 `logs.txt`。其他位置保存的副本仍会保留。
- Windows 的 DPAPI 保护密码存于 `data.db`，会随文件删除。macOS／Linux 须在钥匙串／Secret Service 中单独删除本应用的密码项，查找服务 `io.github.amywarble.kgsnet.desktop.credentials` 和您的 KGS 用户名。删除数据库不会清除这些系统条目。
- 在所选保存位置删除不再需要的导出棋谱、截图及其他文件。

同一文件夹还包含 `sgf` 工作区、恢复文件和备份，以及 `analysis` 引擎／模型文件。删除前请保存希望保留的恢复棋谱。删除整个 KGS Nova 数据文件夹可一并移除这些本地数据。

旧版将 `data.db`、`data-log.db` 和 `logs.txt` 放在应用或启动目录。升级后这些副本可能仍在。备份所需内容后，也请删除旧副本，否则当前数据库缺失时可能再次导入旧数据库。

卸载不一定删除文件或系统凭据。

### Mobi

停止 Mobi 和引擎，并禁用会重启机器人的服务或计划任务。先保存需要保留的棋谱和配置。

- 删除通过 `account.clientIdFile` 或 `--client-id-file` 指定的客户端标识文件。未覆盖路径时，匹配使用 .NET 本地应用数据目录（Windows 下为 `%LOCALAPPDATA%`）中的 `Kgs.Gtp/identities/<server-and-account-hash>`，其他运行默认为 `Kgs.Gtp/client-id`。如果同一机器还有其他机器人，只删除正在退役账号的文件。
- 从启动 shell 及您存储过密码的持久环境设置、启动脚本或服务配置中移除 `KGS_PASSWORD`。Mobi 读取该变量，但本身不保存密码。不再需要时，也移除保存的 `KGS_USERNAME` 值和包含账号名、路径或设置的 TOML 文件。
- 删除通过重定向 stderr 保存的诊断，例如 `bot.log`，以及您能够控制的服务管理器日志或在其他地方共享的副本。
- 查阅围棋引擎文档，删除其自身日志、棋谱、配置或其他数据。引擎／模型文件与 Mobi 分开管理；不要删除其他应用仍在使用的文件。

删除解压后的 Mobi 文件不一定移除上述项目。删除客户端标识不会删除 KGS 账号、重置等级或清除服务器上的棋谱。

## 联系

如需私下咨询任一应用保存的数据，请联系 [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com)。

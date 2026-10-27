---
source_revision: "f77f4ed1d576932db0474a6793f3618116114ca1712e98af8892162d5ac9d665"
layout: localized
title: "账户与数据删除"
lang: "zh-Hans"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/zh-Hans/desktop/account-and-data-deletion/"
nav_group: "policies"
---

## 删除桌面数据

关闭 KGS Nova，备份想保留的已导出棋谱。

- 从操作系统本地应用数据目录的 KGS Nova 文件夹（Windows 为 `%LOCALAPPDATA%\KGS Nova`）删除 `data.db` 和存在的 `data-log.db` 日志文件，可清除账户元数据、设置、客户端标识和应用状态。
- 要删除诊断，请从同一数据文件夹删除 `client.log`、`client.archive*.log` 以及开发版的 `logs.txt`。其他位置保存的副本仍会保留。
- Windows 的 DPAPI 保护密码存于 `data.db`，会随文件删除。macOS／Linux 须在钥匙串／Secret Service 中单独删除本应用的密码项，查找服务 `io.github.amywarble.kgsnet.desktop.credentials` 和您的 KGS 用户名。删除数据库不会清除这些系统条目。
- 在所选保存位置删除不再需要的导出棋谱、截图及其他文件。

同一文件夹还包含 `sgf` 工作区、恢复文件和备份，以及 `analysis` 引擎／模型文件。删除前请保存希望保留的恢复棋谱。删除整个 KGS Nova 数据文件夹可一并移除这些本地数据。

旧版将 `data.db`、`data-log.db` 和 `logs.txt` 放在应用或启动目录。升级后这些副本可能仍在。备份所需内容后，也请删除旧副本，否则当前数据库缺失时可能再次导入旧数据库。

卸载不一定删除文件或系统凭据。删除本地数据不会删除 KGS 账户或服务器记录。

## 请求删除 KGS 账户

KGS 控制账户和服务器数据。私下联系 [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request)，提供用户名和注册邮箱，绝不提供密码。管理员可能核实归属，并解释可删除的数据及保留要求。不要在公开 GitHub 问题中提交账户详情。

本地数据的私下咨询：[hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com)。

---
source_revision: "3aa9378df5f32e6acf17ec4a44bd9f2964f9a6fed7d528cdcba256cfb2358d82"
layout: localized
title: "账户与数据删除"
lang: "zh-Hans"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/zh-Hans/desktop/account-and-data-deletion/"
---

## 删除桌面数据

关闭 KGS Nova，备份想保留的已导出棋谱。

- 从启动应用所用的工作目录删除 `data.db`，以清除账户元数据、设置、客户端标识及应用状态并重置本地设置。从终端启动时，除应用文件夹外也检查该目录。
- 删除应用目录的 `logs.txt`。复制或从控制台保存的其他日志仍留在其保存处。
- Windows 的 DPAPI 保护密码存于 `data.db`，会随文件删除。macOS／Linux 须在钥匙串／Secret Service 中单独删除本应用的密码项，查找服务 `io.github.amywarble.kgsnet.desktop.credentials` 和您的 KGS 用户名。删除数据库不会清除这些系统条目。
- 在所选保存位置删除不再需要的导出棋谱、截图及其他文件。

卸载不一定删除文件或系统凭据。删除本地数据不会删除 KGS 账户或服务器记录。

## 请求删除 KGS 账户

KGS 控制账户和服务器数据。私下联系 [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request)，提供用户名和注册邮箱，绝不提供密码。管理员可能核实归属，并解释可删除的数据及保留要求。不要在公开 GitHub 问题中提交账户详情。

本地数据的私下咨询：[hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com)。

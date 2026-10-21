---
source_revision: "c0720ca8cede62afb75cc2d2bb2188cb6f42790a1a5ec1c815ee03a2934d2d54"
layout: localized
title: "隐私政策"
lang: "zh-Hans"
page_key: "desktop/privacy"
section: "desktop"
nav_order: 10
permalink: "/zh-Hans/desktop/privacy/"
---

_生效日期：2026年10月10日_

本政策适用于 Windows、macOS 和 Linux 版 KGS Nova。它是独立客户端，与 KGS 无隶属关系，也未获认可。KGS 为独立服务，有自己的 [条款和隐私信息](https://www.gokgs.com/tos.jsp)。

## 处理的信息

应用直连 KGS，视功能处理凭据及资料、房间、聊天、私信／离线消息、社交列表与备注、棋谱与落子、邀请、头像和设置。向 KGS 发送您请求的操作并显示回应。其他用户可见内容依 KGS 功能而定。

KGS 收到持久客户端标识、协议版本、语言／地区、系统、架构、运行时及连接网络地址。

合资格教师开启广播时，麦克风经 KGS 传给对局参与者；接收时播放 KGS 音频。停止操作或会话结束即终止广播。不为开发者另行录音。

没有广告、分析或自动崩溃上传。开发者不保存账户、消息、对局或音频的单独服务器副本。

## 本地存储与诊断

- **数据库：** 工作目录中的 `data.db` 保存账户元数据、客户端标识、设置和应用状态。数据库并未整体加密。
- **密码：** Windows 在数据库中使用当前用户的 DPAPI 加密；macOS 使用钥匙串；Linux 使用 Secret Service。可能需要系统解锁或授权。密码保护不加密数据库其余部分。
- **日志：** 应用目录的 `logs.txt` 及控制台／调试输出。文件在启动时替换。可能包含版本、系统、用户名、房间／对局标识、操作、异常和连接／消息失败时的协议数据。不要假设没有个人内容。不会自动上传。
- **导出文件：** 您明确保存的棋谱及其他文件留在所选位置。

有权访问文件或系统账户的他人／软件可能读取数据。卸载或替换不一定删除数据库、日志、导出文件或系统凭据。见 [数据删除说明]({% include page-url.html key='desktop/account-and-data-deletion' %})。

## 通信与第三方

传统连接没有 TLS 或端到端加密。密码转换不保护全部流量免受监视或干预。请使用可信网络。

KGS 声明记录会话且管理员可能查看。避免分享须保密的信息。服务器管理及保留由 KGS 决定。

GitHub 按其 [隐私声明](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement) 托管支持和问题。点击链接会打开浏览器；报告错误会打开含版本、系统、架构、运行时的可编辑草稿，不自动提交或附加日志。提交的公开问题及附件均公开可见。

## 选择与联系

可用访客会话、决定是否记住凭据、限制受支持的私信交互、屏蔽用户、不进行麦克风广播以及删除本地文件。KGS 管理员负责账户删除：[说明]({% include page-url.html key='desktop/account-and-data-deletion' %})。

不要在公开问题中提交儿童个人信息。家长／监护人应在允许未成年人使用前审阅 KGS 条款和通信功能。

应用／隐私私下咨询：[hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com)。KGS 账户及服务器数据：[admin@gokgs.com](mailto:admin@gokgs.com)。漏洞：[私密报告](https://github.com/amywarble/hoshi-hub/security/advisories/new)。

本政策随桌面行为更新；生效日期标示修订版本。

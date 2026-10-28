---
source_revision: "6557edaea14029268590a7f73220e26c62aafda65681a4c44da3dd659e4b7ca7"
layout: "localized"
title: "隐私政策"
lang: "zh-Hans"
page_key: "global/privacy"
section: "global"
nav_order: 3
permalink: "/zh-Hans/privacy/"
redirect_from: "/zh-Hans/desktop/privacy/"
---

_生效日期：2026年10月27日_

本政策涵盖 Android 版 Pocket KGS、Windows、macOS 和 Linux 版 KGS Nova、Windows 和 Linux 版 Mobi，以及本支持网站。三个客户端均获得 KGS 和 American Go Association（AGA）的官方认可。下文先说明共同做法，再列出各应用的存储和控制选项。

## 谁处理您的数据

客户端直接连接 KGS Go Server。客户端开发者不运营 KGS 服务器，也不控制其账号、管理、记录或保存期限。KGS 是独立服务，适用其自身的 [服务条款与隐私说明](https://www.gokgs.com/tos.jsp)。

客户端不含广告、使用情况分析或自动崩溃报告上传。开发者不出售您的个人信息，不将其用于定向广告或跨应用跟踪，也不在另一个服务器上保存您的 KGS 账号、聊天、棋谱、头像或教师音频的副本。

## 处理的信息及用途

根据所用客户端和功能，信息包括：

- **账号与资料：** KGS 登录凭据、电子邮箱、资料文字、头像、等级、账号状态和偏好。
- **通信与社交信息：** 房间和对局聊天、私信和离线消息、好友／关注者／屏蔽列表及备注，以及其他 KGS 内容。
- **对局与活动：** 着手、棋谱、注释、结果、对局邀请、房间成员关系和匹配设置。Mobi 与您配置的围棋引擎交换对局信息，用于生成着手和处理对局。
- **连接信息：** 持久 KGS 客户端标识、应用和协议版本、语言、操作系统和架构、运行时信息及连接状态。连接时 KGS 会收到您的 IP 地址。
- **本地设置与诊断：** 偏好、缓存内容，以及以下各应用部分说明的诊断信息。

这些信息用于登录、维持 KGS 会话、显示内容、向 KGS 发送您请求的操作或配置的机器人操作、记住设置，以及在您选择共享详情时排查问题。

Pocket KGS 和 Nova 还会在有权限的教师明确启动直播时处理麦克风音频，并播放收到的教师音频。您停止广播或相关会话结束时，广播即停止。两个客户端都不会为开发者另行录音。Mobi 不提供教师音频控制功能。

## 信息去向

- **KGS：** 接收账号与连接信息、通信、对局活动及请求的修改。其他用户可见的内容取决于您使用的 KGS 功能。
- **凭据提供方与引擎：** 平台凭据提供方和所选 Mobi 引擎按照下文说明及其各自条款处理信息。
- **GitHub：** 本网站和公开问题跟踪器由 GitHub 托管，适用 [GitHub 隐私声明](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)。公开问题和附件所有人均可见。Nova 的问题报告操作会在浏览器中打开可编辑草稿，包含应用版本、操作系统、架构和运行时详情；不会自动提交问题或附加日志。
- **法律与安全需要：** 您交给开发者的信息，可能在遵守法律、调查滥用、保护用户或维护权利与安全具有合理必要性时被保存或披露。

## 通信与安全

这些客户端使用的旧版 KGS 连接不提供 TLS 或端到端加密。登录协议会在传输前转换密码，但有权接触网络路径的人可能观察或篡改其他流量。请使用可信网络。

KGS 声明所有会话都会记录，管理员在调查举报时可能查阅。不要在 KGS 分享必须保密的信息。服务器端保存由 KGS 控制，棋谱可能保留在其档案中。

## 各应用的存储与选择

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

Pocket 在 Android 应用私有存储中保存偏好、通知选项和 KGS 客户端标识，在 Android 缓存中保存头像。Android 可能清除缓存文件。Pocket 请求 Android 不备份其应用私有数据。清除应用存储或卸载会删除这些本地应用数据。

如果您选择保存凭据，Android Credential Manager 和所选凭据提供方会按照各自条款处理。Pocket 不接收解锁凭据所用的生物识别数据。提供方保存的凭据可能需要单独删除。

正式版本的错误诊断写入 Android 系统日志。可选诊断日志会为当前会话增加细节。发布日志保留版本信息、事件模板、异常类型和堆栈，格式设计为省略运行时参数值、异常消息和源文件路径。Android、设备管理员或收到您日志的人可能访问这些信息。

您可以使用访客会话、选择是否保存凭据、在 Pocket 或 Android 中关闭通知、拒绝麦克风权限、不进行广播，以及通过屏蔽用户阻止支持的互动并隐藏其内容。

### KGS Nova

- **数据库：** 操作系统 KGS Nova 本地应用数据文件夹中的 `data.db`（Windows 下为 `%LOCALAPPDATA%\KGS Nova`）保存账号元数据、客户端标识、偏好和应用状态。整个数据库并未加密。
- **密码：** Windows 使用当前 Windows 用户的 DPAPI 保护数据库内保存的密码。macOS 使用 Keychain，Linux 使用 Secret Service。系统可能要求解锁或授权。这不会加密数据库的其余内容。
- **诊断：** 发布版本错误写入同一文件夹的 `client.log` 和轮换文件 `client.archive*.log`。可选会话诊断更加详细。发布日志采用与 Pocket 相同的省略规则。开发版本可能产生更详细的 `logs.txt` 以及控制台／调试输出。
- **其他文件：** 同一文件夹还包含 `sgf` 工作区、恢复文件和备份，以及 `analysis` 引擎／模型文件。导出的棋谱和其他文件保留在您选定的位置。

能够访问您的文件或系统账号的人或软件可能读取它们。卸载或替换 Nova 不一定删除数据库、日志、导出文件或密钥环条目。您可以使用访客会话、选择是否记住凭据、控制支持的私信互动、屏蔽用户、不广播麦克风音频，以及删除本地数据。

### Mobi

Mobi 需要已注册的 KGS 账号。它从 `KGS_PASSWORD` 读取密码，本身不将密码持久保存。启动脚本、环境设置或服务管理器可能保留您放在其中的凭据。请保护它们和您的系统账号；启动的引擎可能继承其环境变量。

TOML 配置可能包含账号名、服务器、引擎路径和对局设置。Mobi 将 KGS 客户端标识存入本地文件。匹配模式默认使用 .NET 本地应用数据目录（Windows 下为 `%LOCALAPPDATA%`）中的 `Kgs.Gtp/identities/<server-and-account-hash>`；不使用匹配时默认为 `Kgs.Gtp/client-id`。可用 `account.clientIdFile` 或 `--client-id-file` 更改位置。

状态、错误和引擎诊断输出到 stderr。如果您重定向输出或由服务管理器保留，日志就会保存。这些日志不遵循 Pocket/Nova 发布日志的省略规则，可能包含用户名、对局详情、路径或引擎输出。分享前请检查。引擎可能生成额外日志、棋谱或其他文件，并有自身网络行为；请单独查阅其文档与隐私做法。Mobi 不会自动向开发者上传诊断。

引擎、配置、保留输出和本地文件由您控制。操作与诊断请参阅 [Mobi 用户指南]({% include page-url.html key='mobi/user-guide' %})。

## 保存、删除与其他选择

开发者不会自动接收本地文件或诊断。您主动发送的副本可能为处理请求或法律与安全需要而保留。公开 GitHub 问题及其历史会一直保留，直到依照 GitHub 的功能与政策编辑或删除。

您可选择分享哪些资料信息，并在支持时将 KGS 邮箱设为私密。删除文件或卸载客户端不会删除 KGS 托管的数据。KGS 管理员负责账号和服务器数据删除。共同申请流程及各客户端本地清理步骤见 [账号与数据删除]({% include page-url.html key='global/account-and-data-deletion' %})。

Pocket KGS 不面向13岁以下儿童。KGS 是公开通信服务；未成年人使用前，家长或监护人应审阅其条款与适用性。请勿在公开问题中发布儿童个人信息。

## 变更与联系

请及时更新操作系统和客户端，使用 KGS 专用密码，分享日志前先检查。没有系统完全安全。请依照 [安全政策]({% include page-url.html key='global/security-policy' %}) 报告漏洞。

本政策可能随客户端变化而更新；生效日期标识已发布版本。非敏感支持请使用 [公开问题跟踪器](https://github.com/amywarble/hoshi-hub/issues/new/choose)。应用或隐私方面的私密问题请联系 [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com)。KGS 账号、服务器数据或管理问题请联系 [admin@gokgs.com](mailto:admin@gokgs.com)。

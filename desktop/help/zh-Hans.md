---
source_revision: "a5018456d7c6b6ef49fc5b143b52c2707452b29213029b1bba9cf85a02f24031"
layout: localized
title: "入门指南"
lang: "zh-Hans"
page_key: "desktop/help"
section: "desktop"
nav_order: 1
permalink: "/zh-Hans/desktop/help/"
nav_group: "documentation"
redirect_from: "/zh-Hans/desktop/"
---

KGS Nova 是适用于 Windows、macOS 和 Linux 的 [KGS Go Server](https://www.gokgs.com/) 客户端，已获得 KGS 和美国围棋协会（AGA）的官方认可。

## 安装与更新 {#installation}

从 [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) 下载 **KGS Nova** 安装包。Intel/AMD 处理器选择 x64，Apple Silicon 和其他 ARM64 设备选择 ARM64。每个版本均列出可用平台。安装包已包含 .NET 运行时。

- **Windows：** 运行 **Installer**。使用便携版时，将整个 **Portable** ZIP 解压到可写文件夹，然后运行 `Kgs.Client.Desktop.exe`。
- **Linux：** 使用 `chmod +x Kgs.Nova-linux-<architecture>.AppImage`（`x64` 或 `arm64`）为 **AppImage** 添加执行权限，然后启动。请放在可写文件夹中，以便更新。需要 FUSE 支持（Ubuntu 22.04 使用 `libfuse2`）。
- **macOS（如有提供）：** 运行 **Installer**，然后打开 `KGS Nova.app`。使用便携版时，解压整个 **Portable** ZIP，并将应用移到可写的 Applications 文件夹。构建使用临时签名，没有 Apple Developer ID 签名或公证。如果被阻止，请先确认下载可信，再到 **系统设置 > 隐私与安全性** 中允许 Nova 运行。

在 **关于** 中依次选择 **检查更新**、**下载更新**、**重启并更新**。Nova 也会在启动时检查更新。重启前请结束对局并保存工作。如果无法在应用内更新，请手动下载较新的安装包。

### Linux 手动安装

解压 `KGS-Nova-<version>-linux-<architecture>.tar.gz`，然后从该文件夹运行 `./Kgs.Client.Desktop`。这些压缩包需要重新下载才能更新。

Linux 需要 X11 或 XWayland、fontconfig 以及 .NET/Avalonia 使用的 X11 库。音频使用 PipeWire、PulseAudio 或 ALSA。保存密码需要 libsecret（Debian/Ubuntu 使用 `libsecret-1-0`）和 GNOME Keyring 等 Secret Service 提供程序。

### 更新文件

`.nupkg` 和 `releases.*.json` 文件供 Nova 更新程序使用。安装时请使用 **Installer**、**Portable** ZIP 或 **AppImage**。

## 登录

使用现有的 KGS 用户名和密码登录，或以访客身份继续。创建账户时，请使用登录界面的注册链接；它会打开 KGS 网站。

## 对局和探索

选择对局可寻找对手或创建自定义对局。使用房间参与讨论和观战，使用用户列表寻找玩家。查看/编辑可打开 SGF 棋谱进行本地学习。偏好设置可调整外观和应用选项。

## 帮助和政策

应用问题请参阅 [支持]({% include page-url.html key='desktop/support' %})。不受欢迎的互动和举报请参阅 [社区准则]({% include page-url.html key='desktop/community-guidelines' %})。另请阅读 [隐私政策]({% include page-url.html key='global/privacy' %})、[使用条款]({% include page-url.html key='desktop/terms' %}) 和 [共用社区准则]({% include page-url.html key='global/community-guidelines' %})。

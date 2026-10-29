---
source_revision: "a5018456d7c6b6ef49fc5b143b52c2707452b29213029b1bba9cf85a02f24031"
layout: localized
title: "はじめに"
lang: "ja"
page_key: "desktop/help"
section: "desktop"
nav_order: 1
permalink: "/ja/desktop/help/"
nav_group: "documentation"
redirect_from: "/ja/desktop/"
---

KGS Nova は Windows、macOS、Linux 用の [KGS Go Server](https://www.gokgs.com/) クライアントです。KGS と American Go Association（AGA）の公式な承認を受けています。

## インストールと更新 {#installation}

[GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) から **KGS Nova** のパッケージをダウンロードします。Intel/AMD プロセッサには x64、Apple Silicon などの ARM64 デバイスには ARM64 を選んでください。利用可能なプラットフォームは各リリースに記載されています。.NET ランタイムは同梱されています。

- **Windows:** **Installer** を実行します。ポータブル版は **Portable** ZIP 全体を書き込み可能なフォルダーに展開し、`Kgs.Client.Desktop.exe` を実行します。
- **Linux:** `chmod +x Kgs.Nova-linux-<architecture>.AppImage`（`x64` または `arm64`）で **AppImage** に実行権限を付けて起動します。更新できるよう、書き込み可能なフォルダーに保存してください。FUSE が必要です（Ubuntu 22.04 では `libfuse2`）。
- **macOS（提供されている場合）:** **Installer** を実行し、`KGS Nova.app` を開きます。ポータブル版は **Portable** ZIP 全体を展開し、アプリを書き込み可能な Applications フォルダーへ移動します。ビルドはアドホック署名で、Apple Developer ID 署名や公証はありません。ブロックされた場合は、ダウンロードを信頼できることを確認してから **システム設定 > プライバシーとセキュリティ** で Nova を許可してください。

**このアプリについて** で **更新の確認**、**更新のダウンロード**、**再起動して更新** を選びます。Nova は起動時にも更新を確認します。再起動前に対局を終え、作業を保存してください。アプリ内で更新できない場合は、新しいパッケージを手動でダウンロードします。

### Linux での手動インストール

`KGS-Nova-<version>-linux-<architecture>.tar.gz` を展開し、そのフォルダーから `./Kgs.Client.Desktop` を実行します。この形式では更新のたびに再ダウンロードが必要です。

Linux には X11 または XWayland、fontconfig、および .NET/Avalonia が使う X11 ライブラリが必要です。音声には PipeWire、PulseAudio、ALSA のいずれかを使います。パスワードの保存には libsecret（Debian/Ubuntu では `libsecret-1-0`）と GNOME Keyring などの Secret Service プロバイダーが必要です。

### 更新用ファイル

`.nupkg` と `releases.*.json` は Nova の更新機能用です。インストールには **Installer**、**Portable** ZIP、**AppImage** を使ってください。

## ログイン

既存の KGS 利用者名とパスワードでログインするか、ゲストとして続行します。アカウントを作成するにはログイン画面の登録リンクから KGS ウェブサイトを開きます。

## 対局と機能

対局から相手探しやカスタム対局を始めます。部屋で会話や観戦を行い、ユーザー一覧で相手を探します。表示／編集ではローカル学習用の SGF 棋譜を開けます。環境設定で外観や動作を調整します。

## ヘルプとポリシー

アプリの問題は [サポート]({% include page-url.html key='desktop/support' %})、望まれない交流や通報は [コミュニティガイドライン]({% include page-url.html key='desktop/community-guidelines' %}) をご覧ください。[プライバシーポリシー]({% include page-url.html key='global/privacy' %})、[利用規約]({% include page-url.html key='desktop/terms' %})、[共通コミュニティガイドライン]({% include page-url.html key='global/community-guidelines' %}) もお読みください。

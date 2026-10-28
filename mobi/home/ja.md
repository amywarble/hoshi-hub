---
layout: "localized"
title: "Mobi"
nav_title: "はじめに"
lang: "ja"
page_key: "mobi/home"
section: "mobi"
nav_order: 0
permalink: "/ja/gtp/"
source_revision: "b9d339585b5a920216045e5e3c1e6b45997754a2b3e257c811c18c8f9c33e4ca"
---

Mobi は Go Text Protocol（GTP）バージョン 2 に対応した囲碁エンジンを [KGS Go Server](https://www.gokgs.com/) に接続します。ログイン、対局相手の検索、着手、持ち時間、整地、復旧を処理します。囲碁エンジンは別途インストールして設定してください。

Mobi は、KGS および American Go Association (AGA) によって正式に承認されています。

## ダウンロードして始めましょう {#download-and-get-started}

x64 または ARM64 上の Windows または Linux の **Mobi GTP ブリッジ** アーカイブを [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) からダウンロードします。 .NET ランタイムが含まれています。 Windows パッケージは ZIP を使用します。 Linux パッケージは tar.gz を使用します。抽出したファイルをまとめて保管します。

- [ユーザーガイド]({% include page-url.html key='mobi/user-guide' %}): 最初のゲーム、設定、マッチメイキング、ログ、タイムアウト、リカバリ、トラブルシューティング。
- [Java クライアント アップグレード ガイド]({% include page-url.html key='mobi/upgrade-guide' %}): `kgsGtp.jar` および Java プロパティから TOML に移動します。
- [設定例]({{ '/mobi/bot.example.toml' | relative_url }}): `bot.toml` にコピーし、アカウント、エンジン パス、ゲーム設定を設定します。
- [利用規約]({% include page-url.html key='mobi/terms' %}): ボットの操作、エンジンのライセンス、Mobi を使用する際の責任。
- [コミュニティ ガイドライン]({% include page-url.html key='mobi/community-guidelines' %}): 正直なボット ID、フェア プレイ、およびサーバー リソースの責任ある使用。

共有された [プライバシー ポリシー]({% include page-url.html key='global/privacy' %}) および [アカウントとデータの削除]({% include page-url.html key='global/account-and-data-deletion' %}) ページには、Mobi 固有の情報が含まれています。

このガイドでは、Windows と PowerShell、および Linux と Bash をカバーしています。ご使用のオペレーティング システムのセクションを展開します。各アーカイブには、設定例と両方のガイドの英語のオフライン コピーも含まれています。

## クライアントを実行する {#run-the-client}

`bot.toml` を構成した後、抽出したディレクトリからこれらのコマンドを実行します。プローブは、KGS にログインせずにエンジンをチェックします。次のコマンドは、構成されたマッチメイキング設定を使用して 1 つのゲームをプレイします。

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

Ctrl+C を押して停止します。ユーザー ガイドを使用して、継続プレイを選択し、ログを保持し、アップグレード後もクライアント ID を保持します。

バグとドキュメントの修正については、[公開 GitHub 問題を開き](https://github.com/amywarble/hoshi-hub/issues/new/choose)、クライアントを **Mobi** として特定してください。クライアントとエンジンのバージョン、および関連する診断を含めます。パスワードやその他の機密情報は省略します。

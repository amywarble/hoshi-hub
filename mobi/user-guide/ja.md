---
layout: "localized"
title: "Mobi ユーザーガイド"
nav_title: "ユーザーガイド"
lang: "ja"
page_key: "mobi/user-guide"
section: "mobi"
nav_order: 1
permalink: "/ja/gtp/user-guide/"
source_revision: "26bf30c603841ace27c0d2ff994fd0d2297af607b506d24fd1ab9afabb8f1a33"
---

Mobi は、Go エンジンを KGS に接続して、自動的にプレイできるようにします。クライアントを端末で実行し、TOML 構成ファイルまたはコマンドライン オプションを通じて制御します。エンジンを個別にインストールして構成します。クライアントは、ログイン、ゲームの検索、移動、クロック、スコアリングを処理します。

Java `kgsGtp.jar` クライアントから移行しますか? [アップグレード ガイド]({% include page-url.html key='mobi/upgrade-guide' %}) から始めてください。

このガイドでは、Windows および Linux について説明します。オペレーティング システムのセクションを展開して、PowerShell または Bash コマンドを表示します。抽出されたクライアント ディレクトリからパッケージ化されたクライアントのサンプルを実行します。

- [最初のゲーム](#first-game)
- [構成の基本](#configuration-basics)
- [ゲームの選択](#choosing-games)
- [カスタムゲーム設定](#custom-game-settings)
- [ボットの実行](#running-the-bot)
- [タイムアウトとリカバリ](#timeouts-and-recovery)
- [トラブルシューティング](#troubleshooting)

## 最初のゲーム {#first-game}

登録済みの KGS アカウント、GTP バージョンの 2 エンジン、およびエンジンに必要な設定ファイルとモデル ファイルが必要です。ボットを開始する前に、通常の KGS クライアントを使用してアカウントを作成します。 Ranked プレイには追加のサーバー許可が必要です。 Free ゲームから始めます。

オペレーティング システムとアーキテクチャに応じたクライアント パッケージを抽出します。 x64 および ARM64 上の Windows および Linux 用のパッケージが提供されており、.NET ランタイムが含まれています。抽出したファイルをまとめて保管します。実行可能ファイルは、Windows では `Kgs.Gtp.exe`、Linux では `Kgs.Gtp` です。

### 1。構成を作成する {#1-create-your-configuration}

付属の [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) を `bot.toml` にコピーします。

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

`account.username`、`engine.executable`、および `engine.arguments` を編集します。たとえば:

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

エンジンが GTP モードに入るために必要なパスと引数を指定します。各配列要素は 1 つの引数です。スペースを含むパスも 1 つの要素です。

この例では、人間との Free 自動対戦、高速または中速、および連続プレイを選択します。アカウントに数値ランクがない場合は、`automatch.rank` を `30k` と `1k` の間の適切な推定値に設定します。 KGS は、アカウントのランクが利用可能な場合はそれを使用します。最初の実行では、以下のコマンドによりプレイが 1 つのゲームに制限されます。

### 2。エンジンをチェックする {#2-check-the-engine}

抽出したクライアント ディレクトリから、次を実行します。

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

クライアントはエンジン名、バージョン、サポートされているコマンドを出力して終了します。これには KGS 認証情報は必要なく、KGS には接続しません。 GTP の検出をチェックします。追加のルール、クロック、ハンディキャップ、スコアのチェックは、設定されたゲーム モードの開始時に実行されます。

### 3。パスワードを入力してプレイする {#3-supply-the-password-and-play}

パスワードは、`KGS_PASSWORD` 環境変数からのみ取得されます。

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

`Logged in to KGS`、次に `Game ready` を探します。クライアントはゲームをプレイし、自動的にスコアを付けます。 `Game finished` は、KGS の結果を記録します。 `Series: completed game 1` は、要求された合計にカウントされていることを確認します。その後、ログアウトして終了します。ゲームの検索はデフォルトで 5 分に制限されています。最大 1 時間まで許容するには、`--lobby-timeout 3600` を使用します。

## 構成の基本 {#configuration-basics}

必ず `--config` を使用してファイルを明示的に選択してください。クライアントは起動時にそれを 1 回読み取ります。再起動して、エンジン再起動設定の変更などの編集を適用します。自動構成ファイル検索やライブ リロードはありません。

コマンドライン オプションは、その実行のファイル値をオーバーライドします。たとえば:

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

ユーザー名は、`--username`、次に `account.username`、次に `KGS_USERNAME` となります。ファイルにパスワードフィールドを追加しないでください。拒否されます。

名前と選択には引用符で囲まれた文字列を、カウントと秒には整数を、コミには数値を、ブール値には `true` または `false` を使用します。テーブル名とキー名は大文字と小文字が区別されます。不明なキーと無効な値により、診断が行われて起動が停止します。このガイドのすべての期間は秒です。

`/` または `\` を含む相対 `engine.executable`、および相対 `account.clientIdFile` は、構成ファイルのディレクトリに対して相対的です。 `katago` などの裸の実行可能ファイル名では、実行可能ファイルの検索が使用されます。エンジン引数は変更されずに渡され、エンジンはクライアントを起動する作業ディレクトリを継承します。別のディレクトリから起動する場合は、モデルとエンジンの構成引数に絶対パスを使用します。一重引用符で囲まれた TOML 文字列では、Windows バックスラッシュが保持されます。文字列は環境変数を展開しません。

### アカウント、サーバー、エンジン {#account-server-and-engine}

| TOML設定 | CLI オプション | 意味とデフォルト |
| --- | --- | --- |
| `account.username` | `--username` | KGS アカウント名; `KGS_USERNAME` に戻ります。 |
| `account.clientIdFile` | `--client-id-file` | 永続的な ID ファイル。通常はサーバーとアカウントごとに選択されます。 |
| `server.host` | `--host` | KGS サーバー;デフォルトは `goserver.gokgs.com`。 |
| `server.port` | `--port` | TCPポート。デフォルトは `2379`、範囲は 1–65535。 |
| `engine.executable` | `--engine` | 起動するエンジン実行可能ファイル。 |
| `engine.arguments` | `--` の後の引数 | エンジン引数の配列。デフォルトは空です。 |
| `engine.stdio` | `--stdio` | エンジンを起動する代わりに、外部接続されたエンジンを使用します。デフォルトは `false`。 |
| `engine.rules` | `--engine-rules` | `kgs-rules` が不足しているエンジンでルールがすでに構成されています。デフォルト宣言はありません。 |

実行可能ファイルまたは `stdio = true` を選択し、両方を選択することはできません。標準 I/O では、別のプログラムがクライアントの stdin をエンジンの stdout に接続し、クライアントの stdout をエンジンの stdin に接続する必要があります。診断では stderr を使用します。このモードではエンジン引数を指定しないでください。

`engine.rules` は、`Japanese`、`Chinese`、`Aga`、または `NewZealand` を受け入れます。これはエンジンの既存のルールを宣言します。エンジン自体をそれに合わせて設定します。 `kgs-rules` を持つエンジンは、選択したゲームのルールを自動的に受け取ります。

コマンドラインで完全に設定するには、`--` の後にエンジン引数を置きます。

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

明示的な CLI エンジン引数は、ファイル配列全体を置き換えます。配列をクリアした後は何もない後続の `--`。 `--engine` および `--stdio` は、ファイルのエンジン接続の選択をオーバーライドします。 `--stdio` はファイルベースの引数も破棄します。 `--help` はすべてのオプションをリストし、`--version` はクライアントのバージョンを出力します。

## ゲームの選択 {#choosing-games}

マッチメイキング モードを 1 つ選択します:

| `matchmaking.mode` / `--lobby` | ボットが行うこと |
| --- | --- |
| `Automatch` | KGS で対戦相手を見つけてゲーム条件を選択しましょう。 |
| `Offer` | 指定されたルームでカスタム チャレンジを宣伝します。 |
| `Join` | 指定されたルームで一致するカスタム チャレンジを探します。 |

モードがない場合、クライアントはログインして停止するまで待機します。ゲームは見つかりません。 1 回の呼び出しで一度に 1 つのゲームがプレイされます。同時のカスタム チャレンジとオートマッチ、トーナメントへの参加、およびチャット返信は現在サポートされていません。

### Automatch {#automatch}

これらのセクションをアカウントとエンジンの設定と一緒に使用してください。

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

Automatch モードでは、`matchmaking.room`、`opponent`、`opponentPolicy`、`challengeNotes`、および `game` と `timing` の各セクションを省略してください。これらは個別対局申込用の設定で、値が既定値と同じでも自動マッチングとは併用できません。

| TOML設定 | CLI オプション | 選択肢とデフォルト |
| --- | --- | --- |
| `automatch.speed` | `--automatch-speed` | `All` (デフォルト)、`Blitz`、`Fast`、`Medium`、または `["Fast", "Medium"]` などの配列。 CLI の組み合わせではカンマを使用します。 |
| `automatch.rank` | `--automatch-rank` | 推定 `30k` ～ `1k`。アカウントに数値のサーバー ランクがない場合に必要です。 |
| `automatch.opponents` | `--automatch-opponents` | `Humans` (デフォルト)、`Robots`、または `Any`。 |
| `automatch.maxRankDifference` | `--automatch-max-rank-difference` | デフォルトは `0`。範囲は 0–9 (Free の場合)、0–6 (Ranked の場合)。 |

Automatch は日本ルールの公開 19×19 対局で、黒白はサーバーが決めます。互先のコミは 6.5 です。ランク差を許可するとコミが 0.5 になる場合があり、二段階以上の差では固定配置の置き石が使われます。

| 速度 | プレイヤーごとのメインタイム | 日本語びょう読み |
| --- | --- | --- |
| `Blitz` | 60 秒 | 3 期間 10 秒 |
| `Fast` | 600 秒 | 5 期間 20 秒 |
| `Medium` | 1500 秒 | 5 期間 30 秒 |

エンジンは `final_status_list`、`kgs-time_settings`、および `time_left` をサポートする必要があります。ハンディキャップを許可するには、`set_free_handicap` も必要です。 `kgs-rules` がない場合は、日本語ルール用に構成し、`engine.rules = "Japanese"` を設定します。

### カスタムチャレンジ {#custom-challenges}

サンプル ファイルの `matchmaking` セクションと `automatch` セクションをカスタム プロファイルに置き換えます。この例では、公開 19×19 Free ゲームを資格のあるプレイヤーに提供します。

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

KGS に示されている部屋の名前を使用します。名前にはスペースや非 ASCII 文字が含まれる場合があります。ルックアップでは、ログイン後と再接続後に、大文字と小文字を区別しない完全一致が使用されます。名前が欠落しているかあいまいな場合、クライアントは診断で停止します。

特定の対戦相手 1 人の場合、`opponentPolicy` を `"Named"` に変更し、`opponent = "OtherAccount"` を追加します。 `Any` の場合は、`opponent` を省略します。対象となるオープンな対戦相手は、このボット以外の登録済みアカウントに接続されています。人間もロボットも対象となります。

チャレンジに参加するには、`mode = "Join"` を使用し、`challengeNotes` を削除します。ルール、コミ、ハンディキャップ、可視性、クロックなど、すべてのゲーム用語が一致する必要があります。ボット独自の色を選択します。黒をプレイする Offer ボットには、白をプレイする Join ボットが必要です。ランダムな色の場合は両方とも `"Nigiri"` を使用します。条件の変更は黙って受け入れられません。

| TOML設定 | CLI オプション | 選択肢とデフォルト |
| --- | --- | --- |
| `matchmaking.mode` | `--lobby` | `Offer`、`Join`、または `Automatch`;デフォルトモードはありません。 |
| `matchmaking.gameType` | `--game-type` | `Free` (デフォルト) または `Ranked`。 |
| `matchmaking.opponentPolicy` | `--opponent-policy` | `Named` (カスタム チャレンジのデフォルト) または `Any`。 |
| `matchmaking.opponent` | `--opponent` | `Named` では必須。アカウント名では大文字と小文字が区別されません。 |
| `matchmaking.room` | `--room` | Offer および Join には必須の部屋名。たとえば、`"Computer Go"`。 |
| `matchmaking.games` | `--games` | デフォルトは `1`。シリーズの場合は正の数、連続再生の場合は `0`。 |
| `matchmaking.challengeNotes` | `--challenge-notes` | Offer のみ。最大 255 文字 (制御文字は除く)。省略すると相手のノートが生成されます。 |

### Ranked ゲーム {#ranked-games}

`matchmaking.gameType = "Ranked"` を設定して、Ranked ゲームを排他的にリクエストします。アカウントには、サーバーによって付与された `RankedRobot` 権限とランクが有効になっている必要があります。 KGS サーバー管理者にその権限を依頼してください。未設定のランク (`?`) は許可されますが、無効なランク (`-`) は許可されません。アカウントに数値ランクがない場合でも、自動一致では推定が必要です。

Ranked の相手は登録済みでランク機能が有効なアカウントで、アマチュアランクまたは未確定ランクである必要があります。ロボットの相手には `RankedRobot` 権限も必要です。個別条件の Ranked 対局には、公開部屋、公開の 19×19 対局、最大六子、コミ −10 から 10、一人あたり推定 450 秒超の持ち時間が必要です。推定には秒読みを含み、時間無制限も認められます。600 秒の Absolute 設定は時間条件を満たします。不適切な設定や、サーバーによる Free への変更は拒否します。

## カスタムゲーム設定 {#custom-game-settings}

これらの設定は、Offer および Join に適用されます。それらを Automatch 構成から除外します。

| TOML設定 | CLI オプション | 選択肢とデフォルト |
| --- | --- | --- |
| `game.boardSize` | `--board-size` | デフォルトは `9`。範囲は 2–25、エンジンのサポートの対象となります。 |
| `game.rules` | `--rules` | `Chinese` (デフォルト)、`Japanese`、`Aga`、または `NewZealand`。 |
| `game.komi` | `--komi` | デフォルトは `7.5`。 −100～100（半点単位） |
| `game.color` | `--color` | `Black`、`White`、または `Nigiri`;デフォルトは、Offer の場合は黒、Join の場合は白です。 |
| `game.handicap` | `--handicap` | デフォルトは `0`。それ以外の場合は、ボードの配置制限内の 2–9。にぎりとの併用はできません。 |
| `game.private` | `--private` | デフォルトは `false`。選択したルームでアドバタイズされたチャレンジを維持しながら、プライベート ゲームが必要です。 |

置き石を設定してもコミは自動調整されません。両方を明示してください。日本ルールと AGA ルールは固定配置で、盤は最低 7×7、7×7 または一辺が偶数の盤では最大四子です。中国・ニュージーランドルールは自由配置で、最大九子、少なくとも一つの空点が必要です。置き碁には `set_free_handicap` が必要で、自由配置の黒番では `place_free_handicap` も必要です。

### 時間制御 {#time-controls}

| TOML設定 | CLI オプション | デフォルトと範囲 |
| --- | --- | --- |
| `timing.system` | `--time-system` | `Absolute` (デフォルト)、`None`、`Canadian`、または `ByoYomi`。 |
| `timing.mainTime` | `--main-time` | デフォルトは `600`、またはなしの場合は `0`。範囲は0–86400。 |
| `timing.byoYomiTime` | `--byo-yomi-time` | デフォルトは `0`。延長戦を使用する場合は、日本の期間またはカナダのブロックごとに 1–86400。 |
| `timing.byoYomiPeriods` | `--byo-yomi-periods` | デフォルトは `0`。 ByoYomi の 1–255。 |
| `timing.canadianStones` | `--canadian-stones` | デフォルトは `0`。カナダの場合は 1–255。 |

日本の延長戦の場合、メインタイムは 10 分、30 秒のピリオドが 5 回あります。

```toml
[timing]
system = "ByoYomi"
mainTime = 600
byoYomiTime = 30
byoYomiPeriods = 5
```

カナダの延長戦の場合、ブロックあたりの秒数には `system = "Canadian"`、`byoYomiTime`、ブロックあたりのストーン数には `canadianStones` を使用します。 `byoYomiPeriods` は省略します。秒読みによりメインタイムはゼロになります。 Absolute ではプラスのメインタイムが必要であり、秒読みはありません。いずれの場合も、明示的に指定されたすべての時間値がゼロである必要はありません。総クロック リザーブもサーバーの範囲に適合する必要があります。無効な組み合わせが報告されます。

時間制限のあるゲームには、`time_left` と、`time_settings` または `kgs-time_settings` のいずれかが必要です。日本の秒読みには特に `kgs-time_settings` が必要です。無制限のゲームにはクロック コマンドは必要ありません。エンジンの応答タイムアウトはゲームのクロックとは別のものであり、ボットにそれ以上のプレイ時間を与えることはありません。

## ボットの実行 {#running-the-bot}

`matchmaking.games` を正の合計に設定するか、プレイを続けるには `0` に設定します。 KGS で確認された結果のみがカウントされます。ゲームが完了すると、クライアントはゲームを終了し、次のゲームでは元のマッチメイキング設定を使用します。失敗したゲームまたは未完成のゲームは、完了したものとしてカウントされるのではなく、シリーズを停止します。

ゲーム間の待ち時間を長くして継続的にプレイする場合:

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

Ctrl+C を押して停止します。クライアントはログアウトし、エンジンに終了を要求し、必要に応じて起動したエンジンを停止します。試合中に止めても最終結果は確定しません。次の実行を開始する前に、未完了のゲームを確認してください。

### ログと終了コード {#logs-and-exit-codes}

ステータス、エラー、ヘルプ、およびエンジン診断は、stderr に移動します。それらを保持するには:

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

ログローテーションにはサービスマネージャーまたは外部ツールを使用してください。標準 I/O モードでは、stdout をエンジンに接続したままにします。 GTP コマンドを実行します。

| 終了コード | 意味 |
| --- | --- |
| `0` | 要求されたゲームが完了したか、プローブ/ヘルプ/バージョン コマンドが成功しました。 |
| `1` | 構成または実行時のエラー。診断を検査します。 |
| `130` | Ctrl+C を含む演算子のキャンセル。 |

### 永続的な状態と既存のゲーム {#persistent-state-and-existing-games}

クライアントは、KGS によって割り当てられた ID を保存します。マッチメイキング モードでは、デフォルト ファイルは .NET のローカル アプリケーション データ ディレクトリ (`Kgs.Gtp/identities/<server-and-account-hash>`) にあります。 Windows では、これは通常 `%LOCALAPPDATA%` を下回ります。安定した書き込み可能な場所を選択するには、`account.clientIdFile = "./state/client-id"` を設定します。アップグレードやコンテナの交換後も保持します。サーバーとアカウントごとに別のファイルを使用します。

Offer と Join は、まず、選択されたルームで、このアカウントに属する未完成のゲームがないかどうかを確認します。再開できる互換性のあるゲームは 1 つだけです。対戦相手と完全なプロフィールが一致する必要があります。複数のゲームまたは不一致のゲームが起動を停止します。アーカイブされたゲームは自動的にロードされません。

実行中のオートマッチ セッションは、接続が失われた後に割り当てられたゲームを回復できます。新しいプロセスでは、古いオートマッチ ゲームは自動的に検出されません。再登録する前に、未完了のオートマッチ ゲームを解決してください。

### テイクバック、ポーズ、相手の不在 {#takebacks-pauses-and-opponent-absence}

`undo.free` / `--undo-free` と `undo.ranked` / `--undo-ranked` は、それぞれ独立して `Never`（既定）または `Allow` を指定できます。付属例は Free の待ったを許可し、Ranked では拒否します。Allow は通常の対局中、サーバーが認める相手の申請を受け入れます。ボット自身は待ったを申請しません。その後、確定した棋譜を再現するため、エンジンの GTP `undo` 対応は不要です。整地の異議による対局再開は、この設定とは別です。

KGS は、一時停止、延期、再開を制御します。一時停止または中断している間、ボットは新しいゲームプレイやスコアリング アクションを開始しません。連続的な一時停止、延期、対戦相手の不在にはそれぞれ個別の制限があり、デフォルトは 300 秒です。

| TOML の `[interactions]` 設定 | CLI オプション |
| --- | --- |
| `pauseTimeoutFree` | `--pause-timeout-free` |
| `adjournmentTimeoutFree` | `--adjournment-timeout-free` |
| `opponentTimeoutFree` | `--opponent-timeout-free` |
| `pauseTimeoutRanked` | `--pause-timeout-ranked` |
| `adjournmentTimeoutRanked` | `--adjournment-timeout-ranked` |
| `opponentTimeoutRanked` | `--opponent-timeout-ranked` |

それぞれ 1–86400 秒を受け入れます。期限切れはコード 1 でクライアントを停止し、ゲームは未完了のままになります。終了したり、別のゲームを開始したりすることはありません。再接続やエンジンの交換では、これらの待機はリセットされません。他のアクティブな期限は、より早く期限切れになる可能性があります。対戦相手がいない間でも、KGS が許可すればボットは移動することができます。

## タイムアウトとリカバリ {#timeouts-and-recovery}

### 通常のタイムアウト {#normal-timeouts}

すべて 1–86400 秒を受け入れます:

| TOML設定 | CLI オプション | デフォルト | 限界 |
| --- | --- | --- | --- |
| `timeouts.login` | `--login-timeout` | `30` | 接続とログイン。 |
| `timeouts.lobby` | `--lobby-timeout` | `300` | 1 つのチャレンジ ネゴシエーションまたはオートマッチ登録。部屋名の検索も制限します。 |
| `timeouts.move` | `--move-timeout` | `600` | 1 つの通常またはクリーンアップ エンジン検索。 |
| `timeouts.scoring` | `--scoring-timeout` | `120` | 評価と同意を含む 1 回の採点ラウンド。 |
| `timeouts.cleanup` | `--cleanup-timeout` | `300` | すべてのクリーンアップの試みとその後の得点をまとめて記録します。 |

### KGS 接続損失 {#kgs-connection-loss}

クライアントはトランスポートの失敗を再試行し、再度認証し、サーバー履歴を使用して中断されたゲームに再参加します。不確実な手を再送信したり、中断された既知のゲームを新しい挑戦に置き換えたりすることはありません。ログインの拒否、サーバーのログアウト、無効なサーバー データ、不正なエンジンの移動、および拒否されたエンジン コマンドは端末障害です。

| TOML設定 | CLI オプション | デフォルトと範囲 |
| --- | --- | --- |
| `connectionRecovery.attempts` | `--reconnect-attempts` | 停止ごとのオプションの上限。 0–100。デフォルトでは省略されます。ゼロは再試行を無効にします。 |
| `connectionRecovery.delay` | `--reconnect-delay` | `1` - 2 番目の初期ウィンドウ。 0–30、30 秒の上限に倍増、フル ジッター。 |
| `connectionRecovery.timeout` | `--recovery-timeout` | ゲームの再接続による再接続あたり `120` 秒。 1–86400。 |
| `connectionRecovery.budget` | `--recovery-budget` | `180` 秒ごとの停止ごとの合計 (ドレイン、バックオフ、ログイン、再参加を含む)。 1–86400。 |
| `connectionRecovery.resetAfter` | `--recovery-reset-after` | `60` 再接続後、バジェットと再試行回数をリセットするまでの正常な秒数。 1–86400。 |
| `connectionRecovery.engineDrainTimeout` | `--engine-drain-timeout` | 古いエンジンの作業を終了して破棄するのに `30` 秒。 1–86400。 |

停止バジェットは、接続損失が検出されたときに開始されます。すべての再接続は、残りの予算と独自のログイン/再参加タイムアウトによって制限されます。各バックオフ遅延は、ゼロと、1 秒から 30 秒の上限までの 2 倍の上限との間でランダムに選択されます。合計予算または明示的な試行上限がなくなると、リカバリは停止します。

再接続後、ボットは古い回復期限を超えてプレイを続けることができます。その後の切断では、60 の正常な秒数後に新しいバジェットが取得されます。その間隔より前に切断すると、短時間の接続時間を含む、以前の期限と再試行回数が保持されます。ゲームに再参加する必要がある場合、ログインだけでは正常性が確立されません。

### エンジン故障 {#engine-failure}

実行中のエンジンが終了するか、そのストリームが使用できなくなると、クライアントは KGS セッションをアクティブなままにし、元の実行可能ファイルと引数を使用して置換を開始しようとします。続行する前に、置換をチェックし、確認された履歴を再生します。初期のエンジン起動/検出に失敗すると、クライアントが停止します。エンジンが利用できない間も、KGS クロックは継続します。

| TOML設定 | CLI オプション | デフォルトと範囲 |
| --- | --- | --- |
| `engineRecovery.attempts` | `--engine-restart-attempts` | `3` 呼び出し全体での自動置換。 0–100。ゼロはオペレーターの回復を待ちます。 |
| `engineRecovery.delay` | `--engine-restart-delay` | `1` - 2 番目の初期ウィンドウ。 0–30、30 秒の上限に倍増、フル ジッター。 |
| `engineRecovery.timeout` | `--engine-recovery-timeout` | 検出/セットアップと個別の再生に `120` 秒。 1–86400。 |
| `engineRecovery.pipe` | `--engine-recovery-pipe` | ローカル回収パイプ。デフォルトは `kgs-gtp-<process ID>`。 1–100 ASCII 文字、数字、ピリオド、ハイフン、またはアンダースコアを使用します。 |

自動置換がなくなると、診断はローカル回復パイプに名前を付けます。通常のゲームとロビーの期限が続く間、ボットはオペレーターの介入を待ちます。クライアントによって起動されたエンジンを再起動するには、同じオペレーティング システム ユーザーとして接続し、UTF-8 `restart` に続いて LF を送信します。たとえば、`pipe = "YourBot-recovery"` を構成した場合は、待機中の診断の後に別の端末でこれを実行します。

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

Linux の例では、Python 3 が必要で、.NET の Unix ドメイン ソケットに接続します。ボットと同じ `TMPDIR` を使用して、同じユーザーとして実行します (デフォルトは `/tmp`)。 `YourBot-recovery` を構成されたパイプ名に置き換えます。プライベート一時ディレクトリを持つサービスでは、クライアントも同じ環境内で実行する必要があります。

オペレーターの置き換えが成功すると、新しい自動再試行バジェットが開始されます。 TOML ファイルを編集しても、実行中のクライアントの実行可能ファイルや引数は変更されません。

`--stdio` の場合、外部スーパーバイザは二重リカバリ パイプを介して新しいエンジンを接続し、GTP を両方向に中継する必要があります。このモードでは、`restart` グリーティングはありません。元の stdin/stdout 接続は、失敗後に再利用できません。

## トラブルシューティング {#troubleshooting}

| 症状 | 何を確認するか |
| --- | --- |
| エンジン始動前の設定エラー | 名前付きファイルとソースの場所、キーの正確なスペル、引用符で囲まれたルーム名、および TOML 値のタイプを確認してください。レガシー Java プロパティ ファイルは変換する必要があります。 |
| エンジンが始動できない、またはモデルを開くことができない | 実行可能ファイルと引数のパス、GTP モードの引数、および作業ディレクトリを確認してください。 `--probe` を試してください。 |
| GTP コマンドが欠落しているか、プロトコルのバージョンが間違っています | GTP v2 に完全対応したエンジンを使用してください。機能検出には `protocol_version`、`name`、`version`、`known_command`、`list_commands`、`quit`、`boardsize`、`clear_board`、`komi`、`play`、`genmove` が必要です。 |
| ルール、タイミング、スコアのチェックに失敗する | 選択したプロファイルのエンジン機能を確認します。エンジンに `kgs-rules` がない場合にのみ `engine.rules` を宣言し、実際の構成を一致させます。すべての自動ゲームには `final_status_list` が必要です。 |
| ログインに失敗する | 起動環境のアカウント名 `KGS_PASSWORD`、サーバー アドレス、報告された拒否理由を確認します。 |
| 部屋が見つかりません | 選択したサーバー上の KGS からフルネームをコピーします。照合では大文字と小文字は区別されませんが、名前全体が必要です。 |
| ゲームまたはロビーのタイムアウトを待っています | マッチング条件、対戦相手の資格、ルーム名、オートマッチ設定を確認します。待機時間を長くする場合は、`timeouts.lobby` を増やします。 |
| Ranked エントリが拒否されました | RankedRobot 権限、有効なランク、パブリック ルーム、および Ranked プロファイル制限を確認します。 |
| 意見が一致しない場合は得点が停止される | 日本の紛争は支持されない。中国、AGA、ニュージーランドのクリーンアップには `kgs-genmove_cleanup` が必要です。繰り返される紛争、進捗の欠如、クリーンアップの有効期限が切れると、クライアントは停止します。 |
| 一時停止または相手の離脱後にボットが停止する | 関連するインタラクション タイムアウトを確認し、再起動する前に未完了のゲームを検査します。 |
| エンジンは利用できませんが、アカウントはオンラインのままです | エンジン診断とリカバリ パイプ メッセージを検査します。自動再試行が使い果たされる可能性があります。ゲームの時計と締め切りはまだ続いています。 |
| IDファイルエラー | 構成された状態の場所が書き込み可能であり、クライアントが生成した ID ファイルが含まれていることを確認してください。 |

問題を報告するときは、クライアントのバージョン、エンジン名/バージョン、可能な場合はゲーム ID、関連する設定、および stderr 診断を含めてください。パスワードを省略します。

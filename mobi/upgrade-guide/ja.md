---
layout: "localized"
title: "Java GTP クライアントから Mobi にアップグレードします。"
nav_title: "Java 版からの移行"
lang: "ja"
page_key: "mobi/upgrade-guide"
section: "mobi"
nav_order: 2
permalink: "/ja/gtp/upgrade-guide/"
source_revision: "c32ebab17d841776f058eab0acfe73c12237c6953d8b7f6ec6630c41d26de6f1"
---

このガイドでは、ボットを `kgsGtp.jar` とその Java `.properties` 構成から Mobi および TOML に移動します。古いファイルを直接ロードすることはできません。自動インポーターはありません。新しいファイルを作成する際の参照用に保管してください。通常の操作と完全な設定のリファレンスについては、[ユーザー ガイド]({% include page-url.html key='mobi/user-guide' %}) を参照してください。

このガイドでは、Windows および Linux について説明します。オペレーティング システムのセクションを展開して、PowerShell または Bash コマンドを表示します。抽出したクライアント ディレクトリからコマンドを実行します。

## アップグレード手順 {#upgrade-steps}

1. 現在のゲームを終了または解決してから、古いクライアントとそのエンジンを停止します。    交換を試行している間は自動再起動を無効にして、両方のクライアントが同じアカウントでログインしないようにします。
2. Windows または Linux アーキテクチャの Mobi GTP ブリッジ パッケージを抽出します。    パッケージには .NET ランタイムが含まれています。エンジン、モデル、エンジン構成を保持します。これらはクライアントから分離されたままになります。
3. [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) を `bot.toml` にコピーします。以下の表を使用して設定を移動します。 `KGS_PASSWORD` にパスワードを入力し、ゲーム タイプ、テイクバック ポリシー、およびゲーム数を明示的に選択します。
4. 以下のコマンドを使用してエンジンを調べます。ログインする前にエンジン検出エラーを修正します。通常の起動時に追加のゲーム機能チェックが実行されます。
5. `--games 1` を使用して Free ゲームを 1 つ実行します。ログイン、対戦相手の選択、クロック、スコアリング、および `Series: completed game 1` 診断を確認します。
6. 継続的にプレイしたい場合は、`games = 0` を設定し、新しい実行可能ファイル、構成パス、パスワード環境、およびログを使用するようにランチャーまたはサービスを更新します。

テンプレートをコピーし、アカウント、エンジン パス、およびゲーム設定を編集します。

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

編集後、ログインせずにエンジンの検出を確認します。

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

古いクライアントに戻るには、まず新しいクライアントとエンジンを停止し、未完成のゲームを調べて、元のランチャーとプロパティ ファイルを復元します。新しいクライアントの ID ファイルは、後で Mobi に戻るために保管しておいてください。

## 切り替える前に確認すべき変更点 {#changes-to-review-before-switching}

| エリア | 古いクライアント | Mobi |
| --- | --- | --- |
| 打ち上げ | `java -jar kgsGtp.jar bot.properties key=value` | `Kgs.Gtp --config bot.toml --option value`; Windows 実行可能ファイルは `.exe` で終わります。 |
| 構成 | Java エスケープを含む Java プロパティ | UTF-8 TOML 名前付きセクション、引用符で囲まれた文字列、数値、配列、およびブール値。不明なキーはエラーです。 |
| デフォルトモード | Automatch | `matchmaking.mode` または `--lobby` が選択されない限り、マッチメイキングは行われません。 |
| ゲーム数 | ゲームを探し続けます | 組み込みのデフォルトは 1 つの完了したゲームです。連続再生するには `games = 0` を設定します。提供された例ではすでにこれが行われています。 |
| ゲームの種類 | Automatch では、Free と Ranked を一緒に使用できます | `Free` (デフォルト) または `Ranked` を排他的に選択します。混合設定やフォールバックはありません。 |
| 部屋 | 部屋名 | 部屋名、まだ文字列です。 `room = "English Room"`を使用してください。ルックアップでは大文字と小文字が区別されず、正確な名前が必要です。 |
| カスタムゲーム規約 | プレイヤーは変更を提案することができます | 設定された用語は、色、コミ、ハンディキャップ、可視性、時間制御など、正確に一致する必要があります。 |
| テイクバック | 通常、Free ゲームでは許可されますが、Ranked では拒否されます | 両方の組み込みポリシーのデフォルトは `Never` です。通常の Free の動作を維持するには、`undo.free = "Allow"` を設定します。この例ではこれを実行します。 |
| Automatch ハンディキャップ | エンジンがハンディキャップをサポートしている場合、最大 9 ランクまで許可される可能性があります | `maxRankDifference` のデフォルトは `0` です。明示的に選択してください。最大でも Free の場合は 9、または Ranked の場合は 6 です。 |
| 接続の再試行 | `reconnect=t` は継続的な再試行を有効にします | デフォルトの 180 秒の停止予算、ジッターを伴う指数バックオフ、および 60 の正常な秒数後のリセット。 |
| エンジン故障 | `reconnect` からのエンジンの自動再始動はありません | 個別の自動再起動予算。通常の締め切りが続く間、疲労困憊してオペレーターの回復を待ちます。 |
| 相手の退場 | 欠席制限後にマッチメイキングに戻る可能性がある | 新しいクライアントは、設定された待機時間が経過すると、未完了ゲームの診断を表示して停止します。 |

この例は開始時の構成であり、古い動作がすべて維持されるという主張ではありません。特に、連続操作を有効にする前に、このアカウントで Free と Ranked のどちらをプレイするかを決定してください。

## 古い設定をマッピングする {#map-the-old-settings}

以下の新しい設定名では、`section.key` 表記が使用されます。たとえば、`account.username` は、`[account]` の下の `username = "YourBot"` を意味します。

### アカウント、接続、エンジン {#account-connection-and-engine}

| 古い物件 | 新しい設定 | 移行メモ |
| --- | --- | --- |
| `name` | `account.username` / `--username` | ユーザー名が設定されていない場合は、`KGS_USERNAME` もサポートされます。 |
| `password` | 環境変数 `KGS_PASSWORD` | 新しい構成からそれを削除します。パスワードフィールドとパスワード CLI オプションはサポートされていません。 |
| `server.host` | `server.host` / `--host` | 文字列;デフォルトは `goserver.gokgs.com`。 |
| `server.port` | `server.port` / `--port` | 整数;デフォルトは `2379`。 |
| `reconnect=f` | `connectionRecovery.attempts = 0` | KGS トランスポートの再試行を無効にします。エンジン回復は個別に設定されます。 |
| `reconnect=t` | `[connectionRecovery]` | 停止ごとの時間予算を選択します。デフォルトは 180 秒です。試行回数の上限はオプションです。 |
| `engine` | `engine.executable` および `engine.arguments` | コマンドを実行可能ファイルと個別の引数に分割します。以下を参照してください。 |
| エンジン接続プロパティがありません | `engine.stdio = true` / `--stdio` | 標準 I/O を明示的に選択する必要があります。 |
| `gtp.in`, `gtp.out` | 直接設定はありません | 外部ランチャーは、`--stdio` を介して 2 方向を接続できます。クライアントは、構成から名前付きファイルまたは FIFO を開きません。 |
| `engine.port` | 直接設定はありません | エンジン TCP リスナーはありません。 `--stdio` で外部アダプターを使用するか、クライアントにエンジンを起動させます。 |
| `logFile` | stderrを外部からキャプチャする | シェル リダイレクトまたはサービス マネージャーを使用します。組み込みの Java ログの名前付けとローテーションは引き継がれません。 |
| `verbose` | 直接設定はありません | 通常の診断は stderr に進みます。同等の完全な GTP/サーバー トラフィック ロギング スイッチはありません。 |

ローカル `engineRecovery.pipe` は、実行中のセッションで障害が発生したエンジンを交換するためのものです。古い `engine.port`、`gtp.in`、または `gtp.out` の起動設定は置き換えられません。

### マッチメイキングとゲーム設定 {#matchmaking-and-game-settings}

| 古い物件 | 新しい設定 | 移行メモ |
| --- | --- | --- |
| `mode=auto` | `matchmaking.mode = "Automatch"` | ルーム、カスタム対戦相手設定、および `game`/`timing` セクションを省略します。 |
| `mode=custom` | `matchmaking.mode = "Offer"` | オープンチャレンジの場合は `opponentPolicy = "Any"` を追加するか、`"Named"` と `opponent` を追加します。 |
| `mode=wait` | `matchmaking.mode = "Join"` | ルーム名と `opponent` を設定します。提供されたプロファイルは正確に一致する必要があります。 |
| `mode=both` | 複合モードなし | この呼び出しには、Automatch、Offer、または Join を選択します。 |
| `mode=tournament` | サポートされていません | トーナメントへのエントリーは実装されていません。必要な場合は、古いクライアントを保持してください。 |
| `room` | `matchmaking.room` / `--room` | ルーム名を引用符で囲んだ文字列として保持します。 Offer および Join には必須。 Automatch の場合は省略します。最後に使用した部屋のデフォルトはありません。 |
| `opponent` | `matchmaking.opponent` | カスタム チャレンジの場合は、`opponentPolicy = "Named"` を使用します。 Automatch の両方のカスタム対戦相手設定を省略します。 |
| `gameNotes` | `matchmaking.challengeNotes` | Offer のみ。制御文字を除く最大 255 文字。 |
| `rules` | `game.rules` | `Japanese`、`Chinese`、`Aga`、または `NewZealand` を使用します。正確なカスタム ゲーム条件を設定します。 |
| `komi` | `game.komi` | 引用符で囲まれた文字列ではなく数値。ハンディキャップ ゲームを含め、明示的に設定されます。 |
| `rules.boardSize` | `game.boardSize` | 整数。明示的に設定します。新しいカスタム ゲームのデフォルトは 9 です。 |
| `rules.time` | `[timing]` | 以下の例を使用して、システム、秒、および時間外フィールドに分割します。 |
| `automatch.speed` | `automatch.speed` | たとえば、`speed = ["Blitz", "Medium"]`、または `"All"`。 CLI の組み合わせではカンマを使用します。 |
| `automatch.rank` | `automatch.rank` | `30k` から `1k` まで引用されます。数値によるサーバー ランクがない場合でも必要です。 |
| `undo=f` | `[undo]` と `free = "Never"`、`ranked = "Never"` | これらは組み込みのデフォルトでもあります。 |
| `undo=t` または省略 | `[undo]` と `free = "Allow"`、`ranked = "Never"` | 通常の古い Free/Ranked の区別を保持します。必要に応じて、新しい Ranked テイクバックを個別に有効にすることができます。 |
| `talk` | サポートされていません | プライベート チャットの返信とエンジン チャットの転送は実装されていません。 |
| `hint.cleanup`, `hint.noArguing` | サポートされていません | 論争のスコアリングに関する構成可能なチャット ヒントはありません。 |

`game.rules` と `engine.rules` は目的が異なります。前者はカスタム ゲームのルールを選択します。後者は、`kgs-rules` のないエンジンですでに構成されているルールを宣言します。そのエンジンの構成は変更されません。

### エンジンコマンドを分割する {#split-the-engine-command}

古いプロパティは次のようなものです。

```properties
engine=/opt/katago/katago gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

新しい構成は次のとおりです。

```toml
[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]
```

コマンドライン全体を `executable` に入力しないでください。シェル評価はありません。各引数は、スペースを含むパスを含む 1 つの配列要素です。 Windows の場合、一重引用符で囲まれた TOML 文字列はバックスラッシュをリテラルに保ちます。

```toml
[engine]
executable = 'C:\Go Engines\katago.exe'
arguments = ["gtp", "-config", 'C:\Go Engines\gtp.cfg', "-model", 'C:\Go Engines\model.bin.gz']
```

Java プロパティのエスケープを UTF-8 TOML の実際のテキストに置き換えます。区切り文字を含む実行可能相対パスは、TOML ディレクトリから解決されます。引数のパスは起動作業ディレクトリに対する相対パスのままです。絶対モデルと構成パスにより、サービスの起動の再現が容易になります。

### 変換時間コントロール {#convert-time-controls}

これらの `[timing]` セクションの 1 つだけを使用し、Offer または Join とともにのみ使用します。

古い `rules.time=0`:

```toml
[timing]
system = "None"
mainTime = 0
```

古い `rules.time=30:00`:

```toml
[timing]
system = "Absolute"
mainTime = 1800
```

古い `rules.time=30:00+5x0:30`:

```toml
[timing]
system = "ByoYomi"
mainTime = 1800
byoYomiTime = 30
byoYomiPeriods = 5
```

古い `rules.time=30:00+25/10:00`:

```toml
[timing]
system = "Canadian"
mainTime = 1800
byoYomiTime = 600
canadianStones = 25
```

新しい時間値はすべて整数の秒です。別のシステムに属する超過勤務フィールドを削除します。日本の延長戦にはエンジンの `kgs-time_settings` コマンドが必要です。別のクロック システムを使用して近似されることはありません。

## 例: 自動一致ボットを移行する {#example-migrate-an-automatch-bot}

古いファイルの関連部分が次のとおりであるとします。

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

初期 Free ゲーム用にこの `bot.toml` を作成します。 Automatch は部屋設定を必要としないため、古い `room` プロパティは省略されます。

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

Windows の場合、`[engine]` パスを [エンジン コマンドの分割](#split-the-engine-command) の Windows の例に置き換えます。パスワードを設定し、ゲームを 1 つ実行します。

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

この例では、Free ゲームさえも意図的に選択しています。ハンディキャップのマッチングを維持するには、適切な `maxRankDifference` を選択し、エンジンのサポートを確認してください。 Ranked をプレイするには、`gameType = "Ranked"` を選択し、アカウントの RankedRobot 権限と有効なランクを確認し、最大 6 ランクの差を使用します。 1 つの呼び出しで両方のゲーム タイプを受け入れることはできません。

カスタム ボットの場合は、[カスタム チャレンジの例]({% include page-url.html key='mobi/user-guide' %}#custom-challenges) を使用し、古いルーム名をコピーし、ボード サイズ、ルール、コミ、カラー、ハンディキャップ、変換時間の設定を明示的に転送します。

## エンジンの互換性と無人運転 {#engine-compatibility-and-unattended-operation}

Mobi には、GTP v2 とその完全な必須コマンド セットが必要です。古いクライアントではオプションとして扱われていたいくつかのコマンドがここで必要になります。すべての自動ゲームには `final_status_list` も必要です。時間制限のあるゲームには、`time_left` とサポートされているタイミング コマンドが必要です。選択したプロファイルのユーザー ガイドのエンジン要件を確認してください。古い動作設定だけでは互換性は確立されません。

通常の日本の得点協定はサポートされますが、未解決の日本の紛争によりゲームが停止します。中国、AGA、およびニュージーランドのクリーンアップには `kgs-genmove_cleanup` が必要で、試行回数と合計期限が制限されています。自動得点が利用できない場合に、対戦相手がすべての死石を決定できるようにする古いクライアントのフォールバックはありません。

ボットを放置する前に、次のサービス設定を確認してください。

- 再生を継続する必要がある場合は、`games = 0` を明示的に設定します。各ロビーの試行には、デフォルトの 300 秒の期限がまだあります。必要に応じて、`timeouts.lobby` を増やします。
- KGS 接続の再試行とエンジンの再起動を個別に構成します。 KGS リカバリのデフォルトは停止ごとに 180 秒で、正常な 60 秒後にリセットされます。エンジン回復により、呼び出し全体で 3 つの自動置換が可能になります。疲労により、オペレーターの回復を待つライブ KGS セッションが残される可能性があります。
- 一時停止、延期、対戦相手の不在制限を選択します。それぞれのデフォルトは 300 秒です。期限切れは、未完了のゲームをカウントしたり中止したりせずにクライアントを停止します。
- クライアント ID ファイルを書き込み可能な状態のディレクトリに保存します。新しいプロセスでは、古いオートマッチ ゲームは自動的に検出されません。
- stderr をキャプチャし、外部ログの保持を調整します。終了 0 は正常終了を示し、1 は失敗を示し、130 はキャンセルを示します。

[ユーザー ガイド]({% include page-url.html key='mobi/user-guide' %}#timeouts-and-recovery) には、タイムアウト設定、接続回復、オペレーター エンジン回復について詳しく説明されています。

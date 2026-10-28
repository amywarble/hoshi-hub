---
source_revision: "2dd2b5f3a829514cb3f4e94bc67cffcd8f04dad8b5b984ffab73449fda82c3c7"
layout: "localized"
title: "アカウントとデータの削除"
lang: "ja"
page_key: "global/account-and-data-deletion"
section: "global"
nav_order: 2
permalink: "/ja/account-and-data-deletion/"
redirect_from: "/ja/desktop/account-and-data-deletion/"
---

_最終更新：2026年10月27日_

Pocket KGS、KGS Nova、Mobi は、KGS Go Server がホスト・管理するアカウントにログインします。いずれのクライアントにも独自のアカウント制度はありません。アカウントの作成は KGS の [公式登録ページ](https://www.gokgs.com/register/index.html) で行います。

端末内の削除やアンインストールでは、KGS アカウント、メッセージ、対局、プロフィール、その他 KGS 保管データは **削除されません**。

## KGS アカウントとサーバーデータの削除

1. [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) に件名 `KGS account deletion request` で送信します。
2. アカウントと関連サーバーデータの削除を明確に依頼します。
3. 利用者名と登録メールアドレスを含めます。**パスワードは絶対に送らないでください。**

管理者から本人確認の連絡をする場合があります。管理者が処理し、所要時間や安全・サービスの健全性・法令のため保持が必要な情報を説明できます。削除は依頼の受領と確認後に行われ、アンインストールやデータ消去で自動実行されません。

公開 GitHub Issue にアカウント情報を投稿しないでください。

## 端末内のデータを削除する

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

1. Android の **設定** を開きます。
2. **アプリ**、**Pocket KGS** を選びます。
3. **ストレージとキャッシュ** を選びます。
4. **ストレージを消去**（端末により表記が異なります）を選ぶか、アンインストールします。

設定、端末内の KGS クライアント識別子、キャッシュされたアバターが消えます。Pocket KGS はアプリ専用データをバックアップしないよう Android に要求します。

Android Credential Manager で保存したパスワードは、選択した管理アプリ／プロバイダーから別途削除してください。アプリデータ消去だけではそのコピーが消えない場合があります。

### KGS Nova

KGS Nova を終了し、残したい書き出し棋譜をバックアップしてください。

- OS のローカルアプリデータ内の KGS Nova フォルダー（Windows では `%LOCALAPPDATA%\KGS Nova`）から `data.db` と存在する場合は `data-log.db` を削除すると、保存アカウントのメタデータ、設定、識別子、アプリ状態が消えます。
- 診断を削除するには同じデータフォルダーから `client.log`、`client.archive*.log`、開発版の `logs.txt` を削除します。他の場所に保存したコピーは残ります。
- Windows の DPAPI 保護パスワードは `data.db` と共に削除されます。macOS／Linux はキーチェーン／Secret Service のアプリ用項目を別途削除してください。サービス `io.github.amywarble.kgsnet.desktop.credentials` と KGS 利用者名で探します。データベース削除ではこれらの OS 項目は消えません。
- 不要な書き出し棋譜、画像、その他のファイルを各保存場所から削除します。

同じフォルダーに `sgf` の作業データ、復旧ファイルとバックアップ、`analysis` のエンジンやモデルがあります。残したい復旧棋譜を保存してから削除してください。KGS Nova のデータフォルダー全体を削除すると、これらのローカルデータをまとめて消せます。

旧版はアプリや起動時のディレクトリに `data.db`、`data-log.db`、`logs.txt` を置いていました。更新後も残る場合があります。必要なものをバックアップしてから旧コピーも削除してください。現在のデータベースがないと旧データベースが再度取り込まれる場合があります。

アンインストールでファイルや OS の認証情報が消えるとは限りません。

### Mobi

Mobi とエンジンを停止し、ボットを再起動するサービスやスケジュールタスクを無効にしてください。必要な棋譜と設定は保存してください。

- `account.clientIdFile` または `--client-id-file` で指定した識別子ファイルを削除します。指定がない場合、マッチングは .NET のローカルアプリデータ領域（Windows は `%LOCALAPPDATA%`）内の `Kgs.Gtp/identities/<server-and-account-hash>`、その他の起動は `Kgs.Gtp/client-id` を使います。同じ端末で他のボットも動かす場合、引退させるアカウントのファイルだけを削除してください。
- 起動したシェルと、保存先の永続環境設定、起動スクリプト、サービス設定から `KGS_PASSWORD` を削除します。Mobi は変数を読み取りますが、パスワードを自身では保存しません。不要な `KGS_USERNAME` の保存値や、アカウント名、パス、設定を含む TOML ファイルも削除します。
- stderr のリダイレクトで保存した `bot.log` などの診断、サービス管理ツールのログ、他の場所へ共有した管理可能なコピーを削除します。
- 囲碁エンジン独自のログ、棋譜、設定、その他のデータの削除方法は、エンジンの説明書で確認します。エンジン・モデルファイルは Mobi と別に管理されます。他のアプリが使うファイルは削除しないでください。

展開した Mobi ファイルを削除しても、これらは残る場合があります。クライアント識別子の削除は KGS アカウントの削除、ランクのリセット、サーバー上の棋譜の消去にはなりません。

## お問い合わせ

いずれかのアプリが保存するデータに関する個別のご相談は、[hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com) へご連絡ください。

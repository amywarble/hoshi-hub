---
source_revision: "f77f4ed1d576932db0474a6793f3618116114ca1712e98af8892162d5ac9d665"
layout: localized
title: "アカウントとデータの削除"
lang: "ja"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/ja/desktop/account-and-data-deletion/"
nav_group: "policies"
---

## デスクトップのデータ削除

KGS Nova を終了し、残したい書き出し棋譜をバックアップしてください。

- OS のローカルアプリデータ内の KGS Nova フォルダー（Windows では `%LOCALAPPDATA%\KGS Nova`）から `data.db` と存在する場合は `data-log.db` を削除すると、保存アカウントのメタデータ、設定、識別子、アプリ状態が消えます。
- 診断を削除するには同じデータフォルダーから `client.log`、`client.archive*.log`、開発版の `logs.txt` を削除します。他の場所に保存したコピーは残ります。
- Windows の DPAPI 保護パスワードは `data.db` と共に削除されます。macOS／Linux はキーチェーン／Secret Service のアプリ用項目を別途削除してください。サービス `io.github.amywarble.kgsnet.desktop.credentials` と KGS 利用者名で探します。データベース削除ではこれらの OS 項目は消えません。
- 不要な書き出し棋譜、画像、その他のファイルを各保存場所から削除します。

同じフォルダーに `sgf` の作業データ、復旧ファイルとバックアップ、`analysis` のエンジンやモデルがあります。残したい復旧棋譜を保存してから削除してください。KGS Nova のデータフォルダー全体を削除すると、これらのローカルデータをまとめて消せます。

旧版はアプリや起動時のディレクトリに `data.db`、`data-log.db`、`logs.txt` を置いていました。更新後も残る場合があります。必要なものをバックアップしてから旧コピーも削除してください。現在のデータベースがないと旧データベースが再度取り込まれる場合があります。

アンインストールでファイルや OS の認証情報が消えるとは限りません。ローカル削除は KGS アカウントやサーバー記録を削除しません。

## KGS アカウントの削除依頼

アカウントとサーバーデータは KGS が管理します。[admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) に利用者名と登録メールを添えて非公開で依頼し、パスワードは送らないでください。管理者が本人確認を求め、削除可能な範囲や保持要件を説明する場合があります。公開 Issue にアカウント情報を投稿しないでください。

端末データの個別相談：[hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com)。

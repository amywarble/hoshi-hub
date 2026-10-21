---
source_revision: "3aa9378df5f32e6acf17ec4a44bd9f2964f9a6fed7d528cdcba256cfb2358d82"
layout: localized
title: "アカウントとデータの削除"
lang: "ja"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/ja/desktop/account-and-data-deletion/"
---

## デスクトップのデータ削除

KGS Nova を終了し、残したい書き出し棋譜をバックアップしてください。

- 起動時の作業ディレクトリから `data.db` を削除すると、保存アカウントのメタデータ、設定、識別子、アプリ状態が消え、設定が初期化されます。端末から起動した場合はアプリのフォルダーだけでなくそのディレクトリも確認してください。
- アプリディレクトリの `logs.txt` を削除します。コピーやコンソールから保存した他のログは、その保存場所に残ります。
- Windows の DPAPI 保護パスワードは `data.db` と共に削除されます。macOS／Linux はキーチェーン／Secret Service のアプリ用項目を別途削除してください。サービス `io.github.amywarble.kgsnet.desktop.credentials` と KGS 利用者名で探します。データベース削除ではこれらの OS 項目は消えません。
- 不要な書き出し棋譜、画像、その他のファイルを各保存場所から削除します。

アンインストールでファイルや OS の認証情報が消えるとは限りません。ローカル削除は KGS アカウントやサーバー記録を削除しません。

## KGS アカウントの削除依頼

アカウントとサーバーデータは KGS が管理します。[admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) に利用者名と登録メールを添えて非公開で依頼し、パスワードは送らないでください。管理者が本人確認を求め、削除可能な範囲や保持要件を説明する場合があります。公開 Issue にアカウント情報を投稿しないでください。

端末データの個別相談：[hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com)。

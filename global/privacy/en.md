---
layout: "localized"
title: "Privacy Policy"
lang: "en"
page_key: "global/privacy"
section: "global"
nav_order: 3
permalink: "/privacy/"
redirect_from: "/desktop/privacy/"
---

_Effective: October 27, 2026_

This policy covers Pocket KGS for Android, KGS Nova for Windows, macOS, and Linux, Mobi for Windows and Linux, and this support website. All three clients are officially endorsed by KGS and the American Go Association (AGA). Common practices are described first; app-specific storage and controls appear below.

## Who handles your data

The clients connect directly to the KGS Go Server. The client developer does not operate KGS servers or control their accounts, moderation, records, or retention. KGS is a separate service with its own [Terms of Service and privacy information](https://www.gokgs.com/tos.jsp).

The clients contain no advertising, analytics, or automatic crash-report uploads. The developer does not sell your personal information or use it for targeted advertising or cross-app tracking, and does not maintain a separate server-side copy of your KGS account, chats, games, avatars, or teacher audio.

## Information handled and why

Depending on the client and features you use, information includes:

- **Accounts and profiles:** KGS credentials, email address, profile text, avatar, rank, account status, and preferences.
- **Communications and social information:** room and game chat, private and offline messages, buddy/fan/censor lists and notes, and other KGS content.
- **Games and activity:** moves, records, annotations, results, challenges, room membership, and matchmaking settings. Mobi exchanges game information with the Go engine you configure to generate moves and handle games.
- **Connection information:** a persistent KGS client identifier, app/protocol versions, language, operating system and architecture, runtime information, and connection status. KGS receives your IP address when you connect.
- **Local settings and diagnostics:** preferences, cached content, and diagnostics described in the app sections below.

This information supports sign-in, KGS sessions, displaying content, sending requested actions or configured bot actions to KGS, remembering settings, and diagnosing problems when you choose to share details.

Pocket KGS and Nova also handle microphone audio when an eligible teacher explicitly starts a live broadcast, and play received teacher audio. Broadcasting stops when you stop it or the relevant session ends. Neither client creates a separate audio recording for the developer. Mobi does not provide teacher-audio controls.

## Where information goes

- **KGS:** account and connection information, communications, game activity, and requested changes go to KGS. Other users see content according to the KGS feature you use.
- **Credential providers and engines:** platform credential providers and your chosen Mobi engine handle information as described below, subject to their own terms.
- **GitHub:** this website and the public issue tracker are hosted by GitHub under the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Public issues and attachments are visible to everyone. Nova's issue-report action opens an editable browser draft with app version, operating system, architecture, and runtime details; it does not submit the issue or attach logs automatically.
- **Legal and safety needs:** information you provide to the developer may be preserved or disclosed when reasonably necessary to comply with law, investigate abuse, protect users, or protect rights and security.

## Communications and security

The legacy KGS connection used by these clients does not provide TLS or end-to-end encryption. The login protocol transforms the password before transmission, but other traffic may be observed or altered by someone with access to the network path. Use a network you trust.

KGS states that all conversations are logged and may be reviewed by its administrators when investigating reports. Do not share information on KGS that must remain private. KGS controls server-side retention, and game records may remain in its archives.

## App-specific storage and choices

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

Pocket stores preferences, notification choices, and its KGS client identifier in Android app-private storage, and avatars in Android's cache. Android may evict cached files. Pocket requests that Android not back up its app-private data. Clearing app storage or uninstalling removes that local app data.

If you choose to save credentials, Android Credential Manager and your selected credential provider handle them under their own terms. Pocket does not receive biometric data used to unlock a credential. The provider's saved credentials may need to be removed separately.

Production error diagnostics go to Android's system log. Optional diagnostic logging enables more detail for the current session. Release logs retain version information, event templates, exception types, and stack traces, with a layout designed to omit runtime argument values, exception messages, and source-file paths. Android, a device administrator, or someone you give logs to may access them.

You can use a guest session, choose whether to save credentials, disable notifications in Pocket or Android settings, deny microphone permission, avoid broadcasting, and censor users to block supported interactions and hide their content.

### KGS Nova

- **Database:** `data.db` in the OS local application-data folder for KGS Nova (`%LOCALAPPDATA%\KGS Nova` on Windows) holds saved account metadata, the client identifier, preferences, and app state. The database as a whole is not encrypted.
- **Passwords:** Windows protects saved passwords in the database with DPAPI for the current Windows user. macOS uses Keychain; Linux uses Secret Service. The OS may require unlocking or permission. This does not encrypt the rest of the database.
- **Diagnostics:** release errors go to `client.log` and rotating `client.archive*.log` files in the same folder. Optional session diagnostics are more detailed. Release logs use the same omission approach described for Pocket. Developer builds may produce more detailed `logs.txt` and console/debug output.
- **Other files:** the same folder contains the `sgf` workspace, recovery files and backups, and `analysis` engine/model files. Exported records and other files remain wherever you save them.

People or software with access to your files or OS account may read them. Uninstalling or replacing Nova does not necessarily remove its database, logs, exports, or keyring entries. You can use a guest session, choose whether to remember credentials, control supported private-message interactions, censor users, avoid microphone broadcasting, and remove local data.

### Mobi

Mobi requires a registered KGS account. It reads the password from `KGS_PASSWORD` and does not persist it itself. Launch scripts, environment settings, and service managers may retain credentials you put there. Protect those and your OS account; a launched engine can inherit its environment.

Your TOML configuration may contain the account name, server, engine paths, and game settings. Mobi saves the KGS client identifier in a local file. Matchmaking defaults to `Kgs.Gtp/identities/<server-and-account-hash>` under .NET's local application-data directory (`%LOCALAPPDATA%` on Windows); without matchmaking, the default is `Kgs.Gtp/client-id`. `account.clientIdFile` or `--client-id-file` can override the location.

Status, errors, and engine diagnostics go to stderr. Logs persist if you redirect output or a service manager retains it. These logs do not follow Pocket/Nova's release-log omission rules and may contain usernames, game details, paths, or engine output. Review them before sharing. Your engine may create additional logs, records, or other files and may have its own network behavior; review its documentation and privacy practices separately. Mobi does not automatically upload diagnostics to the developer.

You control the engine, configuration, retained output, and local files. See the [Mobi user guide]({% include page-url.html key='mobi/user-guide' %}) for operation and diagnostics.

## Retention, deletion, and other choices

The developer does not automatically receive your local files or diagnostics. Copies you choose to send may be retained to address the request or for legal and safety needs. Public GitHub issues and their history remain until edited or deleted under GitHub's features and policies.

You can choose what profile information to share and mark your KGS email private where supported. Clearing files or uninstalling a client does not delete KGS-hosted data. KGS administrators handle account and server-data deletion. See [Account and Data Deletion]({% include page-url.html key='global/account-and-data-deletion' %}) for the common request process and each client's local-removal instructions.

Pocket KGS is not directed to children under 13. KGS is a public communication service; a parent or guardian should review its terms and suitability before a minor uses it. Do not post a child's personal information in public issues.

## Changes and contact

Keep your OS and client current, use a unique KGS password, and review logs before sharing. No system is completely secure. Report vulnerabilities through the [Security Policy]({% include page-url.html key='global/security-policy' %}).

This policy may change as the clients change; the effective date identifies the published revision. For non-sensitive support, use the [public issue tracker](https://github.com/amywarble/hoshi-hub/issues/new/choose). For private app or privacy concerns, contact [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). For KGS accounts, server data, or moderation, contact [admin@gokgs.com](mailto:admin@gokgs.com).

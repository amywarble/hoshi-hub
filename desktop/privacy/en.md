---
layout: localized
title: "Privacy Policy"
lang: "en"
page_key: "desktop/privacy"
section: "desktop"
nav_order: 10
permalink: "/desktop/privacy/"
nav_group: "policies"
---

_Effective: October 27, 2026_

This policy covers the KGS Nova desktop app for Windows, macOS, and Linux. KGS Nova is officially endorsed by KGS. KGS operates a separate service with its own [terms and privacy information](https://www.gokgs.com/tos.jsp).

## Information handled by the desktop app

The app connects directly to KGS. Depending on the features you use, it handles your KGS credentials and profile, rooms, chat and private messages, offline messages, social lists and notes, game records and moves, challenges, avatars, and preferences. It sends your requested actions to KGS and displays responses from KGS. Other users can see content according to the KGS feature you use.

The app sends KGS a persistent client identifier, protocol version, language/locale, operating system and architecture, and runtime information. KGS also receives the network address used to connect.

When an eligible teacher starts a teacher-audio broadcast, microphone audio is sent to KGS for delivery to game participants. Receiving teacher audio plays audio from KGS. Broadcasting stops when you stop it or the relevant session ends. The desktop client does not create a separate audio recording for the developer.

The desktop app does not include advertising, analytics, or automatic crash-report uploads. The developer does not maintain a separate server-side copy of your KGS account, messages, games, or audio.

## Local storage and diagnostics

- **Database:** `data.db` in the KGS Nova folder in your operating system’s local application-data directory holds saved account metadata, the client identifier, preferences, and application state. On Windows this folder is `%LOCALAPPDATA%\KGS Nova`. The database as a whole is not encrypted.
- **Saved passwords:** On Windows, saved passwords in the database are encrypted with Windows DPAPI for the current Windows user. On macOS, passwords are stored in Keychain. On Linux, passwords are stored through the Secret Service keyring. Native credential storage may require unlocking or permission from your operating system. Password storage does not encrypt the rest of the database.
- **Logs:** Release builds write error diagnostics to `client.log` and rotating `client.archive*.log` files in the same KGS Nova data folder. Optional diagnostic logging enables more detailed events for the current session. Release logs retain version information, event templates, exception types, and stack traces, with a layout designed to omit runtime argument values, exception messages, and source-file paths. Developer builds can produce more detailed `logs.txt` and console/debug output. Review logs before sharing them. They are not automatically uploaded to the developer.
- **Files you save:** Game records and other files you explicitly export remain in the locations you choose.

Other people or software with access to these files or your operating-system account may be able to read them. Uninstalling or replacing the application does not necessarily remove its database, logs, exported files, or native keyring entries. See [desktop data-removal instructions]({% include page-url.html key='desktop/account-and-data-deletion' %}).

The same data folder contains the `sgf` workspace, recovery files and backups, and the `analysis` engine/model files. Save any recovered games you want to keep before deleting these folders. Removing the whole KGS Nova data folder removes this local data together.

## Communications and third-party services

The legacy KGS connection used by this client does not use TLS or end-to-end encryption. The login protocol transforms the password before transmission, but this does not protect all traffic from network observation or interference. Use a network you trust.

KGS says conversations are logged and may be reviewed by its administrators. Avoid sharing information on KGS that must remain private. KGS controls server-side moderation and retention.

Support pages and the issue tracker are hosted by GitHub, under the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Selecting a link opens your browser. Reporting an issue opens an editable draft containing app version, operating system, architecture, and runtime details. The app does not submit the issue or attach logs automatically. Submitted public issues and attachments are visible to the public.

## Your choices and contact

You can use a guest session, choose whether to remember credentials, control supported private-message interactions, censor users, avoid microphone broadcasting, and remove local files. KGS account deletion is handled by KGS administrators; see [Account and Data Deletion]({% include page-url.html key='desktop/account-and-data-deletion' %}).

Do not submit a child's personal information in a public issue. A parent or guardian should review KGS's terms and communication features before allowing a minor to use the service.

For private app or privacy questions, contact [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). For KGS accounts and server-side data, contact [admin@gokgs.com](mailto:admin@gokgs.com). For vulnerabilities, use [private security reporting](https://github.com/amywarble/hoshi-hub/security/advisories/new).

This policy will be updated as desktop behavior changes; the effective date above identifies the revision.

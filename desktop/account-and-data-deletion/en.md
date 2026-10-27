---
layout: localized
title: "Account and Data Deletion"
lang: "en"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/desktop/account-and-data-deletion/"
nav_group: "policies"
---

Close KGS Nova before removing its local data. Back up exported games you want to keep.

- Remove `data.db` and any `data-log.db` journal from the KGS Nova folder in your operating system’s local application-data directory (`%LOCALAPPDATA%\KGS Nova` on Windows) to clear saved account metadata, preferences, the client identifier, and application state.
- To remove diagnostics, delete `client.log`, `client.archive*.log`, and any developer-build `logs.txt` from the same data folder. Copies you saved elsewhere remain in those locations.
- On Windows, saved passwords protected by DPAPI are stored in `data.db` and removed with that file. On macOS and Linux, separately remove this app's saved-password entries from Keychain or your Secret Service keyring; look for the service `io.github.amywarble.kgsnet.desktop.credentials` and your KGS username. Deleting the database does not delete those native entries.
- Delete exported game records, screenshots, and other files from their chosen locations if you no longer want them.

The same data folder contains the `sgf` workspace, recovery files and backups, and the `analysis` engine/model files. Save any recovered games you want to keep before deleting these folders. Removing the whole KGS Nova data folder removes this local data together.

Older versions used `data.db`, `data-log.db`, and `logs.txt` in the application or launch directory. Upgrading can leave those copies behind. After backing up what you need, remove the old copies too; an old database can otherwise be imported again when the current database is absent.

Uninstalling the app does not necessarily remove these files or native credentials. Removing local data does not delete your KGS account or server-side records.

## Request KGS account deletion

KGS controls its accounts and server-side data. Send a private request to [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) with your KGS username and account email address, never your password. A KGS administrator may need to verify ownership and can explain which data can be deleted and any retention requirements. Do not submit account details in a public GitHub issue.

For private questions about desktop data, contact [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

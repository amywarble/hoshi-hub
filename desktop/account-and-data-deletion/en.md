---
layout: localized
title: "Account and Data Deletion"
lang: "en"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/desktop/account-and-data-deletion/"
---

Close KGS Nova before removing its local data. Back up exported games you want to keep.

- Remove `data.db` from the working directory used to launch the app to clear saved account metadata, preferences, the client identifier, and application state. This resets local settings. If you launched the app from a terminal, check that directory as well as the app's folder.
- Remove `logs.txt` from the application directory to clear the desktop diagnostic log. Other logs you copied or captured from console output remain wherever you saved them.
- On Windows, saved passwords protected by DPAPI are stored in `data.db` and removed with that file. On macOS and Linux, separately remove this app's saved-password entries from Keychain or your Secret Service keyring; look for the service `io.github.amywarble.kgsnet.desktop.credentials` and your KGS username. Deleting the database does not delete those native entries.
- Delete exported game records, screenshots, and other files from their chosen locations if you no longer want them.

Uninstalling the app does not necessarily remove these files or native credentials. Removing local data does not delete your KGS account or server-side records.

## Request KGS account deletion

KGS controls its accounts and server-side data. Send a private request to [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) with your KGS username and account email address, never your password. A KGS administrator may need to verify ownership and can explain which data can be deleted and any retention requirements. Do not submit account details in a public GitHub issue.

For private questions about desktop data, contact [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

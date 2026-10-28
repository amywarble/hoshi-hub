---
layout: "localized"
title: "Account and Data Deletion"
lang: "en"
page_key: "global/account-and-data-deletion"
section: "global"
nav_order: 2
permalink: "/account-and-data-deletion/"
redirect_from: "/desktop/account-and-data-deletion/"
---

_Last updated: October 27, 2026_

Pocket KGS, KGS Nova, and Mobi sign in to accounts hosted and controlled by the KGS Go Server. None of these clients operates a separate account system. KGS handles account creation through its [official registration page](https://www.gokgs.com/register/index.html).

Clearing local data or uninstalling does **not** delete your KGS account, messages, games, profile, or other information held by KGS.

## Delete a KGS account and server-side data

To request deletion of your KGS account and its associated server-side data:

1. [Email the KGS administrators](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) at **admin@gokgs.com** with the subject `KGS account deletion request`.
2. State clearly that you want your KGS account and associated server-side data deleted.
3. Include your KGS username and the email address associated with the account. **Never send your password.**

A KGS administrator may contact you to verify account ownership. The administrator will process the deletion request and can explain the expected completion time and whether any information must be retained for security, service-integrity, or legal reasons.

Do not submit account details in a public GitHub issue.

## Delete data stored by the app

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

To remove Pocket KGS data from your Android device:

1. Open Android **Settings**.
2. Select **Apps**, then **Pocket KGS**.
3. Select **Storage & cache**.
4. Select **Clear storage** (wording varies by device), or uninstall Pocket KGS.

This removes Pocket KGS preferences, its locally stored KGS client identifier, and cached avatars from the device. Pocket KGS requests that Android not back up its app-private data.

If you saved a KGS password through Android Credential Manager, remove it separately using the password manager or credential provider you selected. Clearing Pocket KGS data does not necessarily remove that provider's copy.

### KGS Nova

Close KGS Nova before removing its local data. Back up exported games you want to keep.

- Remove `data.db` and any `data-log.db` journal from the KGS Nova folder in your operating system’s local application-data directory (`%LOCALAPPDATA%\KGS Nova` on Windows) to clear saved account metadata, preferences, the client identifier, and application state.
- To remove diagnostics, delete `client.log`, `client.archive*.log`, and any developer-build `logs.txt` from the same data folder. Copies you saved elsewhere remain in those locations.
- On Windows, saved passwords protected by DPAPI are stored in `data.db` and removed with that file. On macOS and Linux, separately remove this app's saved-password entries from Keychain or your Secret Service keyring; look for the service `io.github.amywarble.kgsnet.desktop.credentials` and your KGS username. Deleting the database does not delete those native entries.
- Delete exported game records, screenshots, and other files from their chosen locations if you no longer want them.

The same data folder contains the `sgf` workspace, recovery files and backups, and the `analysis` engine/model files. Save any recovered games you want to keep before deleting these folders. Removing the whole KGS Nova data folder removes this local data together.

Older versions used `data.db`, `data-log.db`, and `logs.txt` in the application or launch directory. Upgrading can leave those copies behind. After backing up what you need, remove the old copies too; an old database can otherwise be imported again when the current database is absent.

Uninstalling the app does not necessarily remove these files or native credentials.

### Mobi

Stop Mobi and its engine, and disable any service or scheduled task that would restart the bot. Save any game records or configuration you want to keep.

- Delete the client identity file chosen by `account.clientIdFile` or `--client-id-file`. Without an override, matchmaking uses `Kgs.Gtp/identities/<server-and-account-hash>` under .NET's local application-data directory (`%LOCALAPPDATA%` on Windows); other runs default to `Kgs.Gtp/client-id`. Remove only the files for the accounts you are retiring if you run other bots on this machine.
- Remove `KGS_PASSWORD` from the launching shell and any persistent environment settings, launch scripts, or service configuration where you stored it. Mobi reads this variable but does not save the password itself. Remove saved `KGS_USERNAME` values and TOML files containing account names, paths, or settings if you no longer need them.
- Delete diagnostics you retained by redirecting stderr, such as `bot.log`, and any retained service-manager logs or copies you shared elsewhere, where you control them.
- Review your Go engine's documentation to remove its own logs, game records, configuration, or other data. Engine/model files are managed separately from Mobi; do not remove files still used by other applications.

Deleting the extracted Mobi files does not necessarily remove these items. Removing a client identity file does not delete the KGS account, reset its ranking, or erase its server-side games.

## Contact

For private questions about data stored by any of these clients, contact [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

---
layout: localized
title: "Mobi"
nav_title: "Getting started"
lang: "en"
page_key: "mobi/home"
section: "mobi"
nav_order: 0
permalink: "/gtp/"
---

Mobi connects a Go engine speaking Go Text Protocol (GTP) version 2 to the
[KGS Go Server](https://www.gokgs.com/). It handles login, matchmaking, moves,
clocks, scoring, and recovery. Install and configure your Go engine separately.

Mobi is officially endorsed by KGS and the American Go Association (AGA).

## Download and get started

Download a **Mobi GTP bridge** archive from
[GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) for Windows or
Linux on x64 or ARM64. The .NET runtime is included. Windows packages use ZIP;
Linux packages use tar.gz. Keep the extracted files together.

- [User guide]({% include page-url.html key='mobi/user-guide' %}): first game,
  configuration, matchmaking, logs, timeouts, recovery, and troubleshooting.
- [Java client upgrade guide]({% include page-url.html key='mobi/upgrade-guide' %}):
  move from `kgsGtp.jar` and Java properties to TOML.
- [Example configuration]({{ '/mobi/bot.example.toml' | relative_url }}): copy to
  `bot.toml` and set your account, engine paths, and game preferences.
- [Terms of Use]({% include page-url.html key='mobi/terms' %}): operating your bot,
  engine licensing, and responsibilities when using Mobi.
- [Community Guidelines]({% include page-url.html key='mobi/community-guidelines' %}):
  honest bot identities, fair play, and responsible use of server resources.

The shared [Privacy Policy]({% include page-url.html key='global/privacy' %}) and
[Account and Data Deletion]({% include page-url.html key='global/account-and-data-deletion' %})
pages include Mobi-specific information.

The guides cover Windows with PowerShell and Linux with Bash. Expand the section
for your operating system. Each archive also includes the example configuration
and English offline copies of both guides.

## Run the client

After configuring `bot.toml`, run these commands from the extracted directory.
The probe checks the engine without logging into KGS; the next command plays
one game with the configured matchmaking settings.

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --probe
$env:KGS_PASSWORD = '<account password>'
.\Kgs.Gtp.exe --config .\bot.toml --games 1
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
chmod +x ./Kgs.Gtp
./Kgs.Gtp --config ./bot.toml --probe
read -r -s -p 'KGS password: ' KGS_PASSWORD
export KGS_PASSWORD
printf '\n'
./Kgs.Gtp --config ./bot.toml --games 1
```

</details>

Press Ctrl+C to stop. Use the user guide to choose continuous play, retain logs,
and preserve the client identity across upgrades.

For bugs and documentation corrections,
[open a public GitHub issue](https://github.com/amywarble/hoshi-hub/issues/new/choose)
and identify the client as **Mobi**. Include the client and engine versions
and relevant diagnostics. Omit passwords and other sensitive information.

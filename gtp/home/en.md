---
layout: localized
title: "KGS GTP"
lang: "en"
page_key: "gtp/home"
section: "gtp"
nav_order: 0
permalink: "/gtp/"
---

Kgs.Gtp connects a Go engine speaking Go Text Protocol (GTP) version 2 to the
[KGS Go Server](https://www.gokgs.com/). It handles login, matchmaking, moves,
clocks, scoring, and recovery. Install and configure your Go engine separately.

## Download and get started

Download a **KGS GTP Bridge** archive from
[GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) for Windows or
Linux on x64 or ARM64. The .NET runtime is included. Windows packages use ZIP;
Linux packages use tar.gz. Keep the extracted files together.

- [User guide]({% include page-url.html key='gtp/user-guide' %}): first game,
  configuration, matchmaking, logs, timeouts, recovery, and troubleshooting.
- [Java client upgrade guide]({% include page-url.html key='gtp/upgrade-guide' %}):
  move from `kgsGtp.jar` and Java properties to TOML.
- [Example configuration]({{ '/gtp/bot.example.toml' | relative_url }}): copy to
  `bot.toml` and set your account, engine paths, and game preferences.

The guides cover Windows with PowerShell and Linux with Bash. Expand the section
for your operating system. Documentation is currently available in English;
offline copies of both guides and the example configuration ship in each archive.

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
and identify the client as **KGS GTP**. Include the client and engine versions
and relevant diagnostics. Omit passwords and other sensitive information.

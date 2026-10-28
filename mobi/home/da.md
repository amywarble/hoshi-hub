---
layout: "localized"
title: "Mobi"
nav_title: "Kom godt i gang"
lang: "da"
page_key: "mobi/home"
section: "mobi"
nav_order: 0
permalink: "/da/gtp/"
source_revision: "b9d339585b5a920216045e5e3c1e6b45997754a2b3e257c811c18c8f9c33e4ca"
---

Mobi forbinder en Go-motor, der understøtter Go Text Protocol (GTP) version 2, med [KGS Go Server](https://www.gokgs.com/). Den håndterer login, matchmaking, træk, ure, optælling og gendannelse. Installer og konfigurer din Go-motor separat.

Mobi er officielt godkendt af KGS og American Go Association (AGA).

## Download og kom i gang {#download-and-get-started}

Download et **Mobi GTP-bro**-arkiv fra [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) til Windows eller Linux på x4. .NET runtime er inkluderet. Windows-pakker bruger ZIP; Linux-pakker bruger tar.gz. Hold de udpakkede filer sammen.

- [Brugervejledning]({% include page-url.html key='mobi/user-guide' %}): første spil, konfiguration, matchmaking, logfiler, timeouts, gendannelse og fejlfinding.
- [Java-klientopgraderingsvejledning]({% include page-url.html key='mobi/upgrade-guide' %}): flyt fra `kgsGtp.jar` og Java-egenskaber til TOML.
- [Eksempel på konfiguration]({{ '/mobi/bot.example.toml' | relative_url }}): kopier til `bot.toml` og indstil din konto, motorstier og spilpræferencer.
- [Brugervilkår]({% include page-url.html key='mobi/terms' %}): betjening af din bot, motorlicenser og ansvar, når du bruger Mobi.
- [Retningslinjer for fællesskabet]({% include page-url.html key='mobi/community-guidelines' %}): ærlige bot-identiteter, fair play og ansvarlig brug af serverressourcer.

De delte sider [Privatlivspolitik]({% include page-url.html key='global/privacy' %}) og [Sletning af konto og data]({% include page-url.html key='global/account-and-data-deletion' %}) indeholder Mobi-specifikke oplysninger.

Guiderne dækker Windows med PowerShell og Linux med Bash. Udvid sektionen for dit operativsystem. Hvert arkiv inkluderer også eksempelkonfigurationen og engelske offlinekopier af begge guider.

## Kør klienten {#run-the-client}

Efter konfiguration af `bot.toml`, kør disse kommandoer fra den udpakkede mappe. Sonden kontrollerer motoren uden at logge på KGS; den næste kommando spiller et spil med de konfigurerede matchmaking-indstillinger.

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

Tryk på Ctrl+C for at stoppe. Brug brugervejledningen til at vælge kontinuerlig afspilning, bevare logfiler og bevare klientidentiteten på tværs af opgraderinger.

For fejl og dokumentationsrettelser, [åbn et offentligt GitHub-problem](https://github.com/amywarble/hoshi-hub/issues/new/choose) og identificer klienten som **Mobi**. Inkluder klient- og motorversionerne og relevant diagnostik. Udelad adgangskoder og andre følsomme oplysninger.

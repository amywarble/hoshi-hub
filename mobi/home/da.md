---
layout: "localized"
title: "Mobi"
nav_title: "Kom godt i gang"
lang: "da"
page_key: "mobi/home"
section: "mobi"
nav_order: 0
permalink: "/da/gtp/"
source_revision: "874054b8ddaecac1e59dd93fb146bb94e87a23f895e0f2763c1c7f0413376a1a"
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

[Rapportér et problem med Mobi](https://github.com/amywarble/hoshi-hub/issues/new?template=mobi_problem_report.yml). Ved rettelser til dokumentationen, [opret en offentlig GitHub-sag](https://github.com/amywarble/hoshi-hub/issues/new/choose) og nævn **Mobi**. Medtag aldrig adgangskoder eller andre følsomme oplysninger.

Du behøver ikke teknisk viden for at rapportere et problem. Beskriv med dine egne ord, hvad der skete, også selv om det kun skete én gang. Udfyld det, du ved; vi kan stille opfølgende spørgsmål. Versioner, trin og skærmbilleder er valgfrie. Skjul private oplysninger i skærmbilleder, før du deler dem.

Bruger du ikke GitHub? Du kan også rapportere app-problemer via mail til [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

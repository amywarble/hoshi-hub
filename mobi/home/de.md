---
layout: "localized"
title: "Mobi"
nav_title: "Erste Schritte"
lang: "de"
page_key: "mobi/home"
section: "mobi"
nav_order: 0
permalink: "/de/gtp/"
source_revision: "b9d339585b5a920216045e5e3c1e6b45997754a2b3e257c811c18c8f9c33e4ca"
---

Mobi verbindet eine Go-Engine, die Go Text Protocol (GTP) Version 2 unterstützt, mit dem [KGS Go Server](https://www.gokgs.com/). Es übernimmt Anmeldung, Spielvermittlung, Züge, Uhren, Zählung und Wiederherstellung. Installieren und konfigurieren Sie Ihre Go-Engine separat.

Mobi wird offiziell von KGS und American Go Association (AGA) unterstützt.

## Herunterladen und loslegen {#download-and-get-started}

Laden Sie ein **Mobi GTP Bridge**-Archiv von [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) für Windows oder Linux auf x64 oder ARM64 herunter. Die .NET-Runtime ist im Lieferumfang enthalten. Windows-Pakete verwenden ZIP; Linux-Pakete verwenden tar.gz. Halten Sie die extrahierten Dateien zusammen.

- [Benutzerhandbuch]({% include page-url.html key='mobi/user-guide' %}): erstes Spiel, Konfiguration, Matchmaking, Protokolle, Zeitüberschreitungen, Wiederherstellung und Fehlerbehebung.
- [Java-Client-Upgrade-Anleitung]({% include page-url.html key='mobi/upgrade-guide' %}): Wechsel von `kgsGtp.jar` und Java-Eigenschaften zu TOML.
- [Beispielkonfiguration]({{ '/mobi/bot.example.toml' | relative_url }}): Kopieren Sie es nach `bot.toml` und legen Sie Ihr Konto, Engine-Pfade und Spieleinstellungen fest.
- [Nutzungsbedingungen]({% include page-url.html key='mobi/terms' %}): Betrieb Ihres Bots, Engine-Lizenzierung und Verantwortlichkeiten bei der Verwendung von Mobi.
- [Community-Richtlinien]({% include page-url.html key='mobi/community-guidelines' %}): Ehrliche Bot-Identitäten, Fairplay und verantwortungsvoller Umgang mit Serverressourcen.

Die gemeinsamen Seiten [Datenschutzerklärung]({% include page-url.html key='global/privacy' %}) und [Konto- und Datenlöschung]({% include page-url.html key='global/account-and-data-deletion' %}) enthalten Mobi-spezifische Informationen.

Die Leitfäden decken Windows mit PowerShell und Linux mit Bash ab. Erweitern Sie den Abschnitt für Ihr Betriebssystem. Jedes Archiv enthält außerdem die Beispielkonfiguration und englische Offline-Kopien beider Handbücher.

## Führen Sie den Client aus {#run-the-client}

Führen Sie nach der Konfiguration von `bot.toml` diese Befehle im extrahierten Verzeichnis aus. Das Probe überprüft die Engine, ohne sich bei KGS anzumelden. Der nächste Befehl spielt ein Spiel mit den konfigurierten Matchmaking-Einstellungen.

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

Drücken Sie Strg+C, um zu stoppen. Verwenden Sie das Benutzerhandbuch, um die kontinuierliche Wiedergabe auszuwählen, Protokolle beizubehalten und die Client-Identität über Upgrades hinweg beizubehalten.

Für Fehler und Dokumentationskorrekturen [öffnen Sie ein öffentliches GitHub-Problem](https://github.com/amywarble/hoshi-hub/issues/new/choose) und identifizieren Sie den Client als **Mobi**. Geben Sie die Client- und Engine-Versionen sowie relevante Diagnosen an. Lassen Sie Passwörter und andere vertrauliche Informationen weg.

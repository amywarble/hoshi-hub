---
source_revision: "a5018456d7c6b6ef49fc5b143b52c2707452b29213029b1bba9cf85a02f24031"
layout: localized
title: "Erste Schritte"
lang: "de"
page_key: "desktop/help"
section: "desktop"
nav_order: 1
permalink: "/de/desktop/help/"
nav_group: "documentation"
redirect_from: "/de/desktop/"
---

KGS Nova ist ein Client für den [KGS Go Server](https://www.gokgs.com/) unter Windows, macOS und Linux. Die App wird offiziell von KGS und der American Go Association (AGA) empfohlen.

## Installation und Updates {#installation}

Lade ein **KGS Nova**-Paket von [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) herunter. Wähle x64 für Intel/AMD-Prozessoren oder ARM64 für Apple Silicon und andere ARM64-Geräte. Jede Veröffentlichung führt die verfügbaren Plattformen auf. Die .NET-Laufzeit ist enthalten.

- **Windows:** Starte den **Installer**. Für eine portable Installation entpacke die vollständige **Portable**-ZIP-Datei in einen beschreibbaren Ordner und starte `Kgs.Client.Desktop.exe`.
- **Linux:** Mache die **AppImage** mit `chmod +x Kgs.Nova-linux-<architecture>.AppImage` (`x64` oder `arm64`) ausführbar und starte sie. Bewahre sie für Updates in einem beschreibbaren Ordner auf. FUSE wird benötigt (`libfuse2` unter Ubuntu 22.04).
- **macOS (wenn verfügbar):** Starte den **Installer** und öffne `KGS Nova.app`. Für eine portable Installation entpacke die vollständige **Portable**-ZIP-Datei und verschiebe die App in einen beschreibbaren Applications-Ordner. Die Builds sind ad hoc signiert, ohne Apple Developer ID-Signierung oder Notarisierung. Wird Nova blockiert, erlaube es unter **Systemeinstellungen > Datenschutz & Sicherheit**, nachdem du die Vertrauenswürdigkeit des Downloads geprüft hast.

Wähle unter **Über** nacheinander **Nach Updates suchen**, **Update herunterladen** und **Neu starten und aktualisieren**. Nova prüft auch beim Start auf Updates. Beende Partien und speichere deine Arbeit vor dem Neustart. Ist die Aktualisierung in der App nicht verfügbar, lade ein neueres Paket manuell herunter.

### Manuelle Linux-Installation

Entpacke `KGS-Nova-<version>-linux-<architecture>.tar.gz` und starte `./Kgs.Client.Desktop` aus diesem Ordner. Für Updates dieser Archive ist ein neuer Download nötig.

Linux benötigt X11 oder XWayland, fontconfig und die von .NET/Avalonia verwendeten X11-Bibliotheken. Audio nutzt PipeWire, PulseAudio oder ALSA. Zum Speichern von Passwörtern sind libsecret (`libsecret-1-0` unter Debian/Ubuntu) und ein Secret Service-Anbieter wie GNOME Keyring nötig.

### Update-Dateien

`.nupkg` und `releases.*.json` dienen Novas Aktualisierungsfunktion. Installiere mit **Installer**, **Portable**-ZIP oder **AppImage**.

## Anmelden

Melden Sie sich mit Ihrem KGS-Nutzernamen und Passwort an oder fahren Sie als Gast fort. Der Registrierungslink im Anmeldebildschirm öffnet die KGS-Website zur Kontoerstellung.

## Spielen und erkunden

Wählen Sie Spielen für die Gegnersuche oder ein eigenes Spiel. Unter Räume finden Sie Gespräche und Spiele zum Zuschauen, unter Personen andere Spieler. Anzeigen/Bearbeiten öffnet SGF-Dateien zum lokalen Studium. Die Einstellungen steuern Darstellung und App-Verhalten.

## Hilfe und Richtlinien

Bei App-Problemen hilft [Support]({% include page-url.html key='desktop/support' %}). Bei unerwünschtem Kontakt und Regelverstößen siehe [Community-Richtlinien]({% include page-url.html key='desktop/community-guidelines' %}). Lesen Sie die [Datenschutzerklärung]({% include page-url.html key='global/privacy' %}) und [Nutzungsbedingungen]({% include page-url.html key='desktop/terms' %}) der App sowie die [gemeinsamen Community-Richtlinien]({% include page-url.html key='global/community-guidelines' %}).

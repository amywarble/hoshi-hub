---
source_revision: "f77f4ed1d576932db0474a6793f3618116114ca1712e98af8892162d5ac9d665"
layout: localized
title: "Konto und Daten löschen"
lang: "de"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/de/desktop/account-and-data-deletion/"
nav_group: "policies"
---

## Desktop-Daten entfernen

Schließen Sie KGS Nova. Sichern Sie exportierte Spiele, die Sie behalten möchten.

- Löschen Sie `data.db` und eine vorhandene `data-log.db` aus dem Ordner KGS Nova für lokale Anwendungsdaten (`%LOCALAPPDATA%\KGS Nova` unter Windows), um gespeicherte Kontometadaten, Einstellungen, Client-Kennung und App-Zustand zu entfernen.
- Zum Entfernen der Diagnosen löschen Sie `client.log`, `client.archive*.log` und gegebenenfalls `logs.txt` aus Entwickler-Builds im selben Datenordner. Anderswo gespeicherte Kopien bleiben dort.
- Unter Windows liegen DPAPI-geschützte Passwörter in `data.db` und werden damit entfernt. Unter macOS/Linux löschen Sie App-Passwörter separat im Schlüsselbund/Secret-Service-Schlüsselbund. Suchen Sie den Dienst `io.github.amywarble.kgsnet.desktop.credentials` und Ihren KGS-Nutzernamen. Datenbanklöschung entfernt diese nativen Einträge nicht.
- Löschen Sie nicht mehr gewünschte Spielaufzeichnungen, Bildschirmfotos und andere Exporte an deren Speicherorten.

Der Datenordner enthält auch den Arbeitsbereich `sgf`, Wiederherstellungsdateien und Sicherungen sowie Engine-/Modelldateien in `analysis`. Speichern Sie gewünschte wiederhergestellte Spiele vor dem Löschen. Das Löschen des gesamten KGS-Nova-Datenordners entfernt diese lokalen Daten gemeinsam.

Ältere Versionen nutzten `data.db`, `data-log.db` und `logs.txt` im App- oder Startverzeichnis. Nach einem Upgrade können diese Kopien verbleiben. Sichern Sie Benötigtes und entfernen Sie auch alte Kopien; sonst kann eine alte Datenbank erneut importiert werden, wenn die aktuelle fehlt.

Deinstallation entfernt Dateien oder native Zugangsdaten nicht unbedingt. Lokales Löschen löscht kein KGS-Konto und keine Serverdaten.

## KGS-Kontolöschung beantragen

KGS kontrolliert Konten und Serverdaten. Senden Sie eine private Anfrage mit Nutzername und Konto-E-Mail-Adresse, niemals Passwort, an [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request). Ein Administrator kann Eigentumsnachweis verlangen und erklärt löschbare Daten und Aufbewahrungspflichten. Keine Kontodaten in öffentlichen GitHub-Issues.

Private Fragen zu Desktop-Daten: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

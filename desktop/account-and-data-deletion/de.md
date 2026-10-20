---
source_revision: "3aa9378df5f32e6acf17ec4a44bd9f2964f9a6fed7d528cdcba256cfb2358d82"
layout: localized
title: "Konto und Daten löschen"
lang: "de"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/de/desktop/account-and-data-deletion/"
---

## Desktop-Daten entfernen

Schließen Sie KGS Nova. Sichern Sie exportierte Spiele, die Sie behalten möchten.

- Löschen Sie `data.db` aus dem Arbeitsverzeichnis, aus dem die App gestartet wurde. Dies entfernt gespeicherte Kontometadaten, Einstellungen, Client-Kennung und App-Zustand und setzt lokale Einstellungen zurück. Bei Terminalstart prüfen Sie dessen Verzeichnis zusätzlich zum App-Ordner.
- Löschen Sie `logs.txt` im App-Verzeichnis. Andere kopierte oder aus Konsolenausgaben gespeicherte Logs bleiben an ihrem Speicherort.
- Unter Windows liegen DPAPI-geschützte Passwörter in `data.db` und werden damit entfernt. Unter macOS/Linux löschen Sie App-Passwörter separat im Schlüsselbund/Secret-Service-Schlüsselbund. Suchen Sie den Dienst `io.github.amywarble.kgsnet.desktop.credentials` und Ihren KGS-Nutzernamen. Datenbanklöschung entfernt diese nativen Einträge nicht.
- Löschen Sie nicht mehr gewünschte Spielaufzeichnungen, Bildschirmfotos und andere Exporte an deren Speicherorten.

Deinstallation entfernt Dateien oder native Zugangsdaten nicht unbedingt. Lokales Löschen löscht kein KGS-Konto und keine Serverdaten.

## KGS-Kontolöschung beantragen

KGS kontrolliert Konten und Serverdaten. Senden Sie eine private Anfrage mit Nutzername und Konto-E-Mail-Adresse, niemals Passwort, an [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request). Ein Administrator kann Eigentumsnachweis verlangen und erklärt löschbare Daten und Aufbewahrungspflichten. Keine Kontodaten in öffentlichen GitHub-Issues.

Private Fragen zu Desktop-Daten: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

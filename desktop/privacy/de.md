---
source_revision: "c0720ca8cede62afb75cc2d2bb2188cb6f42790a1a5ec1c815ee03a2934d2d54"
layout: localized
title: "Datenschutzerklärung"
lang: "de"
page_key: "desktop/privacy"
section: "desktop"
nav_order: 10
permalink: "/de/desktop/privacy/"
---

_Gültig ab: 10. Oktober 2026_

Diese Erklärung gilt für KGS Nova unter Windows, macOS und Linux. Die App ist unabhängig, ohne Verbindung zu oder Unterstützung durch KGS. KGS betreibt einen getrennten Dienst mit eigenen [Bedingungen und Datenschutzhinweisen](https://www.gokgs.com/tos.jsp).

## Verarbeitete Informationen

Die App verbindet sich direkt mit KGS. Je nach Funktion verarbeitet sie Zugangsdaten und Profil, Räume, Chats und private/Offline-Nachrichten, soziale Listen und Notizen, Spielaufzeichnungen und Züge, Herausforderungen, Avatare und Einstellungen. Sie sendet Ihre angeforderten Aktionen und zeigt KGS-Antworten an. Andere Nutzer sehen Inhalte entsprechend der verwendeten KGS-Funktion.

An KGS gehen eine dauerhafte Client-Kennung, Protokollversion, Sprache/Region, Betriebssystem, Architektur und Laufzeitinformationen. KGS erhält auch die verwendete Netzwerkadresse.

Startet ein berechtigter Lehrer eine Unterrichtsübertragung, wird Mikrofonton über KGS an die Spielteilnehmer gesendet. Beim Empfang spielt die App KGS-Audio ab. Senden endet, wenn Sie es beenden oder die Sitzung endet. Es wird keine separate Entwickleraufnahme erstellt.

Keine Werbung, Analysefunktionen oder automatischen Absturz-Uploads. Der Entwickler hält keine separate serverseitige Kopie von Konto, Nachrichten, Spielen oder Audio.

## Lokale Speicherung und Diagnose

- **Datenbank:** `data.db` im Arbeitsverzeichnis enthält gespeicherte Kontometadaten, Client-Kennung, Einstellungen und App-Zustand. Die Datenbank als Ganzes ist nicht verschlüsselt.
- **Passwörter:** Unter Windows werden sie in der Datenbank mittels DPAPI für den aktuellen Windows-Nutzer verschlüsselt; unter macOS liegen sie im Schlüsselbund, unter Linux im Secret-Service-Schlüsselbund. Das Betriebssystem kann Entsperren oder Berechtigung verlangen. Der Passwortschutz verschlüsselt nicht die restliche Datenbank.
- **Protokolle:** `logs.txt` im App-Verzeichnis sowie Konsolen-/Debugausgabe. Die Datei wird bei jedem Start ersetzt. Möglich sind Versions-/Systemdaten, Nutzernamen, Raum-/Spielkennungen, Aktionen, Ausnahmedetails und Protokolldaten bei Verbindungs-/Nachrichtenfehlern. Gehen Sie nicht davon aus, dass Logs frei von persönlichen Inhalten sind. Keine automatische Übermittlung.
- **Exportierte Dateien:** Spielaufzeichnungen und andere bewusst gespeicherte Dateien bleiben am gewählten Ort.

Personen oder Software mit Datei- oder Betriebssystemkontozugriff können diese Daten möglicherweise lesen. Deinstallieren oder Ersetzen entfernt nicht unbedingt Datenbank, Logs, Exporte oder Schlüsselbundeinträge. Siehe [Löschanleitung]({% include page-url.html key='desktop/account-and-data-deletion' %}).

## Kommunikation und Drittanbieter

Die alte KGS-Verbindung nutzt weder TLS noch Ende-zu-Ende-Verschlüsselung. Das Anmeldeprotokoll wandelt Passwörter um, schützt aber nicht den gesamten Verkehr vor Beobachtung oder Eingriffen. Verwenden Sie ein vertrauenswürdiges Netzwerk.

KGS erklärt, Gespräche zu protokollieren und gegebenenfalls durch Administratoren prüfen zu lassen. Teilen Sie keine Informationen, die privat bleiben müssen. Servermoderation und Aufbewahrung kontrolliert KGS.

Supportseiten und Issue-Tracker unterliegen der [GitHub-Datenschutzerklärung](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Links öffnen den Browser. Eine Fehlermeldung öffnet einen editierbaren Entwurf mit App-Version, Betriebssystem, Architektur und Laufzeitdetails. Kein automatisches Absenden oder Anhängen von Logs. Eingereichte öffentliche Issues und Anhänge sind öffentlich sichtbar.

## Möglichkeiten und Kontakt

Sie können Gastsitzungen verwenden, über Speichern von Zugangsdaten entscheiden, unterstützte Privatnachrichten einschränken, Nutzer zensieren, Mikrofonübertragungen vermeiden und lokale Dateien löschen. Kontolöschung erfolgt durch KGS-Administratoren; siehe [Konto und Daten löschen]({% include page-url.html key='desktop/account-and-data-deletion' %}).

Veröffentlichen Sie keine persönlichen Daten von Kindern in Issues. Eltern/Sorgeberechtigte sollten KGS-Bedingungen und Kommunikation vor Nutzung durch Minderjährige prüfen.

Private App-/Datenschutzfragen: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). KGS-Konten und Serverdaten: [admin@gokgs.com](mailto:admin@gokgs.com). Sicherheitslücken: [private Meldung](https://github.com/amywarble/hoshi-hub/security/advisories/new).

Diese Erklärung wird bei Änderungen des Desktop-Verhaltens aktualisiert; das Gültigkeitsdatum kennzeichnet die Fassung.

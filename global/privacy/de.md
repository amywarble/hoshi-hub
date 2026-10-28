---
source_revision: "6557edaea14029268590a7f73220e26c62aafda65681a4c44da3dd659e4b7ca7"
layout: "localized"
title: "Datenschutzerklärung"
lang: "de"
page_key: "global/privacy"
section: "global"
nav_order: 3
permalink: "/de/privacy/"
redirect_from: "/de/desktop/privacy/"
---

_Gültig ab: 27. Oktober 2026_

Diese Erklärung gilt für Pocket KGS für Android, KGS Nova für Windows, macOS und Linux, Mobi für Windows und Linux sowie diese Supportwebsite. Alle drei Clients werden offiziell von KGS und der American Go Association (AGA) unterstützt. Zuerst folgen gemeinsame Praktiken, danach appspezifische Speicherung und Einstellungen.

## Wer Ihre Daten verarbeitet

Die Clients verbinden sich direkt mit dem KGS Go Server. Der Cliententwickler betreibt die KGS-Server nicht und kontrolliert weder Konten, Moderation und Aufzeichnungen noch deren Aufbewahrung. KGS ist ein eigenständiger Dienst mit eigenen [Nutzungsbedingungen und Datenschutzinformationen](https://www.gokgs.com/tos.jsp).

Die Clients enthalten keine Werbung, Analysewerkzeuge oder automatischen Absturzbericht-Uploads. Der Entwickler verkauft Ihre personenbezogenen Daten nicht und verwendet sie weder für gezielte Werbung noch für appübergreifendes Tracking. Er führt keine gesonderte serverseitige Kopie Ihres KGS-Kontos, Ihrer Chats, Partien, Avatare oder Lehrer-Audioübertragungen.

## Verarbeitete Informationen und Zwecke

Abhängig vom Client und den verwendeten Funktionen gehören dazu:

- **Konten und Profile:** KGS-Zugangsdaten, E-Mail-Adresse, Profiltext, Avatar, Rang, Kontostatus und Einstellungen.
- **Kommunikation und soziale Informationen:** Raum- und Partiechat, private und Offline-Nachrichten, Freundes-/Fan-/Zensurlisten mit Notizen sowie andere KGS-Inhalte.
- **Partien und Aktivität:** Züge, Aufzeichnungen, Kommentare, Ergebnisse, Herausforderungen, Raumzugehörigkeit und Matchmaking-Einstellungen. Mobi tauscht Spielinformationen mit der von Ihnen konfigurierten Go-Engine aus, um Züge zu erzeugen und Partien abzuwickeln.
- **Verbindungsinformationen:** dauerhafte KGS-Clientkennung, App-/Protokollversionen, Sprache, Betriebssystem und Architektur, Laufzeitinformationen und Verbindungsstatus. KGS erhält bei der Verbindung Ihre IP-Adresse.
- **Lokale Einstellungen und Diagnosen:** Einstellungen, zwischengespeicherte Inhalte und die unten beschriebenen Diagnosen.

Diese Informationen ermöglichen Anmeldung, KGS-Sitzungen, Inhaltsanzeige, das Senden angeforderter Aktionen oder konfigurierter Botaktionen an KGS, das Speichern von Einstellungen und die Fehlersuche, wenn Sie Details teilen möchten.

Pocket KGS und Nova verarbeiten außerdem Mikrofon-Audio, wenn ein berechtigter Lehrer ausdrücklich eine Liveübertragung startet, und spielen empfangenes Lehrer-Audio ab. Die Übertragung endet, wenn Sie sie stoppen oder die betreffende Sitzung endet. Keiner der Clients erstellt eine separate Audioaufnahme für den Entwickler. Mobi bietet keine Lehrer-Audiofunktionen.

## Wohin Informationen gelangen

- **KGS:** Konto- und Verbindungsinformationen, Kommunikation, Spielaktivität und gewünschte Änderungen werden an KGS gesendet. Andere Nutzer sehen Inhalte gemäß der verwendeten KGS-Funktion.
- **Zugangsdatenanbieter und Engines:** plattformeigene Zugangsdatenanbieter und Ihre gewählte Mobi-Engine verarbeiten Informationen wie unten beschrieben nach ihren eigenen Bedingungen.
- **GitHub:** Website und öffentlicher Issuetracker werden von GitHub gemäß der [GitHub-Datenschutzerklärung](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement) gehostet. Öffentliche Issues und Anhänge sind für alle sichtbar. Novas Fehlerbericht öffnet einen bearbeitbaren Browserentwurf mit Appversion, Betriebssystem, Architektur und Laufzeitdetails; weder Einreichung noch Loganhänge erfolgen automatisch.
- **Recht und Sicherheit:** dem Entwickler übermittelte Informationen können gespeichert oder offengelegt werden, soweit dies angemessen erforderlich ist, um Gesetze einzuhalten, Missbrauch zu untersuchen, Nutzer zu schützen oder Rechte und Sicherheit zu wahren.

## Kommunikation und Sicherheit

Die von diesen Clients verwendete ältere KGS-Verbindung bietet weder TLS noch Ende-zu-Ende-Verschlüsselung. Das Anmeldeprotokoll transformiert das Passwort vor der Übertragung; anderer Verkehr kann jedoch von Personen mit Zugriff auf den Netzwerkpfad gelesen oder verändert werden. Verwenden Sie ein vertrauenswürdiges Netzwerk.

KGS erklärt, dass sämtliche Gespräche protokolliert und bei der Untersuchung von Meldungen von Administratoren geprüft werden können. Teilen Sie auf KGS nichts, was privat bleiben muss. KGS bestimmt die serverseitige Aufbewahrung; Partien können in seinen Archiven verbleiben.

## App-spezifische Speicherung und Wahlmöglichkeiten

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

Pocket speichert Einstellungen, Benachrichtigungsoptionen und seine KGS-Clientkennung im privaten Android-Appspeicher sowie Avatare im Android-Cache. Android kann Cachedateien entfernen. Pocket fordert Android auf, private Appdaten nicht zu sichern. Das Löschen des Appspeichers oder die Deinstallation entfernt diese lokalen Appdaten.

Wenn Sie Zugangsdaten speichern, werden diese durch Android Credential Manager und den gewählten Anbieter nach dessen Bedingungen verwaltet. Pocket erhält keine biometrischen Daten zum Entsperren von Zugangsdaten. Gespeicherte Daten beim Anbieter müssen möglicherweise separat entfernt werden.

Produktionsversionen schreiben Fehlerdiagnosen ins Android-Systemprotokoll. Optionale Diagnoseprotokollierung liefert für die aktuelle Sitzung mehr Details. Release-Logs enthalten Versionsinformationen, Ereignisvorlagen, Ausnahmetypen und Stacktraces; ihr Format soll Laufzeitargumentwerte, Ausnahmemeldungen und Quelldateipfade auslassen. Android, Geräteadministratoren oder Personen, denen Sie Logs geben, können darauf zugreifen.

Sie können eine Gastsitzung verwenden, das Speichern von Zugangsdaten wählen, Benachrichtigungen in Pocket oder Android deaktivieren, die Mikrofonberechtigung verweigern, auf Übertragungen verzichten und Nutzer zensieren, um unterstützte Interaktionen zu blockieren und deren Inhalte auszublenden.

### KGS Nova

- **Datenbank:** `data.db` im lokalen KGS-Nova-Appdatenordner des Betriebssystems (`%LOCALAPPDATA%\KGS Nova` unter Windows) enthält gespeicherte Kontometadaten, Clientkennung, Einstellungen und Appzustand. Die Datenbank als Ganzes ist nicht verschlüsselt.
- **Passwörter:** Windows schützt gespeicherte Passwörter in der Datenbank mit DPAPI für den aktuellen Windows-Nutzer. macOS verwendet Keychain, Linux Secret Service. Das Betriebssystem kann Entsperren oder eine Berechtigung verlangen. Dies verschlüsselt nicht die übrige Datenbank.
- **Diagnosen:** Release-Fehler werden in `client.log` und rotierenden `client.archive*.log` im selben Ordner protokolliert. Optionale Sitzungsdiagnosen sind ausführlicher. Release-Logs verwenden dieselben Auslassungsregeln wie Pocket. Entwicklerversionen können ausführlichere `logs.txt` und Konsolen-/Debugausgaben erzeugen.
- **Weitere Dateien:** derselbe Ordner enthält den Arbeitsbereich `sgf`, Wiederherstellungsdateien und Sicherungen sowie Engine-/Modelldateien in `analysis`. Exportierte Partien und andere Dateien verbleiben an den von Ihnen gewählten Orten.

Personen oder Software mit Zugriff auf Ihre Dateien oder Ihr Betriebssystemkonto können diese lesen. Deinstallation oder Ersetzen von Nova entfernt Datenbank, Logs, Exporte oder Schlüsselbundeinträge nicht unbedingt. Sie können Gastsitzungen verwenden, über das Merken von Zugangsdaten entscheiden, unterstützte private Nachrichten steuern, Nutzer zensieren, Mikrofonübertragungen vermeiden und lokale Daten entfernen.

### Mobi

Mobi benötigt ein registriertes KGS-Konto. Es liest das Passwort aus `KGS_PASSWORD` und speichert es selbst nicht dauerhaft. Startskripte, Umgebungseinstellungen und Dienstmanager können dort hinterlegte Zugangsdaten aufbewahren. Schützen Sie diese und Ihr Betriebssystemkonto; eine gestartete Engine kann ihre Umgebung erben.

Ihre TOML-Konfiguration kann Kontoname, Server, Enginepfade und Spieleinstellungen enthalten. Mobi speichert die KGS-Clientkennung in einer lokalen Datei. Beim Matchmaking liegt sie standardmäßig unter `Kgs.Gtp/identities/<server-and-account-hash>` im lokalen Appdatenverzeichnis von .NET (`%LOCALAPPDATA%` unter Windows); ohne Matchmaking ist der Standard `Kgs.Gtp/client-id`. `account.clientIdFile` oder `--client-id-file` kann den Speicherort ändern.

Status, Fehler und Enginediagnosen gehen an stderr. Logs bleiben erhalten, wenn Sie die Ausgabe umleiten oder ein Dienstmanager sie aufbewahrt. Diese Logs folgen nicht den Release-Auslassungsregeln von Pocket/Nova und können Nutzernamen, Partiedetails, Pfade oder Engineausgaben enthalten. Prüfen Sie sie vor dem Teilen. Ihre Engine kann zusätzliche Logs, Partien oder andere Dateien anlegen und eigene Netzwerkaktivitäten haben; prüfen Sie deren Dokumentation und Datenschutzpraktiken separat. Mobi lädt Diagnosen nicht automatisch zum Entwickler hoch.

Sie kontrollieren Engine, Konfiguration, aufbewahrte Ausgabe und lokale Dateien. Betrieb und Diagnosen erläutert das [Mobi-Benutzerhandbuch]({% include page-url.html key='mobi/user-guide' %}).

## Aufbewahrung, Löschung und weitere Möglichkeiten

Der Entwickler erhält Ihre lokalen Dateien und Diagnosen nicht automatisch. Freiwillig zugesandte Kopien können zur Bearbeitung Ihrer Anfrage oder aus rechtlichen und Sicherheitsgründen aufbewahrt werden. Öffentliche GitHub-Issues und deren Verlauf bleiben erhalten, bis sie nach GitHubs Funktionen und Richtlinien bearbeitet oder gelöscht werden.

Sie können wählen, welche Profilinformationen Sie teilen, und Ihre KGS-E-Mail-Adresse, soweit unterstützt, als privat markieren. Dateien zu löschen oder einen Client zu deinstallieren löscht keine KGS-Daten. KGS-Administratoren bearbeiten die Löschung von Konten und Serverdaten. [Konto- und Datenlöschung]({% include page-url.html key='global/account-and-data-deletion' %}) beschreibt das gemeinsame Antragsverfahren und die lokale Datenentfernung für jeden Client.

Pocket KGS richtet sich nicht an Kinder unter 13 Jahren. KGS ist ein öffentlicher Kommunikationsdienst; Eltern oder Erziehungsberechtigte sollten vor der Nutzung durch Minderjährige dessen Bedingungen und Eignung prüfen. Veröffentlichen Sie keine personenbezogenen Kinderdaten in öffentlichen Issues.

## Änderungen und Kontakt

Halten Sie Betriebssystem und Client aktuell, verwenden Sie ein einzigartiges KGS-Passwort und prüfen Sie Logs vor dem Teilen. Kein System ist vollständig sicher. Melden Sie Schwachstellen über die [Sicherheitsrichtlinie]({% include page-url.html key='global/security-policy' %}).

Diese Erklärung kann sich mit den Clients ändern; das Gültigkeitsdatum kennzeichnet die veröffentlichte Fassung. Nutzen Sie für nicht vertrauliche Hilfe den [öffentlichen Issuetracker](https://github.com/amywarble/hoshi-hub/issues/new/choose). Private App- oder Datenschutzfragen gehen an [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). Für KGS-Konten, Serverdaten oder Moderation wenden Sie sich an [admin@gokgs.com](mailto:admin@gokgs.com).

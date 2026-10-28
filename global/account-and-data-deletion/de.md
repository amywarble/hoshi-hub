---
source_revision: "2dd2b5f3a829514cb3f4e94bc67cffcd8f04dad8b5b984ffab73449fda82c3c7"
layout: "localized"
title: "Konto und Daten löschen"
lang: "de"
page_key: "global/account-and-data-deletion"
section: "global"
nav_order: 2
permalink: "/de/account-and-data-deletion/"
redirect_from: "/de/desktop/account-and-data-deletion/"
---

_Zuletzt aktualisiert: 27. Oktober 2026_

Pocket KGS, KGS Nova und Mobi melden Sie bei Konten an, die vom KGS Go Server gehostet und kontrolliert werden. Keiner dieser Clients betreibt ein eigenes Kontosystem. KGS erstellt Konten über die [offizielle Registrierungsseite](https://www.gokgs.com/register/index.html).

Lokales Löschen oder Deinstallieren löscht **nicht** KGS-Konto, Nachrichten, Spiele, Profil oder andere bei KGS gespeicherte Daten.

## KGS-Konto und Serverdaten löschen

1. Schreiben Sie an [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) mit dem Betreff `KGS account deletion request`.
2. Bitten Sie ausdrücklich um Löschung Ihres Kontos und der zugehörigen serverseitigen Daten.
3. Nennen Sie Nutzername und Konto-E-Mail-Adresse. **Senden Sie niemals Ihr Passwort.**

Ein KGS-Administrator kann zur Eigentumsprüfung Kontakt aufnehmen, bearbeitet die Anfrage und erklärt voraussichtliche Dauer sowie notwendige Aufbewahrung aus Sicherheits-, Dienstintegritäts- oder Rechtsgründen. Die Löschung erfolgt nach Eingang und Prüfung durch einen Administrator, niemals automatisch durch Deinstallation oder lokales Löschen.

Veröffentlichen Sie keine Kontodaten in öffentlichen GitHub-Issues.

## Lokale App-Daten löschen

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

1. Öffnen Sie die Android-**Einstellungen**.
2. Wählen Sie **Apps**, dann **Pocket KGS**.
3. Öffnen Sie **Speicher und Cache**.
4. Wählen Sie **Speicherinhalt löschen** (Bezeichnung geräteabhängig) oder deinstallieren Sie die App.

Dadurch werden Einstellungen, lokale KGS-Client-Kennung und zwischengespeicherte Avatare entfernt. Pocket KGS fordert Android auf, keine Sicherung seiner privaten App-Daten anzulegen.

Über Android Credential Manager gespeicherte Passwörter entfernen Sie separat bei Ihrem gewählten Passwortmanager/Zugangsdatenanbieter. Das Löschen der App-Daten entfernt dessen Kopie nicht unbedingt.

### KGS Nova

Schließen Sie KGS Nova. Sichern Sie exportierte Spiele, die Sie behalten möchten.

- Löschen Sie `data.db` und eine vorhandene `data-log.db` aus dem Ordner KGS Nova für lokale Anwendungsdaten (`%LOCALAPPDATA%\KGS Nova` unter Windows), um gespeicherte Kontometadaten, Einstellungen, Client-Kennung und App-Zustand zu entfernen.
- Zum Entfernen der Diagnosen löschen Sie `client.log`, `client.archive*.log` und gegebenenfalls `logs.txt` aus Entwickler-Builds im selben Datenordner. Anderswo gespeicherte Kopien bleiben dort.
- Unter Windows liegen DPAPI-geschützte Passwörter in `data.db` und werden damit entfernt. Unter macOS/Linux löschen Sie App-Passwörter separat im Schlüsselbund/Secret-Service-Schlüsselbund. Suchen Sie den Dienst `io.github.amywarble.kgsnet.desktop.credentials` und Ihren KGS-Nutzernamen. Datenbanklöschung entfernt diese nativen Einträge nicht.
- Löschen Sie nicht mehr gewünschte Spielaufzeichnungen, Bildschirmfotos und andere Exporte an deren Speicherorten.

Der Datenordner enthält auch den Arbeitsbereich `sgf`, Wiederherstellungsdateien und Sicherungen sowie Engine-/Modelldateien in `analysis`. Speichern Sie gewünschte wiederhergestellte Spiele vor dem Löschen. Das Löschen des gesamten KGS-Nova-Datenordners entfernt diese lokalen Daten gemeinsam.

Ältere Versionen nutzten `data.db`, `data-log.db` und `logs.txt` im App- oder Startverzeichnis. Nach einem Upgrade können diese Kopien verbleiben. Sichern Sie Benötigtes und entfernen Sie auch alte Kopien; sonst kann eine alte Datenbank erneut importiert werden, wenn die aktuelle fehlt.

Deinstallation entfernt Dateien oder native Zugangsdaten nicht unbedingt.

### Mobi

Beenden Sie Mobi und die Engine und deaktivieren Sie Dienste oder geplante Aufgaben, die den Bot neu starten würden. Sichern Sie gewünschte Partien und Konfigurationen.

- Löschen Sie die mit `account.clientIdFile` oder `--client-id-file` gewählte Clientidentitätsdatei. Ohne Änderung verwendet Matchmaking `Kgs.Gtp/identities/<server-and-account-hash>` im lokalen Appdatenverzeichnis von .NET (`%LOCALAPPDATA%` unter Windows); andere Ausführungen verwenden `Kgs.Gtp/client-id`. Falls weitere Bots auf dem Rechner laufen, entfernen Sie nur Dateien der stillgelegten Konten.
- Entfernen Sie `KGS_PASSWORD` aus der startenden Shell und allen dauerhaften Umgebungseinstellungen, Startskripten oder Dienstkonfigurationen, in denen Sie es gespeichert haben. Mobi liest die Variable, speichert das Passwort aber selbst nicht. Entfernen Sie gespeicherte `KGS_USERNAME`-Werte und TOML-Dateien mit Kontonamen, Pfaden oder Einstellungen, wenn diese nicht mehr gebraucht werden.
- Löschen Sie durch Umleiten von stderr aufbewahrte Diagnosen wie `bot.log` sowie gespeicherte Dienstprotokolle oder andernorts geteilte Kopien, soweit Sie diese kontrollieren.
- Lesen Sie die Dokumentation Ihrer Go-Engine zur Entfernung ihrer eigenen Logs, Partien, Konfigurationen und Daten. Engine-/Modelldateien werden unabhängig von Mobi verwaltet; entfernen Sie keine Dateien, die andere Anwendungen noch nutzen.

Das Löschen der entpackten Mobi-Dateien entfernt diese Elemente nicht unbedingt. Das Entfernen einer Clientidentitätsdatei löscht weder das KGS-Konto noch dessen serverseitige Partien und setzt seinen Rang nicht zurück.

## Kontakt

Private Fragen zu den von einem dieser Clients gespeicherten Daten richten Sie an [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

---
layout: "localized"
title: "Upgrade auf Mobi vom Java-Client GTP"
nav_title: "Umstieg von Java"
lang: "de"
page_key: "mobi/upgrade-guide"
section: "mobi"
nav_order: 2
permalink: "/de/gtp/upgrade-guide/"
source_revision: "c32ebab17d841776f058eab0acfe73c12237c6953d8b7f6ec6630c41d26de6f1"
---

Diese Anleitung verschiebt einen Bot von `kgsGtp.jar` und seiner Java-Konfiguration `.properties` nach Mobi und TOML. Die alte Datei kann nicht direkt geladen werden; Es gibt keinen automatischen Importer. Bewahren Sie es als Referenz auf, wenn Sie eine neue Datei erstellen. Informationen zum Normalbetrieb und die vollständige Einstellungsreferenz finden Sie im [Benutzerhandbuch]({% include page-url.html key='mobi/user-guide' %}).

Dieses Handbuch behandelt Windows und Linux. Erweitern Sie den Abschnitt für Ihr Betriebssystem, um die Befehle PowerShell oder Bash anzuzeigen. Führen Sie die Befehle aus dem extrahierten Clientverzeichnis aus.

## Upgrade-Schritte {#upgrade-steps}

1. Beenden oder lösen Sie ein beliebiges aktuelles Spiel und stoppen Sie dann den alten Client und seine Engine.    Deaktivieren Sie den automatischen Neustart, während Sie den Austausch versuchen, damit sich nicht beide Clients mit demselben Konto anmelden.
2. Extrahieren Sie das Brückenpaket Mobi GTP für Ihre Windows- oder Linux-Architektur.    Das Paket enthält die .NET-Runtime. Behalten Sie Ihren Motor, Ihr Modell und Ihre Motorkonfiguration; diese bleiben vom Kunden getrennt.
3. Kopieren Sie [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) nach `bot.toml`. Verschieben Sie die Einstellungen mithilfe der folgenden Tabellen. Geben Sie das Passwort in `KGS_PASSWORD` ein und wählen Sie explizit den Spieltyp, die Rücknahmerichtlinie und die Anzahl der Spiele aus.
4. Testen Sie den Motor mit den folgenden Befehlen. Beheben Sie Engine-Erkennungsfehler, bevor Sie sich anmelden. Zusätzliche Prüfungen der Spielfähigkeit werden beim normalen Start ausgeführt.
5. Führen Sie ein Free-Spiel mit `--games 1` aus. Überprüfen Sie die Anmeldung, die Gegnerauswahl, die Uhren, die Wertung und die `Series: completed game 1`-Diagnose.
6. Legen Sie `games = 0` fest, wenn Sie eine kontinuierliche Wiedergabe wünschen, und aktualisieren Sie dann Ihren Launcher oder Dienst, um die neue ausführbare Datei, den neuen Konfigurationspfad, die neue Kennwortumgebung und die neuen Protokolle zu verwenden.

Kopieren Sie die Vorlage und bearbeiten Sie dann das Konto, die Engine-Pfade und die Spieleinstellungen:

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
Copy-Item .\bot.example.toml .\bot.toml
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
cp ./bot.example.toml ./bot.toml
chmod +x ./Kgs.Gtp
```

</details>

Überprüfen Sie nach der Bearbeitung die Engine-Erkennung, ohne sich anzumelden:

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --probe
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml --probe
```

</details>

Um zum alten Client zurückzukehren, stoppen Sie zunächst den neuen Client und die neue Engine, überprüfen Sie alle unvollendeten Spiele und stellen Sie Ihren ursprünglichen Launcher und Ihre Eigenschaftendatei wieder her. Bewahren Sie die Identitätsdatei des neuen Kunden für eine spätere Rückgabe an Mobi auf.

## Änderungen müssen vor dem Wechsel überprüft werden {#changes-to-review-before-switching}

| Bereich | Alter Kunde | Mobi |
| --- | --- | --- |
| Starten | `java -jar kgsGtp.jar bot.properties key=value` | `Kgs.Gtp --config bot.toml --option value`; Die ausführbare Datei Windows endet in `.exe`. |
| Konfiguration | Java-Eigenschaften, einschließlich Java-Escapes | UTF-8 TOML mit benannten Abschnitten, Zeichenfolgen in Anführungszeichen, Zahlen, Arrays und booleschen Werten. Unbekannte Schlüssel sind Fehler. |
| Standardmodus | Automatch | Kein Matchmaking, es sei denn, `matchmaking.mode` oder `--lobby` ist ausgewählt. |
| Anzahl der Spiele | Findet weiterhin Spiele | Der integrierte Standardwert ist ein abgeschlossenes Spiel. Stellen Sie `games = 0` auf kontinuierliche Wiedergabe ein. Das mitgelieferte Beispiel tut dies bereits. |
| Spieltyp | Automatch könnte Free und Ranked zusammen zulassen | Wählen Sie ausschließlich `Free` (Standard) oder `Ranked` aus. Es gibt keine gemischte Einstellung oder Fallback. |
| Zimmer | Raumname | Raumname, immer noch eine Zeichenfolge; Verwenden Sie `room = "English Room"`. Die Suche ignoriert die Groß-/Kleinschreibung und erfordert einen genauen Namen. |
| Benutzerdefinierte Spielbedingungen | Spieler könnten Änderungen vorschlagen | Konfigurierte Bedingungen müssen exakt übereinstimmen, einschließlich Farben, Komi, Handicap, Sichtbarkeit und Zeitkontrolle. |
| Rücknahmen | Normalerweise in Free-Spielen erlaubt, in Ranked abgelehnt | Beide integrierten Richtlinien sind standardmäßig auf `Never` eingestellt. Legen Sie `undo.free = "Allow"` fest, um das übliche Verhalten von Free beizubehalten. Das Beispiel tut dies. |
| Automatch Handicap | Könnte bis zu neun Ränge ermöglichen, wenn die Engine Handicap unterstützt | `maxRankDifference` ist standardmäßig `0`; Wählen Sie es explizit aus, höchstens 9 für Free oder 6 für Ranked. |
| Verbindungswiederholungen | `reconnect=t` ermöglicht fortgesetzte Wiederholungsversuche | Standardmäßiges 180-Sekunden-Ausfallbudget, exponentielles Backoff mit Jitter und Zurücksetzen nach 60 gesunden Sekunden. |
| Motorschaden | Kein automatischer Motorneustart ab `reconnect` | Separates Budget für den automatischen Neustart; Erschöpfung wartet auf die Erholung des Bedieners, während die normalen Fristen weiterlaufen. |
| Abgang des Gegners | Könnte nach Ablauf der Abwesenheitsbeschränkung zum Matchmaking zurückkehren | Der neue Client stoppt mit der Diagnose „Unbeendetes Spiel“, wenn die konfigurierte Wartezeit abläuft. |

Das Beispiel ist eine Startkonfiguration und kein Anspruch darauf, dass das gesamte alte Verhalten erhalten bleibt. Entscheiden Sie insbesondere, ob dieses Konto Free oder Ranked spielen soll, bevor Sie den Dauerbetrieb aktivieren.

## Ordnen Sie die alten Einstellungen zu {#map-the-old-settings}

Die folgenden neuen Einstellungsnamen verwenden die `section.key`-Notation. Beispielsweise bedeutet `account.username` `username = "YourBot"` unter `[account]`.

### Konto, Verbindung und Engine {#account-connection-and-engine}

| Altes Anwesen | Neue Einstellung | Migrationshinweise |
| --- | --- | --- |
| `name` | `account.username` / `--username` | `KGS_USERNAME` wird auch unterstützt, wenn kein Benutzername konfiguriert ist. |
| `password` | Umgebungsvariable `KGS_PASSWORD` | Entfernen Sie es aus der neuen Konfiguration. Passwortfelder und Passwort-CLI-Optionen werden nicht unterstützt. |
| `server.host` | `server.host` / `--host` | Zeichenfolge; Standardwert `goserver.gokgs.com`. |
| `server.port` | `server.port` / `--port` | Ganzzahl; Standardwert `2379`. |
| `reconnect=f` | `connectionRecovery.attempts = 0` | Deaktiviert KGS-Transportwiederholungen; Die Motorwiederherstellung wird separat konfiguriert. |
| `reconnect=t` | `[connectionRecovery]` | Wählen Sie ein Zeitbudget pro Ausfall; Der Standardwert ist 180 Sekunden. Eine Versuchsobergrenze ist optional. |
| `engine` | `engine.executable` und `engine.arguments` | Teilen Sie den Befehl in ausführbare und einzelne Argumente auf. siehe unten. |
| Keine Motorverbindungseigenschaften | `engine.stdio = true` / `--stdio` | Standard-I/O muss nun explizit ausgewählt werden. |
| `gtp.in`, `gtp.out` | Keine direkte Einstellung | Ein externer Launcher kann die beiden Richtungen über `--stdio` verbinden. Der Client öffnet keine benannten Dateien oder FIFOs aus der Konfiguration. |
| `engine.port` | Keine direkte Einstellung | Es gibt keinen Engine-TCP-Listener. Verwenden Sie einen externen Adapter mit `--stdio` oder lassen Sie den Client die Engine starten. |
| `logFile` | Erfassen Sie stderr extern | Verwenden Sie die Shell-Umleitung oder einen Service-Manager. Die integrierte Benennung und Rotation von Java-Protokollen wird nicht übernommen. |
| `verbose` | Keine direkte Einstellung | Die normale Diagnose geht zu stderr; Es gibt keinen entsprechenden vollständigen GTP/Server-Datenverkehrsprotokollierungsschalter. |

Der lokale `engineRecovery.pipe` dient zum Ersetzen einer ausgefallenen Engine in einer laufenden Sitzung. Es ersetzt nicht die alten Starteinstellungen `engine.port`, `gtp.in` oder `gtp.out`.

### Matchmaking und Spieleinstellungen {#matchmaking-and-game-settings}

| Altes Anwesen | Neue Einstellung | Migrationshinweise |
| --- | --- | --- |
| `mode=auto` | `matchmaking.mode = "Automatch"` | Lassen Sie Raum, benutzerdefinierte Gegnereinstellungen und die Abschnitte `game`/`timing` weg. |
| `mode=custom` | `matchmaking.mode = "Offer"` | Fügen Sie `opponentPolicy = "Any"` für offene Herausforderungen oder `"Named"` plus `opponent` hinzu. |
| `mode=wait` | `matchmaking.mode = "Join"` | Legen Sie den Raumnamen und `opponent` fest; Das angebotene Profil muss genau übereinstimmen. |
| `mode=both` | Kein kombinierter Modus | Wählen Sie für diesen Aufruf Automatch, Offer oder Join. |
| `mode=tournament` | Nicht unterstützt | Die Teilnahme am Turnier ist nicht implementiert; Behalten Sie bei Bedarf den alten Client. |
| `room` | `matchmaking.room` / `--room` | Behalten Sie den Raumnamen als Zeichenfolge in Anführungszeichen bei. Erforderlich für Offer und Join; weglassen für Automatch. Es gibt keine Standardeinstellung für den zuletzt genutzten Raum. |
| `opponent` | `matchmaking.opponent` | Für benutzerdefinierte Herausforderungen verwenden Sie `opponentPolicy = "Named"`. Lassen Sie beide benutzerdefinierten Gegnereinstellungen für Automatch weg. |
| `gameNotes` | `matchmaking.challengeNotes` | Nur Offer; höchstens 255 Zeichen ohne Steuerzeichen. |
| `rules` | `game.rules` | Verwenden Sie `Japanese`, `Chinese`, `Aga` oder `NewZealand`. Legt genaue benutzerdefinierte Spielbedingungen fest. |
| `komi` | `game.komi` | Zahl, keine Zeichenfolge in Anführungszeichen; explizit gesetzt, auch für Handicap-Spiele. |
| `rules.boardSize` | `game.boardSize` | Ganzzahl. Explizit festgelegt: Der neue Standardwert für benutzerdefinierte Spiele ist 9. |
| `rules.time` | `[timing]` | Teilen Sie die Felder mithilfe der folgenden Beispiele in System-, Sekunden- und Nachspielzeitfelder auf. |
| `automatch.speed` | `automatch.speed` | Zum Beispiel `speed = ["Blitz", "Medium"]` oder `"All"`. CLI-Kombinationen verwenden Kommas. |
| `automatch.rank` | `automatch.rank` | Zitiert `30k` bis `1k`; weiterhin erforderlich, wenn kein numerischer Serverrang vorhanden ist. |
| `undo=f` | `[undo]` mit `free = "Never"`, `ranked = "Never"` | Dies sind auch die integrierten Standardeinstellungen. |
| `undo=t` oder weggelassen | `[undo]` mit `free = "Allow"`, `ranked = "Never"` | Behält die übliche alte Unterscheidung Free/Ranked bei. Neue Ranked-Rücknahmen können auf Wunsch separat aktiviert werden. |
| `talk` | Nicht unterstützt | Private Chat-Antworten und Engine-Chat-Weiterleitung sind nicht implementiert. |
| `hint.cleanup`, `hint.noArguing` | Nicht unterstützt | Es gibt keine konfigurierbaren Chat-Hinweise zur Bewertung von Streitfällen. |

`game.rules` und `engine.rules` haben unterschiedliche Zwecke. Ersterer wählt die Regeln des benutzerdefinierten Spiels. Letzteres deklariert Regeln, die bereits in einer Engine konfiguriert sind, der `kgs-rules` fehlt; Es ändert nichts an der Konfiguration dieser Engine.

### Teilen Sie den Motorbefehl auf {#split-the-engine-command}

Eine alte Immobilie könnte sein:

```properties
engine=/opt/katago/katago gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

Die neue Konfiguration ist:

```toml
[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]
```

Fügen Sie keine ganze Befehlszeile in `executable` ein. Es gibt keine Shell-Bewertung. Jedes Argument ist ein Array-Element, einschließlich Pfaden, die Leerzeichen enthalten. Für Windows behalten Zeichenfolgen in einfachen Anführungszeichen TOML Backslashes im Literal bei:

```toml
[engine]
executable = 'C:\Go Engines\katago.exe'
arguments = ["gtp", "-config", 'C:\Go Engines\gtp.cfg', "-model", 'C:\Go Engines\model.bin.gz']
```

Ersetzen Sie Java-Eigenschaften-Escapezeichen durch den tatsächlichen Text in UTF-8 TOML. Relative ausführbare Pfade, die ein Trennzeichen enthalten, werden aus dem Verzeichnis TOML aufgelöst; Argumentpfade bleiben relativ zum Startarbeitsverzeichnis. Absolute Modell- und Konfigurationspfade erleichtern die Reproduzierbarkeit von Dienststarts.

### Konvertieren Sie Zeitsteuerungen {#convert-time-controls}

Verwenden Sie nur einen dieser `[timing]`-Abschnitte und nur mit Offer oder Join.

Alt `rules.time=0`:

```toml
[timing]
system = "None"
mainTime = 0
```

Alt `rules.time=30:00`:

```toml
[timing]
system = "Absolute"
mainTime = 1800
```

Alt `rules.time=30:00+5x0:30`:

```toml
[timing]
system = "ByoYomi"
mainTime = 1800
byoYomiTime = 30
byoYomiPeriods = 5
```

Alt `rules.time=30:00+25/10:00`:

```toml
[timing]
system = "Canadian"
mainTime = 1800
byoYomiTime = 600
canadianStones = 25
```

Alle neuen Zeitwerte sind ganzzahlige Sekunden. Entfernen Sie Nachspielzeitfelder, die zu einem anderen System gehören. Für japanische Nachspielzeit ist der Befehl `kgs-time_settings` der Engine erforderlich. es wird nicht mit einem anderen Uhrensystem angenähert.

## Beispiel: Einen Automatch-Bot migrieren {#example-migrate-an-automatch-bot}

Angenommen, die relevanten Teile der alten Datei sind:

```properties
name=YourBot
password=<account password>
mode=auto
room=English Room
automatch.speed=fast,medium
automatch.rank=20k
undo=t
reconnect=t
engine=/opt/katago/katago gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

Erstellen Sie dieses `bot.toml` für ein erstes Free-Spiel. Automatch nimmt keine Raumeinstellung an, daher wird die alte Eigenschaft `room` weggelassen:

```toml
[account]
username = "YourBot"
clientIdFile = "./state/client-id"

[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]

[matchmaking]
mode = "Automatch"
gameType = "Free"
games = 1

[automatch]
speed = ["Fast", "Medium"]
rank = "20k"
opponents = "Humans"
maxRankDifference = 0

[undo]
free = "Allow"
ranked = "Never"

[connectionRecovery]
budget = 180
resetAfter = 60
```

Ersetzen Sie für Windows die `[engine]`-Pfade durch das Windows-Beispiel in [Motorbefehl aufteilen](#split-the-engine-command). Legen Sie das Passwort fest und führen Sie ein Spiel aus:

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
$env:KGS_PASSWORD = '<account password>'
.\Kgs.Gtp.exe --config .\bot.toml --games 1
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
read -r -s -p 'KGS password: ' KGS_PASSWORD
export KGS_PASSWORD
printf '\n'
./Kgs.Gtp --config ./bot.toml --games 1
```

</details>

In diesem Beispiel werden bewusst sogar Free-Spiele ausgewählt. Um das Handicap-Matching beizubehalten, wählen Sie einen geeigneten `maxRankDifference` aus und prüfen Sie die Motorunterstützung. Um Ranked zu spielen, wählen Sie `gameType = "Ranked"` aus, überprüfen Sie die RankedRobot-Berechtigung und den aktivierten Rang des Kontos und verwenden Sie höchstens sechs Rangunterschiede. Ein Aufruf kann nicht beide Spieltypen akzeptieren.

Verwenden Sie für einen benutzerdefinierten Bot das [Beispiel für eine benutzerdefinierte Herausforderung]({% include page-url.html key='mobi/user-guide' %}#custom-challenges), kopieren Sie den alten Raumnamen und übertragen Sie explizit Brettgröße, Regeln, Komi, Farbe, Handicap und konvertierte Zeiteinstellungen.

## Motorkompatibilität und unbeaufsichtigter Betrieb {#engine-compatibility-and-unattended-operation}

Mobi erfordert GTP v2 und seinen vollständigen obligatorischen Befehlssatz. Hier sind einige Befehle erforderlich, die vom alten Client als optional behandelt wurden. Für alle automatischen Spiele ist außerdem `final_status_list` erforderlich. Zeitgesteuerte Spiele benötigen `time_left` und einen unterstützten Zeitsteuerungsbefehl. Überprüfen Sie die Engine-Anforderungen des Benutzerhandbuchs für Ihr ausgewähltes Profil. Eine alte Arbeitskonfiguration allein stellt keine Kompatibilität her.

Die übliche japanische Wertungsvereinbarung wird unterstützt, aber ungelöste japanische Streitigkeiten stoppen das Spiel. Die Bereinigung in China, AGA und Neuseeland erfordert `kgs-genmove_cleanup` und erfordert begrenzte Versuche und eine Gesamtfrist. Es gibt keinen Old-Client-Fallback, der es einem Gegner ermöglicht, über alle toten Steine ​​zu entscheiden, wenn die automatische Wertung nicht verfügbar ist.

Überprüfen Sie diese Diensteinstellungen, bevor Sie den Bot unbeaufsichtigt lassen:

- Legen Sie `games = 0` explizit fest, wenn die Wiedergabe fortgesetzt werden soll. Jeder Lobby-Versuch hat immer noch eine standardmäßige 300-Sekunden-Frist; Erhöhen Sie bei Bedarf `timeouts.lobby`.
- Konfigurieren Sie KGS Verbindungswiederholungen und Engine-Neustarts separat. Die KGS-Wiederherstellung erfolgt standardmäßig auf 180 Sekunden pro Ausfall und wird nach 60 gesunden Sekunden zurückgesetzt. Die Engine-Wiederherstellung ermöglicht drei automatische Ersetzungen während des Aufrufs. Erschöpfung kann dazu führen, dass eine Live-KGS-Sitzung auf die Wiederherstellung durch den Bediener wartet.
- Wählen Sie Pausen-, Vertagungs- und Gegner-Abwesenheitsgrenzen. Der Standardwert beträgt jeweils 300 Sekunden. Ablauf stoppt den Client, ohne das unvollendete Spiel zu zählen oder abzubrechen.
- Bewahren Sie die Client-Identitätsdatei in einem beschreibbaren Statusverzeichnis auf. Ein neuer Prozess erkennt ältere Automatch-Spiele nicht automatisch.
- Erfassen Sie stderr und veranlassen Sie die externe Protokollaufbewahrung. Exit 0 bedeutet normalen Abschluss, 1 zeigt Fehler an und 130 zeigt Abbruch an.

Das [Benutzerhandbuch]({% include page-url.html key='mobi/user-guide' %}#timeouts-and-recovery) beschreibt die Timeout-Einstellungen, die Verbindungswiederherstellung und die Wiederherstellung der Bedienermaschine im Detail.

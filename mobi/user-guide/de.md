---
layout: "localized"
title: "Mobi Benutzerhandbuch"
nav_title: "Benutzerhandbuch"
lang: "de"
page_key: "mobi/user-guide"
section: "mobi"
nav_order: 1
permalink: "/de/gtp/user-guide/"
source_revision: "26bf30c603841ace27c0d2ff994fd0d2297af607b506d24fd1ab9afabb8f1a33"
---

Mobi verbindet eine Go-Engine mit KGS, sodass diese automatisch abgespielt werden kann. Sie führen den Client in einem Terminal aus und steuern ihn über eine TOML-Konfigurationsdatei oder Befehlszeilenoptionen. Installieren und konfigurieren Sie Ihre Engine separat; Der Client kümmert sich um die Anmeldung, die Suche nach Spielen, Zügen, Uhren und die Wertung.

Wechseln Sie vom Java `kgsGtp.jar`-Client? Beginnen Sie mit der [Upgrade-Anleitung]({% include page-url.html key='mobi/upgrade-guide' %}).

Dieses Handbuch behandelt Windows und Linux. Erweitern Sie den Abschnitt für Ihr Betriebssystem, um die Befehle PowerShell oder Bash anzuzeigen. Führen Sie die Beispiele für gepackte Clients aus dem extrahierten Clientverzeichnis aus.

- [Erstes Spiel](#first-game)
- [Grundlagen der Konfiguration](#configuration-basics)
- [Spiele auswählen](#choosing-games)
- [Benutzerdefinierte Spieleinstellungen](#custom-game-settings)
- [Bot ausführen](#running-the-bot)
- [Zeitüberschreitungen und Wiederherstellung](#timeouts-and-recovery)
- [Fehlerbehebung](#troubleshooting)

## Erstes Spiel {#first-game}

Sie benötigen ein registriertes KGS-Konto, eine GTP-Engine der Version 2 sowie alle Konfigurations- und Modelldateien, die die Engine benötigt. Erstellen Sie das Konto mit einem regulären KGS-Client, bevor Sie den Bot starten. Ranked-Wiedergabe erfordert zusätzliche Serverberechtigung; Beginnen Sie mit einem Free-Spiel.

Extrahieren Sie das Client-Paket für Ihr Betriebssystem und Ihre Architektur. Es werden Pakete für Windows und Linux auf x64 und ARM64 bereitgestellt, einschließlich der .NET-Laufzeit. Halten Sie die extrahierten Dateien zusammen. Die ausführbare Datei ist `Kgs.Gtp.exe` auf Windows und `Kgs.Gtp` auf Linux.

### 1. Erstellen Sie Ihre Konfiguration {#1-create-your-configuration}

Kopieren Sie das enthaltene [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) nach `bot.toml`:

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

Bearbeiten Sie `account.username`, `engine.executable` und `engine.arguments`. Zum Beispiel:

<details markdown="1">
<summary>Windows</summary>

```toml
[account]
username = "YourBot"

[engine]
executable = 'C:\Go\katago.exe'
arguments = ["gtp", "-config", 'C:\Go\gtp.cfg', "-model", 'C:\Go\model.bin.gz']
```

</details>

<details markdown="1">
<summary>Linux</summary>

```toml
[account]
username = "YourBot"

[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]
```

</details>

Geben Sie die Pfade und Argumente an, die Ihre Engine benötigt, um in den GTP-Modus zu wechseln. Jedes Array-Element ist ein Argument; Ein Pfad, der Leerzeichen enthält, ist immer noch ein Element.

Das Beispiel wählt Free Automatch gegen Menschen, schnelle oder mittlere Geschwindigkeit und kontinuierliches Spielen aus. Stellen Sie `automatch.rank` auf einen geeigneten Schätzwert zwischen `30k` und `1k` ein, wenn das Konto keinen numerischen Rang hat. KGS verwendet den Rang des Kontos, sofern einer verfügbar ist. Für den ersten Durchgang begrenzt der folgende Befehl das Spiel auf ein Spiel.

### 2. Überprüfen Sie den Motor {#2-check-the-engine}

Führen Sie im extrahierten Clientverzeichnis Folgendes aus:

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

Der Client gibt den Engine-Namen, die Version und die unterstützten Befehle aus und wird dann beendet. Hierfür sind keine KGS-Anmeldeinformationen erforderlich und es wird keine Verbindung zu KGS hergestellt. Es überprüft die GTP-Erkennung. Die zusätzlichen Regeln, Uhr-, Handicap- und Punkteprüfungen werden beim Starten des konfigurierten Spielmodus ausgeführt.

### 3. Geben Sie das Passwort ein und spielen Sie {#3-supply-the-password-and-play}

Das Passwort stammt nur aus der Umgebungsvariablen `KGS_PASSWORD`:

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

Suchen Sie nach `Logged in to KGS` und dann nach `Game ready`. Der Client spielt und punktet das Spiel automatisch. `Game finished` zeichnet das Ergebnis von KGS auf; `Series: completed game 1` bestätigt, dass es auf die angeforderte Gesamtsumme angerechnet wurde. Anschließend meldet es sich ab und wird beendet. Das Finden eines Spiels ist standardmäßig auf fünf Minuten begrenzt; Verwenden Sie `--lobby-timeout 3600`, um bis zu einer Stunde einzuplanen.

## Konfigurationsgrundlagen {#configuration-basics}

Wählen Sie die Datei immer explizit mit `--config` aus. Der Client liest es einmal beim Start. Starten Sie neu, um die Änderungen zu übernehmen, einschließlich Änderungen an den Einstellungen für den Neustart der Engine. Es gibt keine automatische Suche nach Konfigurationsdateien oder ein Live-Neuladen.

Befehlszeilenoptionen überschreiben Dateiwerte für diese Ausführung. Zum Beispiel:

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --games 3 --undo-free Never
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml --games 3 --undo-free Never
```

</details>

Der Benutzername kommt von `--username`, dann `account.username`, dann `KGS_USERNAME`. Fügen Sie der Datei kein Passwortfeld hinzu: Es wird abgelehnt.

Verwenden Sie Zeichenfolgen in Anführungszeichen für Namen und Auswahlen, Ganzzahlen für Zählungen und Sekunden, Zahlen für Komi und `true` oder `false` für Boolesche Werte. Bei Tabellen- und Schlüsselnamen wird die Groß-/Kleinschreibung beachtet. Unbekannte Schlüssel und ungültige Werte stoppen den Start mit einer Diagnose. Alle Zeitangaben in dieser Anleitung sind Sekunden.

Ein relativer `engine.executable`, der `/` oder `\` enthält, und ein relativer `account.clientIdFile` sind relativ zum Verzeichnis der Konfigurationsdatei. Der Name einer bloßen ausführbaren Datei, wie z. B. `katago`, verwendet die ausführbare Dateisuche. Engine-Argumente werden unverändert übergeben und die Engine erbt das Arbeitsverzeichnis, von dem aus Sie den Client starten. Verwenden Sie absolute Pfade für Modell- und Engine-Konfigurationsargumente, wenn Sie aus verschiedenen Verzeichnissen starten. Zeichenfolgen in einfachen Anführungszeichen TOML behalten die umgekehrten Schrägstriche Windows bei. Zeichenfolgen erweitern keine Umgebungsvariablen.

### Konto, Server und Engine {#account-server-and-engine}

| TOML-Einstellung | CLI-Option | Bedeutung und Vorgabe |
| --- | --- | --- |
| `account.username` | `--username` | KGS Kontoname; Fällt auf `KGS_USERNAME` zurück. |
| `account.clientIdFile` | `--client-id-file` | Persistente Identitätsdatei; Wird normalerweise pro Server und Konto ausgewählt. |
| `server.host` | `--host` | KGS-Server; Standardwert `goserver.gokgs.com`. |
| `server.port` | `--port` | TCP-Port; Standardwert `2379`, Bereich 1–65535. |
| `engine.executable` | `--engine` | Ausführbare Engine-Datei zum Starten. |
| `engine.arguments` | Argumente nach `--` | Array von Engine-Argumenten; Standardmäßig leer. |
| `engine.stdio` | `--stdio` | Verwenden Sie eine extern angeschlossene Engine, anstatt eine zu starten. Standardwert `false`. |
| `engine.rules` | `--engine-rules` | Regeln, die bereits in einer Engine konfiguriert sind, in der `kgs-rules` fehlt. Keine Standarddeklaration. |

Wählen Sie eine ausführbare Datei oder `stdio = true`, niemals beides. Bei Standard-E/A muss ein anderes Programm den stdin des Clients mit dem stdout der Engine und den stdout des Clients mit dem stdin der Engine verbinden. Für die Diagnose wird stderr verwendet. Geben Sie in diesem Modus keine Engine-Argumente an.

`engine.rules` akzeptiert `Japanese`, `Chinese`, `Aga` oder `NewZealand`. Dadurch werden die vorhandenen Regeln der Engine deklariert. Konfigurieren Sie die Engine selbst entsprechend. Engines mit `kgs-rules` erhalten automatisch die Regeln des ausgewählten Spiels.

Um die Konfiguration vollständig über die Befehlszeile durchzuführen, geben Sie Engine-Argumente nach `--` ein:

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --username YourBot --engine 'C:\Go\katago.exe' `
    --lobby Automatch --automatch-rank 20k --games 1 `
    -- gtp -config 'C:\Go\gtp.cfg' -model 'C:\Go\model.bin.gz'
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --username YourBot --engine /opt/katago/katago \
    --lobby Automatch --automatch-rank 20k --games 1 \
    -- gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

</details>

Explizite CLI-Engine-Argumente ersetzen das gesamte Dateiarray. Ein nachgestellter `--` mit nichts, nachdem das Array gelöscht wurde. `--engine` und `--stdio` überschreiben die Engine-Verbindungsauswahl der Datei; `--stdio` verwirft auch dateibasierte Argumente. `--help` listet alle Optionen auf und `--version` druckt die Client-Version.

## Spiele auswählen {#choosing-games}

Wählen Sie einen Matchmaking-Modus:

| `matchmaking.mode` / `--lobby` | Was der Bot macht |
| --- | --- |
| `Automatch` | Lässt KGS einen Gegner finden und die Spielbedingungen auswählen. |
| `Offer` | Bewirbt eine benutzerdefinierte Herausforderung im benannten Raum. |
| `Join` | Sucht im genannten Raum nach einer passenden individuellen Herausforderung. |

Ohne Modus meldet sich der Client an und wartet, bis er gestoppt wird. Es werden keine Spiele gefunden. Ein Aufruf spielt jeweils ein Spiel. Gleichzeitige benutzerdefinierte Herausforderungen und Automatch, Turnierteilnahme und Chat-Antworten werden derzeit nicht unterstützt.

### Automatch {#automatch}

Verwenden Sie diese Abschnitte zusammen mit Ihren Konto- und Engine-Einstellungen:

```toml
[matchmaking]
mode = "Automatch"
gameType = "Free"
games = 0

[automatch]
speed = ["Fast", "Medium"]
rank = "20k"
opponents = "Humans"
maxRankDifference = 0
```

Lassen Sie `matchmaking.room`, `opponent`, `opponentPolicy`, `challengeNotes` und die Abschnitte `game` und `timing` im Automatch-Modus weg. Hierbei handelt es sich um benutzerdefinierte Challenge-Einstellungen, die nicht mit Automatch kombiniert werden können, selbst wenn ihre Werte mit den Standardwerten übereinstimmen.

| TOML-Einstellung | CLI-Option | Auswahlmöglichkeiten und Standard |
| --- | --- | --- |
| `automatch.speed` | `--automatch-speed` | `All` (Standard), `Blitz`, `Fast`, `Medium` oder ein Array wie `["Fast", "Medium"]`. CLI-Kombinationen verwenden Kommas. |
| `automatch.rank` | `--automatch-rank` | Geschätzter Wert `30k` bis `1k`; erforderlich, wenn das Konto keinen numerischen Serverrang hat. |
| `automatch.opponents` | `--automatch-opponents` | `Humans` (Standard), `Robots` oder `Any`. |
| `automatch.maxRankDifference` | `--automatch-max-rank-difference` | Standard `0`; Bereich 0–9 für Free, 0–6 für Ranked. |

Automatch-Partien sind öffentliche 19×19-Partien mit japanischen Regeln und vom Server zugewiesenen Farben. Gleichaufpartien verwenden Komi 6.5. Zugelassene Rangunterschiede können zu Komi 0.5 und bei Unterschieden von zwei oder mehr zu fest platzierten Vorgabesteinen führen.

| Geschwindigkeit | Hauptzeit pro Spieler | Japanisches Byo-Yomi |
| --- | --- | --- |
| `Blitz` | 60 Sekunden | 3 Perioden von 10 Sekunden |
| `Fast` | 600 Sekunden | 5 Perioden von 20 Sekunden |
| `Medium` | 1500 Sekunden | 5 Perioden von 30 Sekunden |

Die Engine muss `final_status_list`, `kgs-time_settings` und `time_left` unterstützen; Für die Zulassung einer Behinderung ist außerdem `set_free_handicap` erforderlich. Wenn `kgs-rules` fehlt, konfigurieren Sie es für japanische Regeln und legen Sie `engine.rules = "Japanese"` fest.

### Individuelle Herausforderungen {#custom-challenges}

Ersetzen Sie die Abschnitte `matchmaking` und `automatch` der Beispieldatei durch ein benutzerdefiniertes Profil. In diesem Beispiel wird berechtigten Spielern ein öffentliches 19×19 Free-Spiel angeboten:

```toml
[matchmaking]
mode = "Offer"
gameType = "Free"
opponentPolicy = "Any"
room = "Computer Go"
games = 0
challengeNotes = "Computer player: 10-minute games"

[game]
boardSize = 19
rules = "Chinese"
komi = 7.5
color = "Nigiri"
handicap = 0
private = false

[timing]
system = "Absolute"
mainTime = 600
```

Verwenden Sie den Namen des Raums wie in KGS gezeigt. Namen können Leerzeichen und Nicht-ASCII-Zeichen enthalten. Die Suche verwendet nach der Anmeldung und nach der erneuten Verbindung eine exakte Übereinstimmung ohne Berücksichtigung der Groß- und Kleinschreibung. Fehlende oder mehrdeutige Namen stoppen den Client mit einer Diagnose.

Ändern Sie für einen bestimmten Gegner `opponentPolicy` in `"Named"` und fügen Sie `opponent = "OtherAccount"` hinzu. Für `Any` `opponent` weglassen; Teilnahmeberechtigte offene Gegner sind verbundene, registrierte Konten, die nicht dieser Bot sind. Teilnahmeberechtigt sind sowohl Menschen als auch Roboter.

Um an Herausforderungen teilzunehmen, verwenden Sie `mode = "Join"` und entfernen Sie `challengeNotes`. Alle Spielbedingungen müssen übereinstimmen, einschließlich Regeln, Komi, Handicap, Sichtbarkeit und Uhren. Wählen Sie die eigene Farbe des Bots: Ein Offer-Bot, der Schwarz spielt, benötigt einen Join-Bot, der Weiß spielt; Für zufällige Farben verwenden beide `"Nigiri"`. Geänderte Bedingungen werden nicht stillschweigend akzeptiert.

| TOML-Einstellung | CLI-Option | Auswahlmöglichkeiten und Standard |
| --- | --- | --- |
| `matchmaking.mode` | `--lobby` | `Offer`, `Join` oder `Automatch`; kein Standardmodus. |
| `matchmaking.gameType` | `--game-type` | `Free` (Standard) oder `Ranked`. |
| `matchmaking.opponentPolicy` | `--opponent-policy` | `Named` (Standard für benutzerdefinierte Herausforderungen) oder `Any`. |
| `matchmaking.opponent` | `--opponent` | Erforderlich bei `Named`; Kontonamen ignorieren die Groß-/Kleinschreibung. |
| `matchmaking.room` | `--room` | Erforderlicher Raumname für Offer und Join; zum Beispiel `"Computer Go"`. |
| `matchmaking.games` | `--games` | Standard `1`; positive Zahl für eine Serie, `0` für kontinuierliches Spielen. |
| `matchmaking.challengeNotes` | `--challenge-notes` | Nur Offer; bis zu 255 Zeichen, ohne Steuerzeichen. Unterlassung erzeugt eine gegnerische Notiz. |

### Ranked Spiele {#ranked-games}

Legen Sie `matchmaking.gameType = "Ranked"` fest, um ausschließlich Ranked-Spiele anzufordern. Das Konto muss über die vom Server gewährte `RankedRobot`-Berechtigung und den aktivierten Rang verfügen. Bitten Sie einen KGS-Serveradministrator um diese Berechtigung. Ein nicht festgelegter Rang (`?`) ist zulässig, ein deaktivierter Rang (`-`) jedoch nicht. Automatch benötigt immer noch eine Schätzung, wenn das Konto keinen numerischen Rang hat.

Ranked-Gegner benötigen registrierte Konten mit aktiviertem Rang und einem Amateurrang oder noch nicht festgelegten Rang. Botgegner benötigen zusätzlich `RankedRobot`. Eigene Ranked-Herausforderungen erfordern einen öffentlichen Raum, eine öffentliche 19×19-Partie, höchstens sechs Vorgabesteine, Komi von −10 bis 10 und eine geschätzte Spielzeit von mehr als 450 Sekunden pro Spieler. Die Schätzung umfasst die Nachspielzeit; unbegrenzte Zeit ist ebenfalls zulässig. Ein Absolute-Profil mit 600 Sekunden erfüllt die Zeitvorgabe. Der Client lehnt unzulässige Einstellungen oder eine serverseitige Änderung zu Free ab.

## Benutzerdefinierte Spieleinstellungen {#custom-game-settings}

Diese Einstellungen gelten für Offer und Join. Lassen Sie sie in den Automatch-Konfigurationen außen vor.

| TOML-Einstellung | CLI-Option | Auswahlmöglichkeiten und Standard |
| --- | --- | --- |
| `game.boardSize` | `--board-size` | Standard `9`; Baureihe 2–25, vorbehaltlich Motorunterstützung. |
| `game.rules` | `--rules` | `Chinese` (Standard), `Japanese`, `Aga` oder `NewZealand`. |
| `game.komi` | `--komi` | Standard `7.5`; −100 bis 100 in Halbpunktschritten. |
| `game.color` | `--color` | `Black`, `White` oder `Nigiri`; Standardmäßig ist Schwarz für Offer und Weiß für Join. |
| `game.handicap` | `--handicap` | Standard `0`; andernfalls 2–9 innerhalb der Platzierungsgrenzen der Platine. Nicht mit Nigiri kombinierbar. |
| `game.private` | `--private` | Standard `false`; erfordert ein privates Spiel unter Beibehaltung der im ausgewählten Raum angekündigten Herausforderung. |

Handicap passt Komi nicht automatisch an. Legen Sie beides ausdrücklich fest. Japanische und AGA-Regeln verwenden feste Platzierung: mindestens 7×7, mit höchstens vier Steinen auf 7×7 oder Brettern mit gerader Seitenlänge. Chinesische und neuseeländische Regeln verwenden freie Platzierung mit höchstens neun Steinen und mindestens einem freien Schnittpunkt. Vorgabepartien benötigen `set_free_handicap`; Schwarz benötigt bei freier Platzierung außerdem `place_free_handicap`.

### Zeitkontrollen {#time-controls}

| TOML-Einstellung | CLI-Option | Standard und Bereich |
| --- | --- | --- |
| `timing.system` | `--time-system` | `Absolute` (Standard), `None`, `Canadian` oder `ByoYomi`. |
| `timing.mainTime` | `--main-time` | Standardwert `600` oder `0` für „Keine“; Bereich 0–86400. |
| `timing.byoYomiTime` | `--byo-yomi-time` | Standard `0`; 1–86400 pro japanischer Periode oder kanadischem Block bei Verwendung von Nachspielzeit. |
| `timing.byoYomiPeriods` | `--byo-yomi-periods` | Standard `0`; 1–255 für ByoYomi. |
| `timing.canadianStones` | `--canadian-stones` | Standard `0`; 1–255 für Kanadier. |

Für japanische Verlängerungen mit zehn Minuten Hauptspielzeit und fünf 30-Sekundenperioden:

```toml
[timing]
system = "ByoYomi"
mainTime = 600
byoYomiTime = 30
byoYomiPeriods = 5
```

Für kanadische Nachspielzeit verwenden Sie `system = "Canadian"`, `byoYomiTime` für Sekunden pro Block und `canadianStones` für Steine pro Block. Lassen Sie `byoYomiPeriods` weg. Nachspielzeit erlauben keine Hauptzeit. Absolut erfordert eine positive Hauptzeit und keine Nachspielzeit; None erfordert, dass alle explizit angegebenen Zeitwerte Null sind. Auch die gesamten Taktreserven müssen zur Reichweite des Servers passen; Ungültige Kombinationen werden gemeldet.

Zeitgesteuerte Spiele erfordern `time_left` und entweder `time_settings` oder `kgs-time_settings`. Für japanische Nachspielzeit ist ausdrücklich `kgs-time_settings` erforderlich. Für unbegrenzte Spiele sind keine Uhrbefehle erforderlich. Zeitüberschreitungen bei der Engine-Reaktion sind unabhängig von der Spieluhr und geben dem Bot nicht mehr Spielzeit.

## Den Bot ausführen {#running-the-bot}

Setzen Sie `matchmaking.games` auf eine positive Summe oder auf `0`, um weiterzuspielen. Es zählen nur KGS-bestätigte Ergebnisse. Nach einem abgeschlossenen Spiel verlässt der Client dieses und verwendet die ursprünglichen Matchmaking-Einstellungen für das nächste Spiel. Ein fehlgeschlagenes oder nicht beendetes Spiel stoppt die Serie, anstatt als abgeschlossen zu zählen.

Für kontinuierliches Spielen mit längerer Wartezeit zwischen den Spielen:

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --games 0 --lobby-timeout 3600
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml --games 0 --lobby-timeout 3600
```

</details>

Drücken Sie Strg+C, um zu stoppen. Der Client meldet sich ab, fordert die Engine zum Beenden auf und stoppt bei Bedarf eine gestartete Engine. Das Anhalten während eines Spiels stellt kein endgültiges Ergebnis dar. Überprüfen Sie jedes noch nicht beendete Spiel, bevor Sie einen weiteren Durchgang starten.

### Protokolle und Exit-Codes {#logs-and-exit-codes}

Status, Fehler, Hilfe und Motordiagnose finden Sie unter stderr. Um sie beizubehalten:

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml 2> .\bot.log
$LASTEXITCODE
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml 2> ./bot.log
echo $?
```

</details>

Verwenden Sie Ihren Service Manager oder externe Tools für die Protokollrotation. Im Standard-I/O-Modus bleibt stdout mit der Engine verbunden; Es trägt GTP-Befehle.

| Exit-Code | Bedeutung |
| --- | --- |
| `0` | Angeforderte Spiele abgeschlossen oder ein Probe-/Hilfe-/Versionsbefehl erfolgreich ausgeführt. |
| `1` | Konfigurations- oder Laufzeitfehler; Überprüfen Sie die Diagnose. |
| `130` | Operator-Abbruch, einschließlich Strg+C. |

### Persistenter Zustand und vorhandene Spiele {#persistent-state-and-existing-games}

Der Client speichert die durch KGS zugewiesene Identität. Im Matchmaking-Modus befindet sich die Standarddatei im lokalen Anwendungsdatenverzeichnis von .NET unter `Kgs.Gtp/identities/<server-and-account-hash>`. Bei Windows liegt dieser normalerweise unter `%LOCALAPPDATA%`. Um einen stabilen beschreibbaren Speicherort auszuwählen, legen Sie `account.clientIdFile = "./state/client-id"` fest. Behalten Sie es bei Upgrades und Container-Austauschen bei. Verwenden Sie für jeden Server und jedes Konto eine separate Datei.

Offer und Join überprüfen zunächst den ausgewählten Raum auf ein unvollendetes Spiel dieses Kontos. Es kann genau ein kompatibles Spiel fortgesetzt werden; sein Gegner und das komplette Profil müssen übereinstimmen. Mehrere oder nicht übereinstimmende Spiele stoppen den Start. Archivierte Spiele werden nicht automatisch geladen.

Eine laufende Automatch-Sitzung kann ihr zugewiesenes Spiel nach einem Verbindungsverlust wiederherstellen. Ein neuer Prozess erkennt ältere Automatch-Spiele nicht automatisch. Lösen Sie ein nicht abgeschlossenes Automatch-Spiel, bevor Sie sich erneut anmelden.

### Rücknahmen, Pausen und Abwesenheit des Gegners {#takebacks-pauses-and-opponent-absence}

`undo.free` / `--undo-free` und `undo.ranked` / `--undo-ranked` akzeptieren unabhängig voneinander `Never` (Standard) oder `Allow`. Das Beispiel erlaubt Zugrücknahmen in Free und verweigert sie in Ranked. Allow gewährt vom Server zugelassene Anfragen des Gegners während des normalen aktiven Spiels; der Bot fordert selbst keine Rücknahmen an. Anschließend spielt er den bestätigten Verlauf erneut ein, sodass die Engine GTP `undo` nicht unterstützen muss. Die Wiederaufnahme nach Zählstreitigkeiten ist davon unabhängig.

KGS steuert Pausen, Vertagungen und Wiederaufnahmen. Während er pausiert oder vertagt ist, startet der Bot kein neues Spiel oder keine Punkteaktionen. Für jede fortlaufende Pause, Unterbrechung und Abwesenheit des Gegners gibt es ein eigenes Limit, das standardmäßig auf 300 Sekunden festgelegt ist:

| TOML-Einstellung in `[interactions]` | CLI-Option |
| --- | --- |
| `pauseTimeoutFree` | `--pause-timeout-free` |
| `adjournmentTimeoutFree` | `--adjournment-timeout-free` |
| `opponentTimeoutFree` | `--opponent-timeout-free` |
| `pauseTimeoutRanked` | `--pause-timeout-ranked` |
| `adjournmentTimeoutRanked` | `--adjournment-timeout-ranked` |
| `opponentTimeoutRanked` | `--opponent-timeout-ranked` |

Jeder akzeptiert 1–86400 Sekunden. Ablauf stoppt den Client mit dem Code 1 und lässt das Spiel unvollendet; es gibt keinen Rücktritt oder beginnt ein neues Spiel. Durch erneutes Anschließen und Austausch des Motors werden diese Wartezeiten nicht zurückgesetzt. Andere aktive Fristen können früher ablaufen. Während ein Gegner abwesend ist, kann sich der Bot dennoch bewegen, wenn KGS dies zulässt.

## Auszeiten und Erholung {#timeouts-and-recovery}

### Normale Zeitüberschreitungen {#normal-timeouts}

Alle akzeptieren 1–86400 Sekunden:

| TOML-Einstellung | CLI-Option | Standard | Grenzen |
| --- | --- | --- | --- |
| `timeouts.login` | `--login-timeout` | `30` | Verbinden und anmelden. |
| `timeouts.lobby` | `--lobby-timeout` | `300` | Eine Challenge-Verhandlung oder Automatch-Registrierung; Begrenzt auch die Suche nach Raumnamen. |
| `timeouts.move` | `--move-timeout` | `600` | Eine normale oder Bereinigungs-Engine-Suche. |
| `timeouts.scoring` | `--scoring-timeout` | `120` | Eine Wertungsrunde inklusive Bewertung und Einigung. |
| `timeouts.cleanup` | `--cleanup-timeout` | `300` | Alle Aufräumversuche und anschließende Wertung zusammen. |

### KGS Verbindungsverlust {#kgs-connection-loss}

Der Client wiederholt Transportfehler, authentifiziert sich erneut und nimmt mithilfe des Serververlaufs wieder am unterbrochenen Spiel teil. Es wird kein unsicherer Zug erneut gesendet oder ein bekanntermaßen unterbrochenes Spiel durch eine neue Herausforderung ersetzt. Abgelehnte Anmeldung, Serverabmeldung, ungültige Serverdaten, illegale Engine-Verschiebungen und abgelehnte Engine-Befehle sind Terminalfehler.

| TOML-Einstellung | CLI-Option | Standard und Bereich |
| --- | --- | --- |
| `connectionRecovery.attempts` | `--reconnect-attempts` | Optionale Obergrenze pro Ausfall; 0–100. Standardmäßig weggelassen; Null deaktiviert Wiederholungsversuche. |
| `connectionRecovery.delay` | `--reconnect-delay` | `1`-zweites Anfangsfenster; 0–30, Verdoppelung auf eine 30-Sekundenobergrenze, mit vollem Jitter. |
| `connectionRecovery.timeout` | `--recovery-timeout` | `120` Sekunden pro erneuter Verbindung durch erneutes Anhängen des Spiels; 1–86400. |
| `connectionRecovery.budget` | `--recovery-budget` | `180` Sekunden insgesamt pro Ausfall, einschließlich Drain, Backoff, Login und Rejoin; 1–86400. |
| `connectionRecovery.resetAfter` | `--recovery-reset-after` | `60` gesunde Sekunden nach dem erneuten Anhängen, bevor das Budget und die Anzahl der Wiederholungsversuche zurückgesetzt werden; 1–86400. |
| `connectionRecovery.engineDrainTimeout` | `--engine-drain-timeout` | `30` Sekunden, um die Arbeit am alten Motor abzuschließen und zu verwerfen; 1–86400. |

Das Ausfallbudget beginnt, wenn ein Verbindungsverlust erkannt wird. Jede erneute Verbindung ist durch das verbleibende Budget sowie durch ein eigenes Anmelde-/Wiederverbindungs-Timeout begrenzt. Jede Backoff-Verzögerung wird zufällig zwischen Null und einer Obergrenze ausgewählt, die sich von 1 Sekunden auf eine 30-Sekunden-Obergrenze verdoppelt. Die Wiederherstellung stoppt, wenn das Gesamtbudget oder eine explizite Versuchsobergrenze erschöpft ist.

Nach dem erneuten Anschließen kann der Bot über die alte Wiederherstellungsfrist hinaus weiterspielen. Eine spätere Trennung erhält nach 60 gesunden Sekunden ein neues Budget. Bei einer Trennung vor diesem Intervall bleiben die vorherige Frist und die Anzahl der Wiederholungsversuche erhalten, einschließlich der Zeit, in der die Verbindung kurzzeitig hergestellt wurde. Die Anmeldung allein stellt noch keinen Zustand dar, wenn einem Spiel noch einmal beigetreten werden muss.

### Motorschaden {#engine-failure}

Wenn eine laufende Engine beendet wird oder ihr Stream unbrauchbar wird, hält der Client die KGS-Sitzung aktiv und versucht, einen Ersatz unter Verwendung der ursprünglichen ausführbaren Datei und der ursprünglichen Argumente zu starten. Es überprüft den Austausch und spielt den bestätigten Verlauf ab, bevor es fortfährt. Anfängliche Engine-Start-/Erkennungsfehler stoppen den Client. KGS-Uhren laufen weiter, während die Engine nicht verfügbar ist.

| TOML-Einstellung | CLI-Option | Standard und Bereich |
| --- | --- | --- |
| `engineRecovery.attempts` | `--engine-restart-attempts` | `3` automatische Ersetzungen während des gesamten Aufrufs; 0–100. Null wartet auf die Wiederherstellung des Bedieners. |
| `engineRecovery.delay` | `--engine-restart-delay` | `1`-zweites Anfangsfenster; 0–30, Verdoppelung auf eine 30-Sekundenobergrenze, mit vollem Jitter. |
| `engineRecovery.timeout` | `--engine-recovery-timeout` | `120` Sekunden für die Erkennung/Einrichtung und separat für die Wiedergabe; 1–86400. |
| `engineRecovery.pipe` | `--engine-recovery-pipe` | Lokale Rückgewinnungsleitung; Standardwert `kgs-gtp-<process ID>`. Verwenden Sie 1–100 ASCII-Buchstaben, Ziffern, Punkte, Bindestriche oder Unterstriche. |

Wenn die automatischen Ersetzungen erschöpft sind, benennt die Diagnose eine lokale Wiederherstellungspipeline. Der Bot wartet auf das Eingreifen des Bedieners, während die normalen Spiel- und Lobbyfristen weiterlaufen. Um eine vom Client gestartete Engine neu zu starten, stellen Sie eine Verbindung mit demselben Betriebssystembenutzer her und senden Sie UTF-8 `restart` gefolgt von LF. Wenn Sie beispielsweise `pipe = "YourBot-recovery"` konfiguriert haben, führen Sie dies nach der Wartediagnose in einem anderen Terminal aus:

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
$pipe = [IO.Pipes.NamedPipeClientStream]::new(
    '.', 'YourBot-recovery', [IO.Pipes.PipeDirection]::InOut)
try {
    $pipe.Connect(5000)
    $request = [Text.Encoding]::UTF8.GetBytes("restart`n")
    $pipe.Write($request, 0, $request.Length)
    $pipe.Flush()
}
finally { $pipe.Dispose() }
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
python3 - <<'PY'
import os
import socket

pipe = os.path.join(os.environ.get("TMPDIR") or "/tmp", "CoreFxPipe_YourBot-recovery")
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as connection:
    connection.settimeout(5)
    connection.connect(pipe)
    connection.sendall(b"restart\n")
PY
```

</details>

Das Linux-Beispiel erfordert Python 3 und stellt eine Verbindung zum Unix-Domänen-Socket von .NET her. Führen Sie es unter demselben Benutzer aus, mit demselben `TMPDIR` wie der Bot (der Standardwert ist `/tmp`). Ersetzen Sie `YourBot-recovery` durch den konfigurierten Pipe-Namen. Ein Dienst mit einem privaten temporären Verzeichnis erfordert auch, dass der Client in derselben Umgebung ausgeführt wird.

Bei einem erfolgreichen Betreiberwechsel wird ein neues automatisches Wiederholungsbudget gestartet. Durch das Bearbeiten der Datei TOML werden die ausführbare Datei oder die Argumente des ausgeführten Clients nicht geändert.

Für `--stdio` muss ein externer Supervisor einen neuen Motor über die Duplex-Rückgewinnungsleitung anschließen und GTP in beide Richtungen weiterleiten. In diesem Modus gibt es keine `restart`-Begrüßung. Die ursprüngliche stdin/stdout-Verbindung kann nach einem Fehler nicht wiederverwendet werden.

## Fehlerbehebung {#troubleshooting}

| Symptom | Was zu überprüfen ist |
| --- | --- |
| Konfigurationsfehler vor Motorstart | Überprüfen Sie die benannte Datei und den Quellspeicherort, die genaue Schreibweise der Schlüssel, die Raumnamen in Anführungszeichen und die Werttypen TOML. Ältere Java-Eigenschaftendateien müssen konvertiert werden. |
| Motor kann nicht starten oder sein Modell öffnen | Überprüfen Sie die Pfade der ausführbaren Dateien und Argumente, die Argumente im GTP-Modus und das Arbeitsverzeichnis. Versuchen Sie es mit `--probe`. |
| Fehlende GTP-Befehle oder falsche Protokollversion | Verwenden Sie eine vollständige GTP v2-Engine. Für die Erkennung sind `protocol_version`, `name`, `version`, `known_command`, `list_commands`, `quit`, `boardsize`, `clear_board` erforderlich. `komi`, `play` und `genmove`. |
| Die Überprüfung der Regeln, des Timings oder der Wertung schlägt fehl | Überprüfen Sie die Engine-Funktionen für das ausgewählte Profil. Deklarieren Sie `engine.rules` nur, wenn der Engine `kgs-rules` fehlt, und stellen Sie sicher, dass die tatsächliche Konfiguration übereinstimmt. Für alle automatischen Spiele ist `final_status_list` erforderlich. |
| Die Anmeldung schlägt fehl | Überprüfen Sie den Kontonamen `KGS_PASSWORD` in der Startumgebung, die Serveradresse und den gemeldeten Ablehnungsgrund. |
| Zimmer wurde nicht gefunden | Kopieren Sie den vollständigen Namen von KGS auf dem ausgewählten Server. Beim Matching wird die Groß-/Kleinschreibung ignoriert, es ist jedoch der gesamte Name erforderlich. |
| Warten auf eine Spiel- oder Lobby-Zeitüberschreitung | Überprüfen Sie übereinstimmende Bedingungen, die Teilnahmeberechtigung des Gegners, den Raumnamen und die Automatch-Einstellungen. Erhöhen Sie `timeouts.lobby`, wenn eine längere Wartezeit beabsichtigt ist. |
| Ranked-Eintrag abgelehnt | Überprüfen Sie die RankedRobot-Berechtigung, den aktivierten Rang, den öffentlichen Raum und die Profilbeschränkungen Ranked. |
| Bei einer Meinungsverschiedenheit endet die Wertung | Japanische Streitigkeiten werden nicht unterstützt. Für die Bereinigung in Chinesisch, AGA und Neuseeland ist `kgs-genmove_cleanup` erforderlich. Wiederholte Streitigkeiten, mangelnder Fortschritt und der Ablauf der Bereinigung stoppen den Kunden. |
| Der Bot stoppt nach einer Pause oder dem Weggang des Gegners | Überprüfen Sie die relevante Interaktionszeitüberschreitung und überprüfen Sie das noch nicht beendete Spiel, bevor Sie es neu starten. |
| Engine nicht verfügbar, aber Konto noch online | Überprüfen Sie die Motordiagnose und die Meldung zur Wiederherstellungsleitung. Automatische Wiederholungsversuche sind möglicherweise ausgeschöpft. Spieluhren und Fristen laufen noch. |
| Fehler in der Identitätsdatei | Stellen Sie sicher, dass der konfigurierte Statusspeicherort beschreibbar ist und die vom Client generierte Identitätsdatei enthält. |

Wenn Sie ein Problem melden, geben Sie die Client-Version, den Namen/die Version der Engine, die Spiel-ID (sofern verfügbar), relevante Einstellungen und die Diagnose stderr an. Passwörter weglassen.

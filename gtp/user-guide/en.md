---
layout: localized
title: "GTP user guide"
lang: "en"
page_key: "gtp/user-guide"
section: "gtp"
nav_order: 1
permalink: "/gtp/user-guide/"
---

Kgs.Gtp connects a Go engine to KGS so that it can play automatically. You run
the client in a terminal and control it through a TOML configuration file or
command-line options. Install and configure your engine separately; the client
handles login, finding games, moves, clocks, and scoring.

Moving from the Java `kgsGtp.jar` client? Start with the
[upgrade guide]({% include page-url.html key='gtp/upgrade-guide' %}).

This guide covers Windows and Linux. Expand the section for your operating
system to see PowerShell or Bash commands. Run the packaged-client examples
from the extracted client directory.

- [First game](#first-game)
- [Configuration basics](#configuration-basics)
- [Choosing games](#choosing-games)
- [Custom game settings](#custom-game-settings)
- [Running the bot](#running-the-bot)
- [Timeouts and recovery](#timeouts-and-recovery)
- [Troubleshooting](#troubleshooting)

## First game

You need a registered KGS account, a GTP version 2 engine, and any configuration
and model files that engine requires. Create the account using a regular KGS
client before starting the bot. Ranked play needs additional server permission;
start with a Free game.

Extract the client package for your operating system and architecture. Packages
are provided for Windows and Linux on x64 and ARM64, with the .NET runtime
included. Keep the extracted files together. The executable is `Kgs.Gtp.exe` on
Windows and `Kgs.Gtp` on Linux.

### 1. Create your configuration

Copy the included [bot.example.toml]({{ '/gtp/bot.example.toml' | relative_url }}) to `bot.toml`:

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

Edit `account.username`, `engine.executable`, and `engine.arguments`. For example:

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

Supply the paths and arguments your engine needs to enter GTP mode. Each array
element is one argument; a path containing spaces is still one element.

The example selects Free automatch against humans, Fast or Medium speed, and
continuous play. Set `automatch.rank` to an appropriate estimate between `30k`
and `1k` if the account does not have a numeric rank. KGS uses the account's rank
when one is available. For the first run, the command below limits play to one game.

### 2. Check the engine

From the extracted client directory, run:

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

The client prints the engine name, version, and supported commands, then exits.
This needs no KGS credentials and does not connect to KGS. It checks GTP discovery;
the additional rules, clock, handicap, and scoring checks run when starting the
configured game mode.

### 3. Supply the password and play

The password comes only from the `KGS_PASSWORD` environment variable:

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

Look for `Logged in to KGS`, then `Game ready`. The client plays and scores the
game automatically. `Game finished` records KGS's result; `Series: completed
game 1` confirms it counted toward the requested total. It then logs out and exits.
Finding a game is limited to five minutes by default; use
`--lobby-timeout 3600` to allow up to an hour.

## Configuration basics

Always select the file explicitly with `--config`. The client reads it once at
startup. Restart to apply edits, including changes to engine restart settings.
There is no automatic configuration-file search or live reload.

Command-line options override file values for that run. For example:

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

The username comes from `--username`, then `account.username`, then
`KGS_USERNAME`. Do not add a password field to the file: it is rejected.

Use quoted strings for names and selections, integers for counts and seconds,
numbers for komi, and `true` or `false` for booleans. Table and key names are
case-sensitive. Unknown keys and invalid values stop startup with a diagnostic.
All durations in this guide are seconds.

A relative `engine.executable` containing `/` or `\`, and a relative
`account.clientIdFile`, are relative to the configuration file's directory. A
bare executable name, such as `katago`, uses executable lookup. Engine arguments
are passed unchanged and the engine inherits the working directory from which
you launch the client. Use absolute paths for model and engine configuration
arguments if you launch from different directories. Single-quoted TOML strings
preserve Windows backslashes. Strings do not expand environment variables.

### Account, server, and engine

| TOML setting | CLI option | Meaning and default |
| --- | --- | --- |
| `account.username` | `--username` | KGS account name; falls back to `KGS_USERNAME`. |
| `account.clientIdFile` | `--client-id-file` | Persistent identity file; normally chosen per server and account. |
| `server.host` | `--host` | KGS server; default `goserver.gokgs.com`. |
| `server.port` | `--port` | TCP port; default `2379`, range 1–65535. |
| `engine.executable` | `--engine` | Engine executable to launch. |
| `engine.arguments` | Arguments after `--` | Array of engine arguments; default empty. |
| `engine.stdio` | `--stdio` | Use an externally connected engine instead of launching one; default `false`. |
| `engine.rules` | `--engine-rules` | Rules already configured in an engine lacking `kgs-rules`. No default declaration. |

Choose an executable or `stdio = true`, never both. With standard I/O, another
program must connect the client's stdin to the engine's stdout and the client's
stdout to the engine's stdin. Diagnostics use stderr. Do not supply engine
arguments in this mode.

`engine.rules` accepts `Japanese`, `Chinese`, `Aga`, or `NewZealand`. This declares
the engine's existing rules; configure the engine itself to match. Engines with
`kgs-rules` receive the selected game's rules automatically.

To configure entirely on the command line, put engine arguments after `--`:

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

Explicit CLI engine arguments replace the entire file array. A trailing `--`
with nothing after it clears that array. `--engine` and `--stdio` override the
file's engine connection choice; `--stdio` also discards file-based arguments.
`--help` lists all options, and `--version` prints the client version.

## Choosing games

Select one matchmaking mode:

| `matchmaking.mode` / `--lobby` | What the bot does |
| --- | --- |
| `Automatch` | Lets KGS find an opponent and choose the game terms. |
| `Offer` | Advertises a custom challenge in the named room. |
| `Join` | Looks for a matching custom challenge in the named room. |

Without a mode, the client logs in and waits until stopped; it does not find games.
One invocation plays one game at a time. Simultaneous custom challenges and
automatch, tournament entry, and chat replies are currently unsupported.

### Automatch

Use these sections alongside your account and engine settings:

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

Omit `matchmaking.room`, `opponent`, `opponentPolicy`, `challengeNotes`, and the
`game` and `timing` sections in Automatch mode. These are custom challenge settings
and cannot be combined with automatch, even if their values match its defaults.

| TOML setting | CLI option | Choices and default |
| --- | --- | --- |
| `automatch.speed` | `--automatch-speed` | `All` (default), `Blitz`, `Fast`, `Medium`, or an array such as `["Fast", "Medium"]`. CLI combinations use commas. |
| `automatch.rank` | `--automatch-rank` | Estimated `30k` through `1k`; required when the account has no numeric server rank. |
| `automatch.opponents` | `--automatch-opponents` | `Humans` (default), `Robots`, or `Any`. |
| `automatch.maxRankDifference` | `--automatch-max-rank-difference` | Default `0`; range 0–9 for Free, 0–6 for Ranked. |

Automatch games are public 19×19 games using Japanese rules and server-assigned
colors. Even games use komi 6.5. Allowing rank differences can produce komi 0.5
and, for differences of two or more, fixed handicap stones.

| Speed | Main time per player | Japanese byo-yomi |
| --- | --- | --- |
| `Blitz` | 60 seconds | 3 periods of 10 seconds |
| `Fast` | 600 seconds | 5 periods of 20 seconds |
| `Medium` | 1500 seconds | 5 periods of 30 seconds |

The engine must support `final_status_list`, `kgs-time_settings`, and `time_left`;
allowing handicap also requires `set_free_handicap`. If it lacks `kgs-rules`,
configure it for Japanese rules and set `engine.rules = "Japanese"`.

### Custom challenges

Replace the example file's `matchmaking` and `automatch` sections with a custom
profile. This example offers a public 19×19 Free game to eligible players:

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

Use the room's name as shown in KGS. Names may contain spaces and non-ASCII
characters. Lookup uses a case-insensitive exact match after login and again
after reconnection. Missing or ambiguous names stop the client with a diagnostic.

For one specific opponent, change `opponentPolicy` to `"Named"` and add
`opponent = "OtherAccount"`. For `Any`, omit `opponent`; eligible open opponents
are connected, registered accounts other than this bot. Both humans and robots
are eligible.

To join challenges, use `mode = "Join"` and remove `challengeNotes`. Every game
term must match, including rules, komi, handicap, visibility, and clocks. Choose
the bot's own color: an Offer bot playing Black needs a Join bot playing White;
for random colors both use `"Nigiri"`. Changed terms are not silently accepted.

| TOML setting | CLI option | Choices and default |
| --- | --- | --- |
| `matchmaking.mode` | `--lobby` | `Offer`, `Join`, or `Automatch`; no default mode. |
| `matchmaking.gameType` | `--game-type` | `Free` (default) or `Ranked`. |
| `matchmaking.opponentPolicy` | `--opponent-policy` | `Named` (default for custom challenges) or `Any`. |
| `matchmaking.opponent` | `--opponent` | Required with `Named`; account names ignore case. |
| `matchmaking.room` | `--room` | Required room name for Offer and Join; for example `"Computer Go"`. |
| `matchmaking.games` | `--games` | Default `1`; positive number for a series, `0` for continuous play. |
| `matchmaking.challengeNotes` | `--challenge-notes` | Offer only; up to 255 characters, without control characters. Omission generates an opponent note. |

### Ranked games

Set `matchmaking.gameType = "Ranked"` to request Ranked games exclusively.
The account must have server-granted `RankedRobot` permission and rank enabled.
Ask a KGS server administrator for that permission. An unset rank (`?`) is
allowed, but disabled rank (`-`) is not; automatch still needs an estimate when
the account has no numeric rank.

Ranked opponents must be registered, rank-enabled amateur accounts or have an
unset rank. Robot opponents also need `RankedRobot` permission. Ranked custom
challenges need a public room, a public 19×19 game, at most six handicap stones,
komi from −10 to 10, and estimated playing time greater than 450 seconds per
player. The estimate includes overtime; unlimited time is also allowed. A
600-second Absolute profile satisfies the timing restriction. The client rejects
ineligible settings or a server change to Free.

## Custom game settings

These settings apply to Offer and Join. Leave them out of Automatch configurations.

| TOML setting | CLI option | Choices and default |
| --- | --- | --- |
| `game.boardSize` | `--board-size` | Default `9`; range 2–25, subject to engine support. |
| `game.rules` | `--rules` | `Chinese` (default), `Japanese`, `Aga`, or `NewZealand`. |
| `game.komi` | `--komi` | Default `7.5`; −100 to 100 in half-point increments. |
| `game.color` | `--color` | `Black`, `White`, or `Nigiri`; defaults to Black for Offer and White for Join. |
| `game.handicap` | `--handicap` | Default `0`; otherwise 2–9 within the board's placement limits. Cannot be combined with Nigiri. |
| `game.private` | `--private` | Default `false`; requires a private game while keeping the challenge advertised in the selected room. |

Handicap does not adjust komi automatically. Set both explicitly. Japanese and
AGA use fixed placement: at least 7×7, with at most four stones on 7×7 or even-sized
boards. Chinese and New Zealand use free placement, with at most nine stones
and at least one empty intersection. Handicap games need `set_free_handicap`;
Black also needs `place_free_handicap` for free placement.

### Time controls

| TOML setting | CLI option | Default and range |
| --- | --- | --- |
| `timing.system` | `--time-system` | `Absolute` (default), `None`, `Canadian`, or `ByoYomi`. |
| `timing.mainTime` | `--main-time` | Default `600`, or `0` for None; range 0–86400. |
| `timing.byoYomiTime` | `--byo-yomi-time` | Default `0`; 1–86400 per Japanese period or Canadian block when using overtime. |
| `timing.byoYomiPeriods` | `--byo-yomi-periods` | Default `0`; 1–255 for ByoYomi. |
| `timing.canadianStones` | `--canadian-stones` | Default `0`; 1–255 for Canadian. |

For Japanese overtime with ten minutes of main time and five 30-second periods:

```toml
[timing]
system = "ByoYomi"
mainTime = 600
byoYomiTime = 30
byoYomiPeriods = 5
```

For Canadian overtime, use `system = "Canadian"`, `byoYomiTime` for seconds per
block, and `canadianStones` for stones per block. Omit `byoYomiPeriods`. Overtime
allows zero main time. Absolute requires positive main time and no overtime;
None requires all explicitly supplied time values to be zero. Total clock
reserves must also fit the server's range; invalid combinations are reported.

Timed games require `time_left` and either `time_settings` or `kgs-time_settings`.
Japanese overtime specifically requires `kgs-time_settings`. Unlimited games
do not require clock commands. Engine response timeouts are separate from the
game's clock and do not give the bot more playing time.

## Running the bot

Set `matchmaking.games` to a positive total, or to `0` to keep playing. Only
KGS-confirmed results count. After a completed game, the client leaves it and
uses the original matchmaking settings for the next game. A failed or unfinished
game stops the series instead of counting as completed.

For continuous play with a longer wait between games:

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

Press Ctrl+C to stop. The client logs out, asks the engine to quit, and stops an
engine it launched if necessary. Stopping during a game does not establish a
final result. Inspect any unfinished game before starting another run.

### Logs and exit codes

Status, errors, help, and engine diagnostics go to stderr. To retain them:

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

Use your service manager or external tools for log rotation. In standard-I/O
mode, keep stdout connected to the engine; it carries GTP commands.

| Exit code | Meaning |
| --- | --- |
| `0` | Requested games completed, or a probe/help/version command succeeded. |
| `1` | Configuration or runtime failure; inspect the diagnostic. |
| `130` | Operator cancellation, including Ctrl+C. |

### Persistent state and existing games

The client saves the identity assigned by KGS. In matchmaking modes the default
file is under .NET's local application-data directory at
`Kgs.Gtp/identities/<server-and-account-hash>`. On Windows this is normally below
`%LOCALAPPDATA%`. To choose a stable writable location, set
`account.clientIdFile = "./state/client-id"`. Preserve it across upgrades and
container replacements. Use a separate file for each server and account.

Offer and Join first check the selected room for an unfinished game belonging
to this account. Exactly one compatible game can be resumed; its opponent and
complete profile must match. Multiple or mismatched games stop startup. Archived
games are not loaded automatically.

A running automatch session can recover its assigned game after connection loss.
A fresh process does not discover older automatch games automatically. Resolve
an unfinished automatch game before enrolling again.

### Takebacks, pauses, and opponent absence

`undo.free` / `--undo-free` and `undo.ranked` / `--undo-ranked` independently
accept `Never` (the default) or `Allow`. The supplied example allows Free
takebacks and refuses Ranked takebacks. Allow grants server-permitted opponent
requests during ordinary active play; the bot does not request takebacks itself.
It replays confirmed history afterward, so engine support for GTP `undo` is not
required. Scoring-dispute resumption is separate from this policy.

KGS controls pauses, adjournment, and resumption. While paused or adjourned the
bot starts no new gameplay or scoring actions. Each continuous pause, adjournment,
and opponent absence has a separate limit, defaulting to 300 seconds:

| TOML setting in `[interactions]` | CLI option |
| --- | --- |
| `pauseTimeoutFree` | `--pause-timeout-free` |
| `adjournmentTimeoutFree` | `--adjournment-timeout-free` |
| `opponentTimeoutFree` | `--opponent-timeout-free` |
| `pauseTimeoutRanked` | `--pause-timeout-ranked` |
| `adjournmentTimeoutRanked` | `--adjournment-timeout-ranked` |
| `opponentTimeoutRanked` | `--opponent-timeout-ranked` |

Each accepts 1–86400 seconds. Expiry stops the client with code 1 and leaves the
game unfinished; it does not resign or begin another game. Reconnection and
engine replacement do not reset these waits. Other active deadlines can expire
sooner. While an opponent is absent, the bot may still move if KGS permits it.

## Timeouts and recovery

### Normal timeouts

All accept 1–86400 seconds:

| TOML setting | CLI option | Default | Limits |
| --- | --- | --- | --- |
| `timeouts.login` | `--login-timeout` | `30` | Connecting and logging in. |
| `timeouts.lobby` | `--lobby-timeout` | `300` | One challenge negotiation or automatch enrollment; also bounds room-name lookup. |
| `timeouts.move` | `--move-timeout` | `600` | One normal or cleanup engine search. |
| `timeouts.scoring` | `--scoring-timeout` | `120` | One scoring round, including evaluation and agreement. |
| `timeouts.cleanup` | `--cleanup-timeout` | `300` | All cleanup attempts and subsequent scoring together. |

### KGS connection loss

The client retries transport failures, authenticates again, and rejoins the
interrupted game using server history. It does not resend an uncertain move or
replace a known interrupted game with a new challenge. Rejected login, server
logout, invalid server data, illegal engine moves, and rejected engine commands
are terminal failures.

| TOML setting | CLI option | Default and range |
| --- | --- | --- |
| `connectionRecovery.attempts` | `--reconnect-attempts` | Optional cap per outage; 0–100. Omitted by default; zero disables retries. |
| `connectionRecovery.delay` | `--reconnect-delay` | `1`-second initial window; 0–30, doubling to a 30-second cap, with full jitter. |
| `connectionRecovery.timeout` | `--recovery-timeout` | `120` seconds per reconnect through game reattachment; 1–86400. |
| `connectionRecovery.budget` | `--recovery-budget` | `180` seconds total per outage, including drain, backoff, login, and rejoin; 1–86400. |
| `connectionRecovery.resetAfter` | `--recovery-reset-after` | `60` healthy seconds after reattachment before resetting the budget and retry count; 1–86400. |
| `connectionRecovery.engineDrainTimeout` | `--engine-drain-timeout` | `30` seconds to finish and discard old engine work; 1–86400. |

The outage budget starts when connection loss is detected. Every reconnect is
limited by the remaining budget as well as its own login/rejoin timeout. Each
backoff delay is selected randomly between zero and a ceiling that doubles from
1 second to a 30-second cap. Recovery stops when the total budget or an explicit
attempt cap is exhausted.

After reattachment, the bot can continue playing beyond the old recovery deadline.
A later disconnect gets a fresh budget after 60 healthy seconds. A disconnect
before that interval retains the previous deadline and retry count, including
the briefly connected time. Login alone does not establish health when a game
still needs to be rejoined.

### Engine failure

If a running engine exits or its stream becomes unusable, the client keeps the
KGS session active and attempts to start a replacement using the original
executable and arguments. It checks the replacement and replays confirmed
history before continuing. Initial engine startup/discovery failures stop the
client. KGS clocks continue while the engine is unavailable.

| TOML setting | CLI option | Default and range |
| --- | --- | --- |
| `engineRecovery.attempts` | `--engine-restart-attempts` | `3` automatic replacements across the invocation; 0–100. Zero waits for operator recovery. |
| `engineRecovery.delay` | `--engine-restart-delay` | `1`-second initial window; 0–30, doubling to a 30-second cap, with full jitter. |
| `engineRecovery.timeout` | `--engine-recovery-timeout` | `120` seconds for discovery/setup and separately for replay; 1–86400. |
| `engineRecovery.pipe` | `--engine-recovery-pipe` | Local recovery pipe; default `kgs-gtp-<process ID>`. Use 1–100 ASCII letters, digits, periods, hyphens, or underscores. |

When automatic replacements are exhausted, the diagnostic names a local recovery
pipe. The bot waits for operator intervention while normal game and lobby
deadlines continue. To restart an engine launched by the client, connect as the
same operating-system user and send UTF-8 `restart` followed by LF. For example,
if you configured `pipe = "YourBot-recovery"`, run this in another terminal
after the waiting diagnostic:

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

The Linux example requires Python 3 and connects to .NET's Unix-domain socket.
Run it as the same user, with the same `TMPDIR` as the bot (the default is `/tmp`).
Replace `YourBot-recovery` with the configured pipe name; a service with a private
temporary directory also needs the client to run inside that same environment.

A successful operator replacement starts a fresh automatic retry budget. Editing
the TOML file does not change the running client's executable or arguments.

For `--stdio`, an external supervisor must attach a fresh engine through the
duplex recovery pipe and relay GTP in both directions. There is no `restart`
greeting in this mode. The original stdin/stdout connection cannot be reused
after failure.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Configuration error before engine startup | Check the named file and source location, exact key spelling, quoted room names, and TOML value types. Legacy Java properties files need conversion. |
| Engine cannot start or open its model | Check executable and argument paths, GTP-mode arguments, and the working directory. Try `--probe`. |
| Missing GTP commands or wrong protocol version | Use a complete GTP v2 engine. Discovery requires `protocol_version`, `name`, `version`, `known_command`, `list_commands`, `quit`, `boardsize`, `clear_board`, `komi`, `play`, and `genmove`. |
| Rules, timing, or scoring check fails | Check engine capabilities for the selected profile. Declare `engine.rules` only when the engine lacks `kgs-rules`, and make its actual configuration match. All automatic games require `final_status_list`. |
| Login fails | Check the account name, `KGS_PASSWORD` in the launching environment, server address, and reported rejection reason. |
| Room is not found | Copy its full name from KGS on the selected server. Matching ignores case but requires the whole name. |
| Waiting for a game or lobby timeout | Check matching terms, opponent eligibility, room name, and automatch preferences. Increase `timeouts.lobby` if a longer wait is intended. |
| Ranked entry rejected | Check RankedRobot permission, enabled rank, public room, and Ranked profile restrictions. |
| Scoring stops on a disagreement | Japanese disputes are unsupported. Chinese, AGA, and New Zealand cleanup requires `kgs-genmove_cleanup`; repeated disputes, lack of progress, and cleanup expiry stop the client. |
| Bot stops after a pause or opponent departure | Review the relevant interaction timeout and inspect the unfinished game before restarting. |
| Engine unavailable but account still online | Inspect engine diagnostics and the recovery-pipe message. Automatic retries may be exhausted; game clocks and deadlines still run. |
| Identity file error | Ensure the configured state location is writable and contains the client-generated identity file. |

When reporting a problem, include the client version, engine name/version, game
ID if available, relevant settings, and stderr diagnostics. Omit passwords.

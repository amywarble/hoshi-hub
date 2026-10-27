---
layout: localized
title: "Upgrade from the Java GTP client"
lang: "en"
page_key: "gtp/upgrade-guide"
section: "gtp"
nav_order: 2
permalink: "/gtp/upgrade-guide/"
---

This guide moves a bot from `kgsGtp.jar` and its Java `.properties` configuration
to Kgs.Gtp and TOML. The old file cannot be loaded directly; there is no automatic
importer. Keep it for reference while creating a new file. See the
[user guide]({% include page-url.html key='gtp/user-guide' %}) for normal operation and the full settings reference.

This guide covers Windows and Linux. Expand the section for your operating
system to see PowerShell or Bash commands. Run the commands from the extracted
client directory.

## Upgrade steps

1. Finish or resolve any current game, then stop the old client and its engine.
   Disable its automatic restart while trying the replacement, so both clients
   do not log in with the same account.
2. Extract the Kgs.Gtp package for your Windows or Linux architecture. The package
   includes the .NET runtime. Keep your engine, model, and engine configuration;
   these remain separate from the client.
3. Copy [bot.example.toml]({{ '/gtp/bot.example.toml' | relative_url }}) to `bot.toml`. Move the settings using
   the tables below. Put the password in `KGS_PASSWORD`, and choose the game type,
   takeback policy, and game count explicitly.
4. Probe the engine with the commands below. Fix engine discovery errors before
   logging in. Additional game capability checks run on normal startup.
5. Run one Free game with `--games 1`. Verify login, opponent selection, clocks,
   scoring, and the `Series: completed game 1` diagnostic.
6. Set `games = 0` if you want continuous play, then update your launcher or service
   to use the new executable, configuration path, password environment, and logs.

Copy the template, then edit the account, engine paths, and game settings:

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

After editing, check engine discovery without logging in:

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

To return to the old client, stop the new client and engine first, inspect any
unfinished game, and restore your original launcher and properties file. Keep
the new client's identity file for a later return to Kgs.Gtp.

## Changes to review before switching

| Area | Old client | Kgs.Gtp |
| --- | --- | --- |
| Launch | `java -jar kgsGtp.jar bot.properties key=value` | `Kgs.Gtp --config bot.toml --option value`; Windows executable ends in `.exe`. |
| Configuration | Java properties, including Java escapes | UTF-8 TOML with named sections, quoted strings, numbers, arrays, and booleans. Unknown keys are errors. |
| Default mode | Automatch | No matchmaking unless `matchmaking.mode` or `--lobby` is selected. |
| Game count | Continues finding games | Built-in default is one completed game. Set `games = 0` for continuous play; the supplied example already does this. |
| Game type | Automatch could allow Free and Ranked together | Select `Free` (default) or `Ranked` exclusively. There is no mixed setting or fallback. |
| Room | Room name | Room name, still a string; use `room = "English Room"`. Lookup ignores case and requires an exact name. |
| Custom game terms | Players could propose changes | Configured terms must match exactly, including colors, komi, handicap, visibility, and time control. |
| Takebacks | Normally allowed in Free games, refused in Ranked | Both built-in policies default to `Never`. Set `undo.free = "Allow"` to retain the usual Free behavior. The example does this. |
| Automatch handicap | Could allow up to nine ranks if the engine supported handicap | `maxRankDifference` defaults to `0`; choose it explicitly, at most 9 for Free or 6 for Ranked. |
| Connection retries | `reconnect=t` enables continued retrying | Default 180-second outage budget, exponential backoff with jitter, and reset after 60 healthy seconds. |
| Engine failure | No automatic engine restart from `reconnect` | Separate automatic restart budget; exhaustion waits for operator recovery while normal deadlines continue. |
| Opponent departure | Could return to matchmaking after its absence limit | The new client stops with an unfinished-game diagnostic when the configured wait expires. |

The example is a starting configuration, not a claim that all old behavior is
preserved. In particular, decide whether this account should play Free or Ranked
before enabling continuous operation.

## Map the old settings

The new setting names below use `section.key` notation. For example,
`account.username` means `username = "YourBot"` under `[account]`.

### Account, connection, and engine

| Old property | New setting | Migration notes |
| --- | --- | --- |
| `name` | `account.username` / `--username` | `KGS_USERNAME` is also supported when no username is configured. |
| `password` | Environment variable `KGS_PASSWORD` | Remove it from the new configuration; password fields and password CLI options are unsupported. |
| `server.host` | `server.host` / `--host` | String; default `goserver.gokgs.com`. |
| `server.port` | `server.port` / `--port` | Integer; default `2379`. |
| `reconnect=f` | `connectionRecovery.attempts = 0` | Disables KGS transport retries; engine recovery is configured separately. |
| `reconnect=t` | `[connectionRecovery]` | Choose a time budget per outage; the default is 180 seconds. An attempt cap is optional. |
| `engine` | `engine.executable` and `engine.arguments` | Split the command into executable and individual arguments; see below. |
| No engine connection properties | `engine.stdio = true` / `--stdio` | Standard I/O must now be selected explicitly. |
| `gtp.in`, `gtp.out` | No direct setting | An external launcher can connect the two directions through `--stdio`. The client does not open named files or FIFOs from configuration. |
| `engine.port` | No direct setting | There is no engine TCP listener. Use an external adapter with `--stdio`, or let the client launch the engine. |
| `logFile` | Capture stderr externally | Use shell redirection or a service manager; built-in Java log naming and rotation do not carry over. |
| `verbose` | No direct setting | Normal diagnostics go to stderr; there is no equivalent full GTP/server traffic logging switch. |

The local `engineRecovery.pipe` is for replacing a failed engine in a running
session. It does not replace the old `engine.port`, `gtp.in`, or `gtp.out` startup
settings.

### Matchmaking and game settings

| Old property | New setting | Migration notes |
| --- | --- | --- |
| `mode=auto` | `matchmaking.mode = "Automatch"` | Omit room, custom opponent settings, and the `game`/`timing` sections. |
| `mode=custom` | `matchmaking.mode = "Offer"` | Add `opponentPolicy = "Any"` for open challenges, or `"Named"` plus `opponent`. |
| `mode=wait` | `matchmaking.mode = "Join"` | Set the room name and `opponent`; the offered profile must match exactly. |
| `mode=both` | No combined mode | Choose Automatch, Offer, or Join for this invocation. |
| `mode=tournament` | Unsupported | Tournament entry is not implemented; keep the old client if this is required. |
| `room` | `matchmaking.room` / `--room` | Preserve the room name as a quoted string. Required for Offer and Join; omit for Automatch. There is no last-used-room default. |
| `opponent` | `matchmaking.opponent` | For custom challenges use `opponentPolicy = "Named"`. Omit both custom opponent settings for Automatch. |
| `gameNotes` | `matchmaking.challengeNotes` | Offer only; at most 255 characters without control characters. |
| `rules` | `game.rules` | Use `Japanese`, `Chinese`, `Aga`, or `NewZealand`. Sets exact custom game terms. |
| `komi` | `game.komi` | Number, not a quoted string; set explicitly, including for handicap games. |
| `rules.boardSize` | `game.boardSize` | Integer. Set explicitly: the new custom-game default is 9. |
| `rules.time` | `[timing]` | Split into system, seconds, and overtime fields using the examples below. |
| `automatch.speed` | `automatch.speed` | For example `speed = ["Blitz", "Medium"]`, or `"All"`. CLI combinations use commas. |
| `automatch.rank` | `automatch.rank` | Quoted `30k` through `1k`; still required when there is no numeric server rank. |
| `undo=f` | `[undo]` with `free = "Never"`, `ranked = "Never"` | These are also the built-in defaults. |
| `undo=t` or omitted | `[undo]` with `free = "Allow"`, `ranked = "Never"` | Retains the usual old Free/Ranked distinction. New Ranked takebacks can be enabled separately if desired. |
| `talk` | Unsupported | Private chat replies and engine chat forwarding are not implemented. |
| `hint.cleanup`, `hint.noArguing` | Unsupported | There are no configurable chat hints for scoring disputes. |

`game.rules` and `engine.rules` have different purposes. The former chooses the
custom game's rules. The latter declares rules already configured in an engine
that lacks `kgs-rules`; it does not change that engine's configuration.

### Split the engine command

An old property might be:

```properties
engine=/opt/katago/katago gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

The new configuration is:

```toml
[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]
```

Do not put a whole command line into `executable`. There is no shell evaluation.
Each argument is one array element, including paths containing spaces. For Windows,
single-quoted TOML strings keep backslashes literal:

```toml
[engine]
executable = 'C:\Go Engines\katago.exe'
arguments = ["gtp", "-config", 'C:\Go Engines\gtp.cfg', "-model", 'C:\Go Engines\model.bin.gz']
```

Replace Java properties escapes with the actual text in UTF-8 TOML. Relative
executable paths containing a separator are resolved from the TOML directory;
argument paths remain relative to the launch working directory. Absolute model
and configuration paths make service launches easier to reproduce.

### Convert time controls

Use only one of these `[timing]` sections, and only with Offer or Join.

Old `rules.time=0`:

```toml
[timing]
system = "None"
mainTime = 0
```

Old `rules.time=30:00`:

```toml
[timing]
system = "Absolute"
mainTime = 1800
```

Old `rules.time=30:00+5x0:30`:

```toml
[timing]
system = "ByoYomi"
mainTime = 1800
byoYomiTime = 30
byoYomiPeriods = 5
```

Old `rules.time=30:00+25/10:00`:

```toml
[timing]
system = "Canadian"
mainTime = 1800
byoYomiTime = 600
canadianStones = 25
```

All new time values are integer seconds. Remove overtime fields that belong to
a different system. Japanese overtime requires the engine's `kgs-time_settings`
command; it is not approximated using another clock system.

## Example: migrate an automatch bot

Suppose the relevant parts of the old file are:

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

Create this `bot.toml` for an initial Free game. Automatch does not take a room
setting, so the old `room` property is omitted:

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

For Windows, replace the `[engine]` paths with the Windows example in
[Split the engine command](#split-the-engine-command). Set the password and run
one game:

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

This example deliberately selects even Free games. To retain handicap matching, select a suitable `maxRankDifference` and
check engine support. To play Ranked, select `gameType = "Ranked"`, verify the
account's RankedRobot permission and enabled rank, and use at most six ranks of
difference. One invocation cannot accept both game types.

For a custom bot, use the [custom challenge example]({% include page-url.html key='gtp/user-guide' %}#custom-challenges),
copy the old room name, and explicitly transfer board size, rules, komi, color,
handicap, and converted time settings.

## Engine compatibility and unattended operation

Kgs.Gtp requires GTP v2 and its complete mandatory command set. Some commands
treated as optional by the old client are required here. All automatic games
also require `final_status_list`. Timed games need `time_left` and a supported
timing command. Check the user guide's engine requirements for your selected
profile; an old working configuration alone does not establish compatibility.

Ordinary Japanese scoring agreement is supported, but unresolved Japanese
disputes stop the game. Chinese, AGA, and New Zealand cleanup requires
`kgs-genmove_cleanup` and has bounded attempts and a total deadline. There is no
old-client fallback that lets an opponent decide all dead stones when automatic
scoring is unavailable.

Review these service settings before leaving the bot unattended:

- Set `games = 0` explicitly if it should keep playing. Each lobby attempt still
  has a default 300-second deadline; increase `timeouts.lobby` if needed.
- Configure KGS connection retries and engine restarts separately. KGS recovery
  defaults to 180 seconds per outage and resets after 60 healthy seconds. Engine
  recovery permits three automatic replacements across the invocation; exhaustion
  can leave a live KGS session awaiting operator recovery.
- Choose pause, adjournment, and opponent-absence limits. Each defaults to 300
  seconds; expiry stops the client without counting or resigning the unfinished game.
- Preserve the client identity file in a writable state directory. A fresh
  process does not automatically discover older automatch games.
- Capture stderr and arrange external log retention. Exit 0 means normal
  completion, 1 indicates failure, and 130 indicates cancellation.

The [user guide]({% include page-url.html key='gtp/user-guide' %}#timeouts-and-recovery) describes timeout settings,
connection recovery, and operator engine recovery in detail.

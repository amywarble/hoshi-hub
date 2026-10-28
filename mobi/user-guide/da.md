---
layout: "localized"
title: "Mobi brugervejledning"
nav_title: "Brugervejledning"
lang: "da"
page_key: "mobi/user-guide"
section: "mobi"
nav_order: 1
permalink: "/da/gtp/user-guide/"
source_revision: "26bf30c603841ace27c0d2ff994fd0d2297af607b506d24fd1ab9afabb8f1a33"
---

Mobi forbinder en Go-motor til KGS, så den kan spille automatisk. Du kører klienten i en terminal og kontrollerer den gennem en TOML konfigurationsfil eller kommandolinjeindstillinger. Installer og konfigurer din motor separat; klienten håndterer login, finde spil, træk, ure og scoring.

Flytter du fra Java `kgsGtp.jar`-klienten? Start med [opgraderingsvejledningen]({% include page-url.html key='mobi/upgrade-guide' %}).

Denne vejledning dækker Windows og Linux. Udvid sektionen for dit operativsystem for at se PowerShell eller Bash kommandoer. Kør eksemplerne på pakkeklienter fra det udpakkede klientbibliotek.

- [Første spil](#first-game)
- [Grundlæggende konfiguration](#configuration-basics)
- [Valg af spil](#choosing-games)
- [Tilpassede spilindstillinger](#custom-game-settings)
- [Kører botten](#running-the-bot)
- [Timeouts og gendannelse](#timeouts-and-recovery)
- [Fejlfinding](#troubleshooting)

## Første spil {#first-game}

Du skal have en registreret KGS-konto, en GTP-version af 2-motoren og eventuelle konfigurations- og modelfiler, som motoren kræver. Opret kontoen ved hjælp af en almindelig KGS-klient, før du starter botten. Ranked spil kræver yderligere servertilladelse; start med et Free-spil.

Udpak klientpakken til dit operativsystem og din arkitektur. Pakker leveres til Windows og Linux på x64 og ARM64, med .NET runtime inkluderet. Hold de udpakkede filer sammen. Den eksekverbare er `Kgs.Gtp.exe` på Windows og `Kgs.Gtp` på Linux.

### 1. Opret din konfiguration {#1-create-your-configuration}

Kopiér den inkluderede [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) til `bot.toml`:

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

Rediger `account.username`, `engine.executable` og `engine.arguments`. For eksempel:

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

Angiv stierne og argumenterne, som din motor skal bruge for at gå i GTP-tilstand. Hvert array-element er ét argument; en sti, der indeholder mellemrum, er stadig ét element.

Eksemplet vælger Free automatch mod mennesker, hurtig eller medium hastighed og kontinuerligt spil. Indstil `automatch.rank` til et passende estimat mellem `30k` og `1k`, hvis kontoen ikke har en numerisk rangering. KGS bruger kontoens rangering, når en er tilgængelig. For det første løb begrænser kommandoen nedenfor spillet til ét spil.

### 2. Tjek motoren {#2-check-the-engine}

Fra den udpakkede klientmappe skal du køre:

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

Klienten udskriver motornavnet, versionen og de understøttede kommandoer og afslutter derefter. Dette kræver ingen KGS-legitimationsoplysninger og forbinder ikke til KGS. Den kontrollerer GTP-opdagelse; de yderligere regler, ur, handicap og scoringskontroller kører, når den konfigurerede spiltilstand startes.

### 3. Angiv adgangskoden og spil {#3-supply-the-password-and-play}

Adgangskoden kommer kun fra miljøvariablen `KGS_PASSWORD`:

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

Se efter `Logged in to KGS`, derefter `Game ready`. Klienten spiller og scorer spillet automatisk. `Game finished` registrerer KGS's resultat; `Series: completed game 1` bekræfter, at det tæller med i den anmodede total. Den logger derefter ud og afslutter. At finde et spil er som standard begrænset til fem minutter; brug `--lobby-timeout 3600` for at tillade op til en time.

## Grundlæggende om konfiguration {#configuration-basics}

Vælg altid filen eksplicit med `--config`. Klienten læser den én gang ved opstart. Genstart for at anvende redigeringer, herunder ændringer af indstillingerne for genstart af motor. Der er ingen automatisk konfigurationsfilsøgning eller live genindlæsning.

Kommandolinjeindstillinger tilsidesætter filværdier for den kørsel. For eksempel:

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

Brugernavnet kommer fra `--username`, derefter `account.username`, derefter `KGS_USERNAME`. Tilføj ikke et kodeordsfelt til filen: den er afvist.

Brug citerede strenge til navne og markeringer, heltal for tællinger og sekunder, tal for komi og `true` eller `false` for booleaner. Tabel- og nøglenavne skelner mellem store og små bogstaver. Ukendte nøgler og ugyldige værdier stopper opstart med en diagnostik. Alle varigheder i denne guide er sekunder.

En relativ `engine.executable`, der indeholder `/` eller `\`, og en relativ `account.clientIdFile`, er relative til konfigurationsfilens bibliotek. Et blottet eksekverbart navn, såsom `katago`, bruger eksekverbart opslag. Motorargumenter sendes uændret, og motoren arver den arbejdsmappe, hvorfra du starter klienten. Brug absolutte stier til model- og motorkonfigurationsargumenter, hvis du starter fra forskellige mapper. Enkelt-citerede TOML-strenge bevarer Windows-omvendte skråstreger. Strenge udvider ikke miljøvariabler.

### Konto, server og motor {#account-server-and-engine}

| TOML indstilling | CLI mulighed | Betydning og standard |
| --- | --- | --- |
| `account.username` | `--username` | KGS kontonavn; falder tilbage til `KGS_USERNAME`. |
| `account.clientIdFile` | `--client-id-file` | Vedvarende identitetsfil; normalt valgt pr. server og konto. |
| `server.host` | `--host` | KGS server; standard `goserver.gokgs.com`. |
| `server.port` | `--port` | TCP-port; standard `2379`, område 1–65535. |
| `engine.executable` | `--engine` | Eksekverbar motor for at starte. |
| `engine.arguments` | Argumenter efter `--` | Vifte af motorargumenter; standard tom. |
| `engine.stdio` | `--stdio` | Brug en eksternt tilsluttet motor i stedet for at starte en; standard `false`. |
| `engine.rules` | `--engine-rules` | Regler, der allerede er konfigureret i en motor, der mangler `kgs-rules`. Ingen standarderklæring. |

Vælg en eksekverbar eller `stdio = true`, aldrig begge dele. Med standard I/O skal et andet program forbinde klientens stdin til motorens stdout og klientens stdout til motorens stdin. Diagnostik bruger stderr. Angiv ikke motorargumenter i denne tilstand.

`engine.rules` accepterer `Japanese`, `Chinese`, `Aga` eller `NewZealand`. Dette erklærer motorens eksisterende regler; konfigurere selve motoren til at matche. Motorer med `kgs-rules` modtager automatisk det valgte spils regler.

For at konfigurere helt på kommandolinjen skal du sætte motorargumenter efter `--`:

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

Eksplicitte CLI-motorargumenter erstatter hele filarrayet. En efterfølgende `--` uden noget, efter den rydder det array. `--engine` og `--stdio` tilsidesætter filens valg af motorforbindelse; `--stdio` kasserer også filbaserede argumenter. `--help` viser alle muligheder, og `--version` udskriver klientversionen.

## Valg af spil {#choosing-games}

Vælg en matchmaking-tilstand:

| `matchmaking.mode` / `--lobby` | Hvad botten gør |
| --- | --- |
| `Automatch` | Lader KGS finde en modstander og vælge spillevilkårene. |
| `Offer` | Annoncerer en tilpasset udfordring i det navngivne rum. |
| `Join` | Leder efter en matchende tilpasset udfordring i det navngivne rum. |

Uden en tilstand logger klienten på og venter, indtil den stoppes; den finder ikke spil. En opfordring spiller et spil ad gangen. Samtidige tilpassede udfordringer og automatch, turneringsadgang og chatsvar understøttes i øjeblikket ikke.

### Automatch {#automatch}

Brug disse sektioner sammen med dine konto- og motorindstillinger:

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

Udelad `matchmaking.room`, `opponent`, `opponentPolicy`, `challengeNotes` samt afsnittene `game` og `timing` i Automatch-tilstand. De er indstillinger for brugerdefinerede udfordringer og kan ikke kombineres med automatisk matchmaking, selv hvis værdierne svarer til standarderne.

| TOML indstilling | CLI mulighed | Valg og standard |
| --- | --- | --- |
| `automatch.speed` | `--automatch-speed` | `All` (standard), `Blitz`, `Fast`, `Medium` eller et array såsom `["Fast", "Medium"]`. CLI-kombinationer bruger kommaer. |
| `automatch.rank` | `--automatch-rank` | Estimeret `30k` til `1k`; påkrævet, når kontoen ikke har nogen numerisk serverrangering. |
| `automatch.opponents` | `--automatch-opponents` | `Humans` (standard), `Robots` eller `Any`. |
| `automatch.maxRankDifference` | `--automatch-max-rank-difference` | Standard `0`; række 0–9 for Free, 0–6 for Ranked. |

Automatch-spil er offentlige 19×19-spil med japanske regler og farver tildelt af serveren. Spil uden handicap bruger komi 6.5. Tilladte rangforskelle kan give komi 0.5 og ved forskelle på to eller mere faste handicapsten.

| Hastighed | Hovedtid pr. spiller | Japansk byo-yomi |
| --- | --- | --- |
| `Blitz` | 60 sekunder | 3 perioder på 10 sekunder |
| `Fast` | 600 sekunder | 5 perioder på 20 sekunder |
| `Medium` | 1500 sekunder | 5 perioder på 30 sekunder |

Motoren skal understøtte `final_status_list`, `kgs-time_settings` og `time_left`; at tillade handicap kræver også `set_free_handicap`. Hvis den mangler `kgs-rules`, skal du konfigurere den til japanske regler og indstille `engine.rules = "Japanese"`.

### Tilpassede udfordringer {#custom-challenges}

Erstat eksempelfilens `matchmaking` og `automatch` sektioner med en brugerdefineret profil. Dette eksempel tilbyder et offentligt 19×19 Free-spil til kvalificerede spillere:

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

Brug rummets navn som vist i KGS. Navne kan indeholde mellemrum og ikke-ASCII-tegn. Opslag bruger et nøjagtigt match, der skelner mellem store og små bogstaver, efter login og igen efter genforbindelse. Manglende eller tvetydige navne stopper klienten med en diagnostik.

For en specifik modstander skal du ændre `opponentPolicy` til `"Named"` og tilføje `opponent = "OtherAccount"`. For `Any`, udelad `opponent`; kvalificerede åbne modstandere er forbundet, registrerede konti andre end denne bot. Både mennesker og robotter er berettigede.

For at deltage i udfordringer skal du bruge `mode = "Join"` og fjerne `challengeNotes`. Hvert spiludtryk skal matche, inklusive regler, komi, handicap, synlighed og ure. Vælg botens egen farve: en Offer-bot, der spiller sort, har brug for en Join-bot, der spiller hvid; for tilfældige farver, brug begge `"Nigiri"`. Ændrede vilkår accepteres ikke stille.

| TOML indstilling | CLI mulighed | Valg og standard |
| --- | --- | --- |
| `matchmaking.mode` | `--lobby` | `Offer`, `Join` eller `Automatch`; ingen standardtilstand. |
| `matchmaking.gameType` | `--game-type` | `Free` (standard) eller `Ranked`. |
| `matchmaking.opponentPolicy` | `--opponent-policy` | `Named` (standard for tilpassede udfordringer) eller `Any`. |
| `matchmaking.opponent` | `--opponent` | Påkrævet med `Named`; kontonavne ignorer store og små bogstaver. |
| `matchmaking.room` | `--room` | Nødvendigt rumnavn for Offer og Join; for eksempel `"Computer Go"`. |
| `matchmaking.games` | `--games` | Standard `1`; positivt tal for en serie, `0` for kontinuerlig afspilning. |
| `matchmaking.challengeNotes` | `--challenge-notes` | Kun Offer; op til 255 tegn, uden kontroltegn. Udeladelse genererer en modstander-note. |

### Ranked spil {#ranked-games}

Indstil `matchmaking.gameType = "Ranked"` til udelukkende at anmode om Ranked-spil. Kontoen skal have server-givet `RankedRobot`-tilladelse og rang aktiveret. Spørg en KGS-serveradministrator om denne tilladelse. En ikke-indstillet rang (`?`) er tilladt, men deaktiveret rang (`-`) er ikke; automatch har stadig brug for et estimat, når kontoen ikke har nogen numerisk rangering.

Ranked-modstandere skal være registrerede konti med rang aktiveret og en amatørrang eller en endnu ikke fastlagt rang. Robotmodstandere kræver også `RankedRobot`-tilladelse. Ranked-udfordringer med egne vilkår kræver et offentligt rum, et offentligt 19×19-spil, højst seks handicapsten, komi fra −10 til 10 og estimeret spilletid over 450 sekunder pr. spiller. Estimatet inkluderer ekstratid; ubegrænset tid er også tilladt. En Absolute-profil på 600 sekunder opfylder tidskravet. Klienten afviser ugyldige indstillinger eller en serverændring til Free.

## Brugerdefinerede spilindstillinger {#custom-game-settings}

Disse indstillinger gælder for Offer og Join. Undlad dem fra Automatch-konfigurationer.

| TOML indstilling | CLI mulighed | Valg og standard |
| --- | --- | --- |
| `game.boardSize` | `--board-size` | Standard `9`; række 2–25, afhængig af motorsupport. |
| `game.rules` | `--rules` | `Chinese` (standard), `Japanese`, `Aga` eller `NewZealand`. |
| `game.komi` | `--komi` | Standard `7.5`; −100 til 100 i halve point-intervaller. |
| `game.color` | `--color` | `Black`, `White` eller `Nigiri`; standard til Sort for Offer og hvid for Join. |
| `game.handicap` | `--handicap` | Standard `0`; ellers 2–9 inden for bestyrelsens placeringsgrænser. Kan ikke kombineres med Nigiri. |
| `game.private` | `--private` | Standard `false`; kræver et privat spil, mens udfordringen bliver annonceret i det valgte rum. |

Handicap justerer ikke komi automatisk. Angiv begge dele udtrykkeligt. Japanske regler og AGA bruger fast placering: mindst 7×7, med højst fire sten på 7×7 eller brætter med lige sidelængde. Kinesiske og newzealandske regler bruger fri placering med højst ni sten og mindst ét tomt kryds. Handicapspil kræver `set_free_handicap`; sort kræver også `place_free_handicap` ved fri placering.

### Tidskontrol {#time-controls}

| TOML indstilling | CLI mulighed | Standard og rækkevidde |
| --- | --- | --- |
| `timing.system` | `--time-system` | `Absolute` (standard), `None`, `Canadian` eller `ByoYomi`. |
| `timing.mainTime` | `--main-time` | Standard `600` eller `0` for Ingen; række 0–86400. |
| `timing.byoYomiTime` | `--byo-yomi-time` | Standard `0`; 1–86400 pr. japansk periode eller canadisk blokering ved brug af ekstratid. |
| `timing.byoYomiPeriods` | `--byo-yomi-periods` | Standard `0`; 1–255 til ByoYomi. |
| `timing.canadianStones` | `--canadian-stones` | Standard `0`; 1–255 til canadisk. |

For japansk ekstratid med ti minutters hovedtid og fem 30-sekunders perioder:

```toml
[timing]
system = "ByoYomi"
mainTime = 600
byoYomiTime = 30
byoYomiPeriods = 5
```

For canadisk ekstratid skal du bruge `system = "Canadian"`, `byoYomiTime` i sekunder pr. blok og `canadianStones` for sten pr. blok. Udelad `byoYomiPeriods`. Ekstratid tillader nul hovedtid. Absolut kræver positiv hovedtid og intet ekstratid; Ingen kræver, at alle eksplicit angivne tidsværdier er nul. Samlede urreserver skal også passe til serverens rækkevidde; ugyldige kombinationer rapporteres.

Tidsindstillede spil kræver `time_left` og enten `time_settings` eller `kgs-time_settings`. Japansk ekstratid kræver specifikt `kgs-time_settings`. Ubegrænsede spil kræver ikke urkommandoer. Timeouts for motorsvar er adskilt fra spillets ur og giver ikke botten mere spilletid.

## Kører botten {#running-the-bot}

Indstil `matchmaking.games` til en positiv total, eller til `0` for at fortsætte med at spille. Kun KGS-bekræftede resultater tæller. Efter et afsluttet spil forlader klienten det og bruger de originale matchmaking-indstillinger til det næste spil. Et mislykket eller uafsluttet spil stopper serien i stedet for at tælle som afsluttet.

For kontinuerlig spil med længere ventetid mellem spil:

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

Tryk på Ctrl+C for at stoppe. Klienten logger ud, beder motoren om at afslutte og stopper en motor, den har startet, hvis det er nødvendigt. Stop under et spil etablerer ikke et endeligt resultat. Undersøg ethvert uafsluttet spil, før du starter endnu et løb.

### Logfiler og udgangskoder {#logs-and-exit-codes}

Status, fejl, hjælp og motordiagnostik går til stderr. For at beholde dem:

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

Brug din service manager eller eksterne værktøjer til logrotation. I standard-I/O-tilstand skal du holde stdout forbundet til motoren; den bærer GTP-kommandoer.

| Udgangskode | Betydning |
| --- | --- |
| `0` | Anmodede spil gennemført, eller en sonde/hjælp/version-kommando lykkedes. |
| `1` | Konfigurations- eller kørselsfejl; inspicere diagnosen. |
| `130` | Operatør annullering, inklusive Ctrl+C. |

### Vedvarende tilstand og eksisterende spil {#persistent-state-and-existing-games}

Klienten gemmer den identitet, der er tildelt af KGS. I matchmaking-tilstande er standardfilen under .NET's lokale programdatamappe på `Kgs.Gtp/identities/<server-and-account-hash>`. På Windows er dette normalt under `%LOCALAPPDATA%`. For at vælge en stabil skrivbar placering skal du indstille `account.clientIdFile = "./state/client-id"`. Bevar det på tværs af opgraderinger og containerudskiftninger. Brug en separat fil for hver server og konto.

Offer og Join kontrollerer først det valgte rum for et ufærdigt spil, der tilhører denne konto. Præcis ét kompatibelt spil kan genoptages; dens modstander og hele profil skal matche. Flere eller uoverensstemmende spil stopper opstart. Arkiverede spil indlæses ikke automatisk.

En kørende automatch-session kan gendanne sit tildelte spil efter tab af forbindelse. En ny proces opdager ikke ældre automatch-spil automatisk. Løs et uafsluttet automatch-spil, før du tilmelder dig igen.

### Takebacks, pauser og modstanderens fravær {#takebacks-pauses-and-opponent-absence}

`undo.free` / `--undo-free` og `undo.ranked` / `--undo-ranked` accepterer hver for sig `Never` (standard) eller `Allow`. Eksemplet tillader fortrydelse af træk i Free og afviser det i Ranked. Allow godkender modstanderens anmodninger, som serveren tillader under almindeligt aktivt spil; botten anmoder ikke selv om fortrydelse. Derefter genafspilles den bekræftede historik, så motoren ikke behøver at understøtte GTP `undo`. Genoptagelse efter uenighed om optællingen er en separat funktion.

KGS styrer pauser, udsættelse og genoptagelse. Mens den er sat på pause eller udsat, starter botten ingen nye gameplay eller scoringshandlinger. Hver kontinuerlig pause, udsættelse og modstanderens fravær har en separat grænse, der som standard er 300 sekunder:

| TOML indstilling i `[interactions]` | CLI mulighed |
| --- | --- |
| `pauseTimeoutFree` | `--pause-timeout-free` |
| `adjournmentTimeoutFree` | `--adjournment-timeout-free` |
| `opponentTimeoutFree` | `--opponent-timeout-free` |
| `pauseTimeoutRanked` | `--pause-timeout-ranked` |
| `adjournmentTimeoutRanked` | `--adjournment-timeout-ranked` |
| `opponentTimeoutRanked` | `--opponent-timeout-ranked` |

Hver accepterer 1–86400 sekunder. Udløb stopper klienten med koden 1 og efterlader spillet ufærdigt; det går ikke tilbage eller begynder et andet spil. Gentilslutning og motorudskiftning nulstiller ikke disse ventetider. Andre aktive deadlines kan udløbe hurtigere. Mens en modstander er fraværende, kan botten stadig bevæge sig, hvis KGS tillader det.

## Timeouts og restitution {#timeouts-and-recovery}

### Normale timeouts {#normal-timeouts}

Alle accepterer 1–86400 sekunder:

| TOML indstilling | CLI mulighed | Standard | Grænser |
| --- | --- | --- | --- |
| `timeouts.login` | `--login-timeout` | `30` | Tilslutning og log ind. |
| `timeouts.lobby` | `--lobby-timeout` | `300` | En udfordringsforhandling eller automatisk tilmelding; begrænser også rumnavnopslag. |
| `timeouts.move` | `--move-timeout` | `600` | En normal eller oprydningsmaskinesøgning. |
| `timeouts.scoring` | `--scoring-timeout` | `120` | Én scoringsrunde, inklusive evaluering og aftale. |
| `timeouts.cleanup` | `--cleanup-timeout` | `300` | Alle oprydningsforsøg og efterfølgende scoring samlet. |

### KGS forbindelsestab {#kgs-connection-loss}

Klienten forsøger igen transportfejl, godkender igen og slutter sig til det afbrudte spil ved hjælp af serverhistorik. Den sender ikke et usikkert træk igen eller erstatter et kendt afbrudt spil med en ny udfordring. Afvist login, serverlogout, ugyldige serverdata, ulovlige motorbevægelser og afviste motorkommandoer er terminalfejl.

| TOML indstilling | CLI mulighed | Standard og rækkevidde |
| --- | --- | --- |
| `connectionRecovery.attempts` | `--reconnect-attempts` | Valgfri hætte pr. udfald; 0–100. Udeladt som standard; nul deaktiverer genforsøg. |
| `connectionRecovery.delay` | `--reconnect-delay` | `1` - andet indledende vindue; 0–30, fordobling til en 30-sekund cap, med fuld jitter. |
| `connectionRecovery.timeout` | `--recovery-timeout` | `120` sekunder pr. gentilslutning gennem gentilknytning af spil; 1–86400. |
| `connectionRecovery.budget` | `--recovery-budget` | `180` sekunder i alt pr. udfald, inklusive dræning, backoff, login og gentilslutning; 1–86400. |
| `connectionRecovery.resetAfter` | `--recovery-reset-after` | `60` sunde sekunder efter gentilknytning, før budgettet nulstilles og tæller igen; 1–86400. |
| `connectionRecovery.engineDrainTimeout` | `--engine-drain-timeout` | `30` sekunder til at afslutte og kassere gammelt motorarbejde; 1–86400. |

Afbrydelsesbudgettet starter, når forbindelsestab opdages. Hver genforbindelse er begrænset af det resterende budget samt dets eget login/gentilslut timeout. Hver tilbagekoblingsforsinkelse vælges tilfældigt mellem nul og et loft, der fordobles fra 1 sekund til en 30-sekund cap. Gendannelse stopper, når det samlede budget eller et eksplicit forsøgsloft er opbrugt.

Efter gentilknytning kan botten fortsætte med at spille ud over den gamle gendannelsesfrist. En senere afbrydelse får et nyt budget efter 60 sunde sekunder. En afbrydelse før dette interval bevarer den tidligere deadline og tæller for genforsøg, inklusive den kortvarigt tilsluttede tid. Login alene etablerer ikke sundhed, når et spil stadig skal tilsluttes igen.

### Motorfejl {#engine-failure}

Hvis en kørende motor afsluttes, eller dens stream bliver ubrugelig, holder klienten KGS-sessionen aktiv og forsøger at starte en erstatning ved hjælp af den originale eksekverbare og argumenter. Den tjekker udskiftningen og afspiller bekræftet historie, før den fortsætter. Indledende motorstart/opdagelsesfejl stopper klienten. KGS ure fortsætter, mens motoren ikke er tilgængelig.

| TOML indstilling | CLI mulighed | Standard og rækkevidde |
| --- | --- | --- |
| `engineRecovery.attempts` | `--engine-restart-attempts` | `3` automatiske udskiftninger på tværs af påkaldelsen; 0–100. Nul venter på operatørgendannelse. |
| `engineRecovery.delay` | `--engine-restart-delay` | `1` - andet indledende vindue; 0–30, fordobling til en 30-sekund cap, med fuld jitter. |
| `engineRecovery.timeout` | `--engine-recovery-timeout` | `120` sekunder til opdagelse/opsætning og separat til genafspilning; 1–86400. |
| `engineRecovery.pipe` | `--engine-recovery-pipe` | Lokal genvindingsrør; standard `kgs-gtp-<process ID>`. Brug 1–100 ASCII-bogstaver, cifre, punktum, bindestreger eller understregninger. |

Når de automatiske udskiftninger er opbrugt, navngiver diagnosticeringen et lokalt genoprettelsesrør. Botten venter på operatørens indgriben, mens normale spil- og lobbydeadlines fortsætter. For at genstarte en motor, der er startet af klienten, skal du oprette forbindelse som den samme operativsystembruger og sende UTF-8 `restart` efterfulgt af LF. For eksempel, hvis du konfigurerede `pipe = "YourBot-recovery"`, skal du køre dette i en anden terminal efter den ventende diagnostik:

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

Linux-eksemplet kræver Python 3 og opretter forbindelse til .NET's Unix-domæne-socket. Kør det som den samme bruger med den samme `TMPDIR` som botten (standarden er `/tmp`). Udskift `YourBot-recovery` med det konfigurerede rørnavn; en tjeneste med en privat midlertidig mappe kræver også, at klienten kører i det samme miljø.

En vellykket operatørudskiftning starter et nyt automatisk genforsøgsbudget. Redigering af TOML-filen ændrer ikke den kørende klients eksekverbare eller argumenter.

For `--stdio` skal en ekstern supervisor tilslutte en frisk motor gennem dupleksgenvindingsrøret og relæet GTP i begge retninger. Der er ingen `restart`-hilsen i denne tilstand. Den originale stdin/stdout-forbindelse kan ikke genbruges efter fejl.

## Fejlfinding {#troubleshooting}

| Symptom | Hvad skal man tjekke |
| --- | --- |
| Konfigurationsfejl før motorstart | Kontroller den navngivne fil og kildeplacering, nøjagtig stavning af nøgler, citerede rumnavne og TOML værdityper. Ældre Java-egenskabsfiler skal konverteres. |
| Motoren kan ikke starte eller åbne sin model | Tjek eksekverbare og argumentstier, GTP-tilstandsargumenter og arbejdsmappen. Prøv `--probe`. |
| Mangler GTP-kommandoer eller forkert protokolversion | Brug en komplet GTP v2-motor. Funktionsregistreringen kræver `protocol_version`, `name`, `version`, `known_command`, `list_commands`, `quit`, `boardsize`, `clear_board`, `komi`, `play` og `genmove`. |
| Regler, timing eller scoringskontrol mislykkes | Tjek motorkapaciteter for den valgte profil. Erklær kun `engine.rules`, når motoren mangler `kgs-rules`, og sørg for, at dens faktiske konfiguration stemmer overens. Alle automatiske spil kræver `final_status_list`. |
| Login mislykkes | Tjek kontonavnet, `KGS_PASSWORD` i lanceringsmiljøet, serveradressen og den rapporterede afvisningsårsag. |
| Værelset blev ikke fundet | Kopier dets fulde navn fra KGS på den valgte server. Matching ignorerer store og små bogstaver, men kræver hele navnet. |
| Venter på et spil eller lobby-timeout | Tjek matchende vilkår, modstanderens berettigelse, værelsesnavn og automatch-præferencer. Forøg `timeouts.lobby`, hvis en længere ventetid er påtænkt. |
| Ranked post afvist | Tjek tilladelse til rangerede robotter, aktiveret rang, offentligt rum og Ranked profilbegrænsninger. |
| Scoring stopper ved uenighed | Japanske tvister er ikke understøttet. Kinesisk, AGA og New Zealand oprydning kræver `kgs-genmove_cleanup`; gentagne tvister, manglende fremskridt og oprydningsudløb stopper klienten. |
| Bot stopper efter en pause eller modstanderens afgang | Gennemgå den relevante interaktions-timeout, og inspicér det ufærdige spil, før du genstarter. |
| Motoren er ikke tilgængelig, men kontoen er stadig online | Efterse motorens diagnostik og meddelelsen om genvindingsrøret. Automatiske genforsøg kan være opbrugt; kampure og deadlines løber stadig. |
| Identitetsfil fejl | Sørg for, at den konfigurerede tilstandsplacering er skrivbar og indeholder den klientgenererede identitetsfil. |

Når du rapporterer et problem, skal du inkludere klientversion, motornavn/version, spil-id, hvis tilgængeligt, relevante indstillinger og stderr-diagnostik. Udelad adgangskoder.

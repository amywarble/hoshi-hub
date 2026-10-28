---
layout: "localized"
title: "Opgrader til Mobi fra Java GTP-klienten"
nav_title: "Opgrader fra Java"
lang: "da"
page_key: "mobi/upgrade-guide"
section: "mobi"
nav_order: 2
permalink: "/da/gtp/upgrade-guide/"
source_revision: "c32ebab17d841776f058eab0acfe73c12237c6953d8b7f6ec6630c41d26de6f1"
---

Denne vejledning flytter en bot fra `kgsGtp.jar` og dens Java `.properties`-konfiguration til Mobi og TOML. Den gamle fil kan ikke indlæses direkte; der er ingen automatisk importør. Gem den til reference, mens du opretter en ny fil. Se [brugervejledningen]({% include page-url.html key='mobi/user-guide' %}) for normal drift og den fulde reference til indstillinger.

Denne vejledning dækker Windows og Linux. Udvid sektionen for dit operativsystem for at se PowerShell eller Bash kommandoer. Kør kommandoerne fra det udpakkede klientbibliotek.

## Opgraderingstrin {#upgrade-steps}

1. Afslut eller løs et hvilket som helst nuværende spil, og stop derefter den gamle klient og dens motor.    Deaktiver dens automatiske genstart, mens du prøver erstatningen, så begge klienter ikke logger på med den samme konto.
2. Udpak Mobi GTP-bropakken til din Windows- eller Linux-arkitektur.    Pakken inkluderer .NET runtime. Behold din motor, model og motorkonfiguration; disse forbliver adskilt fra klienten.
3. Kopiér [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) til `bot.toml`. Flyt indstillingerne ved hjælp af tabellerne nedenfor. Indsæt adgangskoden i `KGS_PASSWORD`, og vælg eksplicit spiltype, tilbagetagelsespolitik og spilantal.
4. Undersøg motoren med kommandoerne nedenfor. Ret motoropdagelsesfejl, før du logger ind. Yderligere kontrol af spilkapacitet kører ved normal opstart.
5. Kør et Free-spil med `--games 1`. Bekræft login, modstandervalg, ure, scoring og `Series: completed game 1` diagnosticering.
6. Indstil `games = 0`, hvis du ønsker kontinuerlig afspilning, og opdater derefter din launcher eller tjeneste for at bruge den nye eksekverbare, konfigurationssti, adgangskodemiljø og logfiler.

Kopiér skabelonen, og rediger derefter konto, motorstier og spilindstillinger:

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

Efter redigering, tjek motoropdagelse uden at logge ind:

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

For at vende tilbage til den gamle klient skal du først stoppe den nye klient og motor, inspicere ethvert ufærdigt spil og gendan din originale launcher og egenskabsfil. Behold den nye klients identitetsfil for en senere tilbagevenden til Mobi.

## Ændringer, der skal gennemgås før skift {#changes-to-review-before-switching}

| Område | Gammel klient | Mobi |
| --- | --- | --- |
| Lancering | `java -jar kgsGtp.jar bot.properties key=value` | `Kgs.Gtp --config bot.toml --option value`; Windows eksekverbar ender på `.exe`. |
| Konfiguration | Java-egenskaber, herunder Java-escapes | UTF-8 TOML med navngivne sektioner, citerede strenge, tal, arrays og booleaner. Ukendte nøgler er fejl. |
| Standardtilstand | Automatch | Ingen matchmaking, medmindre `matchmaking.mode` eller `--lobby` er valgt. |
| Antal spil | Fortsætter med at finde spil | Indbygget standard er ét gennemført spil. Indstil `games = 0` til kontinuerlig afspilning; det medfølgende eksempel gør dette allerede. |
| Spiltype | Automatch kunne tillade Free og Ranked sammen | Vælg udelukkende `Free` (standard) eller `Ranked`. Der er ingen blandet indstilling eller fallback. |
| Værelse | Værelsesnavn | Værelsesnavn, stadig en streng; brug `room = "English Room"`. Opslag ignorerer store og små bogstaver og kræver et nøjagtigt navn. |
| Brugerdefinerede spilvilkår | Spillere kunne foreslå ændringer | Konfigurerede termer skal matche nøjagtigt, inklusive farver, komi, handicap, synlighed og tidskontrol. |
| Tilbagetagelser | Normalt tilladt i Free-spil, nægtet i Ranked | Begge indbyggede politikker er som standard `Never`. Indstil `undo.free = "Allow"` for at bevare den sædvanlige Free-adfærd. Eksemplet gør dette. |
| Automatch handicap | Kunne tillade op til ni rækker, hvis motoren understøttede handicap | `maxRankDifference` er som standard `0`; vælg det eksplicit, højst 9 for Free eller 6 for Ranked. |
| Forbindelsen forsøger igen | `reconnect=t` muliggør fortsat genforsøg | Standard 180-sekunders udfaldsbudget, eksponentiel backoff med jitter og nulstilling efter 60 sunde sekunder. |
| Motorfejl | Ingen automatisk genstart af motoren fra `reconnect` | Separat automatisk genstartsbudget; udmattelse venter på genopretning af operatøren, mens normale deadlines fortsætter. |
| Modstanderens afgang | Kunne vende tilbage til matchmaking efter sin fraværsgrænse | Den nye klient stopper med en uafsluttet spildiagnose, når den konfigurerede ventetid udløber. |

Eksemplet er en startkonfiguration, ikke en påstand om, at al gammel adfærd er bevaret. Bestem især, om denne konto skal spille Free eller Ranked, før du aktiverer kontinuerlig drift.

## Kortlæg de gamle indstillinger {#map-the-old-settings}

De nye indstillingsnavne nedenfor bruger `section.key`-notation. For eksempel betyder `account.username` `username = "YourBot"` under `[account]`.

### Konto, forbindelse og motor {#account-connection-and-engine}

| Gammel ejendom | Ny indstilling | Migrationsnotater |
| --- | --- | --- |
| `name` | `account.username` / `--username` | `KGS_USERNAME` understøttes også, når der ikke er konfigureret et brugernavn. |
| `password` | Miljøvariabel `KGS_PASSWORD` | Fjern det fra den nye konfiguration; adgangskodefelter og adgangskode-CLI-indstillinger understøttes ikke. |
| `server.host` | `server.host` / `--host` | streng; standard `goserver.gokgs.com`. |
| `server.port` | `server.port` / `--port` | heltal; standard `2379`. |
| `reconnect=f` | `connectionRecovery.attempts = 0` | Deaktiverer KGS-transportforsøg igen; motorgenvinding konfigureres separat. |
| `reconnect=t` | `[connectionRecovery]` | Vælg et tidsbudget pr. udfald; standarden er 180 sekunder. Et forsøgsloft er valgfrit. |
| `engine` | `engine.executable` og `engine.arguments` | Opdel kommandoen i eksekverbare og individuelle argumenter; se nedenfor. |
| Ingen motorforbindelsesegenskaber | `engine.stdio = true` / `--stdio` | Standard I/O skal nu vælges eksplicit. |
| `gtp.in`, `gtp.out` | Ingen direkte indstilling | En ekstern launcher kan forbinde de to retninger gennem `--stdio`. Klienten åbner ikke navngivne filer eller FIFO'er fra konfigurationen. |
| `engine.port` | Ingen direkte indstilling | Der er ingen motor TCP-lytter. Brug en ekstern adapter med `--stdio`, eller lad klienten starte motoren. |
| `logFile` | Optag stderr eksternt | Brug shell-omdirigering eller en servicemanager; indbygget Java-lognavngivning og -rotation overføres ikke. |
| `verbose` | Ingen direkte indstilling | Normal diagnostik går til stderr; der er ingen tilsvarende fuld GTP/server trafiklogging switch. |

Den lokale `engineRecovery.pipe` er til udskiftning af en defekt motor i en kørende session. Det erstatter ikke de gamle `engine.port`, `gtp.in` eller `gtp.out` opstartsindstillinger.

### Matchmaking og spilindstillinger {#matchmaking-and-game-settings}

| Gammel ejendom | Ny indstilling | Migrationsnotater |
| --- | --- | --- |
| `mode=auto` | `matchmaking.mode = "Automatch"` | Udelad rum, brugerdefinerede modstanderindstillinger og `game`/`timing` sektionerne. |
| `mode=custom` | `matchmaking.mode = "Offer"` | Tilføj `opponentPolicy = "Any"` for åbne udfordringer, eller `"Named"` plus `opponent`. |
| `mode=wait` | `matchmaking.mode = "Join"` | Indstil rummets navn og `opponent`; den tilbudte profil skal matche nøjagtigt. |
| `mode=both` | Ingen kombineret tilstand | Vælg Automatch, Offer eller Join for denne påkaldelse. |
| `mode=tournament` | Ikke understøttet | Turneringsadgang er ikke implementeret; behold den gamle klient, hvis dette er påkrævet. |
| `room` | `matchmaking.room` / `--room` | Bevar værelsesnavnet som en citeret streng. Påkrævet til Offer og Join; udelad for Automatch. Der er ingen standard for sidst brugte rum. |
| `opponent` | `matchmaking.opponent` | Brug `opponentPolicy = "Named"` til brugerdefinerede udfordringer. Udelad begge brugerdefinerede modstandsindstillinger for Automatch. |
| `gameNotes` | `matchmaking.challengeNotes` | Kun Offer; højst 255 tegn uden kontroltegn. |
| `rules` | `game.rules` | Brug `Japanese`, `Chinese`, `Aga` eller `NewZealand`. Indstiller nøjagtige brugerdefinerede spilvilkår. |
| `komi` | `game.komi` | Nummer, ikke en citeret streng; indstilles eksplicit, herunder til handicapspil. |
| `rules.boardSize` | `game.boardSize` | Heltal. Indstillet eksplicit: den nye standard for brugerdefinerede spil er 9. |
| `rules.time` | `[timing]` | Opdel i system-, sekunder- og overtidsfelter ved hjælp af eksemplerne nedenfor. |
| `automatch.speed` | `automatch.speed` | For eksempel `speed = ["Blitz", "Medium"]` eller `"All"`. CLI-kombinationer bruger kommaer. |
| `automatch.rank` | `automatch.rank` | Citeret `30k` til `1k`; stadig påkrævet, når der ikke er nogen numerisk serverrangering. |
| `undo=f` | `[undo]` med `free = "Never"`, `ranked = "Never"` | Disse er også de indbyggede standardindstillinger. |
| `undo=t` eller udeladt | `[undo]` med `free = "Allow"`, `ranked = "Never"` | Bevarer den sædvanlige gamle Free/Ranked skelnen. Nye Ranked-tilbagetagelser kan aktiveres separat, hvis det ønskes. |
| `talk` | Ikke understøttet | Private chatsvar og videresendelse af motorchat er ikke implementeret. |
| `hint.cleanup`, `hint.noArguing` | Ikke understøttet | Der er ingen konfigurerbare chattip til scoringskonflikter. |

`game.rules` og `engine.rules` har forskellige formål. Førstnævnte vælger det brugerdefinerede spils regler. Sidstnævnte erklærer regler, der allerede er konfigureret i en motor, der mangler `kgs-rules`; det ændrer ikke motorens konfiguration.

### Opdel motorkommandoen {#split-the-engine-command}

En gammel ejendom kan være:

```properties
engine=/opt/katago/katago gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

Den nye konfiguration er:

```toml
[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]
```

Indsæt ikke en hel kommandolinje i `executable`. Der er ingen shell-evaluering. Hvert argument er ét array-element, inklusive stier, der indeholder mellemrum. For Windows, enkelt-citerede TOML-strenge holder omvendte skråstreger bogstavelige:

```toml
[engine]
executable = 'C:\Go Engines\katago.exe'
arguments = ["gtp", "-config", 'C:\Go Engines\gtp.cfg', "-model", 'C:\Go Engines\model.bin.gz']
```

Erstat Java-egenskaber med den faktiske tekst i UTF-8 TOML. Relative eksekverbare stier, der indeholder en separator, løses fra biblioteket TOML; argumentstier forbliver i forhold til startarbejdsmappen. Absolutte model- og konfigurationsstier gør servicelanceringer nemmere at reproducere.

### Konverter tidskontroller {#convert-time-controls}

Brug kun én af disse `[timing]` sektioner og kun med Offer eller Join.

Gammel `rules.time=0`:

```toml
[timing]
system = "None"
mainTime = 0
```

Gammel `rules.time=30:00`:

```toml
[timing]
system = "Absolute"
mainTime = 1800
```

Gammel `rules.time=30:00+5x0:30`:

```toml
[timing]
system = "ByoYomi"
mainTime = 1800
byoYomiTime = 30
byoYomiPeriods = 5
```

Gammel `rules.time=30:00+25/10:00`:

```toml
[timing]
system = "Canadian"
mainTime = 1800
byoYomiTime = 600
canadianStones = 25
```

Alle nye tidsværdier er heltalssekunder. Fjern overarbejdsfelter, der tilhører et andet system. Japansk ekstratid kræver motorens `kgs-time_settings`-kommando; det er ikke tilnærmet ved hjælp af et andet ursystem.

## Eksempel: migrer en automatch-bot {#example-migrate-an-automatch-bot}

Antag, at de relevante dele af den gamle fil er:

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

Opret denne `bot.toml` til et indledende Free-spil. Automatch tager ikke en rumindstilling, så den gamle `room` egenskab er udeladt:

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

For Windows skal du erstatte `[engine]`-stierne med Windows-eksemplet i [Opdel motorkommandoen](#split-the-engine-command). Indstil adgangskoden og kør et spil:

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

Dette eksempel vælger bevidst selv Free-spil. For at bevare handicaptilpasning skal du vælge en passende `maxRankDifference` og kontrollere motorstøtten. For at spille Ranked skal du vælge `gameType = "Ranked"`, verificere kontoens tilladelse til RankingRobot og aktiverede rang, og bruge højst seks rækker af forskel. En invokation kan ikke acceptere begge spiltyper.

For en brugerdefineret bot skal du bruge [custom challenge example]({% include page-url.html key='mobi/user-guide' %}#custom-challenges), kopiere det gamle rumnavn og eksplicit overføre indstillinger for boardstørrelse, regler, komi, farve, handicap og konverterede tidsindstillinger.

## Motorkompatibilitet og uovervåget drift {#engine-compatibility-and-unattended-operation}

Mobi kræver GTP v2 og dets komplette obligatoriske kommandosæt. Nogle kommandoer behandlet som valgfri af den gamle klient er påkrævet her. Alle automatiske spil kræver også `final_status_list`. Tidsindstillede spil kræver `time_left` og en understøttet timing-kommando. Tjek brugervejledningens motorkrav for din valgte profil; en gammel fungerende konfiguration alene etablerer ikke kompatibilitet.

Almindelig japansk scoringsaftale understøttes, men uløste japanske tvister stopper spillet. Kinesisk, AGA og New Zealand oprydning kræver `kgs-genmove_cleanup` og har begrænsede forsøg og en total deadline. Der er ingen gammel-klient fallback, der lader en modstander afgøre alle døde sten, når automatisk scoring ikke er tilgængelig.

Gennemgå disse tjenesteindstillinger, før du efterlader botten uden opsyn:

- Indstil `games = 0` eksplicit, hvis det skal fortsætte med at spille. Hvert lobbyforsøg har stadig en standard 300-sekund deadline; øg `timeouts.lobby` om nødvendigt.
- Konfigurer KGS-forbindelsen igen, og motoren genstartes separat. KGS-gendannelse er som standard 180 sekunder pr. afbrydelse og nulstilles efter 60 sunde sekunder. Motorgendannelse tillader tre automatiske udskiftninger på tværs af påkaldelsen; udmattelse kan efterlade en live KGS-session, der afventer operatørens genopretning.
- Vælg grænser for pause, udsættelse og modstander-fravær. Hver standard er 300 sekunder; udløb stopper klienten uden at tælle eller opgive det uafsluttede spil.
- Bevar klientidentitetsfilen i en skrivbar tilstandsmappe. En ny proces opdager ikke automatisk ældre automatch-spil.
- Fang stderr og arrangere ekstern logopbevaring. Afslut 0 betyder normal afslutning, 1 angiver fejl, og 130 angiver annullering.

[brugervejledningen]({% include page-url.html key='mobi/user-guide' %}#timeouts-and-recovery) beskriver timeoutindstillinger, forbindelsesgendannelse og operatørmotorgendannelse i detaljer.

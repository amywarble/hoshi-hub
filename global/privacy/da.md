---
source_revision: "6557edaea14029268590a7f73220e26c62aafda65681a4c44da3dd659e4b7ca7"
layout: "localized"
title: "Privatlivspolitik"
lang: "da"
page_key: "global/privacy"
section: "global"
nav_order: 3
permalink: "/da/privacy/"
redirect_from: "/da/desktop/privacy/"
---

_Gældende fra: 27. oktober 2026_

Denne politik dækker Pocket KGS til Android, KGS Nova til Windows, macOS og Linux, Mobi til Windows og Linux samt dette supportwebsted. Alle tre klienter er officielt godkendt af KGS og American Go Association (AGA). Fælles praksis beskrives først; appspecifik lagring og indstillinger findes nedenfor.

## Hvem håndterer dine data

Klienterne forbinder direkte til KGS Go Server. Klientudvikleren driver ikke KGS-serverne og bestemmer ikke over deres konti, moderation, registreringer eller opbevaring. KGS er en separat tjeneste med egne [tjenestevilkår og privatlivsoplysninger](https://www.gokgs.com/tos.jsp).

Klienterne indeholder ikke reklamer, analyseværktøjer eller automatisk upload af nedbrudsrapporter. Udvikleren sælger ikke dine personoplysninger og bruger dem ikke til målrettet reklame eller sporing på tværs af apps. Udvikleren opbevarer heller ikke en særskilt serverkopi af din KGS-konto, chat, spil, avatarer eller lærerlyd.

## Oplysninger og formål

Afhængigt af klienten og de anvendte funktioner omfatter oplysningerne:

- **Konti og profiler:** KGS-loginoplysninger, e-mailadresse, profiltekst, avatar, rang, kontostatus og præferencer.
- **Kommunikation og sociale oplysninger:** rum- og spilchat, private og offlinebeskeder, venne-/fan-/censorlister med noter samt andet KGS-indhold.
- **Spil og aktivitet:** træk, partier, kommentarer, resultater, udfordringer, rummemedlemskab og matchmakingindstillinger. Mobi udveksler spiloplysninger med den Go-motor, du konfigurerer til at generere træk og håndtere spil.
- **Forbindelsesoplysninger:** et vedvarende KGS-klient-id, app-/protokolversioner, sprog, operativsystem og arkitektur, runtimeoplysninger og forbindelsesstatus. KGS modtager din IP-adresse ved forbindelse.
- **Lokale indstillinger og diagnostik:** præferencer, cacheindhold og diagnostik beskrevet i appafsnittene nedenfor.

Oplysningerne bruges til login, KGS-sessioner, visning af indhold, afsendelse af ønskede handlinger eller konfigurerede bothandlinger til KGS, lagring af indstillinger og fejlfinding, når du vælger at dele oplysninger.

Pocket KGS og Nova håndterer også mikrofonlyd, når en berettiget underviser udtrykkeligt starter en liveudsendelse, og afspiller modtaget lærerlyd. Udsendelsen stopper, når du stopper den, eller den relevante session slutter. Ingen af klienterne opretter en særskilt lydoptagelse til udvikleren. Mobi har ikke funktioner til lærerlyd.

## Hvor oplysningerne sendes hen

- **KGS:** konto- og forbindelsesoplysninger, kommunikation, spilaktivitet og ønskede ændringer sendes til KGS. Andre brugere ser indhold i henhold til den anvendte KGS-funktion.
- **Loginudbydere og motorer:** platformens loginudbydere og din valgte Mobi-motor håndterer oplysninger som beskrevet nedenfor og efter deres egne vilkår.
- **GitHub:** webstedet og den offentlige fejlrapportering hostes af GitHub under [GitHubs privatlivspolitik](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Offentlige sager og vedhæftninger kan ses af alle. Novas fejlrapportering åbner en redigerbar browserkladde med appversion, operativsystem, arkitektur og runtimeoplysninger; den indsender ikke sagen eller vedhæfter logs automatisk.
- **Lov- og sikkerhedsbehov:** oplysninger, du giver udvikleren, kan opbevares eller videregives, når det med rimelighed er nødvendigt for at overholde loven, undersøge misbrug, beskytte brugere eller beskytte rettigheder og sikkerhed.

## Kommunikation og sikkerhed

Den ældre KGS-forbindelse, som klienterne bruger, tilbyder ikke TLS eller ende-til-ende-kryptering. Loginprotokollen omformer adgangskoden før overførsel, men anden trafik kan læses eller ændres af personer med adgang til netværksvejen. Brug et netværk, du stoler på.

KGS oplyser, at alle samtaler logges og kan gennemgås af administratorer ved undersøgelse af klager. Del ikke oplysninger på KGS, som skal forblive private. KGS styrer opbevaring på serveren, og partier kan forblive i arkiverne.

## Appspecifik lagring og valgmuligheder

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

Pocket gemmer præferencer, notifikationsvalg og sit KGS-klient-id i Androids private applager samt avatarer i Androids cache. Android kan rydde cachefiler. Pocket anmoder om, at Android ikke sikkerhedskopierer appens private data. Rydning af applageret eller afinstallation fjerner disse lokale appdata.

Hvis du gemmer loginoplysninger, håndterer Android Credential Manager og din valgte udbyder dem efter egne vilkår. Pocket modtager ikke biometriske data, der bruges til at låse loginoplysninger op. Gemte oplysninger hos udbyderen skal muligvis fjernes separat.

Produktionsudgaver skriver fejldiagnostik til Androids systemlog. Valgfri diagnostisk logning giver flere detaljer for den aktuelle session. Udgivelseslogs bevarer versionsoplysninger, hændelsesskabeloner, undtagelsestyper og stakspor med et format, der er beregnet til at udelade runtimeargumenters værdier, undtagelsesbeskeder og kildefilstier. Android, en enhedsadministrator eller personer, du giver logs til, kan få adgang til dem.

Du kan bruge en gæstesession, vælge om loginoplysninger gemmes, slå notifikationer fra i Pocket eller Android, nægte mikrofontilladelse, undlade udsendelser og censurere brugere for at blokere understøttede interaktioner og skjule deres indhold.

### KGS Nova

- **Database:** `data.db` i operativsystemets lokale appdatamappe for KGS Nova (`%LOCALAPPDATA%\KGS Nova` på Windows) indeholder gemte kontometadata, klient-id, præferencer og apptilstand. Databasen som helhed er ikke krypteret.
- **Adgangskoder:** Windows beskytter gemte adgangskoder i databasen med DPAPI for den aktuelle Windows-bruger. macOS bruger Keychain; Linux bruger Secret Service. Operativsystemet kan kræve oplåsning eller tilladelse. Resten af databasen krypteres ikke dermed.
- **Diagnostik:** udgivelsesfejl skrives til `client.log` og roterende `client.archive*.log` i samme mappe. Valgfri sessionsdiagnostik er mere detaljeret. Udgivelseslogs bruger samme udeladelsesprincip som Pocket. Udviklerudgaver kan skabe mere detaljeret `logs.txt` og konsol-/debugoutput.
- **Andre filer:** samme mappe indeholder arbejdsområdet `sgf`, gendannelsesfiler og sikkerhedskopier samt motor-/modelfiler i `analysis`. Eksporterede partier og andre filer forbliver der, hvor du gemmer dem.

Personer eller software med adgang til dine filer eller din OS-konto kan læse dem. Afinstallation eller udskiftning af Nova fjerner ikke nødvendigvis database, logs, eksporter eller nøgleringsposter. Du kan bruge en gæstesession, vælge om login huskes, styre understøttede privatbeskedinteraktioner, censurere brugere, undlade mikrofonudsendelser og fjerne lokale data.

### Mobi

Mobi kræver en registreret KGS-konto. Adgangskoden læses fra `KGS_PASSWORD` og gemmes ikke af Mobi selv. Startscripts, miljøindstillinger og tjenestestyring kan beholde loginoplysninger, du placerer der. Beskyt dem og din OS-konto; en startet motor kan arve miljøet.

Din TOML-konfiguration kan indeholde kontonavn, server, motorstier og spilindstillinger. Mobi gemmer KGS-klient-id i en lokal fil. Matchmaking bruger som standard `Kgs.Gtp/identities/<server-and-account-hash>` under .NETs lokale appdatamappe (`%LOCALAPPDATA%` på Windows); uden matchmaking er standarden `Kgs.Gtp/client-id`. `account.clientIdFile` eller `--client-id-file` kan ændre placeringen.

Status, fejl og motordiagnostik sendes til stderr. Logs bevares, hvis du omdirigerer output, eller en tjenestestyring gemmer det. Disse logs følger ikke Pocket/Novas regler for udeladelser og kan indeholde brugernavne, spildetaljer, stier eller motoroutput. Gennemgå dem før deling. Motoren kan oprette yderligere logs, partier eller filer og have egen netværksaktivitet; læs dens dokumentation og privatlivspraksis separat. Mobi uploader ikke automatisk diagnostik til udvikleren.

Du styrer motoren, konfigurationen, bevaret output og lokale filer. Se [Mobi-brugervejledningen]({% include page-url.html key='mobi/user-guide' %}) for drift og diagnostik.

## Opbevaring, sletning og andre valg

Udvikleren modtager ikke automatisk lokale filer eller diagnostik. Kopier, du vælger at sende, kan opbevares for at behandle henvendelsen eller af lov- og sikkerhedshensyn. Offentlige GitHub-sager og deres historik forbliver, indtil de redigeres eller slettes efter GitHubs funktioner og politikker.

Du vælger, hvilke profiloplysninger du deler, og kan markere din KGS-e-mail som privat, hvor det understøttes. Rydning af filer eller afinstallation sletter ikke KGS-hostede data. KGS-administratorer håndterer sletning af konto og serverdata. Se [Sletning af konto og data]({% include page-url.html key='global/account-and-data-deletion' %}) for den fælles anmodningsproces og hver klients lokale fjernelse.

Pocket KGS henvender sig ikke til børn under 13 år. KGS er en offentlig kommunikationstjeneste; en forælder eller værge bør gennemgå vilkår og egnethed, før en mindreårig bruger den. Offentliggør ikke et barns personoplysninger i offentlige sager.

## Ændringer og kontakt

Hold OS og klient opdateret, brug en unik KGS-adgangskode, og gennemgå logs før deling. Intet system er helt sikkert. Anmeld sårbarheder via [Sikkerhedspolitikken]({% include page-url.html key='global/security-policy' %}).

Politikken kan ændres sammen med klienterne; ikrafttrædelsesdatoen angiver den offentliggjorte revision. Brug [den offentlige fejlrapportering](https://github.com/amywarble/hoshi-hub/issues/new/choose) til ikke-følsom support. Kontakt [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com) om private app- eller privatlivsspørgsmål. Kontakt [admin@gokgs.com](mailto:admin@gokgs.com) om KGS-konti, serverdata eller moderation.

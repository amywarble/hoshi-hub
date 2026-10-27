---
source_revision: "2d36d2b70789618639852311a38a6f07a24e7e70cf3e48b416dc750ba7627c90"
layout: localized
title: "Privatlivspolitik"
lang: "da"
page_key: "desktop/privacy"
section: "desktop"
nav_order: 10
permalink: "/da/desktop/privacy/"
nav_group: "policies"
---

_Gældende fra: 27. oktober 2026_

Politikken dækker KGS Nova på Windows, macOS og Linux, en klient, der er officielt anbefalet af KGS. KGS er en separat tjeneste med egne [vilkår og privatlivsoplysninger](https://www.gokgs.com/tos.jsp).

## Behandlede oplysninger

Direkte forbindelse til KGS. Afhængigt af funktioner håndteres legitimationsoplysninger/profil, rum, chat og private/offlinebeskeder, sociale lister/noter, spiloptegnelser/træk, udfordringer, avatarer og indstillinger. Appen sender ønskede handlinger og viser KGS-svar. Andre ser indhold efter den anvendte KGS-funktion.

KGS modtager vedvarende klient-id, protokolversion, sprog/region, system, arkitektur, kørselsmiljø og forbindelsens netværksadresse.

Når en berettiget underviser starter udsendelse, sendes mikrofonen via KGS til deltagere. Modtagelse afspiller KGS-lyd. Udsendelse slutter ved dit stop eller sessionens slutning. Ingen særskilt optagelse til udvikleren.

Ingen reklamer, analyse eller automatisk upload af nedbrud. Ingen særskilt serverkopi hos udvikleren af konto, beskeder, spil eller lyd.

## Lokal lagring og diagnose

- **Database:** `data.db` i mappen KGS Nova under operativsystemets lokale programdata indeholder gemte kontometadata, klient-id, indstillinger og apptilstand. På Windows er mappen `%LOCALAPPDATA%\KGS Nova`. Hele databasen er ikke krypteret.
- **Adgangskoder:** Windows krypterer dem i databasen med DPAPI for den aktuelle bruger; macOS bruger Nøglering; Linux bruger Secret Service. Oplåsning/systemtilladelse kan være nødvendig. Resten af databasen krypteres ikke af adgangskodelagringen.
- **Logfiler:** Udgivelser skriver fejldiagnostik til `client.log` og roterende `client.archive*.log` i samme datamappe. Valgfri diagnoselogning giver flere hændelser i den aktuelle session. Udgivelseslogs bevarer version, hændelsesskabeloner, undtagelsestyper og stakspor med et format beregnet til at udelade argumentværdier, undtagelsesbeskeder og kildefilstier. Udviklerbyg kan give mere detaljeret `logs.txt` og konsol-/debugoutput. Gennemgå logs før deling. Ingen automatisk upload til udvikleren.
- **Eksporter:** spil og andre udtrykkeligt gemte filer bliver, hvor du valgte.

Personer/software med fil- eller systemkontoadgang kan muligvis læse data. Afinstallation/udskiftning fjerner ikke nødvendigvis database, logs, eksporter eller nøgleringsposter. Se [slettevejledningen]({% include page-url.html key='desktop/account-and-data-deletion' %}).

Datamappen indeholder også arbejdsområdet `sgf`, gendannelsesfiler og sikkerhedskopier samt motor-/modelfiler i `analysis`. Gem gendannede spil, du vil beholde, før mapperne slettes. Sletning af hele KGS Nova-datamappen fjerner disse lokale data samlet.

## Kommunikation og tredjeparter

Den gamle forbindelse bruger hverken TLS eller ende-til-ende-kryptering. Omdannelse af adgangskoden før afsendelse beskytter ikke al trafik mod overvågning/indgreb. Brug et betroet netværk.

KGS oplyser, at samtaler logges og kan læses af administratorer. Del ikke oplysninger, der skal være private. KGS styrer servermoderation og opbevaring.

GitHub hoster support og sager efter sin [privatlivserklæring](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Links åbner browseren. Fejlrapportering åbner et redigerbart udkast med version, system, arkitektur og kørselsmiljø. Ingen automatisk indsendelse eller vedhæftning af logs. Offentlige sager og bilag kan ses af alle.

## Valg og kontakt

Du kan bruge gæst, vælge lagring af adgangsdata, begrænse understøttede private interaktioner, censurere, undlade mikrofonudsendelser og slette lokale filer. KGS-administratorer sletter konti: [vejledning]({% include page-url.html key='desktop/account-and-data-deletion' %}).

Læg ikke børns personoplysninger i offentlige sager. Forældre/værger bør vurdere KGS-vilkår og kommunikation før mindreåriges brug.

Privat app/privatliv: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). KGS-konto/serverdata: [admin@gokgs.com](mailto:admin@gokgs.com). Sårbarheder: [privat rapportering](https://github.com/amywarble/hoshi-hub/security/advisories/new).

Politikken opdateres med appens adfærd; datoen angiver revisionen.

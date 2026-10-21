---
source_revision: "c0720ca8cede62afb75cc2d2bb2188cb6f42790a1a5ec1c815ee03a2934d2d54"
layout: localized
title: "Privatlivspolitik"
lang: "da"
page_key: "desktop/privacy"
section: "desktop"
nav_order: 10
permalink: "/da/desktop/privacy/"
---

_Gældende fra: 10. oktober 2026_

Politikken dækker KGS Nova på Windows, macOS og Linux, en uafhængig klient uden tilknytning til eller godkendelse fra KGS. KGS er en separat tjeneste med egne [vilkår og privatlivsoplysninger](https://www.gokgs.com/tos.jsp).

## Behandlede oplysninger

Direkte forbindelse til KGS. Afhængigt af funktioner håndteres legitimationsoplysninger/profil, rum, chat og private/offlinebeskeder, sociale lister/noter, spiloptegnelser/træk, udfordringer, avatarer og indstillinger. Appen sender ønskede handlinger og viser KGS-svar. Andre ser indhold efter den anvendte KGS-funktion.

KGS modtager vedvarende klient-id, protokolversion, sprog/region, system, arkitektur, kørselsmiljø og forbindelsens netværksadresse.

Når en berettiget underviser starter udsendelse, sendes mikrofonen via KGS til deltagere. Modtagelse afspiller KGS-lyd. Udsendelse slutter ved dit stop eller sessionens slutning. Ingen særskilt optagelse til udvikleren.

Ingen reklamer, analyse eller automatisk upload af nedbrud. Ingen særskilt serverkopi hos udvikleren af konto, beskeder, spil eller lyd.

## Lokal lagring og diagnose

- **Database:** `data.db` i arbejdsbiblioteket indeholder gemte kontometadata, klient-id, indstillinger og apptilstand. Hele databasen er ikke krypteret.
- **Adgangskoder:** Windows krypterer dem i databasen med DPAPI for den aktuelle bruger; macOS bruger Nøglering; Linux bruger Secret Service. Oplåsning/systemtilladelse kan være nødvendig. Resten af databasen krypteres ikke af adgangskodelagringen.
- **Logfiler:** `logs.txt` i appbiblioteket samt konsol-/debugoutput. Filen erstattes ved start. Kan indeholde version/system, brugernavne, rum-/spil-id, handlinger, undtagelser og protokoldata ved forbindelses-/beskedfejl. Antag ikke, at logs er uden persondata. Ingen automatisk upload.
- **Eksporter:** spil og andre udtrykkeligt gemte filer bliver, hvor du valgte.

Personer/software med fil- eller systemkontoadgang kan muligvis læse data. Afinstallation/udskiftning fjerner ikke nødvendigvis database, logs, eksporter eller nøgleringsposter. Se [slettevejledningen]({% include page-url.html key='desktop/account-and-data-deletion' %}).

## Kommunikation og tredjeparter

Den gamle forbindelse bruger hverken TLS eller ende-til-ende-kryptering. Omdannelse af adgangskoden før afsendelse beskytter ikke al trafik mod overvågning/indgreb. Brug et betroet netværk.

KGS oplyser, at samtaler logges og kan læses af administratorer. Del ikke oplysninger, der skal være private. KGS styrer servermoderation og opbevaring.

GitHub hoster support og sager efter sin [privatlivserklæring](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Links åbner browseren. Fejlrapportering åbner et redigerbart udkast med version, system, arkitektur og kørselsmiljø. Ingen automatisk indsendelse eller vedhæftning af logs. Offentlige sager og bilag kan ses af alle.

## Valg og kontakt

Du kan bruge gæst, vælge lagring af adgangsdata, begrænse understøttede private interaktioner, censurere, undlade mikrofonudsendelser og slette lokale filer. KGS-administratorer sletter konti: [vejledning]({% include page-url.html key='desktop/account-and-data-deletion' %}).

Læg ikke børns personoplysninger i offentlige sager. Forældre/værger bør vurdere KGS-vilkår og kommunikation før mindreåriges brug.

Privat app/privatliv: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). KGS-konto/serverdata: [admin@gokgs.com](mailto:admin@gokgs.com). Sårbarheder: [privat rapportering](https://github.com/amywarble/hoshi-hub/security/advisories/new).

Politikken opdateres med appens adfærd; datoen angiver revisionen.

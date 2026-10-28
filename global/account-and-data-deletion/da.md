---
source_revision: "2dd2b5f3a829514cb3f4e94bc67cffcd8f04dad8b5b984ffab73449fda82c3c7"
layout: "localized"
title: "Sletning af konto og data"
lang: "da"
page_key: "global/account-and-data-deletion"
section: "global"
nav_order: 2
permalink: "/da/account-and-data-deletion/"
redirect_from: "/da/desktop/account-and-data-deletion/"
---

_Senest opdateret: 27. oktober 2026_

Pocket KGS, KGS Nova og Mobi logger ind på konti, som hostes og kontrolleres af KGS Go Server. Ingen af klienterne har sit eget kontosystem. KGS opretter konti via den [officielle registreringsside](https://www.gokgs.com/register/index.html).

Lokal rydning/afinstallation sletter **ikke** KGS-konto, beskeder, spil, profil eller andre KGS-data.

## Slet KGS-konto og serverdata

1. Skriv til [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) med emnet `KGS account deletion request`.
2. Bed udtrykkeligt om sletning af konto og tilknyttede serverdata.
3. Medtag brugernavn og kontoens mailadresse. **Aldrig adgangskoden.**

En administrator kan kontrollere ejerskab, behandler anmodningen og forklarer forventet tid og eventuel opbevaring af hensyn til sikkerhed, tjenesteintegritet eller lovkrav. Sletning sker efter modtagelse og kontrol af anmodningen, aldrig automatisk ved afinstallation eller lokal rydning.

Del ikke kontooplysninger i offentlige GitHub-sager.

## Slet lokale appdata

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

1. Åbn Androids **Indstillinger**.
2. Vælg **Apps**, derefter **Pocket KGS**.
3. Vælg **Lager og cache**.
4. Vælg **Ryd lager** (navnet varierer) eller afinstallér.

Det fjerner indstillinger, lokalt klient-id og cachede avatarer. Appen beder Android om ikke at sikkerhedskopiere app-private data.

Slet særskilt adgangskoder gemt via Android Credential Manager hos den valgte adgangskodeadministrator/udbyder; datarydning fjerner ikke nødvendigvis dennes kopi.

### KGS Nova

Luk KGS Nova. Sikkerhedskopiér eksporterede spil, du vil beholde.

- Slet `data.db` og en eventuel `data-log.db` fra mappen KGS Nova under operativsystemets lokale programdata (`%LOCALAPPDATA%\KGS Nova` på Windows) for at fjerne gemte kontometadata, indstillinger, klient-id og apptilstand.
- Slet `client.log`, `client.archive*.log` og eventuel `logs.txt` fra udviklerbyg i samme datamappe for at fjerne diagnostik. Kopier gemt andre steder bliver der.
- Windows-adgangskoder beskyttet med DPAPI ligger i `data.db` og slettes med den. På macOS/Linux skal du særskilt slette appens Nøglering-/Secret Service-poster for tjenesten `io.github.amywarble.kgsnet.desktop.credentials` og dit KGS-brugernavn. Databasesletning fjerner ikke disse native poster.
- Slet uønskede eksporterede spil, skærmbilleder og andre filer fra de valgte placeringer.

Datamappen indeholder også arbejdsområdet `sgf`, gendannelsesfiler og sikkerhedskopier samt motor-/modelfiler i `analysis`. Gem gendannede spil, du vil beholde, før mapperne slettes. Sletning af hele KGS Nova-datamappen fjerner disse lokale data samlet.

Ældre versioner brugte `data.db`, `data-log.db` og `logs.txt` i appens eller startens bibliotek. Opgradering kan efterlade dem. Sikkerhedskopiér det nødvendige, og slet også gamle kopier; ellers kan en gammel database importeres igen, når den aktuelle mangler.

Afinstallation fjerner ikke nødvendigvis filer/native adgangsdata.

### Mobi

Stop Mobi og motoren, og deaktiver tjenester eller planlagte opgaver, der kan genstarte botten. Gem partier og konfiguration, du vil beholde.

- Slet klientidentitetsfilen valgt med `account.clientIdFile` eller `--client-id-file`. Uden en tilsidesættelse bruger matchmaking `Kgs.Gtp/identities/<server-and-account-hash>` under .NETs lokale appdatamappe (`%LOCALAPPDATA%` på Windows); andre kørsler bruger `Kgs.Gtp/client-id`. Fjern kun filer til konti, du udfaser, hvis andre bots kører på maskinen.
- Fjern `KGS_PASSWORD` fra startshellen og permanente miljøindstillinger, startscripts eller tjenestekonfiguration, hvor du gemte den. Mobi læser variablen, men gemmer ikke selv adgangskoden. Fjern gemte `KGS_USERNAME`-værdier og TOML-filer med kontonavne, stier eller indstillinger, hvis de ikke længere behøves.
- Slet diagnostik gemt ved omdirigering af stderr, såsom `bot.log`, samt bevarede tjenestelogs eller kopier delt andre steder, hvor du har kontrol over dem.
- Læs Go-motorens dokumentation for at fjerne dens egne logs, partier, konfiguration eller andre data. Motor-/modelfiler administreres separat fra Mobi; fjern ikke filer, som andre programmer stadig bruger.

Sletning af de udpakkede Mobi-filer fjerner ikke nødvendigvis disse elementer. Sletning af en klientidentitetsfil sletter ikke KGS-kontoen, nulstiller ikke dens rang og fjerner ikke serverens partier.

## Kontakt

Private spørgsmål om data gemt af en af appene kan sendes til [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

---
source_revision: "f77f4ed1d576932db0474a6793f3618116114ca1712e98af8892162d5ac9d665"
layout: localized
title: "Sletning af konto og data"
lang: "da"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/da/desktop/account-and-data-deletion/"
nav_group: "policies"
---

## Fjern computerdata

Luk KGS Nova. Sikkerhedskopiér eksporterede spil, du vil beholde.

- Slet `data.db` og en eventuel `data-log.db` fra mappen KGS Nova under operativsystemets lokale programdata (`%LOCALAPPDATA%\KGS Nova` på Windows) for at fjerne gemte kontometadata, indstillinger, klient-id og apptilstand.
- Slet `client.log`, `client.archive*.log` og eventuel `logs.txt` fra udviklerbyg i samme datamappe for at fjerne diagnostik. Kopier gemt andre steder bliver der.
- Windows-adgangskoder beskyttet med DPAPI ligger i `data.db` og slettes med den. På macOS/Linux skal du særskilt slette appens Nøglering-/Secret Service-poster for tjenesten `io.github.amywarble.kgsnet.desktop.credentials` og dit KGS-brugernavn. Databasesletning fjerner ikke disse native poster.
- Slet uønskede eksporterede spil, skærmbilleder og andre filer fra de valgte placeringer.

Datamappen indeholder også arbejdsområdet `sgf`, gendannelsesfiler og sikkerhedskopier samt motor-/modelfiler i `analysis`. Gem gendannede spil, du vil beholde, før mapperne slettes. Sletning af hele KGS Nova-datamappen fjerner disse lokale data samlet.

Ældre versioner brugte `data.db`, `data-log.db` og `logs.txt` i appens eller startens bibliotek. Opgradering kan efterlade dem. Sikkerhedskopiér det nødvendige, og slet også gamle kopier; ellers kan en gammel database importeres igen, når den aktuelle mangler.

Afinstallation fjerner ikke nødvendigvis filer/native adgangsdata. Lokale datasletninger sletter ikke KGS-konto eller serveroptegnelser.

## Anmod om KGS-kontosletning

KGS styrer konti/serverdata. Send privat anmodning til [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) med brugernavn og konto-mail, aldrig adgangskoden. En administrator kan kontrollere ejerskab og forklare sletbare data og opbevaringskrav. Ingen kontodata i offentlige GitHub-sager.

Private spørgsmål om computerdata: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

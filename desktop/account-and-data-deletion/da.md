---
source_revision: "3aa9378df5f32e6acf17ec4a44bd9f2964f9a6fed7d528cdcba256cfb2358d82"
layout: localized
title: "Sletning af konto og data"
lang: "da"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/da/desktop/account-and-data-deletion/"
---

## Fjern computerdata

Luk KGS Nova. Sikkerhedskopiér eksporterede spil, du vil beholde.

- Slet `data.db` fra arbejdsbiblioteket brugt til at starte appen. Det fjerner gemte kontometadata, indstillinger, klient-id og apptilstand og nulstiller lokale indstillinger. Ved terminalstart, kontrollér dette bibliotek samt appmappen.
- Slet `logs.txt` fra appbiblioteket. Andre logs kopieret eller gemt fra konsollen bliver på deres valgte steder.
- Windows-adgangskoder beskyttet med DPAPI ligger i `data.db` og slettes med den. På macOS/Linux skal du særskilt slette appens Nøglering-/Secret Service-poster for tjenesten `io.github.amywarble.kgsnet.desktop.credentials` og dit KGS-brugernavn. Databasesletning fjerner ikke disse native poster.
- Slet uønskede eksporterede spil, skærmbilleder og andre filer fra de valgte placeringer.

Afinstallation fjerner ikke nødvendigvis filer/native adgangsdata. Lokale datasletninger sletter ikke KGS-konto eller serveroptegnelser.

## Anmod om KGS-kontosletning

KGS styrer konti/serverdata. Send privat anmodning til [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) med brugernavn og konto-mail, aldrig adgangskoden. En administrator kan kontrollere ejerskab og forklare sletbare data og opbevaringskrav. Ingen kontodata i offentlige GitHub-sager.

Private spørgsmål om computerdata: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

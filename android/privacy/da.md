---
source_revision: "1ea1406557dd0aedaa3365f2977f3ad59b019646d739221b9e7e12a0593d0e87"
layout: localized
title: "Privatlivspolitik"
lang: "da"
page_key: "android/privacy"
section: "android"
nav_order: 10
permalink: "/da/privacy/"
nav_group: "policies"
---

_Gældende fra: 27. oktober 2026_

Pocket KGS er en Android-klient til KGS Go Server (»KGS«), officielt anbefalet af KGS. Politikken forklarer, hvilke oplysninger appen behandler, formål, modtagere og dine valg. Den dækker Pocket KGS og dette supportwebsted. KGS er en separat tjeneste med egne [service- og privatlivsvilkår](https://www.gokgs.com/tos.jsp).

## Hvem håndterer data

Appen forbinder direkte til KGS. Udvikleren leverer klienten, men driver ikke KGS-serverne og styrer ikke serveroptegnelser, moderation eller opbevaring. Appen indeholder ikke reklamer, brugsanalyse eller automatisk nedbrudsrapportering. Udvikleren sælger ikke dine personoplysninger.

## Oplysninger appen håndterer

Afhængigt af brugte funktioner:

- **Konto og profil:** KGS-brugernavn, adgangskode, mailadresse, profiltekst, avatar, rang, kontostatus og profilindstillinger.
- **Kommunikation og indhold:** offentlige rum- og spilchats, private og offlinebeskeder, spiloptegnelser, kommentarer, udfordringer og andet indhold sendt til eller modtaget fra KGS.
- **Lyd:** mikrofonen, når en berettiget underviser udtrykkeligt starter en undervisningsudsendelse. Appen sender lyden direkte via KGS til spillets deltagere. Udsendelsen stopper, når du stopper den eller sessionen slutter; der oprettes ikke en særskilt optagelse til udvikleren.
- **Sociale oplysninger:** venne-, fan- og censurlister samt dine noter om relationerne.
- **Spil og aktivitet:** spillede/observerede spil, træk, resultater, indstillinger, rumdeltagelse, udfordringer og interaktioner med KGS-funktioner.
- **Enhed og forbindelse:** vedvarende KGS-klient-id, app-/protokolversion, sprog/region, operativsystem og version, processorarkitektur, kørselsmiljøets leverandør/version, netværksstatus og nødvendige forbindelsesdata. KGS modtager nødvendigvis din IP-adresse.
- **Notifikationer:** lokale valg om KGS-hændelser, som må udløse Android-notifikationer.
- **Cache:** avatarer og appindstillinger for effektiv drift.
- **Diagnoselogfiler:** Udgivelser skriver fejldiagnostik til Androids systemlog. Valgfri diagnoselogning giver flere hændelser i den aktuelle session. Udgivelseslogs bevarer version, hændelsesskabeloner, undtagelsestyper og stakspor med et format beregnet til at udelade argumentværdier, undtagelsesbeskeder og kildefilstier. Gennemgå logs før deling. Pocket KGS uploader dem ikke automatisk. Android, enhedsadministratoren eller en person, du giver loggen til, kan have adgang.

## Anvendelse

Oplysninger bruges til login og session; ønskede ændringer i din eksisterende KGS-profil; visning af rum, brugere, spil, profiler, beskeder og andet indhold; afsendelse af træk, beskeder, profilændringer, avatar, lyd og ønskede handlinger; lokale indstillinger, klient-id og notifikationsvalg; aktiverede notifikationer; og fejldiagnose, når du frivilligt deler oplysninger. Ingen målrettede reklamer eller sporing på tværs af apps.

## Modtagere

Kun videregivelse efter behov til:

- **KGS:** kontodata, kommunikation, spilaktivitet, profil, undervisningslyd, enheds-/kørselsmiljødata, klient-id og forbindelsesdata for at levere tjenesten. Andre brugere ser det indhold, som funktionen offentliggør eller deler med dem.
- **Androids legitimationsudbydere:** vælger du adgangskodefunktionen, håndterer Android Credential Manager og den valgte udbyder brugernavn/adgangskode efter egne privatlivsvilkår. Pocket KGS modtager ikke biometriske oplåsningsdata.
- **GitHub:** websted og offentlige sager hostes af GitHub. Indsendelser behandles efter [GitHubs privatlivserklæring](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement); offentlige sager kan ses af alle.
- **Juridiske og sikkerhedsmæssige behov:** oplysninger modtaget af udvikleren kan bevares eller videregives, når rimeligt nødvendigt for lovkrav, beskyttelse af brugere, undersøgelse af misbrug eller beskyttelse af appens og andres rettigheder og sikkerhed.

## Kommunikation og transport

KGS oplyser, at alle samtaler logges og kan gennemgås af administratorer ved undersøgelser. Brug ikke chatten til oplysninger, der skal forblive private.

Den gamle KGS-protokol giver ikke en moderne TLS-beskyttet forbindelse. Loginprotokollen omdanner adgangskoden før afsendelse, men anden trafik er hverken TLS- eller ende-til-ende-krypteret. En person, der kan overvåge eller påvirke netværksvejen, kan muligvis læse eller ændre trafik. Undgå netværk, du ikke stoler på.

## Lagring og opbevaring

Klient-id og indstillinger gemmes privat i appen, avatarer i Android-cache, som kan ryddes ved pladsmangel. Rydning af appdata eller afinstallation fjerner app-private data. Adgangskoder gemt via Android Credential Manager skal muligvis slettes særskilt fra adgangskodeadministratoren.

Udvikleren gemmer ikke særskilte serverkopier af konto, chat, spil, avatar eller undervisningslyd. KGS styrer sin egen opbevaring, oplyser at samtaler logges, og spil kan fortsat være tilgængelige i arkiver.

Anmod om konto- og serverdatasletning hos [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request), med brugernavn og kontoens mailadresse, aldrig adgangskoden. En administrator kan kontrollere ejerskab og behandler anmodningen. Se [slettevejledningen]({% include page-url.html key='android/account-and-data-deletion' %}), også om lokale data. Offentlige GitHub-sager og historik bliver på GitHub indtil redigering/sletning efter deres funktioner og politikker.

## Dine valg

Du kan bruge gæstesession frem for at oprette konto på KGS-webstedet; vælge adgangskodelagring; markere KGS-mailadressen privat, hvor muligt; vælge avatar og profilændringer; nægte mikrofon og undlade undervisningsudsendelser; slå notifikationer fra i appen/Android; censurere brugere for at blokere understøttede interaktioner og skjule indhold; rydde lokale data eller afinstallere; og følge [slettevejledningen]({% include page-url.html key='android/account-and-data-deletion' %}).

## Børn

Pocket KGS er ikke rettet mod børn under 13 år. KGS er en offentlig tjeneste, hvor brugere kommunikerer. Forældre/værger bør gennemgå vilkår og egnethed før mindreåriges brug. Indsend ikke børns personoplysninger i offentlige sager.

## Sikkerhed

Intet system er fuldstændigt sikkert. Hold app/enhed opdateret, brug en unik KGS-adgangskode, og læg ikke legitimationsoplysninger eller privat indhold i offentlige sager. Se [sikkerhedspolitikken]({% include page-url.html key='global/security-policy' %}) om sårbarheder.

## Ændringer

Politikken kan ændres med appen. Datoen opdateres ved væsentlige revisioner. Fortsat brug efter ændring betyder, at den reviderede politik gælder for efterfølgende brug.

## Kontakt

Generel apphjælp uden personlige/følsomme data: [offentlige sager](https://github.com/amywarble/hoshi-hub/issues/new/choose). Private app-, privatlivs- og følsomme sikkerhedsspørgsmål: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). KGS-konti, serverdata, moderation eller tjeneste: [admin@gokgs.com](mailto:admin@gokgs.com).

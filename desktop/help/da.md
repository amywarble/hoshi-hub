---
source_revision: "a5018456d7c6b6ef49fc5b143b52c2707452b29213029b1bba9cf85a02f24031"
layout: localized
title: "Kom godt i gang"
lang: "da"
page_key: "desktop/help"
section: "desktop"
nav_order: 1
permalink: "/da/desktop/help/"
nav_group: "documentation"
redirect_from: "/da/desktop/"
---

KGS Nova er en klient til [KGS Go Server](https://www.gokgs.com/) til Windows, macOS og Linux. Appen er officielt anbefalet af KGS og American Go Association (AGA).

## Installation og opdateringer {#installation}

Hent en **KGS Nova**-pakke fra [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases). Vælg x64 til Intel/AMD-processorer eller ARM64 til Apple Silicon og andre ARM64-enheder. Hver udgivelse viser de tilgængelige platforme. .NET-kørselsmiljøet er inkluderet.

- **Windows:** Kør **Installer**. Til en bærbar installation skal hele **Portable**-ZIP-filen pakkes ud i en mappe med skriveadgang, hvorefter du kører `Kgs.Client.Desktop.exe`.
- **Linux:** Gør **AppImage** eksekverbar med `chmod +x Kgs.Nova-linux-<architecture>.AppImage` (`x64` eller `arm64`), og start den. Opbevar den i en mappe med skriveadgang til opdateringer. FUSE er påkrævet (`libfuse2` på Ubuntu 22.04).
- **macOS (når tilgængelig):** Kør **Installer**, og åbn `KGS Nova.app`. Til en bærbar installation skal hele **Portable**-ZIP-filen pakkes ud, og appen flyttes til en Applications-mappe med skriveadgang. Byggene er ad hoc-signerede uden Apple Developer ID-signering eller notarisering. Hvis appen blokeres, kan du tillade Nova i **Systemindstillinger > Anonymitet & sikkerhed**, når du har bekræftet, at du stoler på overførslen.

Vælg **Søg efter opdateringer**, **Hent opdatering** og derefter **Genstart og opdater** i **Om**. Nova søger også ved opstart. Afslut spil, og gem dit arbejde før genstart. Hvis opdatering i appen ikke er tilgængelig, skal du hente en nyere pakke manuelt.

### Manuel installation på Linux

Pak `KGS-Nova-<version>-linux-<architecture>.tar.gz` ud, og kør `./Kgs.Client.Desktop` fra mappen. Disse arkiver kræver en ny overførsel ved opdatering.

Linux kræver X11 eller XWayland, fontconfig og de X11-biblioteker, som .NET/Avalonia bruger. Lyd bruger PipeWire, PulseAudio eller ALSA. Lagring af adgangskoder kræver libsecret (`libsecret-1-0` på Debian/Ubuntu) og en Secret Service-udbyder som GNOME Keyring.

### Opdateringsfiler

`.nupkg` og `releases.*.json` bruges af Novas opdateringsfunktion. Installer med **Installer**, **Portable**-ZIP eller **AppImage**.

## Log ind

Log ind med dit KGS-brugernavn og din adgangskode, eller fortsæt som gæst. Brug registreringslinket på login-skærmen for at oprette en konto på KGS-webstedet.

## Spil og udforsk

Vælg Spil for at finde en modstander eller oprette et tilpasset spil. Brug Rum til samtaler og til at se spil, og Personer til at finde spillere. Vis/redigér åbner SGF-filer til lokale studier. Præferencer styrer udseende og indstillinger.

## Hjælp og politikker

Ved appproblemer, se [Support]({% include page-url.html key='desktop/support' %}). Om uønsket kontakt og rapporter, se [Fællesskabsregler]({% include page-url.html key='desktop/community-guidelines' %}). Læs appens [Privatlivspolitik]({% include page-url.html key='global/privacy' %}) og [brugsvilkår]({% include page-url.html key='desktop/terms' %}) samt de [fælles fællesskabsregler]({% include page-url.html key='global/community-guidelines' %}).

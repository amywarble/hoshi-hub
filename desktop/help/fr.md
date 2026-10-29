---
source_revision: "a5018456d7c6b6ef49fc5b143b52c2707452b29213029b1bba9cf85a02f24031"
layout: localized
title: "Premiers pas"
lang: "fr"
page_key: "desktop/help"
section: "desktop"
nav_order: 1
permalink: "/fr/desktop/help/"
nav_group: "documentation"
redirect_from: "/fr/desktop/"
---

KGS Nova est un client du [KGS Go Server](https://www.gokgs.com/) pour Windows, macOS et Linux. Il est officiellement approuvé par KGS et l’American Go Association (AGA).

## Installation et mises à jour {#installation}

Téléchargez un paquet **KGS Nova** depuis [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases). Choisissez x64 pour les processeurs Intel/AMD ou ARM64 pour Apple Silicon et les autres appareils ARM64. Chaque version indique les plateformes disponibles. L’environnement d’exécution .NET est inclus.

- **Windows :** Lancez **Installer**. Pour une installation portable, extrayez tout le ZIP **Portable** dans un dossier accessible en écriture, puis lancez `Kgs.Client.Desktop.exe`.
- **Linux :** Rendez **AppImage** exécutable avec `chmod +x Kgs.Nova-linux-<architecture>.AppImage` (`x64` ou `arm64`), puis lancez-le. Conservez-le dans un dossier accessible en écriture pour les mises à jour. FUSE est nécessaire (`libfuse2` sous Ubuntu 22.04).
- **macOS (si disponible) :** Lancez **Installer**, puis ouvrez `KGS Nova.app`. Pour une installation portable, extrayez tout le ZIP **Portable** et déplacez l’application dans un dossier Applications accessible en écriture. Les versions ont une signature ad hoc, sans signature Apple Developer ID ni notarisation. En cas de blocage, autorisez Nova dans **Réglages Système > Confidentialité et sécurité** après avoir vérifié que vous faites confiance au téléchargement.

Dans **À propos**, choisissez **Rechercher des mises à jour**, **Télécharger la mise à jour**, puis **Redémarrer et mettre à jour**. Nova vérifie aussi au démarrage. Terminez vos parties et enregistrez votre travail avant de redémarrer. Si la mise à jour dans l’application est indisponible, téléchargez manuellement un paquet plus récent.

### Installation manuelle sous Linux

Extrayez `KGS-Nova-<version>-linux-<architecture>.tar.gz` et lancez `./Kgs.Client.Desktop` depuis ce dossier. Ces archives nécessitent un nouveau téléchargement pour les mises à jour.

Linux nécessite X11 ou XWayland, fontconfig et les bibliothèques X11 utilisées par .NET/Avalonia. L’audio utilise PipeWire, PulseAudio ou ALSA. Le stockage des mots de passe nécessite libsecret (`libsecret-1-0` sous Debian/Ubuntu) et un fournisseur Secret Service tel que GNOME Keyring.

### Fichiers de mise à jour

Les fichiers `.nupkg` et `releases.*.json` servent au programme de mise à jour de Nova. Installez avec **Installer**, le ZIP **Portable** ou **AppImage**.

## Se connecter

Connectez-vous avec votre identifiant et mot de passe KGS, ou continuez comme invité. Pour créer un compte, utilisez le lien d’inscription de l’écran de connexion ; il ouvre le site KGS.

## Jouer et explorer

Choisissez Jouer pour chercher un adversaire ou créer une partie. Salons permet de discuter et d’observer des parties ; Personnes permet de trouver des joueurs. Voir/modifier ouvre des fichiers SGF pour l’étude locale. Les préférences règlent l’apparence et l’application.

## Aide et politiques

Pour les problèmes d’application, consultez [Assistance]({% include page-url.html key='desktop/support' %}). Pour les contacts indésirables et signalements, voir [Règles de la communauté]({% include page-url.html key='desktop/community-guidelines' %}). Lisez la [Politique de confidentialité]({% include page-url.html key='global/privacy' %}), les [conditions d’utilisation]({% include page-url.html key='desktop/terms' %}) et les [règles de la communauté partagées]({% include page-url.html key='global/community-guidelines' %}).

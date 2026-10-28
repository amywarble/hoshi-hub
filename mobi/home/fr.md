---
layout: "localized"
title: "Mobi"
nav_title: "Premiers pas"
lang: "fr"
page_key: "mobi/home"
section: "mobi"
nav_order: 0
permalink: "/fr/gtp/"
source_revision: "b9d339585b5a920216045e5e3c1e6b45997754a2b3e257c811c18c8f9c33e4ca"
---

Mobi relie un moteur de Go compatible avec Go Text Protocol (GTP) version 2 au [KGS Go Server](https://www.gokgs.com/). Il gère la connexion, l’appariement, les coups, les pendules, le décompte et la récupération. Installez et configurez votre moteur de Go séparément.

Mobi est officiellement approuvé par KGS et American Go Association (AGA).

## Téléchargez et commencez {#download-and-get-started}

Téléchargez une archive **Pont Mobi GTP** à partir de [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) pour Windows ou Linux sur x64 ou ARM64. Le runtime .NET est inclus. Les packages Windows utilisent ZIP ; Les packages Linux utilisent tar.gz. Conservez les fichiers extraits ensemble.

- [Guide de l'utilisateur]({% include page-url.html key='mobi/user-guide' %}) : premier jeu, configuration, matchmaking, journaux, délais d'attente, récupération et dépannage.
- [Guide de mise à niveau du client Java]({% include page-url.html key='mobi/upgrade-guide' %}) : passer des propriétés `kgsGtp.jar` et Java à TOML.
- [Exemple de configuration]({{ '/mobi/bot.example.toml' | relative_url }}) : copiez dans `bot.toml` et définissez votre compte, les chemins du moteur et les préférences de jeu.
- [Conditions d'utilisation]({% include page-url.html key='mobi/terms' %}) : fonctionnement de votre bot, licence du moteur et responsabilités lors de l'utilisation de Mobi.
- [Règlement de la communauté]({% include page-url.html key='mobi/community-guidelines' %}) : identités de robots honnêtes, fair-play et utilisation responsable des ressources du serveur.

Les pages partagées [Politique de confidentialité]({% include page-url.html key='global/privacy' %}) et [Suppression de compte et de données]({% include page-url.html key='global/account-and-data-deletion' %}) incluent des informations spécifiques à Mobi.

Les guides couvrent Windows avec PowerShell et Linux avec Bash. Développez la section correspondant à votre système d'exploitation. Chaque archive comprend également l'exemple de configuration et des copies hors ligne en anglais des deux guides.

## Exécuter le client {#run-the-client}

Après avoir configuré `bot.toml`, exécutez ces commandes à partir du répertoire extrait. La sonde vérifie le moteur sans se connecter à KGS ; la commande suivante joue à un jeu avec les paramètres de matchmaking configurés.

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --probe
$env:KGS_PASSWORD = '<account password>'
.\Kgs.Gtp.exe --config .\bot.toml --games 1
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
chmod +x ./Kgs.Gtp
./Kgs.Gtp --config ./bot.toml --probe
read -r -s -p 'KGS password: ' KGS_PASSWORD
export KGS_PASSWORD
printf '\n'
./Kgs.Gtp --config ./bot.toml --games 1
```

</details>

Appuyez sur Ctrl+C pour arrêter. Utilisez le guide de l'utilisateur pour choisir la lecture continue, conserver les journaux et préserver l'identité du client lors des mises à niveau.

Pour les bogues et les corrections de documentation, [ouvrez un numéro public GitHub](https://github.com/amywarble/hoshi-hub/issues/new/choose) et identifiez le client comme **Mobi**. Incluez les versions du client et du moteur ainsi que les diagnostics pertinents. Omettez les mots de passe et autres informations sensibles.

---
layout: "localized"
title: "Mobi"
nav_title: "Premiers pas"
lang: "fr"
page_key: "mobi/home"
section: "mobi"
nav_order: 0
permalink: "/fr/gtp/"
source_revision: "874054b8ddaecac1e59dd93fb146bb94e87a23f895e0f2763c1c7f0413376a1a"
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

[Signalez un problème avec Mobi](https://github.com/amywarble/hoshi-hub/issues/new?template=mobi_problem_report.yml). Pour corriger la documentation, [ouvrez un ticket public sur GitHub](https://github.com/amywarble/hoshi-hub/issues/new/choose) et mentionnez **Mobi**. N’incluez jamais de mots de passe ni d’autres informations sensibles.

Aucune connaissance technique n’est nécessaire pour signaler un problème. Décrivez avec vos propres mots ce qui s’est passé, même si cela n’est arrivé qu’une fois. Indiquez ce que vous savez ; nous pourrons poser des questions ensuite. Les versions, les étapes et les captures d’écran sont facultatives. Masquez les informations privées dans les captures avant de les partager.

Vous n’utilisez pas GitHub ? Vous pouvez aussi signaler les problèmes de l’application par e-mail à [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

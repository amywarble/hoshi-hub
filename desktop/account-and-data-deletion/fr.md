---
source_revision: "f77f4ed1d576932db0474a6793f3618116114ca1712e98af8892162d5ac9d665"
layout: localized
title: "Suppression du compte et des données"
lang: "fr"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/fr/desktop/account-and-data-deletion/"
nav_group: "policies"
---

## Supprimer les données de l’ordinateur

Fermez KGS Nova et sauvegardez les parties exportées à conserver.

- Supprimez `data.db` et tout journal `data-log.db` du dossier KGS Nova des données locales d’application (`%LOCALAPPDATA%\KGS Nova` sous Windows) pour effacer métadonnées des comptes, préférences, identifiant et état.
- Pour effacer les diagnostics, supprimez `client.log`, `client.archive*.log` et tout `logs.txt` de développement du même dossier. Les copies enregistrées ailleurs y restent.
- Sous Windows, les mots de passe protégés par DPAPI sont dans `data.db` et supprimés avec lui. Sous macOS/Linux, supprimez séparément les entrées du Trousseau/Secret Service : service `io.github.amywarble.kgsnet.desktop.credentials` et nom KGS. Supprimer la base ne supprime pas ces entrées natives.
- Supprimez les parties exportées, captures et autres fichiers dont vous ne voulez plus, là où vous les avez enregistrés.

Ce dossier contient aussi l’espace `sgf`, les fichiers de récupération et sauvegardes, ainsi que les moteurs/modèles dans `analysis`. Enregistrez les parties récupérées à conserver avant suppression. Supprimer tout le dossier de données KGS Nova efface ensemble ces données locales.

Les anciennes versions utilisaient `data.db`, `data-log.db` et `logs.txt` dans le répertoire de l’application ou de lancement. Une mise à niveau peut laisser ces copies. Sauvegardez le nécessaire et supprimez aussi les anciennes copies ; une ancienne base pourrait sinon être réimportée si la base actuelle manque.

Désinstaller ne supprime pas nécessairement fichiers ou identifiants natifs. Effacer les données locales ne supprime ni compte KGS ni dossiers serveur.

## Demander la suppression du compte KGS

KGS contrôle comptes et données serveur. Écrivez en privé à [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) avec nom KGS et adresse du compte, jamais le mot de passe. Un administrateur peut vérifier la propriété et expliquer les données supprimables et obligations de conservation. Ne publiez pas de détails du compte dans GitHub.

Questions privées sur les données locales : [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

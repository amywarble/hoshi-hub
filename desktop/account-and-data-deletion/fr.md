---
source_revision: "3aa9378df5f32e6acf17ec4a44bd9f2964f9a6fed7d528cdcba256cfb2358d82"
layout: localized
title: "Suppression du compte et des données"
lang: "fr"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/fr/desktop/account-and-data-deletion/"
---

## Supprimer les données de l’ordinateur

Fermez KGS Nova et sauvegardez les parties exportées à conserver.

- Supprimez `data.db` du répertoire de travail utilisé pour lancer l’application : cela efface métadonnées des comptes mémorisés, préférences, identifiant client et état, et réinitialise les réglages. En cas de lancement depuis un terminal, vérifiez aussi son répertoire en plus du dossier de l’application.
- Supprimez `logs.txt` dans le répertoire de l’application. Les journaux copiés ou enregistrés depuis la console restent à leurs emplacements.
- Sous Windows, les mots de passe protégés par DPAPI sont dans `data.db` et supprimés avec lui. Sous macOS/Linux, supprimez séparément les entrées du Trousseau/Secret Service : service `io.github.amywarble.kgsnet.desktop.credentials` et nom KGS. Supprimer la base ne supprime pas ces entrées natives.
- Supprimez les parties exportées, captures et autres fichiers dont vous ne voulez plus, là où vous les avez enregistrés.

Désinstaller ne supprime pas nécessairement fichiers ou identifiants natifs. Effacer les données locales ne supprime ni compte KGS ni dossiers serveur.

## Demander la suppression du compte KGS

KGS contrôle comptes et données serveur. Écrivez en privé à [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) avec nom KGS et adresse du compte, jamais le mot de passe. Un administrateur peut vérifier la propriété et expliquer les données supprimables et obligations de conservation. Ne publiez pas de détails du compte dans GitHub.

Questions privées sur les données locales : [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

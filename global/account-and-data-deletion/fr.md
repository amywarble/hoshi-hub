---
source_revision: "2dd2b5f3a829514cb3f4e94bc67cffcd8f04dad8b5b984ffab73449fda82c3c7"
layout: "localized"
title: "Suppression du compte et des données"
lang: "fr"
page_key: "global/account-and-data-deletion"
section: "global"
nav_order: 2
permalink: "/fr/account-and-data-deletion/"
redirect_from: "/fr/desktop/account-and-data-deletion/"
---

_Dernière mise à jour : 27 octobre 2026_

Pocket KGS, KGS Nova et Mobi utilisent des comptes hébergés et contrôlés par KGS Go Server. Aucun de ces clients ne gère de comptes distincts. KGS crée les comptes sur sa [page officielle d’inscription](https://www.gokgs.com/register/index.html).

Effacement local et désinstallation ne suppriment **pas** compte KGS, messages, parties, profil ni autres données détenues par KGS.

## Supprimer le compte KGS et les données serveur

1. Écrivez à [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request), objet `KGS account deletion request`.
2. Demandez explicitement la suppression du compte et des données serveur associées.
3. Indiquez nom KGS et adresse du compte. **Jamais votre mot de passe.**

Un administrateur peut vérifier la propriété du compte, traiter la demande et expliquer le délai et les éventuelles conservations nécessaires pour sécurité, intégrité du service ou raisons légales. La suppression suit une demande reçue et vérifiée par un administrateur ; elle n’est jamais automatique après désinstallation ou effacement local.

Ne publiez pas les informations de votre compte dans un ticket GitHub public.

## Supprimer les données locales

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

1. Ouvrez les **Paramètres** Android.
2. Sélectionnez **Applications**, puis **Pocket KGS**.
3. Ouvrez **Stockage et cache**.
4. Choisissez **Effacer le stockage** (libellé variable) ou désinstallez.

Cela supprime préférences, identifiant client local et avatars en cache. Pocket KGS demande à Android de ne pas sauvegarder ses données privées.

Supprimez séparément les mots de passe enregistrés via Android Credential Manager dans le gestionnaire/fournisseur choisi : effacer l’application ne supprime pas nécessairement sa copie.

### KGS Nova

Fermez KGS Nova et sauvegardez les parties exportées à conserver.

- Supprimez `data.db` et tout journal `data-log.db` du dossier KGS Nova des données locales d’application (`%LOCALAPPDATA%\KGS Nova` sous Windows) pour effacer métadonnées des comptes, préférences, identifiant et état.
- Pour effacer les diagnostics, supprimez `client.log`, `client.archive*.log` et tout `logs.txt` de développement du même dossier. Les copies enregistrées ailleurs y restent.
- Sous Windows, les mots de passe protégés par DPAPI sont dans `data.db` et supprimés avec lui. Sous macOS/Linux, supprimez séparément les entrées du Trousseau/Secret Service : service `io.github.amywarble.kgsnet.desktop.credentials` et nom KGS. Supprimer la base ne supprime pas ces entrées natives.
- Supprimez les parties exportées, captures et autres fichiers dont vous ne voulez plus, là où vous les avez enregistrés.

Ce dossier contient aussi l’espace `sgf`, les fichiers de récupération et sauvegardes, ainsi que les moteurs/modèles dans `analysis`. Enregistrez les parties récupérées à conserver avant suppression. Supprimer tout le dossier de données KGS Nova efface ensemble ces données locales.

Les anciennes versions utilisaient `data.db`, `data-log.db` et `logs.txt` dans le répertoire de l’application ou de lancement. Une mise à niveau peut laisser ces copies. Sauvegardez le nécessaire et supprimez aussi les anciennes copies ; une ancienne base pourrait sinon être réimportée si la base actuelle manque.

Désinstaller ne supprime pas nécessairement fichiers ou identifiants natifs.

### Mobi

Arrêtez Mobi et son moteur, puis désactivez tout service ou tâche planifiée pouvant redémarrer le bot. Sauvegardez les parties ou configurations à conserver.

- Supprimez le fichier d’identité choisi par `account.clientIdFile` ou `--client-id-file`. Sans remplacement, l’appariement utilise `Kgs.Gtp/identities/<server-and-account-hash>` dans le répertoire local de données de .NET (`%LOCALAPPDATA%` sous Windows) ; les autres exécutions utilisent `Kgs.Gtp/client-id`. Si d’autres bots utilisent cette machine, supprimez uniquement les fichiers des comptes retirés.
- Retirez `KGS_PASSWORD` du shell de lancement et des paramètres d’environnement persistants, scripts de lancement ou configurations de service où vous l’avez enregistré. Mobi lit cette variable sans conserver lui-même le mot de passe. Retirez les valeurs enregistrées de `KGS_USERNAME` et les fichiers TOML contenant comptes, chemins ou réglages devenus inutiles.
- Supprimez les diagnostics conservés par redirection de stderr, par exemple `bot.log`, ainsi que les journaux de services ou copies partagées ailleurs que vous contrôlez.
- Consultez la documentation du moteur de Go pour supprimer ses propres journaux, parties, configurations ou données. Les moteurs et modèles sont gérés séparément de Mobi ; ne supprimez pas les fichiers encore utilisés par d’autres applications.

Supprimer les fichiers extraits de Mobi ne supprime pas nécessairement ces éléments. Supprimer une identité client ne supprime ni le compte KGS ni ses parties sur le serveur et ne réinitialise pas son classement.

## Contact

Pour toute question privée concernant les données stockées par l’un de ces clients, contactez [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

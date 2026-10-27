---
source_revision: "2d36d2b70789618639852311a38a6f07a24e7e70cf3e48b416dc750ba7627c90"
layout: localized
title: "Politique de confidentialité"
lang: "fr"
page_key: "desktop/privacy"
section: "desktop"
nav_order: 10
permalink: "/fr/desktop/privacy/"
nav_group: "policies"
---

_En vigueur le 27 octobre 2026_

Cette politique couvre KGS Nova pour Windows, macOS et Linux, client officiellement approuvé par KGS. Le service KGS est distinct et possède ses propres [conditions et informations de confidentialité](https://www.gokgs.com/tos.jsp).

## Informations traitées

Connexion directe à KGS. Selon les fonctions utilisées, l’application traite identifiants et profil, salons, discussions et messages privés/hors ligne, listes sociales et notes, parties et coups, défis, avatars et préférences. Elle envoie les actions demandées et affiche les réponses KGS. Les autres utilisateurs voient les contenus selon la fonction KGS utilisée.

KGS reçoit un identifiant client persistant, version du protocole, langue/région, système, architecture, environnement d’exécution et adresse réseau de connexion.

Lorsqu’un enseignant autorisé lance une diffusion, le microphone est transmis par KGS aux participants ; la réception lit le son de KGS. L’émission cesse à votre arrêt ou à la fin de la session. Aucun enregistrement séparé pour le développeur.

Aucune publicité, analyse ou transmission automatique de plantages. Le développeur ne conserve aucune copie serveur distincte de compte, messages, parties ou audio.

## Stockage local et diagnostics

- **Base de données :** `data.db`, dans le dossier KGS Nova des données locales d’application du système, contient métadonnées des comptes, identifiant client, préférences et état. Sous Windows, il s’agit de `%LOCALAPPDATA%\KGS Nova`. La base entière n’est pas chiffrée.
- **Mots de passe :** sous Windows, chiffrés dans la base avec DPAPI pour l’utilisateur Windows actuel ; sous macOS, dans le Trousseau ; sous Linux, via Secret Service. Déverrouillage ou autorisation du système parfois nécessaires. Cette protection ne chiffre pas le reste de la base.
- **Journaux :** Les versions publiées écrivent les diagnostics d’erreur dans `client.log` et les fichiers tournants `client.archive*.log` du même dossier. La journalisation diagnostique facultative ajoute des événements pour la session en cours. Les journaux conservent version, modèles d’événements, types d’exceptions et traces de pile, avec un format conçu pour omettre valeurs d’arguments, messages d’exceptions et chemins des fichiers source. Les versions de développement peuvent produire un `logs.txt` et des sorties console/débogage plus détaillés. Relisez les journaux avant partage. Aucun envoi automatique au développeur.
- **Exports :** parties et autres fichiers exportés restent à l’emplacement choisi.

Des personnes ou logiciels ayant accès aux fichiers ou au compte système peuvent les lire. Désinstaller/remplacer ne supprime pas nécessairement base, journaux, exports ou entrées du trousseau. Voir [suppression des données]({% include page-url.html key='desktop/account-and-data-deletion' %}).

Ce dossier contient aussi l’espace `sgf`, les fichiers de récupération et sauvegardes, ainsi que les moteurs/modèles dans `analysis`. Enregistrez les parties récupérées à conserver avant suppression. Supprimer tout le dossier de données KGS Nova efface ensemble ces données locales.

## Communications et services tiers

La connexion KGS ancienne n’utilise ni TLS ni chiffrement de bout en bout. Transformer le mot de passe avant transmission ne protège pas tout le trafic contre observation ou modification. Utilisez un réseau fiable.

KGS indique enregistrer les conversations et permettre leur examen par ses administrateurs. Évitez les informations devant rester privées. KGS contrôle modération et conservation serveur.

GitHub héberge assistance et tickets selon sa [déclaration de confidentialité](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Les liens ouvrent le navigateur. Signaler un problème ouvre un brouillon modifiable avec version, système, architecture et environnement d’exécution. Ni envoi ni pièces jointes de journaux automatiques. Tickets publics soumis et pièces jointes sont publics.

## Vos choix et contact

Session invitée, mémorisation facultative des identifiants, restriction des interactions privées prises en charge, censure, absence de diffusion microphone et suppression des fichiers locaux sont possibles. Les administrateurs KGS gèrent la suppression du compte : [instructions]({% include page-url.html key='desktop/account-and-data-deletion' %}).

Ne publiez pas de données d’enfants dans les tickets. Parents/tuteurs doivent examiner conditions et communications KGS avant usage par un mineur.

Questions privées application/confidentialité : [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). Comptes et données serveur : [admin@gokgs.com](mailto:admin@gokgs.com). Vulnérabilités : [signalement privé](https://github.com/amywarble/hoshi-hub/security/advisories/new).

La politique évoluera avec le client ; sa date identifie la révision.

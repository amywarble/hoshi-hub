---
source_revision: "6557edaea14029268590a7f73220e26c62aafda65681a4c44da3dd659e4b7ca7"
layout: "localized"
title: "Politique de confidentialité"
lang: "fr"
page_key: "global/privacy"
section: "global"
nav_order: 3
permalink: "/fr/privacy/"
redirect_from: "/fr/desktop/privacy/"
---

_En vigueur le 27 octobre 2026_

Cette politique couvre Pocket KGS pour Android, KGS Nova pour Windows, macOS et Linux, Mobi pour Windows et Linux, ainsi que ce site d’assistance. Les trois clients sont officiellement soutenus par KGS et l’American Go Association (AGA). Les pratiques communes sont présentées d’abord, puis le stockage et les réglages propres à chaque application.

## Qui traite vos données

Les clients se connectent directement au KGS Go Server. Leur développeur n’exploite pas les serveurs KGS et ne contrôle ni leurs comptes, ni leur modération, leurs enregistrements ou leur conservation. KGS est un service distinct ayant ses propres [conditions et informations de confidentialité](https://www.gokgs.com/tos.jsp).

Les clients ne contiennent ni publicité, ni outils d’analyse, ni envoi automatique de rapports de plantage. Le développeur ne vend pas vos données personnelles et ne les utilise ni pour la publicité ciblée ni pour le suivi entre applications. Il ne conserve pas de copie serveur distincte de votre compte KGS, de vos discussions, parties, avatars ou émissions audio de professeurs.

## Informations traitées et finalités

Selon le client et les fonctions utilisées, elles comprennent :

- **Comptes et profils :** identifiants KGS, adresse électronique, texte de profil, avatar, classement, état du compte et préférences.
- **Communications et informations sociales :** discussions de salles et de parties, messages privés et hors ligne, listes d’amis, d’admirateurs et d’utilisateurs censurés avec leurs notes, et autres contenus KGS.
- **Parties et activité :** coups, enregistrements, commentaires, résultats, défis, appartenance aux salles et paramètres d’appariement. Mobi échange des informations de partie avec le moteur de Go configuré pour générer les coups et gérer les parties.
- **Connexion :** identifiant KGS persistant du client, versions de l’application et du protocole, langue, système et architecture, environnement d’exécution et état de connexion. KGS reçoit votre adresse IP lors de la connexion.
- **Réglages locaux et diagnostics :** préférences, contenus en cache et diagnostics décrits dans les sections ci-dessous.

Ces informations permettent la connexion, les sessions KGS, l’affichage des contenus, l’envoi des actions demandées ou configurées pour le bot, la mémorisation des réglages et le diagnostic des problèmes lorsque vous choisissez de partager des détails.

Pocket KGS et Nova traitent aussi le son du microphone lorsqu’un professeur autorisé démarre explicitement une diffusion en direct, et lisent l’audio reçu. La diffusion cesse lorsque vous l’arrêtez ou à la fin de la session concernée. Aucun ne crée d’enregistrement audio distinct pour le développeur. Mobi ne propose pas de commandes audio de professeur.

## Destinataires des informations

- **KGS :** reçoit les informations de compte et de connexion, communications, activités de jeu et modifications demandées. Les autres utilisateurs voient les contenus selon la fonction KGS utilisée.
- **Fournisseurs d’identifiants et moteurs :** les fournisseurs de la plateforme et le moteur choisi pour Mobi traitent les informations comme indiqué ci-dessous, selon leurs propres conditions.
- **GitHub :** héberge ce site et le suivi public des problèmes selon la [Déclaration de confidentialité de GitHub](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Les tickets publics et pièces jointes sont visibles par tous. Le signalement de Nova ouvre un brouillon modifiable dans le navigateur contenant version, système, architecture et environnement d’exécution ; il ne soumet pas le ticket et ne joint pas automatiquement les journaux.
- **Obligations légales et sécurité :** les informations fournies au développeur peuvent être conservées ou divulguées si cela est raisonnablement nécessaire pour respecter la loi, enquêter sur des abus, protéger les utilisateurs ou préserver les droits et la sécurité.

## Communications et sécurité

L’ancienne connexion KGS utilisée par ces clients ne fournit ni TLS ni chiffrement de bout en bout. Le protocole de connexion transforme le mot de passe avant transmission, mais une personne ayant accès au trajet réseau peut observer ou modifier le reste du trafic. Utilisez un réseau de confiance.

KGS indique que toutes les conversations sont journalisées et peuvent être examinées par ses administrateurs lors d’enquêtes sur des signalements. Ne partagez sur KGS aucune information devant rester privée. KGS contrôle la conservation côté serveur et les parties peuvent rester dans ses archives.

## Stockage et choix propres aux applications

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

Pocket stocke préférences, choix de notifications et identifiant KGS du client dans l’espace privé de l’application Android, et les avatars dans le cache Android. Android peut supprimer les fichiers en cache. Pocket demande à Android de ne pas sauvegarder ses données privées. Effacer le stockage ou désinstaller supprime ces données locales.

Si vous enregistrez des identifiants, Android Credential Manager et le fournisseur choisi les gèrent selon leurs conditions. Pocket ne reçoit pas les données biométriques servant à leur déverrouillage. Les identifiants conservés par le fournisseur peuvent devoir être supprimés séparément.

Les diagnostics d’erreur de production sont écrits dans le journal système Android. La journalisation diagnostique facultative fournit plus de détails pour la session actuelle. Les journaux de publication conservent versions, modèles d’événements, types d’exception et traces de pile dans un format conçu pour omettre les valeurs d’arguments à l’exécution, messages d’exception et chemins des fichiers sources. Android, un administrateur de l’appareil ou une personne à qui vous remettez les journaux peut y accéder.

Vous pouvez utiliser une session invitée, choisir l’enregistrement des identifiants, désactiver les notifications dans Pocket ou Android, refuser le microphone, éviter les diffusions et censurer des utilisateurs pour bloquer les interactions prises en charge et masquer leur contenu.

### KGS Nova

- **Base de données :** `data.db`, dans le dossier local de données de KGS Nova du système (`%LOCALAPPDATA%\KGS Nova` sous Windows), contient métadonnées des comptes enregistrés, identifiant client, préférences et état de l’application. La base entière n’est pas chiffrée.
- **Mots de passe :** Windows protège ceux enregistrés dans la base par DPAPI pour l’utilisateur Windows actuel. macOS utilise Keychain ; Linux utilise Secret Service. Le système peut demander un déverrouillage ou une autorisation. Le reste de la base n’est pas chiffré pour autant.
- **Diagnostics :** les erreurs de publication vont dans `client.log` et les fichiers tournants `client.archive*.log` du même dossier. Les diagnostics facultatifs de session sont plus détaillés. Les journaux de publication suivent les mêmes règles d’omission que Pocket. Les versions de développement peuvent produire un `logs.txt` et des sorties console/débogage plus détaillés.
- **Autres fichiers :** le même dossier contient l’espace `sgf`, les fichiers de récupération et sauvegardes, ainsi que les moteurs/modèles de `analysis`. Les parties exportées et autres fichiers restent aux emplacements choisis.

Des personnes ou logiciels ayant accès à vos fichiers ou à votre compte système peuvent les lire. Désinstaller ou remplacer Nova ne supprime pas forcément base, journaux, exports ou entrées du trousseau. Vous pouvez utiliser une session invitée, choisir de mémoriser les identifiants, contrôler les interactions privées prises en charge, censurer des utilisateurs, éviter les diffusions du microphone et supprimer les données locales.

### Mobi

Mobi nécessite un compte KGS enregistré. Il lit le mot de passe dans `KGS_PASSWORD` sans le conserver lui-même. Les scripts de lancement, paramètres d’environnement et gestionnaires de services peuvent conserver les identifiants que vous y placez. Protégez-les ainsi que votre compte système ; un moteur lancé peut hériter de son environnement.

La configuration TOML peut contenir nom du compte, serveur, chemins du moteur et paramètres de jeu. Mobi enregistre l’identifiant KGS du client dans un fichier local. L’appariement utilise par défaut `Kgs.Gtp/identities/<server-and-account-hash>` dans le répertoire local de données de .NET (`%LOCALAPPDATA%` sous Windows) ; sans appariement, le défaut est `Kgs.Gtp/client-id`. `account.clientIdFile` ou `--client-id-file` permet de changer l’emplacement.

État, erreurs et diagnostics du moteur sont envoyés à stderr. Les journaux persistent si vous redirigez la sortie ou si un gestionnaire de services la conserve. Ils ne suivent pas les règles d’omission de Pocket/Nova et peuvent contenir noms d’utilisateurs, détails de parties, chemins ou sorties du moteur. Relisez-les avant partage. Votre moteur peut créer d’autres journaux, parties ou fichiers et avoir ses propres activités réseau ; examinez séparément sa documentation et ses pratiques de confidentialité. Mobi n’envoie pas automatiquement de diagnostics au développeur.

Vous contrôlez moteur, configuration, sortie conservée et fichiers locaux. Voir le [guide de Mobi]({% include page-url.html key='mobi/user-guide' %}) pour le fonctionnement et les diagnostics.

## Conservation, suppression et autres choix

Le développeur ne reçoit pas automatiquement vos fichiers locaux ou diagnostics. Les copies volontairement envoyées peuvent être conservées pour traiter la demande ou pour des besoins légaux et de sécurité. Les tickets publics GitHub et leur historique restent présents jusqu’à modification ou suppression selon les fonctionnalités et politiques de GitHub.

Vous pouvez choisir les informations de profil partagées et marquer votre adresse KGS comme privée si cette option est disponible. Effacer des fichiers ou désinstaller un client ne supprime pas les données hébergées par KGS. Les administrateurs KGS traitent la suppression des comptes et données serveur. [Suppression du compte et des données]({% include page-url.html key='global/account-and-data-deletion' %}) décrit la demande commune et la suppression locale pour chaque client.

Pocket KGS ne s’adresse pas aux enfants de moins de 13 ans. KGS est un service de communication public ; un parent ou responsable légal devrait examiner ses conditions et son adéquation avant l’utilisation par un mineur. Ne publiez pas les données personnelles d’un enfant dans les tickets publics.

## Modifications et contact

Gardez système et client à jour, utilisez un mot de passe KGS unique et relisez les journaux avant partage. Aucun système n’est parfaitement sûr. Signalez les vulnérabilités selon la [Politique de sécurité]({% include page-url.html key='global/security-policy' %}).

Cette politique peut évoluer avec les clients ; la date d’entrée en vigueur identifie la version publiée. Pour l’aide non confidentielle, utilisez le [suivi public des problèmes](https://github.com/amywarble/hoshi-hub/issues/new/choose). Pour les questions privées concernant les applications ou la confidentialité, écrivez à [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). Pour les comptes KGS, données serveur ou la modération, à [admin@gokgs.com](mailto:admin@gokgs.com).

---
source_revision: "d6af0143a1e9eaabd1ffd1cb7c13389da26853a7ce6ab3ca381060ce302d9ad0"
layout: localized
title: "Politique de confidentialité"
lang: "fr"
page_key: "android/privacy"
section: "android"
nav_order: 4
permalink: "/fr/privacy/"
---

_En vigueur le 23 septembre 2026_

Pocket KGS est un client Android indépendant du KGS Go Server (« KGS »), sans affiliation ni approbation de KGS. Cette politique décrit les informations traitées, leurs usages, leurs destinataires et vos choix. Elle couvre Pocket KGS et ce site d’assistance. KGS est un service distinct avec ses propres [conditions d’utilisation et de confidentialité](https://www.gokgs.com/tos.jsp).

## Responsabilité des données

L’application se connecte directement à KGS. Le développeur fournit le client mais n’exploite pas les serveurs KGS et ne contrôle ni leurs dossiers, ni la modération, ni la conservation. Pocket KGS n’intègre ni publicité, ni analyse d’utilisation, ni signalement automatique de plantages. Le développeur ne vend pas vos données personnelles.

## Informations traitées

Selon les fonctions utilisées :

- **Compte et profil :** nom d’utilisateur KGS, mot de passe, adresse électronique, texte du profil, avatar, classement, état du compte et préférences du profil.
- **Communications et contenus :** discussions publiques des salons et parties, messages privés et hors ligne, enregistrements et annotations de parties, défis et autres contenus échangés avec KGS.
- **Audio :** son du microphone lorsqu’un enseignant autorisé lance explicitement une diffusion pédagogique. Le son est envoyé en direct par KGS aux participants de la partie. La diffusion s’arrête lorsque vous l’arrêtez ou à la fin de la session ; aucun enregistrement séparé n’est créé pour le développeur.
- **Relations sociales :** listes d’amis, de fans et de personnes censurées, avec vos notes.
- **Jeu et activité :** parties jouées ou observées, coups, résultats, préférences, participation aux salons, défis et interactions avec KGS.
- **Appareil et connexion :** identifiant client KGS persistant, versions de l’application et du protocole, langue/région, système et version, architecture du processeur, fournisseur/version de l’environnement d’exécution, état réseau et données nécessaires à la connexion. KGS reçoit nécessairement votre adresse IP.
- **Notifications :** choix locaux des événements KGS pouvant déclencher des notifications Android.
- **Cache local :** avatars et préférences nécessaires au bon fonctionnement.
- **Journaux de diagnostic :** les versions de production écrivent des informations limitées dans le journal système Android. La journalisation de la couche protocole KGS est désactivée dans les versions publiées ; les journaux de production sont conçus pour ne pas enregistrer d’événements du protocole KGS ni de contenus de messages. Ils se limitent aux informations Android/interface et aux avertissements ou erreurs des couches interface/client. Ils peuvent contenir nom KGS, identifiants de salon/partie/canal, actions, état Android et exceptions liés à une panne. Aucun envoi automatique au développeur. Android, l’administrateur de votre appareil ou une personne à qui vous fournissez volontairement un journal peuvent y accéder.

## Utilisation

Les informations servent à vous connecter et maintenir la session ; modifier votre profil existant à votre demande ; afficher salons, utilisateurs, parties, profils, messages et autres contenus ; transmettre coups, messages, modifications de profil, avatar, audio et actions demandées ; mémoriser réglages, identifiant client et notifications sur votre appareil ; afficher les notifications activées ; et diagnostiquer les pannes lorsque vous partagez volontairement des détails. Aucune publicité ciblée ni suivi entre applications.

## Destinataires

Communication uniquement selon les besoins suivants :

- **KGS :** données de compte, communications, activité de jeu, profil, audio pédagogique, données appareil/environnement, identifiant client et connexion pour fournir le service. Les autres utilisateurs voient ce que la fonction KGS rend public ou partage avec eux.
- **Fournisseurs d’identifiants Android :** si vous choisissez l’enregistrement des mots de passe, Android Credential Manager et le fournisseur sélectionné traitent le nom et le mot de passe selon leurs propres politiques. Pocket KGS ne reçoit pas les données biométriques de déverrouillage.
- **GitHub :** hébergement du site et du suivi public des tickets. Les données soumises relèvent de la [déclaration de confidentialité GitHub](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement) et les tickets publics sont visibles par tous.
- **Obligations légales et sécurité :** les informations reçues par le développeur peuvent être conservées ou divulguées lorsque raisonnablement nécessaire pour respecter la loi, protéger les utilisateurs, enquêter sur un abus ou défendre les droits et la sécurité de l’application et d’autrui.

## Communications et transport

KGS indique que toutes les conversations sont enregistrées et peuvent être examinées par ses administrateurs lors d’enquêtes. Ne partagez pas dans le chat d’informations devant rester privées.

Le protocole ancien de KGS ne fournit pas de connexion moderne protégée par TLS. Le mot de passe est transformé par le protocole de connexion avant transmission, mais le reste du trafic n’est protégé ni par TLS ni par chiffrement de bout en bout. Une personne observant ou modifiant le chemin réseau pourrait lire ou altérer le trafic. Évitez les réseaux non fiables.

## Stockage et conservation

Identifiant client et préférences sont dans le stockage privé de l’application ; les avatars dans le cache Android, qu’Android peut supprimer en cas de manque d’espace. Effacer les données ou désinstaller supprime les données privées de Pocket KGS. Les identifiants conservés via Android Credential Manager peuvent devoir être supprimés séparément du gestionnaire de mots de passe.

Le développeur ne conserve pas de copie serveur séparée de votre compte, de vos discussions, parties, avatar ou audio. KGS contrôle sa conservation ; il indique enregistrer les conversations et les parties peuvent rester dans ses archives.

Pour supprimer le compte et les données serveur associées, écrivez à [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) avec nom KGS et adresse du compte, jamais le mot de passe. Un administrateur peut vérifier la propriété et traitera la demande. Voir [Suppression du compte et des données]({% include page-url.html key='android/account-and-data-deletion' %}) pour les instructions complètes, y compris locales. Les tickets publics et leur historique restent sur GitHub jusqu’à modification ou suppression selon ses fonctions et politiques.

## Vos choix

Vous pouvez utiliser une session invitée au lieu de créer un compte sur le site KGS ; choisir d’enregistrer ou non un mot de passe ; marquer votre adresse KGS comme privée lorsque possible ; choisir avatar et modifications du profil ; refuser le microphone et la diffusion pédagogique ; désactiver les notifications dans l’application ou Android ; censurer un utilisateur pour bloquer les interactions prises en charge et masquer ses contenus ; effacer les données locales ou désinstaller ; et suivre les [instructions de suppression]({% include page-url.html key='android/account-and-data-deletion' %}).

## Enfants

Pocket KGS ne s’adresse pas aux enfants de moins de 13 ans. KGS est un service public permettant la communication entre utilisateurs. Un parent ou tuteur doit examiner les conditions et l’adéquation du service avant d’autoriser un mineur. Ne soumettez pas de données personnelles d’enfants dans un ticket public.

## Sécurité

Aucun système n’est totalement sûr. Mettez à jour appareil et application, utilisez un mot de passe KGS unique et ne publiez pas d’identifiants ni de contenu privé. Consultez la [politique de sécurité]({% include page-url.html key='global/security-policy' %}) pour signaler une vulnérabilité.

## Modifications

Cette politique peut évoluer avec Pocket KGS. Sa date d’entrée en vigueur sera actualisée pour une révision importante. Continuer à utiliser l’application après modification signifie que la nouvelle politique s’applique à l’utilisation ultérieure.

## Contact

Questions générales sans données personnelles ou sensibles : [tickets publics](https://github.com/amywarble/hoshi-hub/issues/new/choose). Questions privées sur Pocket KGS, confidentialité ou sécurité sensible : [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). Comptes KGS, données serveur, modération et service : [admin@gokgs.com](mailto:admin@gokgs.com).

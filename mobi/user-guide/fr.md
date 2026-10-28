---
layout: "localized"
title: "Guide d'utilisation du Mobi"
nav_title: "Guide utilisateur"
lang: "fr"
page_key: "mobi/user-guide"
section: "mobi"
nav_order: 1
permalink: "/fr/gtp/user-guide/"
source_revision: "26bf30c603841ace27c0d2ff994fd0d2297af607b506d24fd1ab9afabb8f1a33"
---

Mobi connecte un moteur Go à KGS afin qu'il puisse jouer automatiquement. Vous exécutez le client dans un terminal et le contrôlez via un fichier de configuration TOML ou des options de ligne de commande. Installez et configurez votre moteur séparément ; le client gère la connexion, la recherche de jeux, les mouvements, les horloges et les scores.

Vous quittez le client Java `kgsGtp.jar` ? Commencez par le [guide de mise à niveau]({% include page-url.html key='mobi/upgrade-guide' %}).

Ce guide couvre les Windows et Linux. Développez la section de votre système d'exploitation pour voir les commandes PowerShell ou Bash. Exécutez les exemples de clients packagés à partir du répertoire client extrait.

- [Premier jeu](#first-game)
- [Bases de la configuration](#configuration-basics)
- [Choisir des jeux](#choosing-games)
- [Paramètres de jeu personnalisés](#custom-game-settings)
- [Exécuter le bot](#running-the-bot)
- [Délai d'attente et récupération](#timeouts-and-recovery)
- [Dépannage](#troubleshooting)

## Premier match {#first-game}

Vous avez besoin d'un compte KGS enregistré, d'un moteur GTP version 2 et de tous les fichiers de configuration et de modèle requis par le moteur. Créez le compte à l'aide d'un client KGS standard avant de démarrer le bot. La lecture de Ranked nécessite une autorisation supplémentaire du serveur ; commencez par un jeu Free.

Extrayez le package client pour votre système d’exploitation et votre architecture. Les packages sont fournis pour Windows et Linux sur x64 et ARM64, avec le runtime .NET inclus. Conservez les fichiers extraits ensemble. L'exécutable est `Kgs.Gtp.exe` sur Windows et `Kgs.Gtp` sur Linux.

### 1. Créez votre configuration {#1-create-your-configuration}

Copiez le [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) inclus dans `bot.toml` :

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
Copy-Item .\bot.example.toml .\bot.toml
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
cp ./bot.example.toml ./bot.toml
chmod +x ./Kgs.Gtp
```

</details>

Modifiez `account.username`, `engine.executable` et `engine.arguments`. Par exemple :

<details markdown="1">
<summary>Windows</summary>

```toml
[account]
username = "YourBot"

[engine]
executable = 'C:\Go\katago.exe'
arguments = ["gtp", "-config", 'C:\Go\gtp.cfg', "-model", 'C:\Go\model.bin.gz']
```

</details>

<details markdown="1">
<summary>Linux</summary>

```toml
[account]
username = "YourBot"

[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]
```

</details>

Fournissez les chemins et les arguments dont votre moteur a besoin pour passer en mode GTP. Chaque élément du tableau est un argument ; un chemin contenant des espaces est toujours un élément.

L'exemple sélectionne la correspondance automatique Free contre des humains, une vitesse rapide ou moyenne et une lecture continue. Définissez `automatch.rank` sur une estimation appropriée entre `30k` et `1k` si le compte n'a pas de classement numérique. KGS utilise le classement du compte lorsqu'il est disponible. Pour la première exécution, la commande ci-dessous limite le jeu à une seule partie.

### 2. Vérifiez le moteur {#2-check-the-engine}

Depuis le répertoire client extrait, exécutez :

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --probe
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml --probe
```

</details>

Le client imprime le nom du moteur, la version et les commandes prises en charge, puis se ferme. Cela ne nécessite aucune information d’identification KGS et ne se connecte pas à KGS. Il vérifie la découverte GTP ; les règles supplémentaires, l'horloge, le handicap et les contrôles de score s'exécutent au démarrage du mode de jeu configuré.

### 3. Fournissez le mot de passe et jouez {#3-supply-the-password-and-play}

Le mot de passe provient uniquement de la variable d'environnement `KGS_PASSWORD` :

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
$env:KGS_PASSWORD = '<account password>'
.\Kgs.Gtp.exe --config .\bot.toml --games 1
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
read -r -s -p 'KGS password: ' KGS_PASSWORD
export KGS_PASSWORD
printf '\n'
./Kgs.Gtp --config ./bot.toml --games 1
```

</details>

Recherchez `Logged in to KGS`, puis `Game ready`. Le client joue et marque le jeu automatiquement. `Game finished` enregistre le résultat de KGS ; `Series: completed game 1` confirme qu'il a été comptabilisé dans le total demandé. Il se déconnecte ensuite et quitte. La recherche d'un jeu est limitée à cinq minutes par défaut ; utilisez `--lobby-timeout 3600` pour prévoir jusqu'à une heure.

## Bases de configuration {#configuration-basics}

Sélectionnez toujours le fichier explicitement avec `--config`. Le client le lit une fois au démarrage. Redémarrez pour appliquer les modifications, y compris les modifications apportées aux paramètres de redémarrage du moteur. Il n'y a pas de recherche automatique de fichier de configuration ni de rechargement en direct.

Les options de ligne de commande remplacent les valeurs de fichier pour cette exécution. Par exemple :

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --games 3 --undo-free Never
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml --games 3 --undo-free Never
```

</details>

Le nom d'utilisateur vient de `--username`, puis `account.username`, puis `KGS_USERNAME`. N'ajoutez pas de champ de mot de passe au fichier : il est rejeté.

Utilisez des chaînes entre guillemets pour les noms et les sélections, des entiers pour les nombres et les secondes, des nombres pour les komi et `true` ou `false` pour les booléens. Les noms de table et de clé sont sensibles à la casse. Les clés inconnues et les valeurs non valides arrêtent le démarrage avec un diagnostic. Toutes les durées dans ce guide sont en secondes.

Un `engine.executable` relatif contenant `/` ou `\`, et un `account.clientIdFile` relatif, sont relatifs au répertoire du fichier de configuration. Un nom d'exécutable simple, tel que `katago`, utilise la recherche d'exécutable. Les arguments du moteur sont transmis tels quels et le moteur hérite du répertoire de travail à partir duquel vous lancez le client. Utilisez des chemins absolus pour les arguments de configuration du modèle et du moteur si vous lancez à partir de répertoires différents. Les chaînes TOML entre guillemets simples préservent les barres obliques inverses Windows. Les chaînes ne développent pas les variables d'environnement.

### Compte, serveur et moteur {#account-server-and-engine}

| Paramètre TOML | Option CLI | Signification et défaut |
| --- | --- | --- |
| `account.username` | `--username` | Nom du compte KGS ; revient à `KGS_USERNAME`. |
| `account.clientIdFile` | `--client-id-file` | Fichier d'identité persistant ; normalement choisi par serveur et compte. |
| `server.host` | `--host` | Serveur KGS ; par défaut `goserver.gokgs.com`. |
| `server.port` | `--port` | Port TCP ; par défaut `2379`, plage 1–65535. |
| `engine.executable` | `--engine` | Exécutable du moteur à lancer. |
| `engine.arguments` | Arguments après `--` | Tableau d'arguments du moteur ; vide par défaut. |
| `engine.stdio` | `--stdio` | Utilisez un moteur connecté en externe au lieu d’en lancer un ; par défaut `false`. |
| `engine.rules` | `--engine-rules` | Règles déjà configurées dans un moteur dépourvu de `kgs-rules`. Aucune déclaration par défaut. |

Choisissez un exécutable ou `stdio = true`, jamais les deux. Avec les E/S standard, un autre programme doit connecter le stdin du client au stdout du moteur et le stdout du client au stdin du moteur. Les diagnostics utilisent stderr. Ne fournissez pas d’arguments de moteur dans ce mode.

`engine.rules` accepte `Japanese`, `Chinese`, `Aga` ou `NewZealand`. Ceci déclare les règles existantes du moteur ; configurer le moteur lui-même pour qu'il corresponde. Les moteurs avec `kgs-rules` reçoivent automatiquement les règles du jeu sélectionné.

Pour configurer entièrement sur la ligne de commande, placez les arguments du moteur après `--` :

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --username YourBot --engine 'C:\Go\katago.exe' `
    --lobby Automatch --automatch-rank 20k --games 1 `
    -- gtp -config 'C:\Go\gtp.cfg' -model 'C:\Go\model.bin.gz'
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --username YourBot --engine /opt/katago/katago \
    --lobby Automatch --automatch-rank 20k --games 1 \
    -- gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

</details>

Les arguments du moteur fournis explicitement en ligne de commande remplacent tout le tableau du fichier. Un `--` final sans argument après lui vide ce tableau. `--engine` et `--stdio` remplacent le mode de connexion au moteur choisi dans le fichier ; `--stdio` ignore aussi les arguments du fichier. `--help` affiche toutes les options et `--version` affiche la version du client.

## Choisir des jeux {#choosing-games}

Sélectionnez un mode de mise en relation :

| `matchmaking.mode` / `--lobby` | Ce que fait le robot |
| --- | --- |
| `Automatch` | Permet à KGS de trouver un adversaire et de choisir les conditions du jeu. |
| `Offer` | Annonce un défi personnalisé dans la salle nommée. |
| `Join` | Recherche un défi personnalisé correspondant dans la salle nommée. |

Sans mode, le client se connecte et attend d'être arrêté ; il ne trouve pas de jeux. Une invocation joue un jeu à la fois. Les défis personnalisés simultanés, les correspondances automatiques, les participations aux tournois et les réponses au chat ne sont actuellement pas pris en charge.

### Automatch {#automatch}

Utilisez ces sections avec les paramètres de votre compte et de votre moteur :

```toml
[matchmaking]
mode = "Automatch"
gameType = "Free"
games = 0

[automatch]
speed = ["Fast", "Medium"]
rank = "20k"
opponents = "Humans"
maxRankDifference = 0
```

Omettez `matchmaking.room`, `opponent`, `opponentPolicy`, `challengeNotes` et les sections `game` et `timing` en mode Automatch. Il s'agit de paramètres de défi personnalisés et ne peuvent pas être combinés avec la correspondance automatique, même si leurs valeurs correspondent à ses valeurs par défaut.

| Paramètre TOML | Option CLI | Choix et défaut |
| --- | --- | --- |
| `automatch.speed` | `--automatch-speed` | `All` (par défaut), `Blitz`, `Fast`, `Medium` ou un tableau tel que `["Fast", "Medium"]`. Les combinaisons CLI utilisent des virgules. |
| `automatch.rank` | `--automatch-rank` | Estimation de `30k` à `1k` ; requis lorsque le compte n’a pas de rang de serveur numérique. |
| `automatch.opponents` | `--automatch-opponents` | `Humans` (par défaut), `Robots` ou `Any`. |
| `automatch.maxRankDifference` | `--automatch-max-rank-difference` | Par défaut `0` ; gamme 0–9 pour Free, 0–6 pour Ranked. |

Les parties Automatch sont publiques, sur 19×19, avec règles japonaises et couleurs attribuées par le serveur. Les parties à égalité utilisent un komi de 6.5. Autoriser des écarts de rang peut donner un komi de 0.5 et, pour des écarts de deux rangs ou plus, des pierres de handicap à placement fixe.

| Vitesse | Temps principal par joueur | Byo-yomi japonais |
| --- | --- | --- |
| `Blitz` | 60 secondes | Périodes 3 de secondes 10 |
| `Fast` | 600 secondes | Périodes 5 de secondes 20 |
| `Medium` | 1500 secondes | Périodes 5 de secondes 30 |

Le moteur doit prendre en charge `final_status_list`, `kgs-time_settings` et `time_left` ; autoriser le handicap nécessite également `set_free_handicap`. S'il manque `kgs-rules`, configurez-le pour les règles japonaises et définissez `engine.rules = "Japanese"`.

### Défis personnalisés {#custom-challenges}

Remplacez les sections `matchmaking` et `automatch` du fichier exemple par un profil personnalisé. Cet exemple propose un jeu public 19×19 Free aux joueurs éligibles :

```toml
[matchmaking]
mode = "Offer"
gameType = "Free"
opponentPolicy = "Any"
room = "Computer Go"
games = 0
challengeNotes = "Computer player: 10-minute games"

[game]
boardSize = 19
rules = "Chinese"
komi = 7.5
color = "Nigiri"
handicap = 0
private = false

[timing]
system = "Absolute"
mainTime = 600
```

Utilisez le nom de la pièce comme indiqué dans KGS. Les noms peuvent contenir des espaces et des caractères non-ASCII. Lookup utilise une correspondance exacte insensible à la casse après la connexion et à nouveau après la reconnexion. Les noms manquants ou ambigus arrêtent le client avec un diagnostic.

Pour un adversaire spécifique, remplacez `opponentPolicy` par `"Named"` et ajoutez `opponent = "OtherAccount"`. Pour `Any`, omettez `opponent` ; les adversaires ouverts éligibles sont des comptes connectés et enregistrés autres que ce bot. Les humains et les robots sont éligibles.

Pour participer aux défis, utilisez `mode = "Join"` et supprimez `challengeNotes`. Chaque terme du jeu doit correspondre, y compris les règles, les komi, le handicap, la visibilité et les horloges. Choisissez la couleur du bot : un bot Offer jouant en Noir a besoin d'un bot Join jouant en Blanc ; pour les couleurs aléatoires, utilisez `"Nigiri"`. Les conditions modifiées ne sont pas acceptées silencieusement.

| Paramètre TOML | Option CLI | Choix et défaut |
| --- | --- | --- |
| `matchmaking.mode` | `--lobby` | `Offer`, `Join` ou `Automatch` ; pas de mode par défaut. |
| `matchmaking.gameType` | `--game-type` | `Free` (par défaut) ou `Ranked`. |
| `matchmaking.opponentPolicy` | `--opponent-policy` | `Named` (par défaut pour les défis personnalisés) ou `Any`. |
| `matchmaking.opponent` | `--opponent` | Requis avec `Named` ; les noms de comptes ignorent la casse. |
| `matchmaking.room` | `--room` | Nom de pièce requis pour Offer et Join ; par exemple `"Computer Go"`. |
| `matchmaking.games` | `--games` | Par défaut `1` ; nombre positif pour une série, `0` pour une lecture continue. |
| `matchmaking.challengeNotes` | `--challenge-notes` | Offer uniquement ; jusqu'à caractères 255, sans caractères de contrôle. L'omission génère une note de l'adversaire. |

### Jeux Ranked {#ranked-games}

Configurez `matchmaking.gameType = "Ranked"` pour demander exclusivement les jeux Ranked. Le compte doit disposer de l'autorisation `RankedRobot` accordée par le serveur et du classement activé. Demandez cette autorisation à un administrateur de serveur KGS. Un rang non défini (`?`) est autorisé, mais le rang désactivé (`-`) ne l'est pas ; la correspondance automatique a toujours besoin d'une estimation lorsque le compte n'a pas de classement numérique.

Les adversaires Ranked doivent avoir un compte enregistré avec classement activé, de rang amateur ou encore indéterminé. Les robots adverses ont aussi besoin de `RankedRobot`. Les défis personnalisés Ranked exigent une salle publique, une partie publique sur 19×19, au plus six pierres de handicap, un komi de −10 à 10 et une durée estimée supérieure à 450 secondes par joueur. L’estimation inclut le temps additionnel ; le temps illimité est également autorisé. Un profil Absolute de 600 secondes respecte cette restriction. Le client refuse les réglages non admissibles ou un changement du serveur vers Free.

## Paramètres de jeu personnalisés {#custom-game-settings}

Ces paramètres s'appliquent à Offer et Join. Laissez-les en dehors des configurations Automatch.

| Paramètre TOML | Option CLI | Choix et défaut |
| --- | --- | --- |
| `game.boardSize` | `--board-size` | Par défaut `9` ; gamme 2–25, sous réserve de support moteur. |
| `game.rules` | `--rules` | `Chinese` (par défaut), `Japanese`, `Aga` ou `NewZealand`. |
| `game.komi` | `--komi` | Par défaut `7.5` ; −100 à 100 par incréments d'un demi-point. |
| `game.color` | `--color` | `Black`, `White` ou `Nigiri` ; la valeur par défaut est Noir pour Offer et Blanc pour Join. |
| `game.handicap` | `--handicap` | Par défaut `0` ; sinon 2–9 dans les limites de placement sur le goban. Ne peut être combiné avec Nigiri. |
| `game.private` | `--private` | Par défaut `false` ; nécessite un jeu privé tout en gardant le défi annoncé dans la salle sélectionnée. |

Le handicap ne modifie pas automatiquement le komi. Définissez les deux explicitement. Les règles japonaises et AGA utilisent un placement fixe : au moins 7×7, avec au plus quatre pierres sur 7×7 ou sur les plateaux de taille paire. Les règles chinoises et néo-zélandaises utilisent un placement libre, avec au plus neuf pierres et au moins une intersection vide. Les parties à handicap nécessitent `set_free_handicap` ; Noir a aussi besoin de `place_free_handicap` pour le placement libre.

### Contrôles horaires {#time-controls}

| Paramètre TOML | Option CLI | Valeur par défaut et plage |
| --- | --- | --- |
| `timing.system` | `--time-system` | `Absolute` (par défaut), `None`, `Canadian` ou `ByoYomi`. |
| `timing.mainTime` | `--main-time` | `600` par défaut ou `0` pour Aucun ; gamme 0–86400. |
| `timing.byoYomiTime` | `--byo-yomi-time` | Par défaut `0` ; 1–86400 par période japonaise ou bloc canadien lors de l'utilisation des temps additionnel. |
| `timing.byoYomiPeriods` | `--byo-yomi-periods` | Par défaut `0` ; 1–255 pour ByoYomi. |
| `timing.canadianStones` | `--canadian-stones` | Par défaut `0` ; 1–255 pour Canadien. |

Pour les temps additionnel japonaises avec dix minutes de temps principal et cinq périodes de secondes 30 :

```toml
[timing]
system = "ByoYomi"
mainTime = 600
byoYomiTime = 30
byoYomiPeriods = 5
```

Pour les temps additionnel canadiennes, utilisez `system = "Canadian"`, `byoYomiTime` pour les secondes par bloc et `canadianStones` pour les pierres par bloc. Omettre `byoYomiPeriods`. Les temps additionnel ne permettent aucun temps principal. L'absolu nécessite un temps principal positif et aucune heure supplémentaire ; Aucun n'exige que toutes les valeurs de temps explicitement fournies soient nulles. Les réserves totales d'horloge doivent également correspondre à la plage du serveur ; les combinaisons invalides sont signalées.

Les jeux chronométrés nécessitent `time_left` et `time_settings` ou `kgs-time_settings`. Les temps additionnel japonaises nécessitent spécifiquement `kgs-time_settings`. Les jeux illimités ne nécessitent pas de commandes d'horloge. Les délais de réponse du moteur sont distincts de l'horloge du jeu et ne donnent pas plus de temps de jeu au robot.

## Exécuter le bot {#running-the-bot}

Réglez `matchmaking.games` sur un total positif ou sur `0` pour continuer à jouer. Seuls les résultats confirmés par KGS comptent. Après une partie terminée, le client la quitte et utilise les paramètres de matchmaking d'origine pour la partie suivante. Une partie ratée ou inachevée arrête la série au lieu de compter comme terminée.

Pour un jeu continu avec une attente plus longue entre les parties :

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --games 0 --lobby-timeout 3600
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml --games 0 --lobby-timeout 3600
```

</details>

Appuyez sur Ctrl+C pour arrêter. Le client se déconnecte, demande au moteur de s'arrêter et arrête un moteur qu'il a lancé si nécessaire. S'arrêter pendant une partie n'établit pas de résultat final. Inspectez tout jeu inachevé avant de commencer une autre partie.

### Journaux et codes de sortie {#logs-and-exit-codes}

L'état, les erreurs, l'aide et les diagnostics du moteur sont accessibles sur stderr. Pour les conserver :

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml 2> .\bot.log
$LASTEXITCODE
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
./Kgs.Gtp --config ./bot.toml 2> ./bot.log
echo $?
```

</details>

Utilisez votre gestionnaire de services ou des outils externes pour la rotation des journaux. En mode E/S standard, gardez le stdout connecté au moteur ; il transporte les commandes GTP.

| Code de sortie | Signification |
| --- | --- |
| `0` | Jeux demandés terminés ou commande de sonde/aide/version réussie. |
| `1` | Échec de configuration ou d’exécution ; inspecter le diagnostic. |
| `130` | Annulation de l'opérateur, y compris Ctrl+C. |

### État persistant et jeux existants {#persistent-state-and-existing-games}

Le client enregistre l'identité attribuée par KGS. Dans les modes de mise en relation, le fichier par défaut se trouve dans le répertoire de données d'application local de .NET à `Kgs.Gtp/identities/<server-and-account-hash>`. Sur Windows, cette valeur est normalement inférieure à `%LOCALAPPDATA%`. Pour choisir un emplacement stable en écriture, définissez `account.clientIdFile = "./state/client-id"`. Préservez-le lors des mises à niveau et des remplacements de conteneurs. Utilisez un fichier distinct pour chaque serveur et compte.

Offer et Join vérifient d'abord la salle sélectionnée pour un jeu inachevé appartenant à ce compte. Exactement un jeu compatible peut être repris ; son adversaire et son profil complet doivent correspondre. Des jeux multiples ou incompatibles arrêtent le démarrage. Les jeux archivés ne sont pas chargés automatiquement.

Une session de correspondance automatique en cours d'exécution peut récupérer le jeu qui lui a été attribué après une perte de connexion. Un nouveau processus ne découvre pas automatiquement les anciens jeux de correspondance automatique. Résolvez une partie de correspondance automatique inachevée avant de vous inscrire à nouveau.

### Reprises, pauses et absence de l'adversaire {#takebacks-pauses-and-opponent-absence}

`undo.free` / `--undo-free` et `undo.ranked` / `--undo-ranked` acceptent indépendamment `Never` (par défaut) ou `Allow`. L’exemple autorise les annulations de coups en Free et les refuse en Ranked. Allow accepte les demandes adverses permises par le serveur pendant le jeu actif normal ; le bot ne demande pas lui-même d’annulation. Il rejoue ensuite l’historique confirmé : le moteur n’a donc pas besoin de GTP `undo`. La reprise après désaccord sur le décompte est indépendante de cette politique.

KGS contrôle les pauses, les ajournements et la reprise. Lorsqu'il est en pause ou ajourné, le bot ne démarre aucune nouvelle action de jeu ou de score. Chaque pause continue, ajournement et absence d'un adversaire a une limite distincte, par défaut 300 secondes :

| Paramètre TOML dans `[interactions]` | Option CLI |
| --- | --- |
| `pauseTimeoutFree` | `--pause-timeout-free` |
| `adjournmentTimeoutFree` | `--adjournment-timeout-free` |
| `opponentTimeoutFree` | `--opponent-timeout-free` |
| `pauseTimeoutRanked` | `--pause-timeout-ranked` |
| `adjournmentTimeoutRanked` | `--adjournment-timeout-ranked` |
| `opponentTimeoutRanked` | `--opponent-timeout-ranked` |

Chacun accepte les secondes 1–86400. L'expiration arrête le client avec le code 1 et laisse le jeu inachevé ; il ne démissionne pas et ne commence pas une autre partie. La reconnexion et le remplacement du moteur ne réinitialisent pas ces attentes. Les autres délais actifs peuvent expirer plus tôt. Lorsqu'un adversaire est absent, le bot peut toujours se déplacer si KGS le permet.

## Délais d'attente et récupération {#timeouts-and-recovery}

### Délais d'attente normaux {#normal-timeouts}

Tous acceptent les secondes 1–86400 :

| Paramètre TOML | Option CLI | Par défaut | Limites |
| --- | --- | --- | --- |
| `timeouts.login` | `--login-timeout` | `30` | Connexion et connexion. |
| `timeouts.lobby` | `--lobby-timeout` | `300` | Une négociation de défi ou une inscription automatique ; limite également la recherche du nom de la pièce. |
| `timeouts.move` | `--move-timeout` | `600` | Une recherche normale ou un moteur de nettoyage. |
| `timeouts.scoring` | `--scoring-timeout` | `120` | Un tour de notation, comprenant évaluation et accord. |
| `timeouts.cleanup` | `--cleanup-timeout` | `300` | Toutes les tentatives de nettoyage et les scores ultérieurs ensemble. |

### Perte de connexion KGS {#kgs-connection-loss}

Le client réessaye en cas d'échec de transport, s'authentifie à nouveau et rejoint le jeu interrompu en utilisant l'historique du serveur. Il ne renvoie pas un coup incertain ni ne remplace une partie interrompue connue par un nouveau défi. Les connexions rejetées, les déconnexions du serveur, les données de serveur invalides, les mouvements de moteur illégaux et les commandes de moteur rejetées sont des échecs de terminal.

| Paramètre TOML | Option CLI | Valeur par défaut et plage |
| --- | --- | --- |
| `connectionRecovery.attempts` | `--reconnect-attempts` | Plafond facultatif par panne ; 0–100. Omis par défaut ; zéro désactive les tentatives. |
| `connectionRecovery.delay` | `--reconnect-delay` | `1`-deuxième fenêtre initiale ; 0–30, doublé en un deuxième plafond 30, avec gigue complète. |
| `connectionRecovery.timeout` | `--recovery-timeout` | `120` secondes par reconnexion via la réattachement du jeu ; 1–86400. |
| `connectionRecovery.budget` | `--recovery-budget` | `180` secondes totales par panne, y compris la vidange, l'interruption, la connexion et la réinscription ; 1–86400. |
| `connectionRecovery.resetAfter` | `--recovery-reset-after` | `60` secondes saines après le rattachement avant de réinitialiser le budget et le nombre de nouvelles tentatives ; 1–86400. |
| `connectionRecovery.engineDrainTimeout` | `--engine-drain-timeout` | `30` secondes pour terminer et jeter l'ancien travail du moteur ; 1–86400. |

Le budget d'indisponibilité démarre lorsqu'une perte de connexion est détectée. Chaque reconnexion est limitée par le budget restant ainsi que par son propre délai de connexion/réadhésion. Chaque délai d'attente est sélectionné de manière aléatoire entre zéro et un plafond qui double de 1 seconde à un plafond 30 seconde. La récupération s'arrête lorsque le budget total ou un plafond de tentative explicite est épuisé.

Après le réattachement, le bot peut continuer à jouer au-delà de l'ancienne date limite de récupération. Une déconnexion ultérieure obtient un nouveau budget après des secondes saines 60. Une déconnexion avant cet intervalle conserve le délai précédent et le nombre de nouvelles tentatives, y compris le temps de connexion brève. La connexion seule n'établit pas la santé lorsqu'un jeu doit encore être rejoint.

### Panne moteur {#engine-failure}

Si un moteur en cours d'exécution se ferme ou si son flux devient inutilisable, le client maintient la session KGS active et tente de démarrer un remplacement à l'aide de l'exécutable et des arguments d'origine. Il vérifie le remplacement et relit l'historique confirmé avant de continuer. Les échecs initiaux de démarrage/découverte du moteur arrêtent le client. Les horloges KGS continuent pendant que le moteur est indisponible.

| Paramètre TOML | Option CLI | Valeur par défaut et plage |
| --- | --- | --- |
| `engineRecovery.attempts` | `--engine-restart-attempts` | Remplacements automatiques `3` au cours de l’invocation ; 0–100. Zéro attente pour la récupération de l'opérateur. |
| `engineRecovery.delay` | `--engine-restart-delay` | `1`-deuxième fenêtre initiale ; 0–30, doublé en un deuxième plafond 30, avec gigue complète. |
| `engineRecovery.timeout` | `--engine-recovery-timeout` | `120` secondes pour la découverte/configuration et séparément pour la relecture ; 1–86400. |
| `engineRecovery.pipe` | `--engine-recovery-pipe` | Canalisation de récupération locale ; par défaut `kgs-gtp-<process ID>`. Utilisez des lettres, des chiffres, des points, des traits d'union ou des traits de soulignement ASCII 1–100. |

Lorsque les remplacements automatiques sont épuisés, le diagnostic nomme un canal de récupération local. Le bot attend l’intervention de l’opérateur pendant que les délais normaux de jeu et de lobby se poursuivent. Pour redémarrer un moteur lancé par le client, connectez-vous en tant que même utilisateur du système d'exploitation et envoyez UTF-8 `restart` suivi de LF. Par exemple, si vous avez configuré `pipe = "YourBot-recovery"`, exécutez-le dans un autre terminal après le diagnostic en attente :

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
$pipe = [IO.Pipes.NamedPipeClientStream]::new(
    '.', 'YourBot-recovery', [IO.Pipes.PipeDirection]::InOut)
try {
    $pipe.Connect(5000)
    $request = [Text.Encoding]::UTF8.GetBytes("restart`n")
    $pipe.Write($request, 0, $request.Length)
    $pipe.Flush()
}
finally { $pipe.Dispose() }
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
python3 - <<'PY'
import os
import socket

pipe = os.path.join(os.environ.get("TMPDIR") or "/tmp", "CoreFxPipe_YourBot-recovery")
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as connection:
    connection.settimeout(5)
    connection.connect(pipe)
    connection.sendall(b"restart\n")
PY
```

</details>

L'exemple Linux nécessite Python 3 et se connecte au socket de domaine Unix de .NET. Exécutez-le en tant que même utilisateur, avec le même `TMPDIR` que le bot (la valeur par défaut est `/tmp`). Remplacez `YourBot-recovery` par le nom du canal configuré ; un service avec un répertoire temporaire privé a également besoin que le client s'exécute dans ce même environnement.

Un remplacement d’opérateur réussi démarre un nouveau budget de tentatives automatiques. La modification du fichier TOML ne modifie pas l'exécutable ni les arguments du client en cours d'exécution.

Pour `--stdio`, un superviseur externe doit connecter un nouveau moteur via le tuyau de récupération duplex et relayer le GTP dans les deux sens. Il n'y a pas de message d'accueil `restart` dans ce mode. La connexion stdin/stdout d'origine ne peut pas être réutilisée après un échec.

## Dépannage {#troubleshooting}

| Symptôme | Que vérifier |
| --- | --- |
| Erreur de configuration avant le démarrage du moteur | Vérifiez le fichier nommé et l'emplacement source, l'orthographe exacte des touches, les noms de pièces cités et les types de valeurs TOML. Les anciens fichiers de propriétés Java doivent être convertis. |
| Le moteur ne peut pas démarrer ou ouvrir son modèle | Vérifiez les chemins de l'exécutable et des arguments, les arguments du mode GTP et le répertoire de travail. Essayez `--probe`. |
| Commandes GTP manquantes ou mauvaise version du protocole | Utilisez un moteur complet GTP v2. La découverte nécessite `protocol_version`, `name`, `version`, `known_command`, `list_commands`, `quit`, `boardsize`, `clear_board`, `komi`, `play` et `genmove`. |
| La vérification des règles, du timing ou du score échoue | Vérifiez les capacités du moteur pour le profil sélectionné. Déclarez `engine.rules` uniquement lorsque le moteur ne dispose pas de `kgs-rules` et faites correspondre sa configuration réelle. Tous les jeux automatiques nécessitent `final_status_list`. |
| La connexion échoue | Vérifiez le nom du compte, `KGS_PASSWORD` dans l'environnement de lancement, l'adresse du serveur et le motif de rejet signalé. |
| La chambre n'est pas trouvée | Copiez son nom complet depuis KGS sur le serveur sélectionné. La correspondance ignore la casse mais nécessite le nom complet. |
| En attente d'un timeout de jeu ou de lobby | Vérifiez les conditions de correspondance, l’éligibilité des adversaires, le nom de la salle et les préférences de correspondance automatique. Augmentez `timeouts.lobby` si une attente plus longue est prévue. |
| Entrée Ranked rejetée | Vérifiez l'autorisation RankedRobot, le classement activé, la salle publique et les restrictions de profil Ranked. |
| Le score s'arrête sur un désaccord | Les différends japonais ne sont pas étayés. Le nettoyage chinois, AGA et néo-zélandais nécessite `kgs-genmove_cleanup` ; les litiges répétés, le manque de progrès et l'expiration du nettoyage arrêtent le client. |
| Le bot s'arrête après une pause ou le départ de l'adversaire | Vérifiez le délai d'expiration de l'interaction concerné et inspectez le jeu inachevé avant de redémarrer. |
| Moteur indisponible mais compte toujours en ligne | Inspectez les diagnostics du moteur et le message du tuyau de récupération. Les tentatives automatiques peuvent être épuisées ; les chronomètres de jeu et les délais fonctionnent toujours. |
| Erreur du fichier d'identité | Assurez-vous que l'emplacement d'état configuré est accessible en écriture et contient le fichier d'identité généré par le client. |

Lorsque vous signalez un problème, incluez la version du client, le nom/la version du moteur, l'ID du jeu si disponible, les paramètres pertinents et les diagnostics stderr. Omettez les mots de passe.

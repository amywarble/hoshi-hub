---
layout: "localized"
title: "Mise à niveau vers Mobi à partir du client Java GTP"
nav_title: "Migrer depuis Java"
lang: "fr"
page_key: "mobi/upgrade-guide"
section: "mobi"
nav_order: 2
permalink: "/fr/gtp/upgrade-guide/"
source_revision: "c32ebab17d841776f058eab0acfe73c12237c6953d8b7f6ec6630c41d26de6f1"
---

Ce guide déplace un bot de `kgsGtp.jar` et sa configuration Java `.properties` vers Mobi et TOML. L'ancien fichier ne peut pas être chargé directement ; il n'y a pas d'importateur automatique. Conservez-le pour référence lors de la création d'un nouveau fichier. Consultez le [guide de l'utilisateur]({% include page-url.html key='mobi/user-guide' %}) pour le fonctionnement normal et la référence complète des paramètres.

Ce guide couvre les Windows et Linux. Développez la section de votre système d'exploitation pour voir les commandes PowerShell ou Bash. Exécutez les commandes à partir du répertoire client extrait.

## Étapes de mise à niveau {#upgrade-steps}

1. Terminez ou résolvez n'importe quel jeu en cours, puis arrêtez l'ancien client et son moteur.    Désactivez son redémarrage automatique lors de la tentative de remplacement, afin que les deux clients ne se connectent pas avec le même compte.
2. Extrayez le package de pont Mobi GTP pour votre architecture Windows ou Linux.    Le package inclut le runtime .NET. Conservez votre moteur, votre modèle et la configuration du moteur ; ceux-ci restent distincts du client.
3. Copiez [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) dans `bot.toml`. Déplacez les paramètres à l'aide des tableaux ci-dessous. Mettez le mot de passe dans `KGS_PASSWORD` et choisissez explicitement le type de jeu, la politique de reprise et le nombre de jeux.
4. Sondez le moteur avec les commandes ci-dessous. Corrigez les erreurs de découverte du moteur avant de vous connecter. Des vérifications supplémentaires des capacités du jeu s'exécutent au démarrage normal.
5. Exécutez un jeu Free avec `--games 1`. Vérifiez la connexion, la sélection de l'adversaire, les chronomètres, le score et le diagnostic `Series: completed game 1`.
6. Définissez `games = 0` si vous souhaitez une lecture continue, puis mettez à jour votre lanceur ou service pour utiliser le nouvel exécutable, le chemin de configuration, l'environnement de mot de passe et les journaux.

Copiez le modèle, puis modifiez le compte, les chemins du moteur et les paramètres du jeu :

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

Après l'édition, vérifiez la découverte du moteur sans vous connecter :

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

Pour revenir à l'ancien client, arrêtez d'abord le nouveau client et le nouveau moteur, inspectez tout jeu inachevé et restaurez votre lanceur et votre fichier de propriétés d'origine. Conservez le dossier d'identité du nouveau client pour un retour ultérieur à Mobi.

## Modifications à examiner avant de changer {#changes-to-review-before-switching}

| Zone | Ancien client | Mobi |
| --- | --- | --- |
| Lancement | `java -jar kgsGtp.jar bot.properties key=value` | `Kgs.Gtp --config bot.toml --option value` ; L'exécutable Windows se termine par `.exe`. |
| Configuration | Propriétés Java, y compris les échappements Java | UTF-8 TOML avec sections nommées, chaînes entre guillemets, nombres, tableaux et booléens. Les clés inconnues sont des erreurs. |
| Mode par défaut | Automatch | Pas de matchmaking sauf si `matchmaking.mode` ou `--lobby` est sélectionné. |
| Nombre de parties | Continue à trouver des jeux | La valeur par défaut intégrée est un jeu terminé. Réglez `games = 0` pour une lecture continue ; l'exemple fourni le fait déjà. |
| Type de jeu | Automatch pourrait permettre à Free et Ranked ensemble | Sélectionnez `Free` (par défaut) ou `Ranked` exclusivement. Il n’y a pas de paramètre mixte ni de solution de secours. |
| Chambre | Nom de la pièce | Nom de la salle, toujours une chaîne ; utilisez `room = "English Room"`. La recherche ignore la casse et nécessite un nom exact. |
| Conditions de jeu personnalisées | Les joueurs pourraient proposer des changements | Les termes configurés doivent correspondre exactement, y compris les couleurs, les komi, le handicap, la visibilité et le contrôle du temps. |
| Reprises | Normalement autorisé dans les jeux Free, refusé dans Ranked | Les deux stratégies intégrées sont par défaut `Never`. Définissez `undo.free = "Allow"` pour conserver le comportement habituel de Free. L'exemple fait cela. |
| Automatch handicap | Pourrait permettre jusqu'à neuf rangs si le moteur prenait en charge le handicap | `maxRankDifference` est par défaut `0` ; choisissez-le explicitement, au plus 9 pour Free ou 6 pour Ranked. |
| Nouvelles tentatives de connexion | `reconnect=t` permet de continuer à réessayer | Budget de panne par seconde 180 par défaut, interruption exponentielle avec instabilité et réinitialisation après des secondes saines 60. |
| Panne moteur | Pas de redémarrage automatique du moteur à partir de `reconnect` | Budget de redémarrage automatique séparé ; l'épuisement attend le rétablissement de l'opérateur alors que les délais normaux se poursuivent. |
| Départ de l'adversaire | Pourrait revenir au matchmaking après sa limite d'absence | Le nouveau client s'arrête avec un diagnostic de jeu inachevé lorsque l'attente configurée expire. |

L'exemple est une configuration de départ et non une affirmation selon laquelle tous les anciens comportements sont préservés. En particulier, décidez si ce compte doit jouer à Free ou Ranked avant d'activer le fonctionnement continu.

## Mapper les anciens paramètres {#map-the-old-settings}

Les nouveaux noms de paramètres ci-dessous utilisent la notation `section.key`. Par exemple, `account.username` signifie `username = "YourBot"` sous `[account]`.

### Compte, connexion et moteur {#account-connection-and-engine}

| Ancienne propriété | Nouveau paramètre | Notes de migration |
| --- | --- | --- |
| `name` | `account.username` / `--username` | `KGS_USERNAME` est également pris en charge lorsqu'aucun nom d'utilisateur n'est configuré. |
| `password` | Variable d'environnement `KGS_PASSWORD` | Supprimez-le de la nouvelle configuration ; Les champs de mot de passe et les options CLI de mot de passe ne sont pas pris en charge. |
| `server.host` | `server.host` / `--host` | Chaîne ; par défaut `goserver.gokgs.com`. |
| `server.port` | `server.port` / `--port` | Entier ; par défaut `2379`. |
| `reconnect=f` | `connectionRecovery.attempts = 0` | Désactive les tentatives de transport KGS ; la récupération du moteur est configurée séparément. |
| `reconnect=t` | `[connectionRecovery]` | Choisissez un budget temps par panne ; la valeur par défaut est 180 secondes. Un plafond de tentative est facultatif. |
| `engine` | `engine.executable` et `engine.arguments` | Divisez la commande en arguments exécutables et individuels ; voir ci-dessous. |
| Aucune propriété de connexion moteur | `engine.stdio = true` / `--stdio` | Les E/S standard doivent maintenant être sélectionnées explicitement. |
| `gtp.in`, `gtp.out` | Pas de réglage direct | Un lanceur externe peut connecter les deux directions via `--stdio`. Le client n'ouvre pas les fichiers nommés ou les FIFO à partir de la configuration. |
| `engine.port` | Pas de réglage direct | Il n’y a pas d’écouteur TCP du moteur. Utilisez un adaptateur externe avec `--stdio` ou laissez le client lancer le moteur. |
| `logFile` | Capturer stderr en externe | Utilisez la redirection shell ou un gestionnaire de services ; la dénomination et la rotation des journaux Java intégrés ne sont pas conservées. |
| `verbose` | Pas de réglage direct | Les diagnostics normaux vont à stderr ; il n’existe pas de commutateur de journalisation du trafic GTP/serveur complet équivalent. |

Le `engineRecovery.pipe` local sert à remplacer un moteur en panne lors d'une session en cours d'exécution. Il ne remplace pas les anciens paramètres de démarrage `engine.port`, `gtp.in` ou `gtp.out`.

### Matchmaking et paramètres de jeu {#matchmaking-and-game-settings}

| Ancienne propriété | Nouveau paramètre | Notes de migration |
| --- | --- | --- |
| `mode=auto` | `matchmaking.mode = "Automatch"` | Omettez l'espace, les paramètres personnalisés de l'adversaire et les sections `game`/`timing`. |
| `mode=custom` | `matchmaking.mode = "Offer"` | Ajoutez `opponentPolicy = "Any"` pour les défis ouverts, ou `"Named"` plus `opponent`. |
| `mode=wait` | `matchmaking.mode = "Join"` | Définissez le nom de la pièce et `opponent` ; le profil proposé doit correspondre exactement. |
| `mode=both` | Pas de mode combiné | Choisissez Automatch, Offer ou Join pour cet appel. |
| `mode=tournament` | Non pris en charge | L'inscription au tournoi n'est pas mise en œuvre ; conserver l'ancien client si cela est nécessaire. |
| `room` | `matchmaking.room` / `--room` | Conservez le nom de la salle sous forme de chaîne entre guillemets. Requis pour Offer et Join ; omettre pour Automatch. Il n’y a pas de valeur par défaut pour la dernière pièce utilisée. |
| `opponent` | `matchmaking.opponent` | Pour les défis personnalisés, utilisez `opponentPolicy = "Named"`. Omettez les deux paramètres personnalisés de l'adversaire pour Automatch. |
| `gameNotes` | `matchmaking.challengeNotes` | Offer uniquement ; au plus des caractères 255 sans caractères de contrôle. |
| `rules` | `game.rules` | Utilisez `Japanese`, `Chinese`, `Aga` ou `NewZealand`. Définit les conditions de jeu personnalisées exactes. |
| `komi` | `game.komi` | Nombre, pas une chaîne entre guillemets ; défini explicitement, y compris pour les jeux à handicap. |
| `rules.boardSize` | `game.boardSize` | Entier. Définir explicitement : la nouvelle valeur par défaut du jeu personnalisé est 9. |
| `rules.time` | `[timing]` | Divisez-le en champs système, secondes et temps additionnel à l'aide des exemples ci-dessous. |
| `automatch.speed` | `automatch.speed` | Par exemple `speed = ["Blitz", "Medium"]` ou `"All"`. Les combinaisons CLI utilisent des virgules. |
| `automatch.rank` | `automatch.rank` | Cité de `30k` à `1k` ; toujours requis lorsqu'il n'y a pas de rang de serveur numérique. |
| `undo=f` | `[undo]` avec `free = "Never"`, `ranked = "Never"` | Ce sont également les valeurs par défaut intégrées. |
| `undo=t` ou omis | `[undo]` avec `free = "Allow"`, `ranked = "Never"` | Conserve l'ancienne distinction habituelle Free/Ranked. Les nouvelles reprises Ranked peuvent être activées séparément si vous le souhaitez. |
| `talk` | Non pris en charge | Les réponses au chat privé et le transfert de chat du moteur ne sont pas implémentés. |
| `hint.cleanup`, `hint.noArguing` | Non pris en charge | Il n'existe pas d'indices de discussion configurables pour les litiges de notation. |

`game.rules` et `engine.rules` ont des objectifs différents. Le premier choisit les règles du jeu personnalisé. Ce dernier déclare des règles déjà configurées dans un moteur dépourvu de `kgs-rules` ; cela ne change pas la configuration de ce moteur.

### Diviser la commande du moteur {#split-the-engine-command}

Une propriété ancienne peut être :

```properties
engine=/opt/katago/katago gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

La nouvelle configuration est :

```toml
[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]
```

Ne placez pas une ligne de commande entière dans `executable`. Il n’y a pas d’évaluation shell. Chaque argument est un élément du tableau, comprenant des chemins contenant des espaces. Pour Windows, les chaînes TOML entre guillemets simples conservent les barres obliques inverses littérales :

```toml
[engine]
executable = 'C:\Go Engines\katago.exe'
arguments = ["gtp", "-config", 'C:\Go Engines\gtp.cfg', "-model", 'C:\Go Engines\model.bin.gz']
```

Remplacez les échappements des propriétés Java par le texte réel dans UTF-8 TOML. Les chemins d'accès relatifs aux exécutables contenant un séparateur sont résolus à partir du répertoire TOML ; les chemins d'argument restent relatifs au répertoire de travail de lancement. Les chemins de modèle et de configuration absolus facilitent la reproduction des lancements de services.

### Convertir les contrôles de temps {#convert-time-controls}

Utilisez une seule de ces sections `[timing]`, et uniquement avec Offer ou Join.

Ancien `rules.time=0` :

```toml
[timing]
system = "None"
mainTime = 0
```

Ancien `rules.time=30:00` :

```toml
[timing]
system = "Absolute"
mainTime = 1800
```

Ancien `rules.time=30:00+5x0:30` :

```toml
[timing]
system = "ByoYomi"
mainTime = 1800
byoYomiTime = 30
byoYomiPeriods = 5
```

Ancien `rules.time=30:00+25/10:00` :

```toml
[timing]
system = "Canadian"
mainTime = 1800
byoYomiTime = 600
canadianStones = 25
```

Toutes les nouvelles valeurs de temps sont des secondes entières. Supprimez les champs d'temps additionnel qui appartiennent à un autre système. Les temps additionnel japonaises nécessitent la commande `kgs-time_settings` du moteur ; il n'est pas approximé en utilisant un autre système d'horloge.

## Exemple : migrer un bot de correspondance automatique {#example-migrate-an-automatch-bot}

Supposons que les parties pertinentes de l'ancien fichier soient :

```properties
name=YourBot
password=<account password>
mode=auto
room=English Room
automatch.speed=fast,medium
automatch.rank=20k
undo=t
reconnect=t
engine=/opt/katago/katago gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

Créez ce `bot.toml` pour un premier jeu Free. Automatch ne prend pas de paramètre de pièce, donc l'ancienne propriété `room` est omise :

```toml
[account]
username = "YourBot"
clientIdFile = "./state/client-id"

[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]

[matchmaking]
mode = "Automatch"
gameType = "Free"
games = 1

[automatch]
speed = ["Fast", "Medium"]
rank = "20k"
opponents = "Humans"
maxRankDifference = 0

[undo]
free = "Allow"
ranked = "Never"

[connectionRecovery]
budget = 180
resetAfter = 60
```

Pour Windows, remplacez les chemins `[engine]` par l'exemple Windows dans [Diviser la commande du moteur](#split-the-engine-command). Définissez le mot de passe et lancez un jeu :

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

Cet exemple sélectionne délibérément même les jeux Free. Pour conserver la correspondance de handicap, sélectionnez un `maxRankDifference` approprié et vérifiez le support moteur. Pour jouer à Ranked, sélectionnez `gameType = "Ranked"`, vérifiez l'autorisation RankedRobot et le classement activé du compte, et utilisez au maximum six rangs de différence. Une invocation ne peut pas accepter les deux types de jeux.

Pour un bot personnalisé, utilisez l'[exemple de défi personnalisé]({% include page-url.html key='mobi/user-guide' %}#custom-challenges), copiez l'ancien nom de la salle et transférez explicitement la taille du tableau, les règles, les komi, la couleur, le handicap et les paramètres de temps convertis.

## Compatibilité moteur et fonctionnement sans surveillance {#engine-compatibility-and-unattended-operation}

Mobi nécessite GTP v2 et son jeu de commandes obligatoire complet. Certaines commandes traitées comme facultatives par l'ancien client sont obligatoires ici. Tous les jeux automatiques nécessitent également `final_status_list`. Les jeux chronométrés nécessitent `time_left` et une commande de synchronisation prise en charge. Vérifiez les exigences du moteur du guide de l'utilisateur pour votre profil sélectionné ; une ancienne configuration fonctionnelle à elle seule n’établit pas la compatibilité.

L'accord de notation japonais ordinaire est soutenu, mais les différends japonais non résolus arrêtent le jeu. Le nettoyage chinois, AGA et néo-zélandais nécessite `kgs-genmove_cleanup` et comporte des tentatives limitées et un délai total. Il n'existe pas de solution de secours d'ancien client permettant à un adversaire de décider de toutes les pierres mortes lorsque la notation automatique n'est pas disponible.

Vérifiez ces paramètres de service avant de laisser le bot sans surveillance :

- Définissez explicitement `games = 0` s'il doit continuer à jouer. Chaque tentative de lobbying a toujours un délai par défaut de 300 en secondes ; augmentez `timeouts.lobby` si nécessaire.
- Configurez séparément les tentatives de connexion KGS et les redémarrages du moteur. La récupération KGS est définie par défaut sur 180 secondes par panne et se réinitialise après les secondes saines 60. La récupération du moteur permet trois remplacements automatiques au cours de l'invocation ; l'épuisement peut laisser une session KGS en direct en attente de récupération de l'opérateur.
- Choisissez les limites de pause, d’ajournement et d’absence de l’adversaire. Chaque valeur par défaut est 300 secondes ; l'expiration arrête le client sans compter ni abandonner la partie inachevée.
- Conservez le fichier d'identité du client dans un répertoire d'état accessible en écriture. Un nouveau processus ne découvre pas automatiquement les anciens jeux de correspondance automatique.
- Capturez stderr et organisez la conservation des journaux externes. Quitter 0 signifie un achèvement normal, 1 indique un échec et 130 indique une annulation.

Le [guide de l'utilisateur]({% include page-url.html key='mobi/user-guide' %}#timeouts-and-recovery) décrit en détail les paramètres de délai d'expiration, la récupération de connexion et la récupération du moteur de l'opérateur.

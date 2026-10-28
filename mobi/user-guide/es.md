---
layout: "localized"
title: "Guía del usuario Mobi"
nav_title: "Guía del usuario"
lang: "es"
page_key: "mobi/user-guide"
section: "mobi"
nav_order: 1
permalink: "/es/gtp/user-guide/"
source_revision: "26bf30c603841ace27c0d2ff994fd0d2297af607b506d24fd1ab9afabb8f1a33"
---

Mobi conecta un motor Go a KGS para que pueda reproducirse automáticamente. Ejecuta el cliente en una terminal y lo controla a través de un archivo de configuración TOML u opciones de línea de comandos. Instale y configure su motor por separado; el cliente maneja el inicio de sesión, la búsqueda de juegos, movimientos, relojes y puntuación.

¿Pasar del cliente Java `kgsGtp.jar`? Comience con la [guía de actualización]({% include page-url.html key='mobi/upgrade-guide' %}).

Esta guía cubre Windows y Linux. Expanda la sección de su sistema operativo para ver los comandos PowerShell o Bash. Ejecute los ejemplos de clientes empaquetados desde el directorio del cliente extraído.

- [Primer juego](#first-game)
- [Conceptos básicos de configuración](#configuration-basics)
- [Elegir juegos](#choosing-games)
- [Configuración de juego personalizada](#custom-game-settings)
- [Ejecutando el bot](#running-the-bot)
- [Tiempos de espera y recuperación](#timeouts-and-recovery)
- [Solución de problemas](#troubleshooting)

## primer juego {#first-game}

Necesita una cuenta KGS registrada, un motor GTP versión 2 y cualquier archivo de configuración y modelo que requiera ese motor. Cree la cuenta utilizando un cliente KGS normal antes de iniciar el bot. El juego Ranked necesita permiso de servidor adicional; Comience con un juego Free.

Extraiga el paquete de cliente para su sistema operativo y arquitectura. Se proporcionan paquetes para Windows y Linux en x64 y ARM64, con el tiempo de ejecución .NET incluido. Mantenga los archivos extraídos juntos. El ejecutable es `Kgs.Gtp.exe` en Windows y `Kgs.Gtp` en Linux.

### 1. Crea tu configuración {#1-create-your-configuration}

Copie el [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) incluido en `bot.toml`:

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

Edite `account.username`, `engine.executable` y `engine.arguments`. Por ejemplo:

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

Proporcione las rutas y argumentos que su motor necesita para ingresar al modo GTP. Cada elemento de la matriz es un argumento; un camino que contiene espacios sigue siendo un elemento.

El ejemplo selecciona Free coincidencia automática contra humanos, velocidad rápida o media y juego continuo. Establezca `automatch.rank` en una estimación adecuada entre `30k` y `1k` si la cuenta no tiene una clasificación numérica. KGS utiliza el rango de la cuenta cuando hay uno disponible. Para la primera ejecución, el siguiente comando limita el juego a un juego.

### 2. comprobar el motor {#2-check-the-engine}

Desde el directorio del cliente extraído, ejecute:

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

El cliente imprime el nombre del motor, la versión y los comandos admitidos y luego sale. Esto no necesita credenciales KGS y no se conecta a KGS. Comprueba el descubrimiento GTP; Las reglas adicionales, el reloj, el hándicap y las comprobaciones de puntuación se ejecutan al iniciar el modo de juego configurado.

### 3. Proporciona la contraseña y juega. {#3-supply-the-password-and-play}

La contraseña proviene únicamente de la variable de entorno `KGS_PASSWORD`:

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

Busque `Logged in to KGS` y luego `Game ready`. El cliente juega y puntúa el juego automáticamente. `Game finished` registra el resultado de KGS; `Series: completed game 1` confirma que contó para el total solicitado. Luego cierra la sesión y sale. La búsqueda de un juego está limitada a cinco minutos de forma predeterminada; use `--lobby-timeout 3600` para permitir hasta una hora.

## Conceptos básicos de configuración {#configuration-basics}

Seleccione siempre el archivo explícitamente con `--config`. El cliente lo lee una vez al inicio. Reinicie para aplicar las ediciones, incluidos los cambios en la configuración de reinicio del motor. No hay búsqueda automática de archivos de configuración ni recarga en vivo.

Las opciones de la línea de comandos anulan los valores del archivo para esa ejecución. Por ejemplo:

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

El nombre de usuario proviene de `--username`, luego `account.username` y luego `KGS_USERNAME`. No agregue un campo de contraseña al archivo: se rechaza.

Utilice cadenas entre comillas para nombres y selecciones, números enteros para conteos y segundos, números para komi y `true` o `false` para booleanos. Los nombres de tablas y claves distinguen entre mayúsculas y minúsculas. Las claves desconocidas y los valores no válidos detienen el inicio con un diagnóstico. Todas las duraciones en esta guía son segundos.

Un `engine.executable` relativo que contiene `/` o `\`, y un `account.clientIdFile` relativo, son relativos al directorio del archivo de configuración. Un nombre ejecutable simple, como `katago`, utiliza la búsqueda de ejecutables. Los argumentos del motor se pasan sin cambios y el motor hereda el directorio de trabajo desde el que inicia el cliente. Utilice rutas absolutas para los argumentos de configuración del modelo y del motor si inicia desde directorios diferentes. Las cadenas TOML entre comillas simples conservan las barras invertidas Windows. Las cadenas no expanden las variables de entorno.

### Cuenta, servidor y motor {#account-server-and-engine}

| Configuración TOML | Opción CLI | Significado y valor predeterminado |
| --- | --- | --- |
| `account.username` | `--username` | Nombre de cuenta KGS; vuelve a caer en `KGS_USERNAME`. |
| `account.clientIdFile` | `--client-id-file` | Archivo de identidad persistente; normalmente elegido por servidor y cuenta. |
| `server.host` | `--host` | Servidor KGS; predeterminado `goserver.gokgs.com`. |
| `server.port` | `--port` | Puerto TCP; predeterminado `2379`, rango 1–65535. |
| `engine.executable` | `--engine` | Motor ejecutable para iniciar. |
| `engine.arguments` | Argumentos posteriores a `--` | Matriz de argumentos del motor; vacío por defecto. |
| `engine.stdio` | `--stdio` | Utilice un motor conectado externamente en lugar de iniciar uno; predeterminado `false`. |
| `engine.rules` | `--engine-rules` | Reglas ya configuradas en un motor que carece de `kgs-rules`. Sin declaración de incumplimiento. |

Elija un ejecutable o `stdio = true`, nunca ambos. Con E/S estándar, otro programa debe conectar el stdin del cliente al stdout del motor y el stdout del cliente al stdin del motor. Los diagnósticos utilizan stderr. No proporcione argumentos del motor en este modo.

`engine.rules` acepta `Japanese`, `Chinese`, `Aga` o `NewZealand`. Esto declara las reglas existentes del motor; Configure el motor para que coincida. Los motores con `kgs-rules` reciben automáticamente las reglas del juego seleccionado.

Para configurar completamente en la línea de comando, coloque los argumentos del motor después de `--`:

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

Los argumentos explícitos del motor CLI reemplazan toda la matriz de archivos. Un `--` final sin nada después de borrar esa matriz. `--engine` y `--stdio` anulan la opción de conexión del motor del archivo; `--stdio` también descarta argumentos basados ​​en archivos. `--help` enumera todas las opciones y `--version` imprime la versión del cliente.

## Elegir juegos {#choosing-games}

Selecciona un modo de emparejamiento:

| `matchmaking.mode` / `--lobby` | Que hace el robot |
| --- | --- |
| `Automatch` | Permitamos que KGS encuentre un oponente y elija los términos del juego. |
| `Offer` | Anuncia un desafío personalizado en la sala nombrada. |
| `Join` | Busca un desafío personalizado coincidente en la sala nombrada. |

Sin un modo, el cliente inicia sesión y espera hasta que se detenga; no encuentra juegos. Una invocación juega un juego a la vez. Actualmente no se admiten desafíos personalizados simultáneos ni coincidencias automáticas, entradas a torneos ni respuestas de chat.

### Automatch {#automatch}

Utilice estas secciones junto con la configuración de su cuenta y motor:

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

Omita las secciones `matchmaking.room`, `opponent`, `opponentPolicy`, `challengeNotes` y `game` y `timing` en el modo Automatch. Estas son configuraciones de desafío personalizadas y no se pueden combinar con la coincidencia automática, incluso si sus valores coinciden con los predeterminados.

| Configuración TOML | Opción CLI | Opciones y valores predeterminados |
| --- | --- | --- |
| `automatch.speed` | `--automatch-speed` | `All` (predeterminado), `Blitz`, `Fast`, `Medium` o una matriz como `["Fast", "Medium"]`. Las combinaciones CLI utilizan comas. |
| `automatch.rank` | `--automatch-rank` | Estimado desde `30k` hasta `1k`; requerido cuando la cuenta no tiene rango de servidor numérico. |
| `automatch.opponents` | `--automatch-opponents` | `Humans` (predeterminado), `Robots` o `Any`. |
| `automatch.maxRankDifference` | `--automatch-max-rank-difference` | Predeterminado `0`; gama 0–9 para Free, 0–6 para Ranked. |

Las partidas Automatch son públicas, de 19×19, con reglas japonesas y colores asignados por el servidor. Las partidas sin hándicap usan komi 6.5. Permitir diferencias de rango puede dar komi 0.5 y, para diferencias de dos o más, piedras de hándicap de colocación fija.

| Velocidad | Tiempo principal por jugador | Byoyomi japonés |
| --- | --- | --- |
| `Blitz` | 60 segundos | 3 períodos de 10 segundos |
| `Fast` | 600 segundos | 5 períodos de 20 segundos |
| `Medium` | 1500 segundos | 5 períodos de 30 segundos |

El motor debe admitir `final_status_list`, `kgs-time_settings` y `time_left`; permitir handicap también requiere `set_free_handicap`. Si falta `kgs-rules`, configúrelo para las reglas japonesas y configure `engine.rules = "Japanese"`.

### Desafíos personalizados {#custom-challenges}

Reemplace las secciones `matchmaking` y `automatch` del archivo de ejemplo con un perfil personalizado. Este ejemplo ofrece un juego público 19×19 Free a jugadores elegibles:

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

Utilice el nombre de la habitación como se muestra en KGS. Los nombres pueden contener espacios y caracteres no ASCII. La búsqueda utiliza una coincidencia exacta que no distingue entre mayúsculas y minúsculas después de iniciar sesión y nuevamente después de la reconexión. Los nombres faltantes o ambiguos detienen al cliente con un diagnóstico.

Para un oponente específico, cambie `opponentPolicy` por `"Named"` y agregue `opponent = "OtherAccount"`. Para `Any`, omita `opponent`; Los oponentes abiertos elegibles son cuentas conectadas y registradas distintas de este bot. Tanto los humanos como los robots son elegibles.

Para unirse a desafíos, use `mode = "Join"` y elimine `challengeNotes`. Todos los términos del juego deben coincidir, incluidas las reglas, komi, hándicap, visibilidad y relojes. Elija el color del bot: un bot Offer que juegue con negras necesita un bot Join que juegue con blancas; para colores aleatorios, ambos usan `"Nigiri"`. Los términos modificados no se aceptan silenciosamente.

| Configuración TOML | Opción CLI | Opciones y valores predeterminados |
| --- | --- | --- |
| `matchmaking.mode` | `--lobby` | `Offer`, `Join` o `Automatch`; sin modo predeterminado. |
| `matchmaking.gameType` | `--game-type` | `Free` (predeterminado) o `Ranked`. |
| `matchmaking.opponentPolicy` | `--opponent-policy` | `Named` (predeterminado para desafíos personalizados) o `Any`. |
| `matchmaking.opponent` | `--opponent` | Requerido con `Named`; Los nombres de cuentas ignoran mayúsculas y minúsculas. |
| `matchmaking.room` | `--room` | Nombre de habitación requerido para Offer y Join; por ejemplo `"Computer Go"`. |
| `matchmaking.games` | `--games` | Predeterminado `1`; Número positivo para una serie, `0` para juego continuo. |
| `matchmaking.challengeNotes` | `--challenge-notes` | Solo Offer; hasta caracteres 255, sin caracteres de control. La omisión genera una nota de oponente. |

### Juegos Ranked {#ranked-games}

Configure `matchmaking.gameType = "Ranked"` para solicitar juegos Ranked exclusivamente. La cuenta debe tener el permiso `RankedRobot` otorgado por el servidor y el rango habilitado. Solicite ese permiso a un administrador del servidor KGS. Se permite un rango no establecido (`?`), pero no un rango deshabilitado (`-`); La coincidencia automática aún necesita una estimación cuando la cuenta no tiene clasificación numérica.

Los rivales Ranked deben tener cuentas registradas con rango habilitado y un rango aficionado o aún sin determinar. Los rivales robot también necesitan `RankedRobot`. Los desafíos personalizados Ranked requieren sala pública, partida pública de 19×19, como máximo seis piedras de hándicap, komi de −10 a 10 y tiempo estimado superior a 450 segundos por jugador. La estimación incluye tiempo adicional; también se permite tiempo ilimitado. Un perfil Absolute de 600 segundos cumple el requisito. El cliente rechaza ajustes no válidos o un cambio del servidor a Free.

## Configuraciones de juego personalizadas {#custom-game-settings}

Estas configuraciones se aplican a Offer y Join. Déjalos fuera de las configuraciones Automatch.

| Configuración TOML | Opción CLI | Opciones y valores predeterminados |
| --- | --- | --- |
| `game.boardSize` | `--board-size` | Predeterminado `9`; gama 2–25, sujeto al soporte del motor. |
| `game.rules` | `--rules` | `Chinese` (predeterminado), `Japanese`, `Aga` o `NewZealand`. |
| `game.komi` | `--komi` | Predeterminado `7.5`; −100 a 100 en incrementos de medio punto. |
| `game.color` | `--color` | `Black`, `White` o `Nigiri`; El valor predeterminado es Negro para Offer y Blanco para Join. |
| `game.handicap` | `--handicap` | Predeterminado `0`; de lo contrario, 2–9 dentro de los límites de colocación del tablero. No se puede combinar con Nigiri. |
| `game.private` | `--private` | Predeterminado `false`; requiere un juego privado manteniendo el desafío anunciado en la sala seleccionada. |

El hándicap no ajusta el komi automáticamente. Configure ambos de forma explícita. Las reglas japonesas y AGA usan colocación fija: al menos 7×7 y como máximo cuatro piedras en 7×7 o tableros de lado par. Las reglas chinas y neozelandesas usan colocación libre, con un máximo de nueve piedras y al menos una intersección vacía. Las partidas con hándicap requieren `set_free_handicap`; las negras también necesitan `place_free_handicap` para colocación libre.

### Controles de tiempo {#time-controls}

| Configuración TOML | Opción CLI | Predeterminado y rango |
| --- | --- | --- |
| `timing.system` | `--time-system` | `Absolute` (predeterminado), `None`, `Canadian` o `ByoYomi`. |
| `timing.mainTime` | `--main-time` | Valor predeterminado `600` o `0` para Ninguno; rango 0–86400. |
| `timing.byoYomiTime` | `--byo-yomi-time` | Predeterminado `0`; 1–86400 por período japonés o bloque canadiense cuando se utilizan tiempo adicional. |
| `timing.byoYomiPeriods` | `--byo-yomi-periods` | Predeterminado `0`; 1–255 para ByoYomi. |
| `timing.canadianStones` | `--canadian-stones` | Predeterminado `0`; 1–255 para canadiense. |

Para tiempo extra japonés con diez minutos de tiempo principal y cinco periodos de 30 segundos:

```toml
[timing]
system = "ByoYomi"
mainTime = 600
byoYomiTime = 30
byoYomiPeriods = 5
```

Para el tiempo adicional canadiense, utilice `system = "Canadian"`, `byoYomiTime` para segundos por bloque y `canadianStones` para piedras por bloque. Omita `byoYomiPeriods`. El tiempo adicional permite cero tiempo principal. Absoluto requiere tiempo principal positivo y no tiempo adicional; Ninguno requiere que todos los valores de tiempo proporcionados explícitamente sean cero. Las reservas totales de reloj también deben ajustarse al rango del servidor; Se informan combinaciones no válidas.

Los juegos cronometrados requieren `time_left` y `time_settings` o `kgs-time_settings`. El tiempo adicional japonés requiere específicamente `kgs-time_settings`. Los juegos ilimitados no requieren comandos de reloj. Los tiempos de espera de respuesta del motor están separados del reloj del juego y no le dan al robot más tiempo de juego.

## Ejecutando el robot {#running-the-bot}

Establece `matchmaking.games` en un total positivo o en `0` para seguir jugando. Solo cuentan los resultados confirmados por KGS. Después de completar un juego, el cliente lo abandona y usa la configuración de emparejamiento original para el siguiente juego. Un juego fallido o inacabado detiene la serie en lugar de contar como completada.

Para juego continuo con una espera más larga entre juegos:

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

Presione Ctrl+C para detener. El cliente cierra la sesión, solicita al motor que se cierre y detiene el motor que inició si es necesario. Detenerse durante un juego no establece un resultado final. Inspeccione cualquier juego sin terminar antes de comenzar otra ejecución.

### Registros y códigos de salida {#logs-and-exit-codes}

El estado, los errores, la ayuda y los diagnósticos del motor van a stderr. Para retenerlos:

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

Utilice su administrador de servicios o herramientas externas para la rotación de registros. En modo de E/S estándar, mantenga stdout conectado al motor; lleva comandos GTP.

| código de salida | Significado |
| --- | --- |
| `0` | Los juegos solicitados se completaron o un comando de sonda/ayuda/versión se realizó correctamente. |
| `1` | Fallo de configuración o tiempo de ejecución; inspeccionar el diagnóstico. |
| `130` | Cancelación del operador, incluido Ctrl+C. |

### Estado persistente y juegos existentes. {#persistent-state-and-existing-games}

El cliente guarda la identidad asignada por KGS. En los modos de emparejamiento, el archivo predeterminado se encuentra en el directorio de datos de la aplicación local de .NET en `Kgs.Gtp/identities/<server-and-account-hash>`. En Windows esto normalmente está por debajo de `%LOCALAPPDATA%`. Para elegir una ubicación de escritura estable, configure `account.clientIdFile = "./state/client-id"`. Consérvelo durante las actualizaciones y reemplazos de contenedores. Utilice un archivo independiente para cada servidor y cuenta.

Offer y Join primero verifican la sala seleccionada en busca de un juego sin terminar que pertenezca a esta cuenta. Se puede reanudar exactamente un juego compatible; su oponente y su perfil completo deben coincidir. Varios juegos o que no coinciden dejan de iniciarse. Los juegos archivados no se cargan automáticamente.

Una sesión de coincidencia automática en ejecución puede recuperar su juego asignado después de una pérdida de conexión. Un proceso nuevo no descubre automáticamente juegos de combinación automática más antiguos. Resuelve un juego de coincidencia automática sin terminar antes de volver a inscribirte.

### Recuperaciones, pausas y ausencia del oponente {#takebacks-pauses-and-opponent-absence}

`undo.free` / `--undo-free` y `undo.ranked` / `--undo-ranked` aceptan independientemente `Never` (predeterminado) o `Allow`. El ejemplo permite deshacer jugadas en Free y lo rechaza en Ranked. Allow concede las solicitudes del rival que permita el servidor durante el juego activo normal; el bot no pide deshacer jugadas. Después reproduce el historial confirmado, por lo que el motor no necesita GTP `undo`. La reanudación por desacuerdo en el recuento es independiente de esta política.

KGS controla las pausas, el aplazamiento y la reanudación. Mientras está en pausa o en pausa, el bot no inicia ningún juego nuevo ni acciones de puntuación. Cada pausa continua, aplazamiento y ausencia del oponente tiene un límite separado, por defecto 300 segundos:

| Configuración de TOML en `[interactions]` | Opción CLI |
| --- | --- |
| `pauseTimeoutFree` | `--pause-timeout-free` |
| `adjournmentTimeoutFree` | `--adjournment-timeout-free` |
| `opponentTimeoutFree` | `--opponent-timeout-free` |
| `pauseTimeoutRanked` | `--pause-timeout-ranked` |
| `adjournmentTimeoutRanked` | `--adjournment-timeout-ranked` |
| `opponentTimeoutRanked` | `--opponent-timeout-ranked` |

Cada uno acepta segundos 1–86400. La caducidad detiene al cliente con el código 1 y deja el juego sin terminar; no renuncia ni comienza otro juego. La reconexión y el reemplazo del motor no restablecen estas esperas. Otros plazos activos pueden expirar antes. Mientras un oponente esté ausente, el bot aún puede moverse si KGS lo permite.

## Tiempos de espera y recuperación {#timeouts-and-recovery}

### Tiempos de espera normales {#normal-timeouts}

Todos aceptan segundos 1–86400:

| Configuración TOML | Opción CLI | Predeterminado | Límites |
| --- | --- | --- | --- |
| `timeouts.login` | `--login-timeout` | `30` | Conectándose e iniciando sesión. |
| `timeouts.lobby` | `--lobby-timeout` | `300` | Una negociación de desafío o inscripción de coincidencia automática; también limita la búsqueda de nombres de habitaciones. |
| `timeouts.move` | `--move-timeout` | `600` | Un motor de búsqueda normal o de limpieza. |
| `timeouts.scoring` | `--scoring-timeout` | `120` | Una ronda de puntuación, que incluye evaluación y acuerdo. |
| `timeouts.cleanup` | `--cleanup-timeout` | `300` | Todos los intentos de limpieza y puntuación posterior juntos. |

### Pérdida de conexión KGS {#kgs-connection-loss}

El cliente vuelve a intentar fallas de transporte, se autentica nuevamente y se reincorpora al juego interrumpido usando el historial del servidor. No reenvía un movimiento incierto ni reemplaza un juego interrumpido conocido con un nuevo desafío. El inicio de sesión rechazado, el cierre de sesión del servidor, los datos del servidor no válidos, los movimientos ilegales del motor y los comandos del motor rechazados son fallas del terminal.

| Configuración TOML | Opción CLI | Predeterminado y rango |
| --- | --- | --- |
| `connectionRecovery.attempts` | `--reconnect-attempts` | Límite opcional por interrupción; 0–100. Omitido por defecto; cero deshabilita los reintentos. |
| `connectionRecovery.delay` | `--reconnect-delay` | `1`-segunda ventana inicial; 0–30, duplicándose a un límite de segundo 30, con fluctuación total. |
| `connectionRecovery.timeout` | `--recovery-timeout` | `120` segundos por reconexión mediante la reinserción del juego; 1–86400. |
| `connectionRecovery.budget` | `--recovery-budget` | `180` segundos totales por interrupción, incluidos drenaje, retroceso, inicio de sesión y reincorporación; 1–86400. |
| `connectionRecovery.resetAfter` | `--recovery-reset-after` | `60` segundos saludables después de la nueva conexión antes de restablecer el presupuesto y el recuento de reintentos; 1–86400. |
| `connectionRecovery.engineDrainTimeout` | `--engine-drain-timeout` | `30` segundos para finalizar y descartar trabajos antiguos del motor; 1–86400. |

El presupuesto de interrupción comienza cuando se detecta una pérdida de conexión. Cada reconexión está limitada por el presupuesto restante, así como por su propio tiempo de espera para iniciar sesión/reunirse. Cada retraso de retroceso se selecciona aleatoriamente entre cero y un límite máximo que se duplica desde 1 segundos hasta un límite 30 de segundos. La recuperación se detiene cuando se agota el presupuesto total o un límite de intento explícito.

Después de volver a conectarse, el bot puede continuar jugando más allá de la fecha límite de recuperación anterior. Una desconexión posterior obtiene un nuevo presupuesto después de 60 segundos saludables. Una desconexión antes de ese intervalo conserva la fecha límite anterior y el recuento de reintentos, incluido el tiempo de conexión breve. El inicio de sesión por sí solo no establece la salud cuando aún es necesario volver a unirse a un juego.

### Fallo del motor {#engine-failure}

Si un motor en ejecución sale o su flujo queda inutilizable, el cliente mantiene activa la sesión KGS e intenta iniciar un reemplazo utilizando el ejecutable y los argumentos originales. Comprueba el reemplazo y reproduce el historial confirmado antes de continuar. Las fallas iniciales de arranque/descubrimiento del motor detienen al cliente. Los relojes KGS continúan mientras el motor no está disponible.

| Configuración TOML | Opción CLI | Predeterminado y rango |
| --- | --- | --- |
| `engineRecovery.attempts` | `--engine-restart-attempts` | `3` reemplazos automáticos a lo largo de la invocación; 0–100. Zero espera la recuperación del operador. |
| `engineRecovery.delay` | `--engine-restart-delay` | `1`-segunda ventana inicial; 0–30, duplicándose a un límite de segundo 30, con fluctuación total. |
| `engineRecovery.timeout` | `--engine-recovery-timeout` | `120` segundos para descubrimiento/configuración y por separado para reproducción; 1–86400. |
| `engineRecovery.pipe` | `--engine-recovery-pipe` | Tubería de recuperación local; predeterminado `kgs-gtp-<process ID>`. Utilice 1–100 letras, dígitos, puntos, guiones o guiones bajos ASCII. |

Cuando se agotan los reemplazos automáticos, el diagnóstico nombra una tubería de recuperación local. El bot espera la intervención del operador mientras continúan los plazos normales del juego y del lobby. Para reiniciar un motor iniciado por el cliente, conéctese como el mismo usuario del sistema operativo y envíe UTF-8 `restart` seguido de LF. Por ejemplo, si configuró `pipe = "YourBot-recovery"`, ejecútelo en otra terminal después del diagnóstico de espera:

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

El ejemplo Linux requiere Python 3 y se conecta al socket de dominio Unix de .NET. Ejecútelo como el mismo usuario, con el mismo `TMPDIR` que el bot (el valor predeterminado es `/tmp`). Reemplace `YourBot-recovery` con el nombre de la tubería configurada; un servicio con un directorio temporal privado también necesita que el cliente se ejecute dentro de ese mismo entorno.

Un reemplazo exitoso del operador inicia un nuevo presupuesto de reintento automático. La edición del archivo TOML no cambia el ejecutable ni los argumentos del cliente en ejecución.

Para `--stdio`, un supervisor externo debe conectar un motor nuevo a través del tubo de recuperación dúplex y transmitir GTP en ambas direcciones. No hay ningún saludo `restart` en este modo. La conexión original stdin/stdout no se puede reutilizar después de una falla.

## Solución de problemas {#troubleshooting}

| Síntoma | Que comprobar |
| --- | --- |
| Error de configuración antes del arranque del motor. | Verifique el archivo con nombre y la ubicación de origen, la ortografía exacta de las claves, los nombres de las habitaciones entre comillas y los tipos de valores TOML. Los archivos de propiedades Java heredados necesitan conversión. |
| El motor no puede arrancar ni abrir su modelo. | Verifique las rutas del ejecutable y de los argumentos, los argumentos en modo GTP y el directorio de trabajo. Pruebe `--probe`. |
| Faltan comandos GTP o versión de protocolo incorrecta | Utilice un motor GTP v2 completo. El descubrimiento requiere `protocol_version`, `name`, `version`, `known_command`, `list_commands`, `quit`, `boardsize`, `clear_board`, `komi`, `play` y `genmove`. |
| La verificación de reglas, tiempo o puntuación falla | Verifique las capacidades del motor para el perfil seleccionado. Declare `engine.rules` solo cuando el motor carezca de `kgs-rules` y haga que su configuración real coincida. Todos los juegos automáticos requieren `final_status_list`. |
| El inicio de sesión falla | Verifique el nombre de la cuenta, `KGS_PASSWORD` en el entorno de inicio, la dirección del servidor y el motivo del rechazo informado. |
| No se encuentra la habitación | Copie su nombre completo de KGS en el servidor seleccionado. La coincidencia ignora las mayúsculas y minúsculas pero requiere el nombre completo. |
| Esperando el tiempo de espera de un juego o lobby | Verifique los términos coincidentes, la elegibilidad del oponente, el nombre de la sala y las preferencias de coincidencia automática. Aumente `timeouts.lobby` si se prevé una espera más larga. |
| Entrada Ranked rechazada | Verifique el permiso de ClasificadoRobot, el rango habilitado, la sala pública y las restricciones del perfil Ranked. |
| La puntuación se detiene ante un desacuerdo | Las disputas japonesas no tienen fundamento. La limpieza de China, AGA y Nueva Zelanda requiere `kgs-genmove_cleanup`; Las disputas repetidas, la falta de progreso y la caducidad de la limpieza detienen al cliente. |
| El bot se detiene después de una pausa o de la salida del oponente. | Revise el tiempo de espera de interacción relevante e inspeccione el juego inacabado antes de reiniciar. |
| Motor no disponible pero la cuenta aún está en línea | Inspeccione los diagnósticos del motor y el mensaje del tubo de recuperación. Los reintentos automáticos pueden agotarse; Los relojes de juego y las fechas límite aún corren. |
| Error en el archivo de identidad | Asegúrese de que se pueda escribir en la ubicación del estado configurado y que contenga el archivo de identidad generado por el cliente. |

Al informar un problema, incluya la versión del cliente, el nombre/versión del motor, la ID del juego si está disponible, la configuración relevante y los diagnósticos stderr. Omitir contraseñas.

---
layout: "localized"
title: "Actualice a Mobi desde el cliente Java GTP"
nav_title: "Migrar desde Java"
lang: "es"
page_key: "mobi/upgrade-guide"
section: "mobi"
nav_order: 2
permalink: "/es/gtp/upgrade-guide/"
source_revision: "c32ebab17d841776f058eab0acfe73c12237c6953d8b7f6ec6630c41d26de6f1"
---

Esta guía mueve un bot de `kgsGtp.jar` y su configuración Java `.properties` a Mobi y TOML. El archivo antiguo no se puede cargar directamente; no hay importador automático. Guárdelo como referencia mientras crea un nuevo archivo. Consulte la [guía del usuario]({% include page-url.html key='mobi/user-guide' %}) para conocer el funcionamiento normal y la referencia completa de configuración.

Esta guía cubre Windows y Linux. Expanda la sección de su sistema operativo para ver los comandos PowerShell o Bash. Ejecute los comandos desde el directorio del cliente extraído.

## Pasos de actualización {#upgrade-steps}

1. Finaliza o resuelve cualquier juego actual y luego detiene el cliente anterior y su motor.    Desactive su reinicio automático mientras intenta el reemplazo, para que ambos clientes no inicien sesión con la misma cuenta.
2. Extraiga el paquete puente Mobi GTP para su arquitectura Windows o Linux.    El paquete incluye el tiempo de ejecución .NET. Mantenga su motor, modelo y configuración del motor; estos permanecen separados del cliente.
3. Copie [bot.example.toml]({{ '/mobi/bot.example.toml' | relative_url }}) a `bot.toml`. Mueva la configuración usando las tablas a continuación. Ingrese la contraseña en `KGS_PASSWORD` y elija explícitamente el tipo de juego, la política de devolución y el recuento de juegos.
4. Sondee el motor con los siguientes comandos. Corrija los errores de descubrimiento del motor antes de iniciar sesión. Se ejecutan comprobaciones adicionales de capacidad del juego durante el inicio normal.
5. Ejecute un juego Free con `--games 1`. Verifique el inicio de sesión, la selección de oponente, los relojes, la puntuación y el diagnóstico `Series: completed game 1`.
6. Configure `games = 0` si desea una reproducción continua, luego actualice su iniciador o servicio para usar el nuevo ejecutable, la ruta de configuración, el entorno de contraseña y los registros.

Copie la plantilla, luego edite la cuenta, las rutas del motor y la configuración del juego:

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

Después de editar, verifique el descubrimiento del motor sin iniciar sesión:

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

Para volver al cliente anterior, primero detenga el nuevo cliente y el motor, inspeccione cualquier juego sin terminar y restaure su iniciador y archivo de propiedades originales. Guarde el archivo de identidad del nuevo cliente para devolverlo más tarde a Mobi.

## Cambios a revisar antes de cambiar {#changes-to-review-before-switching}

| Área | viejo cliente | Mobi |
| --- | --- | --- |
| Lanzamiento | `java -jar kgsGtp.jar bot.properties key=value` | `Kgs.Gtp --config bot.toml --option value`; El ejecutable Windows termina en `.exe`. |
| Configuración | Propiedades de Java, incluidos los escapes de Java | UTF-8 TOML con secciones con nombre, cadenas entre comillas, números, matrices y valores booleanos. Las claves desconocidas son errores. |
| Modo predeterminado | Automatch | No hay emparejamiento a menos que se seleccione `matchmaking.mode` o `--lobby`. |
| recuento de juegos | Sigue encontrando juegos | El valor predeterminado incorporado es un juego completo. Configure `games = 0` para reproducción continua; el ejemplo proporcionado ya hace esto. |
| Tipo de juego | Automatch podría permitir que Free y Ranked estén juntos | Seleccione `Free` (predeterminado) o `Ranked` exclusivamente. No hay ninguna configuración mixta ni alternativa. |
| Habitación | Nombre de la habitación | Nombre de la habitación, todavía una cadena; utilice `room = "English Room"`. La búsqueda ignora mayúsculas y minúsculas y requiere un nombre exacto. |
| Términos de juego personalizados | Los jugadores podrían proponer cambios. | Los términos configurados deben coincidir exactamente, incluidos colores, komi, discapacidad, visibilidad y control de tiempo. |
| Recuperaciones | Normalmente permitido en juegos Free, rechazado en Ranked | Ambas políticas integradas tienen el valor predeterminado `Never`. Configure `undo.free = "Allow"` para conservar el comportamiento habitual de Free. El ejemplo hace esto. |
| Hándicap Automatch | Podría permitir hasta nueve filas si el motor admitiera handicap. | `maxRankDifference` por defecto es `0`; elíjalo explícitamente, como máximo 9 para Free o 6 para Ranked. |
| Reintentos de conexión | `reconnect=t` permite continuar reintentando | Presupuesto de interrupción predeterminado de 180-segundo, retroceso exponencial con fluctuación y reinicio después de 60 segundos saludables. |
| Fallo del motor | No hay reinicio automático del motor desde `reconnect` | Presupuesto de reinicio automático separado; El agotamiento espera la recuperación del operador mientras continúan los plazos normales. |
| Salida del oponente | Podría volver al emparejamiento después de su límite de ausencias | El nuevo cliente se detiene con un diagnóstico de juego inacabado cuando expira la espera configurada. |

El ejemplo es una configuración inicial, no una afirmación de que se conserva todo el comportamiento anterior. En particular, decida si esta cuenta debe jugar Free o Ranked antes de habilitar la operación continua.

## Mapear la configuración anterior {#map-the-old-settings}

Los nuevos nombres de configuración que aparecen a continuación utilizan la notación `section.key`. Por ejemplo, `account.username` significa `username = "YourBot"` en `[account]`.

### Cuenta, conexión y motor {#account-connection-and-engine}

| Propiedad antigua | Nueva configuración | Notas de migración |
| --- | --- | --- |
| `name` | `account.username` / `--username` | `KGS_USERNAME` también se admite cuando no se configura ningún nombre de usuario. |
| `password` | Variable de entorno `KGS_PASSWORD` | Elimínelo de la nueva configuración; Los campos de contraseña y las opciones CLI de contraseña no son compatibles. |
| `server.host` | `server.host` / `--host` | Cadena; predeterminado `goserver.gokgs.com`. |
| `server.port` | `server.port` / `--port` | Entero; predeterminado `2379`. |
| `reconnect=f` | `connectionRecovery.attempts = 0` | Deshabilita los reintentos de transporte KGS; La recuperación del motor se configura por separado. |
| `reconnect=t` | `[connectionRecovery]` | Elija un presupuesto de tiempo por interrupción; el valor predeterminado es 180 segundos. Un límite de intentos es opcional. |
| `engine` | `engine.executable` y `engine.arguments` | Divida el comando en argumentos ejecutables e individuales; vea abajo. |
| Sin propiedades de conexión del motor | `engine.stdio = true` / `--stdio` | La E/S estándar ahora debe seleccionarse explícitamente. |
| `gtp.in`, `gtp.out` | Sin configuración directa | Un lanzador externo puede conectar las dos direcciones a través de `--stdio`. El cliente no abre archivos con nombre ni FIFO desde la configuración. |
| `engine.port` | Sin configuración directa | No hay ningún escucha TCP del motor. Utilice un adaptador externo con `--stdio` o deje que el cliente inicie el motor. |
| `logFile` | Capturar stderr externamente | Utilice la redirección de shell o un administrador de servicios; La rotación y el nombre de los registros Java integrados no se transfieren. |
| `verbose` | Sin configuración directa | Los diagnósticos normales van a stderr; no existe un conmutador de registro de tráfico de servidor/GTP completo equivalente. |

El `engineRecovery.pipe` local sirve para reemplazar un motor fallido en una sesión en ejecución. No reemplaza las antiguas configuraciones de inicio `engine.port`, `gtp.in` o `gtp.out`.

### Configuración de emparejamiento y juego {#matchmaking-and-game-settings}

| Propiedad antigua | Nueva configuración | Notas de migración |
| --- | --- | --- |
| `mode=auto` | `matchmaking.mode = "Automatch"` | Omita la sala, la configuración personalizada del oponente y las secciones `game`/`timing`. |
| `mode=custom` | `matchmaking.mode = "Offer"` | Agregue `opponentPolicy = "Any"` para desafíos abiertos, o `"Named"` más `opponent`. |
| `mode=wait` | `matchmaking.mode = "Join"` | Establezca el nombre de la habitación y `opponent`; el perfil ofrecido debe coincidir exactamente. |
| `mode=both` | Sin modo combinado | Elija Automatch, Offer o Join para esta invocación. |
| `mode=tournament` | No compatible | La entrada al torneo no está implementada; conservar el cliente anterior si es necesario. |
| `room` | `matchmaking.room` / `--room` | Conserve el nombre de la habitación como una cadena entrecomillada. Requerido para Offer y Join; omitir para Automatch. No existe un valor predeterminado de última habitación utilizada. |
| `opponent` | `matchmaking.opponent` | Para desafíos personalizados, utilice `opponentPolicy = "Named"`. Omita ambas configuraciones de oponente personalizadas para Automatch. |
| `gameNotes` | `matchmaking.challengeNotes` | Solo Offer; como máximo caracteres 255 sin caracteres de control. |
| `rules` | `game.rules` | Utilice `Japanese`, `Chinese`, `Aga` o `NewZealand`. Establece términos de juego personalizados exactos. |
| `komi` | `game.komi` | Número, no una cadena entre comillas; establecidos explícitamente, incluso para juegos con handicap. |
| `rules.boardSize` | `game.boardSize` | Entero. Establecer explícitamente: el nuevo valor predeterminado del juego personalizado es 9. |
| `rules.time` | `[timing]` | Divida en campos de sistema, segundos y tiempo adicional usando los ejemplos siguientes. |
| `automatch.speed` | `automatch.speed` | Por ejemplo `speed = ["Blitz", "Medium"]` o `"All"`. Las combinaciones CLI utilizan comas. |
| `automatch.rank` | `automatch.rank` | Citado desde `30k` hasta `1k`; Todavía es necesario cuando no hay una clasificación de servidor numérica. |
| `undo=f` | `[undo]` con `free = "Never"`, `ranked = "Never"` | Estos también son los valores predeterminados integrados. |
| `undo=t` u omitido | `[undo]` con `free = "Allow"`, `ranked = "Never"` | Conserva la antigua distinción habitual Free/Ranked. Las nuevas recuperaciones Ranked se pueden habilitar por separado si se desea. |
| `talk` | No compatible | Las respuestas de chat privado y el reenvío de chat del motor no están implementados. |
| `hint.cleanup`, `hint.noArguing` | No compatible | No hay sugerencias de chat configurables para disputas de puntuación. |

`game.rules` y `engine.rules` tienen diferentes propósitos. El primero elige las reglas del juego personalizado. Este último declara reglas ya configuradas en un motor que carece de `kgs-rules`; no cambia la configuración de ese motor.

### Dividir el comando del motor {#split-the-engine-command}

Una propiedad antigua podría ser:

```properties
engine=/opt/katago/katago gtp -config /srv/go/gtp.cfg -model /srv/go/model.bin.gz
```

La nueva configuración es:

```toml
[engine]
executable = "/opt/katago/katago"
arguments = ["gtp", "-config", "/srv/go/gtp.cfg", "-model", "/srv/go/model.bin.gz"]
```

No coloque una línea de comando completa en `executable`. No hay evaluación de shell. Cada argumento es un elemento de matriz, incluidas las rutas que contienen espacios. Para Windows, las cadenas TOML entre comillas simples mantienen barras invertidas literales:

```toml
[engine]
executable = 'C:\Go Engines\katago.exe'
arguments = ["gtp", "-config", 'C:\Go Engines\gtp.cfg', "-model", 'C:\Go Engines\model.bin.gz']
```

Reemplace los escapes de propiedades de Java con el texto real en UTF-8 TOML. Las rutas ejecutables relativas que contienen un separador se resuelven desde el directorio TOML; Las rutas de argumentos permanecen relativas al directorio de trabajo de inicio. El modelo absoluto y las rutas de configuración hacen que los lanzamientos de servicios sean más fáciles de reproducir.

### Convertir controles de tiempo {#convert-time-controls}

Utilice sólo una de estas secciones `[timing]` y sólo con Offer o Join.

Antiguo `rules.time=0`:

```toml
[timing]
system = "None"
mainTime = 0
```

Antiguo `rules.time=30:00`:

```toml
[timing]
system = "Absolute"
mainTime = 1800
```

Antiguo `rules.time=30:00+5x0:30`:

```toml
[timing]
system = "ByoYomi"
mainTime = 1800
byoYomiTime = 30
byoYomiPeriods = 5
```

Antiguo `rules.time=30:00+25/10:00`:

```toml
[timing]
system = "Canadian"
mainTime = 1800
byoYomiTime = 600
canadianStones = 25
```

Todos los valores de tiempo nuevos son segundos enteros. Elimine los campos de tiempo adicional que pertenecen a un sistema diferente. El tiempo adicional japonés requiere el comando `kgs-time_settings` del motor; no se aproxima utilizando otro sistema de reloj.

## Ejemplo: migrar un bot de coincidencia automática {#example-migrate-an-automatch-bot}

Supongamos que las partes relevantes del archivo antiguo son:

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

Crea este `bot.toml` para un juego Free inicial. Automatch no toma una configuración de habitación, por lo que se omite la antigua propiedad `room`:

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

Para Windows, reemplace las rutas de `[engine]` con el ejemplo de Windows en [Dividir el comando del motor](#split-the-engine-command). Establece la contraseña y ejecuta un juego:

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

Este ejemplo selecciona deliberadamente incluso juegos Free. Para mantener la coincidencia de handicap, seleccione un `maxRankDifference` adecuado y verifique el soporte del motor. Para jugar Ranked, seleccione `gameType = "Ranked"`, verifique el permiso de ClasificadoRobot de la cuenta y el rango habilitado, y use como máximo seis rangos de diferencia. Una invocación no puede aceptar ambos tipos de juego.

Para un bot personalizado, utilice el [ejemplo de desafío personalizado]({% include page-url.html key='mobi/user-guide' %}#custom-challenges), copie el nombre de la sala anterior y transfiera explícitamente el tamaño del tablero, las reglas, el komi, el color, el hándicap y la configuración de tiempo convertida.

## Compatibilidad del motor y funcionamiento sin supervisión {#engine-compatibility-and-unattended-operation}

Mobi requiere GTP v2 y su conjunto de comandos obligatorio completo. Aquí se requieren algunos comandos que el cliente anterior consideraba opcionales. Todos los juegos automáticos también requieren `final_status_list`. Los juegos cronometrados necesitan `time_left` y un comando de cronometraje compatible. Consulte los requisitos del motor de la guía del usuario para su perfil seleccionado; una configuración antigua que funcione por sí sola no establece la compatibilidad.

Se apoya el acuerdo de puntuación japonés ordinario, pero las disputas japonesas no resueltas detienen el juego. La limpieza de China, AGA y Nueva Zelanda requiere `kgs-genmove_cleanup` y tiene intentos limitados y una fecha límite total. No existe un respaldo del cliente antiguo que permita a un oponente decidir todas las piedras muertas cuando la puntuación automática no está disponible.

Revise estas configuraciones de servicio antes de dejar el bot desatendido:

- Configure `games = 0` explícitamente si debe seguir reproduciéndose. Cada intento de lobby todavía tiene una fecha límite predeterminada de segundo 300; aumente `timeouts.lobby` si es necesario.
- Configure los reintentos de conexión KGS y los reinicios del motor por separado. La recuperación de KGS tiene como valor predeterminado 180 segundos por interrupción y se restablece después de 60 segundos saludables. La recuperación del motor permite tres reemplazos automáticos durante la invocación; El agotamiento puede dejar una sesión KGS en vivo esperando la recuperación del operador.
- Elija límites de pausa, aplazamiento y ausencia del oponente. Cada uno tiene como valor predeterminado 300 segundos; La caducidad detiene al cliente sin contar o renunciar al juego inacabado.
- Conserve el archivo de identidad del cliente en un directorio de estado grabable. Un proceso nuevo no descubre automáticamente juegos de combinación automática más antiguos.
- Capture stderr y organice la retención de registros externos. Salir 0 significa finalización normal, 1 indica falla y 130 indica cancelación.

La [guía del usuario]({% include page-url.html key='mobi/user-guide' %}#timeouts-and-recovery) describe en detalle la configuración del tiempo de espera, la recuperación de la conexión y la recuperación del motor del operador.

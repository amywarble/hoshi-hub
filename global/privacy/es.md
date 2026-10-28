---
source_revision: "6557edaea14029268590a7f73220e26c62aafda65681a4c44da3dd659e4b7ca7"
layout: "localized"
title: "Política de privacidad"
lang: "es"
page_key: "global/privacy"
section: "global"
nav_order: 3
permalink: "/es/privacy/"
redirect_from: "/es/desktop/privacy/"
---

_Vigente desde: 27 de octubre de 2026_

Esta política cubre Pocket KGS para Android, KGS Nova para Windows, macOS y Linux, Mobi para Windows y Linux y este sitio de soporte. Los tres clientes cuentan con el respaldo oficial de KGS y de la American Go Association (AGA). Primero se describen las prácticas comunes y después el almacenamiento y los controles de cada aplicación.

## Quién trata sus datos

Los clientes se conectan directamente al KGS Go Server. El desarrollador no opera los servidores de KGS ni controla sus cuentas, moderación, registros o conservación de datos. KGS es un servicio independiente con sus propias [condiciones y política de privacidad](https://www.gokgs.com/tos.jsp).

Los clientes no incluyen publicidad, análisis de uso ni envío automático de informes de fallos. El desarrollador no vende sus datos personales ni los usa para publicidad dirigida o seguimiento entre aplicaciones, y no mantiene una copia independiente en servidores de su cuenta de KGS, chats, partidas, avatares o audio de profesores.

## Información tratada y finalidades

Según el cliente y las funciones utilizadas, la información incluye:

- **Cuentas y perfiles:** credenciales de KGS, correo electrónico, texto del perfil, avatar, rango, estado de la cuenta y preferencias.
- **Comunicaciones e información social:** chat de salas y partidas, mensajes privados y sin conexión, listas de amigos, seguidores y usuarios censurados con notas y otros contenidos de KGS.
- **Partidas y actividad:** jugadas, registros, comentarios, resultados, desafíos, pertenencia a salas y ajustes de emparejamiento. Mobi intercambia información de las partidas con el motor de Go que configure para generar jugadas y gestionar partidas.
- **Conexión:** identificador persistente del cliente KGS, versiones de aplicación y protocolo, idioma, sistema operativo y arquitectura, información del entorno de ejecución y estado de conexión. KGS recibe su dirección IP al conectarse.
- **Ajustes locales y diagnósticos:** preferencias, contenido en caché y diagnósticos descritos en los apartados de cada aplicación.

Esta información permite iniciar sesión, mantener sesiones de KGS, mostrar contenido, enviar acciones solicitadas o acciones configuradas del bot a KGS, recordar ajustes y diagnosticar problemas cuando decide compartir detalles.

Pocket KGS y Nova también tratan audio del micrófono cuando un profesor autorizado inicia expresamente una emisión en directo, y reproducen el audio recibido. La emisión termina cuando usted la detiene o finaliza la sesión correspondiente. Ninguno crea una grabación independiente para el desarrollador. Mobi no ofrece controles de audio de profesores.

## Destinatarios de la información

- **KGS:** recibe información de cuenta y conexión, comunicaciones, actividad de juego y cambios solicitados. Otros usuarios ven el contenido según la función utilizada de KGS.
- **Proveedores de credenciales y motores:** los proveedores de la plataforma y el motor elegido para Mobi tratan información como se indica abajo, conforme a sus propias condiciones.
- **GitHub:** aloja este sitio y el gestor público de incidencias bajo la [Declaración de privacidad de GitHub](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Las incidencias públicas y sus adjuntos son visibles para todos. La función de informes de Nova abre un borrador editable en el navegador con versión de la aplicación, sistema operativo, arquitectura y entorno de ejecución; no envía la incidencia ni adjunta registros automáticamente.
- **Necesidades legales y de seguridad:** la información que entregue al desarrollador puede conservarse o divulgarse cuando sea razonablemente necesario para cumplir la ley, investigar abusos, proteger a los usuarios o proteger derechos y seguridad.

## Comunicaciones y seguridad

La conexión heredada de KGS usada por estos clientes no ofrece TLS ni cifrado de extremo a extremo. El protocolo de inicio de sesión transforma la contraseña antes de transmitirla, pero alguien con acceso a la ruta de red podría observar o modificar otro tráfico. Use una red de confianza.

KGS declara que todas las conversaciones se registran y que sus administradores pueden revisarlas al investigar denuncias. No comparta en KGS información que deba ser privada. KGS controla la conservación en el servidor y las partidas pueden permanecer en sus archivos.

## Almacenamiento y opciones de cada aplicación

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

Pocket guarda preferencias, opciones de notificación y su identificador de cliente KGS en el almacenamiento privado de Android, y avatares en la caché. Android puede eliminar archivos de caché. Pocket solicita que Android no haga copias de seguridad de sus datos privados. Borrar el almacenamiento o desinstalar elimina esos datos locales.

Si decide guardar credenciales, Android Credential Manager y el proveedor seleccionado las gestionan con sus propias condiciones. Pocket no recibe los datos biométricos usados para desbloquearlas. Puede ser necesario eliminar por separado las credenciales guardadas por el proveedor.

Los diagnósticos de errores de producción se escriben en el registro del sistema Android. El registro diagnóstico opcional añade detalles durante la sesión actual. Los registros de publicación conservan versiones, plantillas de eventos, tipos de excepción y trazas de pila, con un formato diseñado para omitir valores de argumentos en ejecución, mensajes de excepción y rutas de archivos fuente. Android, un administrador del dispositivo o quien reciba sus registros podría acceder a ellos.

Puede usar una sesión de invitado, decidir si guarda credenciales, desactivar notificaciones en Pocket o Android, denegar acceso al micrófono, no emitir audio y censurar usuarios para bloquear interacciones compatibles y ocultar su contenido.

### KGS Nova

- **Base de datos:** `data.db`, en la carpeta local de datos de KGS Nova del sistema (`%LOCALAPPDATA%\KGS Nova` en Windows), contiene metadatos de cuentas guardadas, identificador del cliente, preferencias y estado. La base completa no está cifrada.
- **Contraseñas:** Windows protege las contraseñas de la base mediante DPAPI para el usuario actual. macOS usa Keychain y Linux, Secret Service. El sistema puede pedir desbloqueo o permiso. Esto no cifra el resto de la base.
- **Diagnósticos:** los errores de publicación van a `client.log` y archivos rotatorios `client.archive*.log` en la misma carpeta. Los diagnósticos opcionales de sesión son más detallados. Los registros de publicación siguen las mismas omisiones descritas para Pocket. Las compilaciones de desarrollo pueden producir `logs.txt` y salida de consola o depuración más detallados.
- **Otros archivos:** la misma carpeta contiene el espacio `sgf`, archivos de recuperación y copias de seguridad, y motores/modelos de `analysis`. Las partidas exportadas y otros archivos permanecen donde los guarde.

Personas o programas con acceso a sus archivos o cuenta del sistema pueden leerlos. Desinstalar o sustituir Nova no elimina necesariamente la base, registros, exportaciones ni entradas del llavero. Puede usar sesiones de invitado, elegir si recuerda credenciales, controlar interacciones privadas compatibles, censurar usuarios, evitar emisiones del micrófono y eliminar datos locales.

### Mobi

Mobi requiere una cuenta registrada de KGS. Lee la contraseña de `KGS_PASSWORD` y no la guarda por sí mismo. Los scripts de inicio, ajustes del entorno y gestores de servicios pueden conservar las credenciales que coloque allí. Protéjalos y proteja su cuenta del sistema; un motor iniciado puede heredar su entorno.

Su configuración TOML puede contener el nombre de cuenta, servidor, rutas del motor y ajustes de juego. Mobi guarda el identificador del cliente KGS en un archivo local. El emparejamiento usa por defecto `Kgs.Gtp/identities/<server-and-account-hash>` en la carpeta local de datos de .NET (`%LOCALAPPDATA%` en Windows); sin emparejamiento, el valor predeterminado es `Kgs.Gtp/client-id`. `account.clientIdFile` o `--client-id-file` permiten cambiar la ubicación.

Estado, errores y diagnósticos del motor se envían a stderr. Los registros se conservan si redirige la salida o si los retiene un gestor de servicios. No siguen las reglas de omisión de Pocket/Nova y pueden contener usuarios, detalles de partidas, rutas o salida del motor. Revíselos antes de compartirlos. El motor puede generar registros, partidas u otros archivos adicionales y tener su propio comportamiento de red; revise su documentación y prácticas de privacidad por separado. Mobi no sube diagnósticos automáticamente al desarrollador.

Usted controla el motor, configuración, salida conservada y archivos locales. Consulte la [guía de Mobi]({% include page-url.html key='mobi/user-guide' %}) para funcionamiento y diagnósticos.

## Conservación, eliminación y otras opciones

El desarrollador no recibe automáticamente archivos locales ni diagnósticos. Las copias enviadas voluntariamente pueden conservarse para atender su solicitud o por necesidades legales y de seguridad. Las incidencias públicas de GitHub y su historial permanecen hasta que se editen o eliminen según las funciones y políticas de GitHub.

Puede elegir qué información de perfil comparte y marcar su correo de KGS como privado cuando se permita. Borrar archivos o desinstalar un cliente no elimina los datos alojados por KGS. Sus administradores gestionan la eliminación de cuentas y datos del servidor. Consulte [Eliminación de cuentas y datos]({% include page-url.html key='global/account-and-data-deletion' %}) para el proceso común y la eliminación local de cada cliente.

Pocket KGS no está dirigido a menores de 13 años. KGS es un servicio público de comunicación; un progenitor o tutor debe revisar sus condiciones e idoneidad antes de que lo use un menor. No publique datos personales de menores en incidencias públicas.

## Cambios y contacto

Mantenga actualizados el sistema y el cliente, use una contraseña exclusiva para KGS y revise los registros antes de compartirlos. Ningún sistema es totalmente seguro. Informe de vulnerabilidades mediante la [Política de seguridad]({% include page-url.html key='global/security-policy' %}).

Esta política puede cambiar con los clientes; la fecha de vigencia identifica la revisión publicada. Para soporte no confidencial use el [gestor público de incidencias](https://github.com/amywarble/hoshi-hub/issues/new/choose). Para consultas privadas sobre aplicaciones o privacidad, escriba a [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). Para cuentas de KGS, datos del servidor o moderación, a [admin@gokgs.com](mailto:admin@gokgs.com).

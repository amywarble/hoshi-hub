---
source_revision: "d6af0143a1e9eaabd1ffd1cb7c13389da26853a7ce6ab3ca381060ce302d9ad0"
layout: localized
title: "Política de privacidad"
lang: "es"
page_key: "android/privacy"
section: "android"
nav_order: 4
permalink: "/es/privacy/"
---

_En vigor: 23 de septiembre de 2026_

Pocket KGS es un cliente Android independiente del KGS Go Server («KGS»), sin afiliación ni respaldo de KGS. Esta política explica qué información trata, para qué, adónde se envía y sus opciones. Cubre Pocket KGS y este sitio de ayuda. KGS es un servicio separado con sus propias [condiciones de servicio y privacidad](https://www.gokgs.com/tos.jsp).

## Quién trata los datos

La aplicación se conecta directamente a KGS. El desarrollador proporciona el cliente, pero no opera los servidores KGS ni controla sus registros, moderación o conservación. Pocket KGS no incluye publicidad, análisis de uso ni informes automáticos de fallos. El desarrollador no vende sus datos personales.

## Información tratada

Según las funciones utilizadas:

- **Cuenta y perfil:** usuario KGS, contraseña, correo, texto del perfil, avatar, rango, estado de cuenta y preferencias del perfil.
- **Comunicaciones y contenido:** chats públicos de salas y partidas, mensajes privados y sin conexión, registros y anotaciones de partidas, desafíos y otros contenidos enviados o recibidos de KGS.
- **Audio:** micrófono cuando un profesor autorizado inicia expresamente una emisión de audio docente. Pocket KGS envía el audio en directo mediante KGS a los participantes de la partida. Termina cuando usted lo detiene o finaliza la sesión; no crea una grabación separada para el desarrollador.
- **Información social:** listas de amigos, seguidores y usuarios censurados, con sus notas.
- **Juego y actividad:** partidas jugadas u observadas, movimientos, resultados, preferencias, pertenencia a salas, desafíos e interacciones con KGS.
- **Dispositivo y conexión:** identificador KGS persistente del cliente, versiones de aplicación/protocolo, idioma/región, sistema operativo y versión, arquitectura del procesador, proveedor/versión del entorno de ejecución, estado de red y datos necesarios para conectarse. KGS recibe necesariamente su dirección IP.
- **Notificaciones:** preferencias locales sobre qué eventos KGS pueden generar notificaciones Android.
- **Caché local:** avatares y preferencias para el funcionamiento eficiente de la aplicación.
- **Diagnóstico:** las versiones de producción escriben información limitada en el registro del sistema Android. El registro de la capa de protocolo KGS está desactivado en las versiones publicadas; los registros de producción están diseñados para no contener eventos del protocolo ni cargas de mensajes. Se limitan a eventos informativos Android/interfaz y avisos o errores de las capas interfaz/cliente. Pueden incluir usuario KGS, identificadores de sala/partida/canal, acciones, estado Android y excepciones pertinentes a un fallo. No se suben automáticamente al desarrollador. Android, el administrador del dispositivo o quien reciba voluntariamente un registro pueden acceder a ellos.

## Uso de la información

Se usa para iniciar y mantener la sesión; actualizar su perfil existente cuando lo solicita; mostrar salas, usuarios, partidas, perfiles, mensajes y otros contenidos; enviar movimientos, mensajes, cambios de perfil, avatar, audio y acciones solicitadas; recordar ajustes, identificador y preferencias de notificación en el dispositivo; mostrar notificaciones activadas; y diagnosticar errores cuando usted comparte detalles voluntariamente. No hay publicidad dirigida ni seguimiento entre aplicaciones.

## Destinatarios

Solo se comunica información según sea necesario para:

- **KGS:** datos de cuenta, comunicaciones, actividad, perfil, audio docente, dispositivo/entorno, identificador y conexión para prestar el servicio. Otros usuarios ven lo que la función de KGS hace público o comparte con ellos.
- **Proveedores de credenciales Android:** si elige guardar contraseñas, Android Credential Manager y el proveedor seleccionado tratan usuario y contraseña según sus propias políticas. Pocket KGS no recibe los datos biométricos de desbloqueo.
- **GitHub:** aloja el sitio y las incidencias públicas. Los envíos se rigen por su [declaración de privacidad](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement); las incidencias públicas son visibles para todos.
- **Necesidades legales y de seguridad:** la información recibida por el desarrollador puede conservarse o divulgarse cuando sea razonablemente necesario para cumplir la ley, proteger usuarios, investigar abusos o proteger derechos y seguridad de la aplicación y de otros.

## Comunicaciones y transporte

KGS afirma que todas las conversaciones se registran y pueden ser revisadas por administradores al investigar denuncias. No use el chat para información que deba permanecer privada.

El protocolo antiguo KGS no ofrece una conexión moderna protegida con TLS. El protocolo de inicio de sesión transforma la contraseña antes de transmitirla, pero el resto del tráfico no tiene TLS ni cifrado de extremo a extremo. Quien observe o interfiera en la ruta de red podría leer o modificar el tráfico. Evite redes no fiables.

## Almacenamiento y conservación

Identificador y preferencias están en el almacenamiento privado de la aplicación; los avatares en la caché Android, que puede borrarse por falta de espacio. Borrar los datos o desinstalar elimina los datos privados de Pocket KGS. Las credenciales guardadas con Android Credential Manager pueden requerir eliminación separada en el gestor de contraseñas.

El desarrollador no guarda una copia separada en servidores de su cuenta, chats, partidas, avatar o audio. KGS controla su conservación, declara registrar las conversaciones y puede mantener partidas en sus archivos.

Para eliminar cuenta y datos del servidor asociados, escriba a [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) con usuario y correo de la cuenta, nunca contraseña. Un administrador puede verificar la titularidad y tramitará la solicitud. Consulte [Eliminación de cuentas y datos]({% include page-url.html key='android/account-and-data-deletion' %}) para instrucciones completas, incluida la eliminación local. Las incidencias públicas y su historial permanecen en GitHub hasta que se editen o eliminen según sus funciones y políticas.

## Sus opciones

Puede usar una sesión de invitado en vez de crear una cuenta en la web KGS; decidir si guarda contraseña; marcar su correo KGS como privado cuando exista esa opción; elegir avatar y cambios de perfil; denegar micrófono y no emitir audio docente; desactivar notificaciones en la aplicación o Android; censurar usuarios para bloquear interacciones y ocultar contenido compatibles; borrar datos locales o desinstalar; y seguir las [instrucciones de eliminación]({% include page-url.html key='android/account-and-data-deletion' %}).

## Menores

Pocket KGS no está dirigido a menores de 13 años. KGS es un servicio público de comunicación. Padres o tutores deben revisar sus condiciones y decidir si es adecuado antes de permitir su uso a un menor. No publique datos personales de menores en incidencias públicas.

## Seguridad

Ningún sistema es totalmente seguro. Actualice dispositivo y aplicación, use una contraseña KGS única y no publique credenciales o contenido privado en las incidencias. Para vulnerabilidades, consulte la [política de seguridad]({% include page-url.html key='global/security-policy' %}).

## Cambios

La política puede cambiar con Pocket KGS. La fecha se actualizará al publicar cambios importantes. Seguir usando la aplicación tras un cambio implica aplicar la política revisada al uso posterior.

## Contacto

Consultas generales sin datos personales o sensibles: [incidencias públicas](https://github.com/amywarble/hoshi-hub/issues/new/choose). Consultas privadas de aplicación, privacidad o seguridad sensible: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). Cuentas, datos del servidor, moderación o servicio KGS: [admin@gokgs.com](mailto:admin@gokgs.com).

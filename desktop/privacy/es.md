---
source_revision: "c0720ca8cede62afb75cc2d2bb2188cb6f42790a1a5ec1c815ee03a2934d2d54"
layout: localized
title: "Política de privacidad"
lang: "es"
page_key: "desktop/privacy"
section: "desktop"
nav_order: 10
permalink: "/es/desktop/privacy/"
---

_En vigor: 10 de octubre de 2026_

Esta política cubre KGS Nova para Windows, macOS y Linux, cliente independiente sin afiliación ni respaldo de KGS. KGS es un servicio separado con sus propias [condiciones y privacidad](https://www.gokgs.com/tos.jsp).

## Información tratada

Conexión directa con KGS. Según las funciones, trata credenciales y perfil, salas, chats y mensajes privados/sin conexión, listas sociales y notas, registros de partidas y movimientos, desafíos, avatares y preferencias. Envía acciones solicitadas y muestra respuestas KGS. Los demás ven contenido conforme a la función KGS usada.

KGS recibe identificador persistente del cliente, versión del protocolo, idioma/región, sistema, arquitectura, entorno de ejecución y dirección de red de conexión.

Si un profesor autorizado inicia una emisión, se envía audio del micrófono mediante KGS a los participantes. La recepción reproduce audio KGS. Emitir termina cuando usted lo detiene o acaba la sesión. No se crea grabación separada para el desarrollador.

Sin publicidad, análisis ni subidas automáticas de fallos. El desarrollador no conserva copia separada en servidores de cuenta, mensajes, partidas o audio.

## Almacenamiento y diagnóstico

- **Base de datos:** `data.db` en el directorio de trabajo guarda metadatos de cuentas recordadas, identificador, preferencias y estado. No está cifrada en su totalidad.
- **Contraseñas:** Windows las cifra en la base con DPAPI para el usuario actual; macOS usa el Llavero y Linux Secret Service. Puede requerirse desbloqueo o permiso del sistema. Esta protección no cifra el resto de la base.
- **Registros:** `logs.txt` en el directorio de la aplicación y salida de consola/depuración. El archivo se reemplaza al iniciar. Puede contener versiones, sistema, usuarios, identificadores de sala/partida, acciones, excepciones y datos del protocolo si falla una conexión o mensaje. No presuponga ausencia de datos personales. No se suben automáticamente.
- **Exportaciones:** partidas y otros archivos guardados expresamente permanecen en la ubicación elegida.

Personas o programas con acceso a los archivos o cuenta del sistema podrían leerlos. Desinstalar o reemplazar no elimina necesariamente base, registros, exportaciones ni entradas del llavero. Consulte [eliminación de datos]({% include page-url.html key='desktop/account-and-data-deletion' %}).

## Comunicaciones y terceros

La conexión antigua no usa TLS ni cifrado de extremo a extremo. Transformar la contraseña antes de transmitirla no protege todo el tráfico ante observación o manipulación. Use una red fiable.

KGS declara registrar conversaciones y permitir su revisión por administradores. No comparta información que deba ser privada. KGS controla moderación y conservación del servidor.

GitHub aloja ayuda e incidencias según su [declaración de privacidad](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Los enlaces abren el navegador. Notificar un error abre un borrador editable con versión, sistema, arquitectura y entorno. No envía la incidencia ni adjunta registros automáticamente. Incidencias públicas enviadas y adjuntos son públicos.

## Opciones y contacto

Puede usar sesión invitada, decidir si recuerda credenciales, limitar interacciones privadas compatibles, censurar usuarios, evitar emisiones del micrófono y eliminar archivos locales. KGS administra la eliminación de cuentas: [instrucciones]({% include page-url.html key='desktop/account-and-data-deletion' %}).

No publique datos personales infantiles. Padres o tutores deben revisar condiciones y funciones de comunicación KGS antes de permitir el uso a menores.

Consultas privadas de aplicación/privacidad: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). Cuenta y datos KGS: [admin@gokgs.com](mailto:admin@gokgs.com). Vulnerabilidades: [notificación privada](https://github.com/amywarble/hoshi-hub/security/advisories/new).

Esta política se actualizará con el comportamiento del cliente; la fecha identifica la revisión.

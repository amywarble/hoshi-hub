---
source_revision: "2dd2b5f3a829514cb3f4e94bc67cffcd8f04dad8b5b984ffab73449fda82c3c7"
layout: "localized"
title: "Eliminación de cuentas y datos"
lang: "es"
page_key: "global/account-and-data-deletion"
section: "global"
nav_order: 2
permalink: "/es/account-and-data-deletion/"
redirect_from: "/es/desktop/account-and-data-deletion/"
---

_Última actualización: 27 de octubre de 2026_

Pocket KGS, KGS Nova y Mobi inician sesión en cuentas alojadas y controladas por KGS Go Server. Ninguno de estos clientes tiene un sistema de cuentas independiente. KGS gestiona la creación de cuentas en su [página oficial de registro](https://www.gokgs.com/register/index.html).

Borrar datos locales o desinstalar **no** elimina cuenta KGS, mensajes, partidas, perfil ni otros datos de KGS.

## Eliminar cuenta y datos del servidor KGS

1. Escriba a [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request), asunto `KGS account deletion request`.
2. Solicite expresamente borrar la cuenta y sus datos del servidor asociados.
3. Incluya usuario y correo de la cuenta. **Nunca envíe su contraseña.**

Un administrador puede verificar la titularidad, tramitará la solicitud y explicará plazo y posibles retenciones por seguridad, integridad del servicio o motivos legales. La eliminación se hace tras recibir y verificar la solicitud; no ocurre automáticamente al desinstalar o borrar almacenamiento.

No publique datos de su cuenta en incidencias públicas de GitHub.

## Borrar datos locales

- [Pocket KGS · Android](#pocket-kgs)
- [KGS Nova · Windows, macOS, Linux](#kgs-nova)
- [Mobi · Windows, Linux](#mobi)

### Pocket KGS

1. Abra **Ajustes** de Android.
2. Elija **Aplicaciones** y **Pocket KGS**.
3. Abra **Almacenamiento y caché**.
4. Pulse **Borrar almacenamiento** (el nombre puede variar) o desinstale.

Se eliminan preferencias, identificador local del cliente KGS y avatares en caché. Pocket KGS pide a Android no hacer copias de seguridad de sus datos privados.

Elimine aparte las contraseñas guardadas mediante Android Credential Manager en el gestor/proveedor elegido; borrar los datos no elimina necesariamente su copia.

### KGS Nova

Cierre KGS Nova y haga copia de las partidas exportadas que quiera conservar.

- Borre `data.db` y cualquier diario `data-log.db` de la carpeta KGS Nova de datos locales de aplicaciones (`%LOCALAPPDATA%\KGS Nova` en Windows) para eliminar metadatos de cuentas, preferencias, identificador y estado.
- Para borrar diagnósticos, elimine `client.log`, `client.archive*.log` y cualquier `logs.txt` de desarrollo de la misma carpeta. Las copias guardadas en otros sitios permanecen allí.
- En Windows, las contraseñas protegidas con DPAPI están en `data.db` y se eliminan con él. En macOS/Linux, borre aparte las entradas de Llavero/Secret Service del servicio `io.github.amywarble.kgsnet.desktop.credentials` y su usuario KGS. Borrar la base no elimina esas entradas nativas.
- Borre partidas exportadas, capturas y otros archivos no deseados de sus ubicaciones elegidas.

La carpeta contiene también el espacio `sgf`, recuperación y copias de seguridad, y los archivos de motores/modelos de `analysis`. Guarde las partidas recuperadas que quiera conservar antes de borrar esas carpetas. Borrar toda la carpeta de datos KGS Nova elimina conjuntamente estos datos locales.

Versiones antiguas usaban `data.db`, `data-log.db` y `logs.txt` en el directorio de la aplicación o de inicio. Una actualización puede dejar esas copias. Tras guardar lo necesario, elimínelas también; de lo contrario, una base antigua puede volver a importarse si falta la actual.

Desinstalar no elimina necesariamente archivos ni credenciales nativas.

### Mobi

Detenga Mobi y su motor y desactive los servicios o tareas programadas que reinicien el bot. Guarde las partidas o la configuración que quiera conservar.

- Elimine el archivo de identidad elegido mediante `account.clientIdFile` o `--client-id-file`. Sin una ruta personalizada, el emparejamiento usa `Kgs.Gtp/identities/<server-and-account-hash>` en el directorio local de datos de .NET (`%LOCALAPPDATA%` en Windows); otras ejecuciones usan `Kgs.Gtp/client-id`. Si ejecuta otros bots en el equipo, elimine solo los archivos de las cuentas que retira.
- Quite `KGS_PASSWORD` de la consola de inicio y de los ajustes persistentes del entorno, scripts de inicio o configuración del servicio donde lo haya guardado. Mobi lee la variable, pero no guarda la contraseña por sí mismo. Quite valores guardados de `KGS_USERNAME` y archivos TOML con cuentas, rutas o ajustes que ya no necesite.
- Elimine los diagnósticos guardados al redirigir stderr, como `bot.log`, y los registros del gestor de servicios o copias compartidas en otros lugares que estén bajo su control.
- Consulte la documentación del motor de Go para eliminar sus propios registros, partidas, configuración y datos. Los motores y modelos se gestionan aparte de Mobi; no borre archivos que otras aplicaciones sigan usando.

Eliminar los archivos extraídos de Mobi no elimina necesariamente estos elementos. Borrar una identidad del cliente no elimina la cuenta KGS, no reinicia su rango ni borra las partidas del servidor.

## Contacto

Para consultas privadas sobre los datos guardados por cualquiera de las aplicaciones, escriba a [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

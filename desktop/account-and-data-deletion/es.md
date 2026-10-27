---
source_revision: "f77f4ed1d576932db0474a6793f3618116114ca1712e98af8892162d5ac9d665"
layout: localized
title: "Eliminación de cuentas y datos"
lang: "es"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/es/desktop/account-and-data-deletion/"
nav_group: "policies"
---

## Eliminar datos del escritorio

Cierre KGS Nova y haga copia de las partidas exportadas que quiera conservar.

- Borre `data.db` y cualquier diario `data-log.db` de la carpeta KGS Nova de datos locales de aplicaciones (`%LOCALAPPDATA%\KGS Nova` en Windows) para eliminar metadatos de cuentas, preferencias, identificador y estado.
- Para borrar diagnósticos, elimine `client.log`, `client.archive*.log` y cualquier `logs.txt` de desarrollo de la misma carpeta. Las copias guardadas en otros sitios permanecen allí.
- En Windows, las contraseñas protegidas con DPAPI están en `data.db` y se eliminan con él. En macOS/Linux, borre aparte las entradas de Llavero/Secret Service del servicio `io.github.amywarble.kgsnet.desktop.credentials` y su usuario KGS. Borrar la base no elimina esas entradas nativas.
- Borre partidas exportadas, capturas y otros archivos no deseados de sus ubicaciones elegidas.

La carpeta contiene también el espacio `sgf`, recuperación y copias de seguridad, y los archivos de motores/modelos de `analysis`. Guarde las partidas recuperadas que quiera conservar antes de borrar esas carpetas. Borrar toda la carpeta de datos KGS Nova elimina conjuntamente estos datos locales.

Versiones antiguas usaban `data.db`, `data-log.db` y `logs.txt` en el directorio de la aplicación o de inicio. Una actualización puede dejar esas copias. Tras guardar lo necesario, elimínelas también; de lo contrario, una base antigua puede volver a importarse si falta la actual.

Desinstalar no elimina necesariamente archivos ni credenciales nativas. Borrar datos locales no elimina cuenta KGS ni datos del servidor.

## Solicitar eliminación de la cuenta KGS

KGS controla cuentas y datos del servidor. Envíe una solicitud privada a [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) con usuario y correo de la cuenta, nunca contraseña. Un administrador puede verificar la titularidad y explicar datos eliminables y retenciones obligatorias. No publique datos de cuenta en GitHub.

Consultas privadas sobre datos locales: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

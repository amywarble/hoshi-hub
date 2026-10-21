---
source_revision: "3aa9378df5f32e6acf17ec4a44bd9f2964f9a6fed7d528cdcba256cfb2358d82"
layout: localized
title: "Eliminación de cuentas y datos"
lang: "es"
page_key: "desktop/account-and-data-deletion"
section: "desktop"
nav_order: 13
permalink: "/es/desktop/account-and-data-deletion/"
---

## Eliminar datos del escritorio

Cierre KGS Nova y haga copia de las partidas exportadas que quiera conservar.

- Borre `data.db` del directorio de trabajo usado al iniciar la aplicación: elimina metadatos de cuentas recordadas, preferencias, identificador y estado, restableciendo ajustes. Si inició desde terminal, revise ese directorio además del de la aplicación.
- Borre `logs.txt` en el directorio de la aplicación. Los registros copiados o capturados de la consola permanecen donde los guardó.
- En Windows, las contraseñas protegidas con DPAPI están en `data.db` y se eliminan con él. En macOS/Linux, borre aparte las entradas de Llavero/Secret Service del servicio `io.github.amywarble.kgsnet.desktop.credentials` y su usuario KGS. Borrar la base no elimina esas entradas nativas.
- Borre partidas exportadas, capturas y otros archivos no deseados de sus ubicaciones elegidas.

Desinstalar no elimina necesariamente archivos ni credenciales nativas. Borrar datos locales no elimina cuenta KGS ni datos del servidor.

## Solicitar eliminación de la cuenta KGS

KGS controla cuentas y datos del servidor. Envíe una solicitud privada a [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request) con usuario y correo de la cuenta, nunca contraseña. Un administrador puede verificar la titularidad y explicar datos eliminables y retenciones obligatorias. No publique datos de cuenta en GitHub.

Consultas privadas sobre datos locales: [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

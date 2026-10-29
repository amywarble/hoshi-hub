---
source_revision: "a5018456d7c6b6ef49fc5b143b52c2707452b29213029b1bba9cf85a02f24031"
layout: localized
title: "Primeros pasos"
lang: "es"
page_key: "desktop/help"
section: "desktop"
nav_order: 1
permalink: "/es/desktop/help/"
nav_group: "documentation"
redirect_from: "/es/desktop/"
---

KGS Nova es un cliente del [KGS Go Server](https://www.gokgs.com/) para Windows, macOS y Linux. Cuenta con el respaldo oficial de KGS y de la American Go Association (AGA).

## Instalación y actualizaciones {#installation}

Descarga un paquete de **KGS Nova** desde [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases). Elige x64 para procesadores Intel/AMD o ARM64 para Apple Silicon y otros dispositivos ARM64. Cada versión indica las plataformas disponibles. El entorno de ejecución de .NET está incluido.

- **Windows:** Ejecuta **Installer**. Para una instalación portátil, extrae todo el ZIP **Portable** en una carpeta con permisos de escritura y ejecuta `Kgs.Client.Desktop.exe`.
- **Linux:** Haz ejecutable **AppImage** con `chmod +x Kgs.Nova-linux-<architecture>.AppImage` (`x64` o `arm64`) y ábrelo. Guárdalo en una carpeta con permisos de escritura para las actualizaciones. Requiere FUSE (`libfuse2` en Ubuntu 22.04).
- **macOS (cuando esté disponible):** Ejecuta **Installer** y abre `KGS Nova.app`. Para una instalación portátil, extrae todo el ZIP **Portable** y mueve la app a una carpeta Applications con permisos de escritura. Las compilaciones tienen firma ad hoc, sin firma de Apple Developer ID ni notarización. Si se bloquea, permite Nova en **Ajustes del Sistema > Privacidad y seguridad** después de comprobar que confías en la descarga.

En **Acerca de**, elige **Buscar actualizaciones**, **Descargar actualización** y **Reiniciar y actualizar**. Nova también busca actualizaciones al iniciarse. Termina las partidas y guarda tu trabajo antes de reiniciar. Si no puedes actualizar desde la app, descarga manualmente un paquete más reciente.

### Instalación manual en Linux

Extrae `KGS-Nova-<version>-linux-<architecture>.tar.gz` y ejecuta `./Kgs.Client.Desktop` desde esa carpeta. Estos archivos requieren una nueva descarga para actualizarse.

Linux requiere X11 o XWayland, fontconfig y las bibliotecas X11 que usa .NET/Avalonia. El audio usa PipeWire, PulseAudio o ALSA. Para guardar contraseñas se necesita libsecret (`libsecret-1-0` en Debian/Ubuntu) y un proveedor de Secret Service como GNOME Keyring.

### Archivos de actualización

Los archivos `.nupkg` y `releases.*.json` sirven al actualizador de Nova. Instala mediante **Installer**, el ZIP **Portable** o **AppImage**.

## Iniciar sesión

Inicie sesión con su usuario y contraseña KGS o continúe como invitado. Para crear una cuenta, use el enlace de registro de la pantalla de acceso; abre el sitio web KGS.

## Jugar y explorar

Elija Jugar para buscar rival o crear una partida. Use Salas para conversar y observar partidas, y Personas para buscar jugadores. Ver/editar abre archivos SGF para estudio local. Las preferencias controlan apariencia y ajustes.

## Ayuda y políticas

Para problemas de la aplicación, consulte [Ayuda]({% include page-url.html key='desktop/support' %}). Para contactos no deseados y denuncias, vea [Normas de la comunidad]({% include page-url.html key='desktop/community-guidelines' %}). Lea la [Política de privacidad]({% include page-url.html key='global/privacy' %}), las [condiciones de uso]({% include page-url.html key='desktop/terms' %}) y las [normas comunitarias compartidas]({% include page-url.html key='global/community-guidelines' %}).

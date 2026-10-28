---
layout: "localized"
title: "Mobi"
nav_title: "Primeros pasos"
lang: "es"
page_key: "mobi/home"
section: "mobi"
nav_order: 0
permalink: "/es/gtp/"
source_revision: "874054b8ddaecac1e59dd93fb146bb94e87a23f895e0f2763c1c7f0413376a1a"
---

Mobi conecta un motor de go compatible con Go Text Protocol (GTP) versión 2 al [KGS Go Server](https://www.gokgs.com/). Gestiona el inicio de sesión, el emparejamiento, las jugadas, los relojes, el recuento y la recuperación. Instale y configure el motor de go por separado.

Mobi cuenta con el respaldo oficial de KGS y American Go Association (AGA).

## Descargue y comience {#download-and-get-started}

Descargue un archivo **Mobi GTP bridge** de [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) para Windows o Linux en x64 o ARM64. El tiempo de ejecución .NET está incluido. Los paquetes Windows utilizan ZIP; Los paquetes Linux utilizan tar.gz. Mantenga los archivos extraídos juntos.

- [Guía de usuario]({% include page-url.html key='mobi/user-guide' %}): primer juego, configuración, emparejamiento, registros, tiempos de espera, recuperación y solución de problemas.
- [Guía de actualización del cliente Java]({% include page-url.html key='mobi/upgrade-guide' %}): pase de `kgsGtp.jar` y las propiedades de Java a TOML.
- [Configuración de ejemplo]({{ '/mobi/bot.example.toml' | relative_url }}): copie a `bot.toml` y configure su cuenta, rutas del motor y preferencias de juego.
- [Términos de uso]({% include page-url.html key='mobi/terms' %}): operación de su bot, licencia del motor y responsabilidades al usar Mobi.
- [Pautas de la comunidad]({% include page-url.html key='mobi/community-guidelines' %}): identidades de bot honestas, juego limpio y uso responsable de los recursos del servidor.

Las páginas compartidas [Política de privacidad]({% include page-url.html key='global/privacy' %}) y [Eliminación de cuenta y datos]({% include page-url.html key='global/account-and-data-deletion' %}) incluyen información específica de Mobi.

Las guías cubren Windows con PowerShell y Linux con Bash. Expanda la sección correspondiente a su sistema operativo. Cada archivo también incluye la configuración de ejemplo y copias sin conexión en inglés de ambas guías.

## Ejecute el cliente {#run-the-client}

Después de configurar `bot.toml`, ejecute estos comandos desde el directorio extraído. La sonda verifica el motor sin iniciar sesión en KGS; el siguiente comando juega un juego con los ajustes de emparejamiento configurados.

<details markdown="1">
<summary>Windows (PowerShell)</summary>

```powershell
.\Kgs.Gtp.exe --config .\bot.toml --probe
$env:KGS_PASSWORD = '<account password>'
.\Kgs.Gtp.exe --config .\bot.toml --games 1
```

</details>

<details markdown="1">
<summary>Linux (Bash)</summary>

```bash
chmod +x ./Kgs.Gtp
./Kgs.Gtp --config ./bot.toml --probe
read -r -s -p 'KGS password: ' KGS_PASSWORD
export KGS_PASSWORD
printf '\n'
./Kgs.Gtp --config ./bot.toml --games 1
```

</details>

Presione Ctrl+C para detener. Utilice la guía del usuario para elegir la reproducción continua, conservar registros y preservar la identidad del cliente durante las actualizaciones.

[Notifique un problema con Mobi](https://github.com/amywarble/hoshi-hub/issues/new?template=mobi_problem_report.yml). Para corregir la documentación, [abra una incidencia pública en GitHub](https://github.com/amywarble/hoshi-hub/issues/new/choose) y mencione **Mobi**. Nunca incluya contraseñas ni otra información confidencial.

No necesita conocimientos técnicos para notificar un problema. Describa con sus propias palabras lo que ocurrió, aunque solo haya pasado una vez. Indique lo que sepa; podemos hacer preguntas después. Las versiones, los pasos y las capturas son opcionales. Oculte la información privada en las capturas antes de compartirlas.

¿No utiliza GitHub? También puede notificar problemas de la aplicación por correo a [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com).

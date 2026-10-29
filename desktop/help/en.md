---
layout: localized
title: "Getting started"
lang: "en"
page_key: "desktop/help"
section: "desktop"
nav_order: 1
permalink: "/desktop/help/"
nav_group: "documentation"
redirect_from: "/desktop/"
---

KGS Nova is a client for the [KGS Go Server](https://www.gokgs.com/) for Windows, macOS, and Linux. It is officially endorsed by KGS and the American Go Association (AGA).

## Installation and updates {#installation}

Download a **KGS Nova** package from [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases). Choose x64 for Intel/AMD processors or ARM64 for Apple Silicon and other ARM64 devices. Available platforms are listed with each release. The .NET runtime is included.

- **Windows:** Run the **Installer**. For a portable installation, extract the complete **Portable** ZIP into a writable folder and run `Kgs.Client.Desktop.exe`.
- **Linux:** Make the **AppImage** executable with `chmod +x Kgs.Nova-linux-<architecture>.AppImage` (`x64` or `arm64`), then launch it. Keep it in a writable directory for updates. FUSE support is required (`libfuse2` on Ubuntu 22.04).
- **macOS (when available):** Run the **Installer**, then open `KGS Nova.app`. For a portable installation, extract the complete **Portable** ZIP and move the app into a writable Applications directory. Builds are ad hoc signed, without Apple Developer ID signing or notarization. If blocked, allow Nova in **System Settings > Privacy & Security** after confirming you trust the download.

In **About**, choose **Check for updates**, **Download update**, then **Restart and update**. Nova also checks at startup. Finish games and save your work before restarting. If in-app updating is unavailable, download a newer package manually.

### Manual Linux installation

Extract `KGS-Nova-<version>-linux-<architecture>.tar.gz` and run `./Kgs.Client.Desktop` from that folder. These archives require a new download to update.

Linux requires X11 or XWayland, fontconfig, and the X11 libraries used by .NET/Avalonia. Audio uses PipeWire, PulseAudio, or ALSA. Password storage requires libsecret (`libsecret-1-0` on Debian/Ubuntu) and a Secret Service provider such as GNOME Keyring.

### Update files

`.nupkg` and `releases.*.json` files serve Nova's updater. Install using the **Installer**, **Portable** ZIP, or **AppImage**.

## Sign in

Sign in with your existing KGS username and password, or continue as a guest. To create an account, use the registration link on the sign-in screen; it opens the KGS website.

## Play and explore

Choose Play to find an opponent or set up a custom game. Use Rooms to join discussions and observe games, and People to find players. View/edit opens SGF game records for local study. Preferences controls the app’s appearance and settings.

## Help and policies

For app problems, use [Support]({% include page-url.html key='desktop/support' %}). For unwanted interactions and conduct reports, see [Community Guidelines]({% include page-url.html key='desktop/community-guidelines' %}). Read this app’s [Privacy Policy]({% include page-url.html key='global/privacy' %}) and [Terms of Use]({% include page-url.html key='desktop/terms' %}), and the [shared Community Guidelines]({% include page-url.html key='global/community-guidelines' %}).

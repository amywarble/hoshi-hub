---
source_revision: "a5018456d7c6b6ef49fc5b143b52c2707452b29213029b1bba9cf85a02f24031"
layout: localized
title: "Начало работы"
lang: "ru"
page_key: "desktop/help"
section: "desktop"
nav_order: 1
permalink: "/ru/desktop/help/"
nav_group: "documentation"
redirect_from: "/ru/desktop/"
---

KGS Nova — клиент [KGS Go Server](https://www.gokgs.com/) для Windows, macOS и Linux, официально одобренный KGS и Американской ассоциацией го (AGA).

## Установка и обновления {#installation}

Скачайте пакет **KGS Nova** из [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases). Выберите x64 для процессоров Intel/AMD или ARM64 для Apple Silicon и других устройств ARM64. Доступные платформы указаны в каждом выпуске. Среда выполнения .NET включена.

- **Windows:** Запустите **Installer**. Для переносной установки распакуйте весь ZIP **Portable** в папку с правом записи и запустите `Kgs.Client.Desktop.exe`.
- **Linux:** Сделайте **AppImage** исполняемым командой `chmod +x Kgs.Nova-linux-<architecture>.AppImage` (`x64` или `arm64`) и запустите его. Для обновлений храните его в папке с правом записи. Требуется FUSE (`libfuse2` в Ubuntu 22.04).
- **macOS (если доступно):** Запустите **Installer**, затем откройте `KGS Nova.app`. Для переносной установки распакуйте весь ZIP **Portable** и переместите приложение в папку Applications с правом записи. Сборки имеют подпись ad hoc, без подписи Apple Developer ID и нотариального заверения. При блокировке разрешите Nova в **Системные настройки > Конфиденциальность и безопасность**, убедившись, что доверяете загрузке.

В разделе **О программе** выберите **Проверить обновления**, **Скачать обновление**, затем **Перезапустить и обновить**. Nova также проверяет обновления при запуске. Завершите партии и сохраните работу перед перезапуском. Если обновление в приложении недоступно, скачайте новый пакет вручную.

### Ручная установка в Linux

Распакуйте `KGS-Nova-<version>-linux-<architecture>.tar.gz` и запустите `./Kgs.Client.Desktop` из этой папки. Для обновления таких архивов требуется новая загрузка.

Linux требует X11 или XWayland, fontconfig и библиотеки X11, используемые .NET/Avalonia. Для звука используются PipeWire, PulseAudio или ALSA. Хранение паролей требует libsecret (`libsecret-1-0` в Debian/Ubuntu) и поставщика Secret Service, например GNOME Keyring.

### Файлы обновления

Файлы `.nupkg` и `releases.*.json` предназначены для обновления Nova. Для установки используйте **Installer**, ZIP **Portable** или **AppImage**.

## Вход

Войдите с существующим именем и паролем KGS или продолжите как гость. Для создания аккаунта используйте ссылку регистрации на экране входа: она открывает сайт KGS.

## Игра и возможности

Выберите Играть для поиска соперника или создания партии. Раздел Комнаты позволяет общаться и наблюдать партии, а Люди — искать игроков. Просмотр/редактирование открывает SGF для локального изучения. Параметры управляют оформлением и настройками.

## Помощь и правила

При проблемах с приложением см. [Поддержка]({% include page-url.html key='desktop/support' %}). О нежелательных контактах и жалобах см. [Правила сообщества]({% include page-url.html key='desktop/community-guidelines' %}). Прочитайте [Политика конфиденциальности]({% include page-url.html key='global/privacy' %}), [условия использования]({% include page-url.html key='desktop/terms' %}) и [общие правила сообщества]({% include page-url.html key='global/community-guidelines' %}).

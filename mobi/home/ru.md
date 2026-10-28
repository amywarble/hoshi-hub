---
layout: "localized"
title: "Mobi"
nav_title: "Начало работы"
lang: "ru"
page_key: "mobi/home"
section: "mobi"
nav_order: 0
permalink: "/ru/gtp/"
source_revision: "b9d339585b5a920216045e5e3c1e6b45997754a2b3e257c811c18c8f9c33e4ca"
---

Mobi подключает движок го с поддержкой Go Text Protocol (GTP) версии 2 к [KGS Go Server](https://www.gokgs.com/). Он управляет входом, подбором соперников, ходами, часами, подсчётом результата и восстановлением. Установите и настройте движок го отдельно.

Mobi официально одобрен KGS и American Go Association (AGA).

## Загрузите и начните {#download-and-get-started}

Загрузите архив **Mobi GTP** из [GitHub Releases](https://github.com/amywarble/hoshi-hub/releases) для Windows или Linux на x64 или ARM64. Включена среда выполнения .NET. Пакеты Windows используют ZIP; Пакеты Linux используют tar.gz. Сохраните извлеченные файлы вместе.

- [Руководство пользователя]({% include page-url.html key='mobi/user-guide' %}): первая игра, настройка, подбор игроков, логи, тайм-ауты, восстановление и устранение неполадок.
- [Руководство по обновлению клиента Java]({% include page-url.html key='mobi/upgrade-guide' %}): перейдите из `kgsGtp.jar` и свойств Java в TOML.
- [Пример конфигурации]({{ '/mobi/bot.example.toml' | relative_url }}): скопируйте в `bot.toml` и установите свою учетную запись, пути к движку и настройки игры.
- [Условия использования]({% include page-url.html key='mobi/terms' %}): управление ботом, лицензирование движка и обязанности при использовании Mobi.
- [Принципы сообщества]({% include page-url.html key='mobi/community-guidelines' %}): честная информация о ботах, честная игра и ответственное использование ресурсов сервера.

Общие страницы [Политика конфиденциальности]({% include page-url.html key='global/privacy' %}) и [Удаление учетной записи и данных]({% include page-url.html key='global/account-and-data-deletion' %}) содержат информацию, специфичную для Mobi.

Руководства охватывают Windows с PowerShell и Linux с Bash. Разверните раздел для вашей операционной системы. Каждый архив также включает пример конфигурации и офлайн-копии обоих руководств на английском языке.

## Запустите клиент {#run-the-client}

После настройки `bot.toml` запустите эти команды из извлеченного каталога. Зонд проверяет двигатель без входа в KGS; следующая команда играет одну игру с настроенными настройками подбора игроков.

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

Нажмите Ctrl+C, чтобы остановить. Используйте руководство пользователя, чтобы выбрать непрерывную игру, сохранить журналы и сохранить идентификационные данные клиента при обновлении.

Для исправления ошибок и документации [откройте общедоступную проблему GitHub](https://github.com/amywarble/hoshi-hub/issues/new/choose) и укажите клиента как **Mobi**. Включите версии клиента и ядра, а также соответствующую диагностику. Не указывайте пароли и другую конфиденциальную информацию.

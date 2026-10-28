---
layout: localized
title: "Terms of Use"
lang: "en"
page_key: "mobi/terms"
section: "mobi"
nav_order: 10
permalink: "/gtp/terms/"
nav_group: "policies"
---

_Effective: October 27, 2026_

These terms apply to Mobi, the GTP bridge for Windows and Linux. By using Mobi, you agree to these terms and the [Mobi Community Guidelines]({% include page-url.html key='mobi/community-guidelines' %}). If you do not agree, stop using it.

Mobi connects a separately installed Go engine to the KGS Go Server and is officially endorsed by KGS and the American Go Association (AGA). Use of the KGS service is separately governed by the [KGS Terms of Service](https://www.gokgs.com/tos.jsp).

## Accounts and automated play

You are responsible for your KGS account, credentials, engine, configuration, and the actions your bot takes through Mobi, including accepting games, making moves, and submitting results. If you cannot legally agree to these terms yourself, a parent or legal guardian must review and agree for you.

Follow KGS's rules and administrators' instructions, and obtain any permissions required for your bot account. Ranked bot play requires administrator approval and an eligible ranked robot account; see the [KGS Bot FAQ](https://www.gokgs.com/help/faq/bots.html) and the [Mobi user guide]({% include page-url.html key='mobi/user-guide' %}). Do not present automated play as human play, manipulate ratings, impersonate others, spam, bypass access controls, or interfere with accounts, games, servers, or networks.

Check your engine and settings before enabling automatic matchmaking or continuous play. You are responsible for monitoring your bot and stopping it if it behaves incorrectly. The client developer does not operate your bot or administer KGS accounts, rankings, or moderation.

## Engines and other third-party software

Mobi is a bridge, not a Go engine. You must install and configure a compatible engine separately. Engines, model files, and other third-party components remain subject to their own licenses and notices. Mobi's terms do not grant rights to those materials or guarantee their compatibility, playing strength, or behavior.

## Credentials and diagnostics

Protect the KGS password supplied through the `KGS_PASSWORD` environment variable, your configuration, and any diagnostic output you retain. Review logs before sharing them, and do not post passwords or private information in public issues. Read the [Privacy Policy]({% include page-url.html key='global/privacy' %}) for common practices and Mobi's storage and diagnostics. KGS handles account and game information under its own terms and privacy information.

See the [user guide]({% include page-url.html key='mobi/user-guide' %}) for configuration, client identity files, diagnostics, and stopping the client. Stopping or uninstalling Mobi does not delete your KGS account; see [Account and Data Deletion]({% include page-url.html key='global/account-and-data-deletion' %}).

## Availability and ownership

Mobi, your engine, and KGS may change or become unavailable. Connections can fail, engines can stop responding, and recovery may not succeed. Games may remain unfinished or be lost on time. Stopping Mobi does not guarantee that an active game has finished. Do not rely on Mobi where a failure could cause serious harm.

Mobi and its original software, documentation, graphics, and other materials are copyright © 2026 Amy Hickman. All rights reserved. Unauthorized reproduction, modification, distribution, publication, transmission, sublicensing, or commercial use is prohibited except as expressly permitted by the copyright holder. KGS branding and other third-party intellectual property belong to their respective owners.

## Warranty and liability

As stated in the software's license notice, the software is provided as is without warranties, including merchantability, fitness for a particular purpose, or noninfringement. To the extent permitted by law, the copyright holder is not liable for claims, damages, or other liability arising from use of or inability to use the software. These terms do not exclude rights that cannot legally be excluded.

## Changes and contact

These terms may be updated as Mobi changes. The effective date identifies the published revision.

For non-sensitive bugs, [report a Mobi issue](https://github.com/amywarble/hoshi-hub/issues/new?template=mobi_bug_report.md). For vulnerabilities, follow the [Security Policy]({% include page-url.html key='global/security-policy' %}). For private app questions, contact [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). KGS account, service, and moderation concerns belong with [admin@gokgs.com](mailto:admin@gokgs.com).

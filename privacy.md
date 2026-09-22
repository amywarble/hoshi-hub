---
layout: default
title: Privacy Policy
permalink: /privacy/
nav_order: 3
---

_Effective: September 23, 2026_

Pocket KGS is an independent Android client that connects you to the KGS Go Server ("KGS"). Pocket KGS is not affiliated with or endorsed by KGS. This policy explains what information the Pocket KGS app handles, why it handles it, where it goes, and the choices available to you.

This policy covers Pocket KGS and this support website. KGS is a separate service with its own [Terms of Service and privacy terms](https://www.gokgs.com/tos.jsp).

## Who handles your data

The app connects directly to KGS. The Pocket KGS developer provides the client software but does not operate the KGS servers or control KGS's server-side records, moderation, or retention practices.

Pocket KGS does not include advertising, analytics, or an automatic crash-reporting service. The developer does not sell your personal information.

## Information the app handles

Depending on the features you use, Pocket KGS handles the following information:

- **Account and profile information:** your KGS username, password, email address, profile text, avatar, rank, account status, and profile preferences.
- **Communications and user content:** public room chat, game chat, private messages, offline messages, game records, game annotations, challenges, and other content you send to or receive from KGS.
- **Audio:** microphone audio when an eligible teacher explicitly starts a teacher-audio broadcast. Pocket KGS sends that live audio to KGS participants in the game. The app stops broadcasting when you stop it or the relevant session ends; Pocket KGS does not create a separate audio recording for the developer.
- **Social information:** buddy, fan, and censor lists, including notes you attach to those relationships.
- **Game and activity information:** games played or observed, moves, results, preferences, room membership, challenges, and interactions with KGS features.
- **Device and connection information:** a persistent KGS client identifier, app and protocol version, language/locale, operating system and version, processor architecture, runtime vendor/version, network status, and information needed to establish a connection. KGS necessarily receives your IP address when you connect.
- **Notification information:** locally stored choices about which KGS events may produce Android notifications.
- **Locally cached content:** avatars and app preferences used to make the app function efficiently.
- **Diagnostic logs:** production releases write a limited set of diagnostic information to Android's system log. KGS protocol-layer logging is disabled in release builds, and production logging is designed not to record KGS protocol events or message payloads. Logs are limited to Android/UI informational events and warnings or errors from the app's UI and client layers. They may include a KGS username, room/game/channel identifiers, app actions, Android state, and exception details when relevant to a failure. Pocket KGS does not automatically upload these logs to the developer. Android, your device administrator, or a person to whom you deliberately provide a log may be able to access them.

## How information is used

Pocket KGS uses information to:

- sign you in and maintain your KGS session;
- update your existing KGS account profile when you request it;
- display rooms, users, games, profiles, messages, and other KGS content;
- send your moves, messages, profile changes, avatar, audio, and other requested actions to KGS;
- remember app settings, your KGS client identifier, and notification preferences on your device;
- show notifications you enable; and
- diagnose app failures when you choose to share relevant details with the developer.

Pocket KGS does not use this information for targeted advertising or cross-app tracking.

## Where information is sent

Information is disclosed only as needed for the following purposes:

- **KGS:** Account data, communications, game activity, profile information, live teacher audio, device/runtime information, the KGS client identifier, and connection information are sent to KGS to provide the service. Other KGS users can see information and content that the KGS feature makes public or shares with them.
- **Android credential providers:** If you choose the password-manager feature, Android Credential Manager and the credential provider you select handle the saved username and password under their own privacy terms. Pocket KGS does not receive biometric data used by Android to unlock a credential.
- **GitHub:** This support website and its public issue tracker are hosted by GitHub. Information you submit there is processed under the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement) and, for public issues, is visible to the public.
- **Legal and safety needs:** Information received by the developer may be preserved or disclosed when reasonably necessary to comply with law, protect users, investigate abuse, or protect the rights and security of the app and others.

## Important communication and transport notice

KGS states that all conversations on its service are logged and may be reviewed by KGS administrators when investigating reports. Do not use KGS chat for information that must remain private.

The legacy KGS protocol used by Pocket KGS does not provide a modern TLS-protected connection. The password is transformed using the KGS login protocol before transmission, but other traffic is not protected by TLS or end-to-end encryption. Someone able to observe or interfere with the network path may be able to read or alter traffic. Avoid using Pocket KGS on networks you do not trust.

## Storage and retention

Pocket KGS stores its client identifier and preferences in app-private storage and caches avatar images in Android's cache area. Android may remove cached files when space is needed. Clearing Pocket KGS storage or uninstalling the app removes Pocket KGS's app-private data; credentials saved through Android Credential Manager may need to be removed separately from your password manager.

The developer does not maintain a separate server-side copy of your KGS account, chats, games, avatar, or teacher audio. KGS controls its own server-side retention. KGS states that conversations are logged, and game records may remain available in its archives.

To request deletion of your KGS account and associated server-side data, email the KGS administrators at [admin@gokgs.com](mailto:admin@gokgs.com?subject=KGS%20account%20deletion%20request). Include your KGS username and account email address, but never your password. A KGS administrator may contact you to verify ownership and will process the request. See [Account and Data Deletion]({{ '/account-and-data-deletion/' | relative_url }}) for complete instructions, including removal of data stored locally by Pocket KGS.

Public GitHub issues and their history remain on GitHub until they are edited or deleted in accordance with GitHub's features and policies.

## Your choices

You can:

- use a guest KGS session instead of creating an account on the KGS website;
- decide whether to save a password through Android Credential Manager;
- mark your KGS email address private where that option is available;
- choose whether to upload an avatar or edit profile information;
- deny microphone permission and avoid teacher-audio broadcasting;
- disable Pocket KGS notifications in the app or Android settings;
- censor a KGS user to block supported interactions and hide their content;
- clear local app data or uninstall Pocket KGS; and
- follow the instructions on the [Account and Data Deletion]({{ '/account-and-data-deletion/' | relative_url }}) page.

## Children

Pocket KGS is not directed to children under 13. KGS is a public online service where users can communicate with one another. A parent or guardian should review KGS's terms and decide whether the service is appropriate before allowing a minor to use it. Do not submit personal information about a child through a public GitHub issue.

## Security

No system is completely secure. Keep your device and app up to date, use a unique KGS password, and do not post credentials or private content in the public issue tracker. See the [Security Policy](https://github.com/amywarble/pocket-kgs-support/security/policy) for vulnerability-reporting instructions.

## Changes to this policy

This policy may change as Pocket KGS changes. The effective date at the top will be updated when a material revision is published. Continued use after a change means the revised policy applies to later use of the app.

## Contact

General app-support requests may be submitted through the [public issue tracker](https://github.com/amywarble/pocket-kgs-support/issues/new/choose), provided they contain no personal or sensitive information.

For private questions or concerns about Pocket KGS, including privacy and sensitive safety matters, email the Pocket KGS developer at [hoshihatchery@gmail.com](mailto:hoshihatchery@gmail.com). For concerns about KGS accounts, server-side data, moderation, or the KGS service, contact the KGS administrators at [admin@gokgs.com](mailto:admin@gokgs.com).

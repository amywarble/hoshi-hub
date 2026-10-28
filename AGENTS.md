# Hoshi Hub maintenance

This file contains repository guidance for maintainers and coding agents. Keep
it excluded from the generated website and do not link to it from the public
README or site navigation. Keep the README focused on the apps, documentation,
downloads, and support routes available to visitors.

App source code belongs in the private application repository. Public issues in
this repository are only for non-sensitive app bugs, feature requests, and
documentation corrections. The Pocket pages currently document Android;
platform-specific iOS documentation has not been added yet.

## Pages and languages

Each page has its own source folder, containing one Markdown file per language:

```text
android/
  help/en.md, da.md, de.md, es.md, fr.md, ja.md, ru.md, zh-Hans.md
  support/
  terms/
  community-guidelines/
desktop/
  help/
  support/
  terms/
  community-guidelines/
mobi/
  home/
  user-guide/
  upgrade-guide/
  terms/
  community-guidelines/
  bot.example.toml
  legacy-bot-config.toml
global/
  home/
  privacy/
  account-and-data-deletion/
  community-guidelines/
  security-policy/
```

All Android, desktop, global, and Mobi page folders contain the same eight languages:
English, Danish, German, Spanish, French, Japanese, Russian, and Simplified
Chinese. The root `SECURITY.md` is a short pointer retained for GitHub's
security-policy discovery; the complete website policy and its translations live
under `global/security-policy/`.
Mobi is the public name of the GTP bridge; executable and configuration examples
continue to use `Kgs.Gtp.exe` and `Kgs.Gtp`. Its English documentation is at
`/gtp/`, `/gtp/user-guide/`, `/gtp/upgrade-guide/`, `/gtp/terms/`, and
`/gtp/community-guidelines/`, with the usual language prefixes for translations.
Its source files, page keys, and navigation section use `mobi/` and `mobi`.
Explicit permalinks retain the existing `/gtp/` website routes. The example
configuration is maintained at `mobi/bot.example.toml`; `mobi/legacy-bot-config.toml`
publishes the same content at `/gtp/bot.example.toml` through an include, preserving
older downloads without keeping a second copy of the configuration.
Keep all Mobi pages and homepage links in the selected language. Do not add an
English-only note or fallback labels for translated pages. Translated guides
preserve fenced executable examples and inline technical identifiers exactly;
explicit heading IDs keep section links stable as headings are translated.
The downloadable app archives currently contain English offline guides; do not
imply that website translations are included in those packages.
The Mobi guides use collapsible Windows (PowerShell) and Linux (Bash) examples,
with `markdown="1"` on `<details>` so Jekyll renders the code blocks. They work
without JavaScript. Keep these public guides and `mobi/bot.example.toml` aligned
with the offline guides and example configuration shipped by Kgs.Gtp.

Explicit permalinks preserve the original English policy URLs, including
`/privacy/`, `/terms/`, and `/desktop/privacy/`. The original app landing routes
`/android/` and `/desktop/` redirect to their getting-started guides; the shared
home page remains `/`. Other languages add a language
prefix, for example `/ja/privacy/` and `/fr/desktop/support/`. These paths are
relative to the site's `/hoshi-hub` base URL.

## Documentation and shared content

The shared homepage uses `_includes/client-grid.html` to show Pocket KGS, Nova,
and Mobi with their important links. It uses the full content width without the
article sidebar; the client panels stack on smaller screens. Keep interface
labels in `_data/languages.json` and page links in the current language.
Pocket KGS has no download link until a
public distribution route is available. Documentation logos live in
`assets/images/`, including `mobi.png` for Mobi. Homepages include the grid once.
It is followed by `_includes/home-policies.html`. One box contains all policy
groups. An "All clients" group contains Privacy, Account and Data Deletion, and
Security links. Below a divider, one list per
client contains its Terms of Use, Community Guidelines, and applicable controls.
Pocket and Nova each link to the shared conduct rules; Mobi links to its own bot
guidelines. Use document names as links and keep every group visible, without
tables, merged cells, placeholder dashes, or repeated Read labels. The client
lists stack on smaller screens. Mobi's Terms of Use and Community Guidelines link
to the selected language, like the other clients' policies.
Keep homepage policy links visible without expandable groups. Each client panel has
a direct "Report a Bug" link to its own template in `.github/ISSUE_TEMPLATE/`;
general issue reporting follows the policy section. The app-specific conduct
links are labeled "Blocking and reporting" to distinguish them from the shared
conduct rules.

Bug-report links use `bug_report.yml` for Pocket KGS, `nova_bug_report.yml` for
Nova, and `mobi_problem_report.yml` for Mobi. Keep the older
`desktop_bug_report.md` and `mobi_bug_report.md` text templates available for
released app links and bookmarks. Nova prefills the `app-info` field by URL;
coordinate changes to that field ID or template filename with the app source.

Each app has one getting-started page, combining its introduction and guide, at
`/android/help/` or `/desktop/help/`. Nova already opens `/desktop/help/` from its
online help menu. Keep these entry points stable as more task guides are added.
Each guide declares `redirect_from` for its former app landing route, including
the language prefix; `jekyll-redirect-from` retains those incoming links.
App pages declare `nav_group: "documentation"` for help and support, or
`nav_group: "policies"` for terms and community safety tools.
`nav_order` orders pages within each group. The sidebar lists documentation
links directly and puts policies in a translated, collapsible group that opens
automatically on the current app's policy pages. Both work without JavaScript.
An optional `nav_title` shortens a sidebar label without changing the page title.

The common conduct rules live in `global/community-guidelines/`, published at
`/shared/community-guidelines/` with the usual language prefixes. Maintain the
rules once per language. The original `/community-guidelines/` and
`/desktop/community-guidelines/` routes remain readable app pages: they link to
the common rules and describe that app's blocking and reporting controls.
Keep app terms and consent links working at those existing routes.

Account and data deletion is maintained once per language in
`global/account-and-data-deletion/`, at the retained `/account-and-data-deletion/`
route. The former `/desktop/account-and-data-deletion/` routes redirect there,
including the matching language prefixes. Keep KGS account-deletion guidance
shared, and preserve the separate Pocket KGS and Nova local-removal sections.
Use `global/account-and-data-deletion` for internal links. The homepage lists it
once under "All clients". Preserve the Mobi section's
distinction between KGS account deletion and local identity, environment, logs,
configuration, and separately managed engine data.

The Privacy Policy is maintained in `global/privacy/`, at `/privacy/` and the
usual language prefixes. Former `/desktop/privacy/` routes redirect there.
Use `global/privacy` for internal links. Common privacy practices cover all three
clients; preserve separate Pocket KGS, Nova, and Mobi storage and control sections.
Do not apply Pocket/Nova's release-log omission promises to Mobi's stderr output
or separately installed engines. Mobi's bot-operation rules remain in
`mobi/community-guidelines/`, linked from its Terms of Use and landing page.

Keep platform-specific terms, installation, and troubleshooting
details in the appropriate app space. Share an article only when its instructions
and scope apply to every client that links to it. KGS-wide account and service
information should link to the maintained KGS website; client button locations
and feature instructions belong here. Mobi's existing guides remain in its own
space.

To add a task guide, create a folder under its app space, declare a unique
`page_key` and stable permalink, and link it from the app's help page. Add its key
to the translation checker and supply all eight translations. Verify every
documented control against the client before publishing.

`_layouts/localized.html` shares the dark Just the Docs styling and renders the
language bar, navigation, and page heading. Each translation declares the same
`page_key`, so switching languages opens the equivalent document. Local links
use `{% include page-url.html key='global/privacy' %}` to stay in the current
language. The layout emits language and alternate-language metadata. Reading,
language switching, and navigation work without JavaScript. Optional search uses
one static index per language and supports substring matching, including Japanese
and Chinese. The theme's single-language search is disabled in favor of this
language-specific search.

## Updating translations

Edit a page's `en.md` and update every translation in the same folder. Preserve
technical identifiers, contact addresses, links, policy dates, and the meaning of
the source, including platform differences. The front matter supplies the page
title; use second-level headings for sections inside the document.

Each translation's `source_revision` is the SHA-256 of the English Markdown body
(excluding front matter, stripping leading/trailing whitespace, using LF line
endings). The checker reports the current hash if a translation becomes stale.
Update that field only after reviewing and updating the translation against the
current English source. The initial translations have not had independent
native-speaker review.

## Build and verification

Keep local toolchains and generated caches in `_config.yml`'s `exclude` list.
Jekyll's watcher uses that list independently of `.gitignore`; watching the
cached Linux Ruby files under `.cache/` causes continuous rebuilds on Windows.

See `scripts/README.md` for Windows installation and local browser preview with
Jekyll and LiveReload. Keep development setup instructions out of the public
README and website navigation.

Run the source checks with Python 3:

```sh
python scripts/check-translations.py
```

To build with the GitHub Pages dependency set, install Ruby and Bundler, then run:

```sh
bundle install
bundle exec jekyll build --strict_front_matter
python scripts/check-translations.py --site _site
bundle exec jekyll serve
```

The output check verifies language selectors, navigation language, generated
links, page headings, search indexes, and the retained English routes. Generated
HTML and dependency caches are ignored; source translations remain ordinary
Markdown reviewed in Git.

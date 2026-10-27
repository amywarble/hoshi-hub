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
  home/en.md, da.md, de.md, es.md, fr.md, ja.md, ru.md, zh-Hans.md
  help/
  support/
  privacy/
  terms/
  community-guidelines/
  account-and-data-deletion/
desktop/
  home/
  help/
  support/
  privacy/
  terms/
  community-guidelines/
  account-and-data-deletion/
gtp/
  home/en.md
  user-guide/en.md
  upgrade-guide/en.md
  bot.example.toml
global/
  home/
  community-guidelines/
  security-policy/
```

The Android, desktop, and global page folders contain the same eight languages:
English, Danish, German, Spanish, French, Japanese, Russian, and Simplified
Chinese. The root `SECURITY.md` is a short pointer retained for GitHub's
security-policy discovery; the complete website policy and its translations live
under `global/security-policy/`.
GTP documentation is currently English-only at `/gtp/`, `/gtp/user-guide/`, and
`/gtp/upgrade-guide/`. Its page groups declare only the available language;
links from translated home pages fall back to the English GTP landing page.
The GTP guides use collapsible Windows (PowerShell) and Linux (Bash) examples,
with `markdown="1"` on `<details>` so Jekyll renders the code blocks. They work
without JavaScript. Keep these public guides and `gtp/bot.example.toml` aligned
with the offline guides and example configuration shipped by Kgs.Gtp.

Explicit permalinks preserve the original English policy URLs, including
`/privacy/`, `/terms/`, and `/desktop/privacy/`. Android's landing page is
`/android/`; the shared home page remains `/`. Other languages add a language
prefix, for example `/ja/privacy/` and `/fr/desktop/support/`. These paths are
relative to the site's `/hoshi-hub` base URL.

## Documentation and shared content

The app home pages lead to short getting-started guides at `/android/help/` and
`/desktop/help/`. Nova already opens `/desktop/help/` from its online help menu.
Keep these entry points stable as more task guides are added. App pages declare
`nav_group: "documentation"` for home, help, and support, or `nav_group: "policies"`
for privacy, terms, community safety tools, and deletion. `nav_order` orders pages
within each group. The sidebar uses translated group labels.

The common conduct rules live in `global/community-guidelines/`, published at
`/shared/community-guidelines/` with the usual language prefixes. Maintain the
rules once per language. The original `/community-guidelines/` and
`/desktop/community-guidelines/` routes remain readable app pages: they link to
the common rules and describe that app's blocking and reporting controls.
Keep app terms and consent links working at those existing routes.

Keep platform-specific privacy, terms, deletion, installation, and troubleshooting
details in the appropriate app space. Share an article only when its instructions
and scope apply to every client that links to it. KGS-wide account and service
information should link to the maintained KGS website; client button locations
and feature instructions belong here. GTP's existing guides remain in its own
space.

To add a task guide, create a folder under its app space, declare a unique
`page_key` and stable permalink, and link it from the app's help page. Add its key
to the translation checker and supply all eight translations, or explicitly
declare English-only coverage if translations are not available. Verify every
documented control against the client before publishing.

`_layouts/localized.html` shares the dark Just the Docs styling and renders the
language bar, navigation, and page heading. Each translation declares the same
`page_key`, so switching languages opens the equivalent document. Local links
use `{% include page-url.html key='android/privacy' %}` to stay in the current
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

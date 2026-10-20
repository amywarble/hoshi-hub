# Hoshi Hub

This repository contains the public support, privacy, terms, safety, and deletion information for the Pocket KGS Android/iOS apps and the KGS Nova desktop apps.

<https://amywarble.github.io/hoshi-hub/>

App source code belongs in the private application repository. Public issues in this repository are only for non-sensitive app bugs, feature requests, and documentation corrections.

## Pages and languages

Each page has its own source folder, containing one Markdown file per language:

```text
android/
  home/en.md, da.md, de.md, es.md, fr.md, ja.md, ru.md, zh-Hans.md
  support/
  privacy/
  terms/
  community-guidelines/
  account-and-data-deletion/
desktop/
  home/
  support/
  privacy/
  terms/
  community-guidelines/
  account-and-data-deletion/
global/
  home/
  security-policy/
```

All folders contain the same eight languages: English, Danish, German, Spanish,
French, Japanese, Russian, and Simplified Chinese. The root `SECURITY.md` is a
short pointer retained for GitHub's security-policy discovery; the complete
website policy and its translations live under `global/security-policy/`.

Explicit permalinks preserve the original English policy URLs, including
`/privacy/`, `/terms/`, and `/desktop/privacy/`. Android's landing page is
`/android/`; the shared home page remains `/`. Other languages add a language
prefix, for example `/ja/privacy/` and `/fr/desktop/support/`. These paths are
relative to the site's `/hoshi-hub` base URL.

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

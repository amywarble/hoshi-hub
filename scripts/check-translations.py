"""Validate translation coverage, source revisions, routes, and generated HTML."""

import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = json.loads((ROOT / '_data/languages.json').read_text(encoding='utf-8'))
SECTIONS = ('global', 'android', 'desktop', 'gtp')
PAGE_NAMES = ('home', 'help', 'support', 'privacy', 'terms', 'community-guidelines', 'account-and-data-deletion')
LOCALIZED_KEYS = {'global/home', 'global/security-policy', 'global/community-guidelines'} | {
    f'{section}/{name}' for section in ('android', 'desktop') for name in PAGE_NAMES
}
ENGLISH_ONLY_KEYS = {'gtp/home', 'gtp/user-guide', 'gtp/upgrade-guide'}
EXPECTED_KEYS = LOCALIZED_KEYS | ENGLISH_ONLY_KEYS
LINK_PATTERN = re.compile(r"\{%\s*include page-url.html key='([^']+)'\s*%\}")
ASSET_PATTERN = re.compile(r"\{\{ '([^']+)' \| relative_url \}\}")


def available_languages(key):
    """Keep complete translation coverage for localized pages and explicit English-only guides."""
    return ('en',) if key in ENGLISH_ONLY_KEYS else tuple(LANGUAGES)


def read_page(path):
    """Read the generated scalar-only front matter without a YAML dependency."""
    text = path.read_text(encoding='utf-8')
    assert text.startswith('---\n'), f'{path}: missing front matter'
    _, front, body = text.split('---', 2)
    metadata = {}
    for line in front.strip().splitlines():
        name, value = line.split(':', 1)
        assert name not in metadata, f'{path}: duplicate front matter field {name}'
        value = value.strip()
        metadata[name] = json.loads(value) if value.startswith('"') or value.isdigit() else value
    return metadata, body.strip()


def expected_url(key, lang):
    if key == 'global/home':
        route = '/'
    elif key == 'global/community-guidelines':
        route = '/shared/community-guidelines/'
    elif key == 'android/help':
        route = '/android/help/'
    elif key.endswith('/home'):
        route = f'/{key.split("/")[0]}/'
    elif key.startswith(('global/', 'android/')):
        route = f'/{key.split("/")[1]}/'
    else:
        route = f'/{key}/'
    return route if lang == 'en' else f'/{lang}{route}'


class Document(HTMLParser):
    """Collect accessibility, navigation, and link metadata from built pages."""

    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.language = None
        self.links = []
        self.selector = []
        self.sidebar = []
        self.alternates = {}
        self.current_language = []
        self.current_page = []
        self.headings = 0
        self.ids = set()
        self.regions = []
        self.feed(html)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'html':
            self.language = attrs.get('lang')
        if tag == 'h1':
            self.headings += 1
        if attrs.get('id'):
            assert attrs['id'] not in self.ids, f'Duplicate id {attrs["id"]}'
            self.ids.add(attrs['id'])
        if tag == 'nav':
            self.regions.append('selector' if 'hoshi-languages' in attrs.get('class', '') else 'sidebar')
        if tag == 'a':
            if self.regions and self.regions[-1] == 'selector':
                self.selector.append((attrs.get('lang'), attrs.get('href')))
                if attrs.get('aria-current'):
                    self.current_language.append(attrs.get('lang'))
            elif self.regions and self.regions[-1] == 'sidebar':
                self.sidebar.append(attrs.get('href'))
                if attrs.get('aria-current') == 'page':
                    self.current_page.append(attrs.get('href'))
        if tag == 'link' and attrs.get('rel') == 'alternate':
            self.alternates[attrs['hreflang']] = attrs.get('href')
        for attribute in ('href', 'src'):
            if attribute in attrs:
                self.links.append(attrs[attribute])

    def handle_endtag(self, tag):
        if tag == 'nav':
            self.regions.pop()


def check_sources():
    pages = {}
    routes = set()
    for section in SECTIONS:
        for path in (ROOT / section).rglob('*.md'):
            data, body = read_page(path)
            key, lang = data['page_key'], data['lang']
            assert key in EXPECTED_KEYS, f'{path}: unexpected page key'
            assert lang in LANGUAGES and path.stem == lang, f'{path}: invalid language'
            assert key == path.parent.relative_to(ROOT).as_posix(), f'{path}: folder does not match page key'
            assert data['section'] == section, f'{path}: incorrect section'
            assert data['layout'] == 'localized', f'{path}: incorrect layout'
            if section in ('android', 'desktop'):
                group = 'documentation' if path.parent.name in ('home', 'help', 'support') else 'policies'
                assert data.get('nav_group') == group, f'{path}: incorrect navigation group'
            assert data['permalink'] == expected_url(key, lang), f'{path}: route changed'
            assert data['permalink'] not in routes, f'{path}: duplicate route'
            routes.add(data['permalink'])
            assert body and '\ufffd' not in body, f'{path}: missing or damaged content'
            assert not re.search(r'^# ', body, re.MULTILINE), f'{path}: duplicate page heading'
            assert not re.search(r'\bTODO\b|\bTBD\b', body), f'{path}: unfinished content'
            assert (key, lang) not in pages, f'{path}: duplicate translation'
            pages[key, lang] = (data, body)

    expected_pages = {(key, lang) for key in EXPECTED_KEYS for lang in available_languages(key)}
    assert set(pages) == expected_pages, 'Translation set incomplete'
    for (key, lang), (data, body) in pages.items():
        for target in LINK_PATTERN.findall(body):
            assert (target, lang) in pages or (target, 'en') in pages, f'{key}/{lang}: missing linked page {target}'
        for asset in ASSET_PATTERN.findall(body):
            assert asset.startswith('/') and (ROOT / asset.lstrip('/')).is_file(), f'{key}/{lang}: missing asset {asset}'
        assert body.count('{%') == len(LINK_PATTERN.findall(body)), f'{key}/{lang}: unexpected Liquid tag'
        if lang != 'en':
            english = pages[key, 'en'][1]
            revision = hashlib.sha256(english.encode('utf-8')).hexdigest()
            assert data.get('source_revision') == revision, f'{key}/{lang}: stale translation; current source_revision: {revision}'

    for lang, labels in LANGUAGES.items():
        assert all(value and '?' not in value and '\ufffd' not in value for value in labels.values()), f'{lang}: damaged interface label'
    print(f'Source checks passed: {len(EXPECTED_KEYS)} page groups, {len(LANGUAGES)} languages, {len(pages)} pages.')
    return pages


def check_output(site, pages):
    config = (ROOT / '_config.yml').read_text(encoding='utf-8')
    baseurl = re.search(r'^baseurl: "([^"]+)"', config, re.MULTILINE)[1]
    siteurl = re.search(r'^url: "([^"]+)"', config, re.MULTILINE)[1]
    documents = {}
    for identity, (data, _) in pages.items():
        output = site / data['permalink'].lstrip('/') / 'index.html'
        assert output.is_file(), f'Missing output: {output}'
        html = output.read_text(encoding='utf-8')
        assert '{%' not in html and '{{' not in html, f'{output}: unresolved Liquid'
        document = Document(html)
        key, lang = identity
        languages = available_languages(key)
        assert document.language == lang, f'{output}: incorrect HTML language'
        assert document.headings == 1, f'{output}: expected one page heading'
        assert dict(document.selector) == {
            language: baseurl + pages[key, language][0]['permalink'] for language in languages
        }, f'{output}: incorrect language selector'
        assert len(document.selector) == len(languages), f'{output}: duplicate language links'
        assert document.current_language == [lang], f'{output}: incorrect selected language'
        assert set(document.sidebar) == {
            baseurl + metadata['permalink'] for (page_key, language), (metadata, _) in pages.items() if language == lang
        }, f'{output}: navigation mixes languages or omits pages'
        assert document.current_page == [baseurl + data['permalink']], f'{output}: incorrect active page'
        for language in languages:
            assert document.alternates[language] == siteurl + baseurl + pages[key, language][0]['permalink']
        assert document.alternates['x-default'] == siteurl + baseurl + pages[key, 'en'][0]['permalink']
        documents[data['permalink']] = document

    for route, document in documents.items():
        for link in document.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            if not parsed.path:
                assert not parsed.fragment or unquote(parsed.fragment) in document.ids, f'{route}: missing anchor {link}'
                continue
            assert parsed.path.startswith(baseurl + '/'), f'{route}: link missing baseurl: {link}'
            target = site / unquote(parsed.path[len(baseurl) + 1:])
            if parsed.path.endswith('/'):
                target /= 'index.html'
            assert target.is_file(), f'{route}: broken local link {link}'

    for lang in LANGUAGES:
        path = site / 'assets/search' / f'{lang}.json'
        index = json.loads(path.read_text(encoding='utf-8'))
        expected = {baseurl + data['permalink'] for (key, language), (data, _) in pages.items() if language == lang}
        assert len(index) == len(expected) and {item['url'] for item in index} == expected, f'{lang}: incorrect search coverage'
        assert all(item['title'] and item['text'] for item in index), f'{lang}: empty search document'
        assert all('{%' not in item['text'] for item in index), f'{lang}: unresolved Liquid in search'

    css = (site / 'assets/css/just-the-docs-default.css').read_text(encoding='utf-8')
    assert '.hoshi-languages' in css and '<html' not in css, 'Missing or incorrectly wrapped stylesheet'
    assert not (site / 'scripts').exists(), 'Development scripts leaked into site'
    print(f'Output checks passed: {len(documents)} documents, language selectors, local links, metadata, and search indexes.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, help='Also validate a built Jekyll output directory.')
    args = parser.parse_args()
    source_pages = check_sources()
    if args.site:
        check_output(args.site.resolve(), source_pages)

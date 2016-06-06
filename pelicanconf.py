#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DATE_FORMATS = { 'br': ('pt_BR.UTF-8','%d de %B de %Y') }
DEFAULT_DATE_FORMAT = ('%d/%m/%Y')
DEFAULT_LANG = 'pt_BR'
LOCALE='pt_BR'
TIMEZONE = 'America/Sao_Paulo'

AUTHOR = u'318bot'
SITENAME = u'318br ctf-team'
SITEURL = 'http://318br.github.io'

PATH = 'content'

MD_EXTENSIONS = ['codehilite(noclasses=True,linenums=False,guess_lang=False,use_pygments=True,pygments_style=native)', 'extra']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_ORDER_BY = 'reversed-date'
PAGE_ORDER_BY = 'reversed-date'

ARTICLE_URL = 'posts/{date:%Y}-{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}-{date:%m}/{slug}.html'
PAGE_URL = 'posts/{date:%Y}-{date:%m}/{slug}.html'
PAGE_SAVE_AS = 'posts/{date:%Y}-{date:%m}/{slug}.html'

CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

THEME = 'themes/318br'

# Static paths will be copied without parsing their contents
STATIC_PATHS = ['robots.txt', '.dotfile', 'img']

# Links
LINKS = (('atcasanova', 'https://github.com/atcasanova'),
         ('deadcow', 'https://github.com/deadc'),
         ('fallc0nn', 'https://github.com/fallc0nn'),
         ('kirah', 'https://github.com/kirahh'),
         ('Odysseus', 'https://github.com/ualvesdias'),)

# Social
SOCIAL = (('Asciinema (fallc0nn)', 'https://asciinema.org/~fallc0nn'),
          ('CTF-Time', 'https://ctftime.org/team/24500'),
          ('Github', 'https://github.com/318br'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

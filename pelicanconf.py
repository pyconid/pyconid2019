#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PyCon Indonesia'
SITENAME = 'PyCon Indonesia 2019'
SITEURL = ''
SITESUBTITLE = 'Surabaya Python User Group'
DESCRIPTION = 'Surabaya Python User Group'
SITEIMAGE = '/images/logo.png'
TICKETING_SITE_URL = 'https://ticket.pycon.id'

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

THEME = 'themes/eventalk'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images', 'pdfs']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Page Configurations
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

# Article Configurations
ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{slug}'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

# Menu Items configurations
MENUITEMS = (
    # ('About', 'about'),
    ('Sponsor', 'sponsor'),
    ('Participant', 'participant-mail-list'),
    # ('Speak at Pycon ID', 'call-for-paper'),
    ('Code of Conduct', 'code-of-conduct'),
    # ('Speakers', 'speakers'),
    # ('Schedule', 'schedule'),
    # ('Blog', 'blog'),
    # ('Contact', 'contact'),
)
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Christoph Witzany'
SITENAME = u'Distinguishable from Magic'
SITEURL = ''

TIMEZONE = 'Europe/Paris'
LOCALE = 'en_US'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('<i class="fa fa-twitter" title="@DoubleMalt"></i>', 'https://twitter.com/DoubleMalt'),
          ('<i class="fa fa-github" title="@DoubleMalt"></i>', 'https://github.com/DoubleMalt'),
          )

THEME = u'pelican-distiguishable-from-magic'
TAGLINE = (u'Every technology distinguishable ' 
           u'from magic is not advanced enough')
AUTHOR_BIO = (u'Musings about science, technology and freedom '
              u'by the founder of ' 
              u'<a href="https://cloudfleet.io/">cloudfleet.io</a>')

DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 64
TYPOGRIFY = True
WITH_FUTURE_DATES = False


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

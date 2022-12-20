from __future__ import unicode_literals

AUTHOR = 'Crypt-BC-Lab'
SITENAME = 'Sydney Crypto Seminar Series'
SITESUBTITLE = 'Feature Most Exciting Progress in Cryptography & Blockchain'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Australia/Sydney'
DEFAULT_LANG = 'en'

# Theme config
THEME = 'themes/Peli-Kiera'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'neighbors']
STATIC_PATHS = ['images']

# Article summary length on main index page
SUMMARY_MAX_LENGTH = 150
DEFAULT_PAGINATION = 10
GITHUB_URL = 'https://alkistang.github.io/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/'),
    ('github', 'https://github.com/'),
    ('facebook', 'https://facebook.com'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#!/usr/bin/env python

from os.path import dirname, abspath
import sys

import django
from django.conf import settings
from django.core.management import call_command
from django_clickbank import settings as django_clickbank_defaults

INSTALLED_APPS=[
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sites',
	'django_clickbank',
	'django_nose',
]

#see http://django.readthedocs.org/en/latest/releases/1.7.html#standalone-scripts
try:
	django.setup()
except AttributeError:
	pass

from django import VERSION
if VERSION <= (1, 6):
	INSTALLED_APPS.append('south')
	SOUTH_MIGRATION_MODULES = {
        'django_clickbank': 'django_clickbank.south_migrations',
    }
else:
	SOUTH_MIGRATION_MODULES = None  

if not settings.configured:
	settings.configure(
		MIDDLEWARE_CLASSES = (
		    'django.contrib.sessions.middleware.SessionMiddleware',
    		'django.contrib.auth.middleware.AuthenticationMiddleware',
    		'django.contrib.messages.middleware.MessageMiddleware',
		),
		CLICKBANK_DEBUG=False,
		CLICKBANK_STORE_POSTS=True,
		CLICKBANK_KEEP_INVALID=True,
		CLICKBANK_SIGNAL_INVALID=False,
		CLICKBANK_IGNORE_DUPLICATES=False,
		CLICKBANK_SECRET_KEY='76AFC0778E648BDA05705047BAFA96ED',
		ROOT_URLCONF='django_clickbank.urls',
		DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': ':memory:',}},
		INSTALLED_APPS=INSTALLED_APPS,
		TEST_RUNNER = 'django_nose.NoseTestSuiteRunner',
		SOUTH_MIGRATION_MODULES=SOUTH_MIGRATION_MODULES,
		SOUTH_TESTS_MIGRATE=True,
	)


def runtests(*test_args):
	parent = dirname(abspath(__file__))
	sys.path.insert(0, parent)
	
	output = call_command('test', verbosity=1, interactive=True)
	sys.exit(output)


if __name__ == '__main__':
	runtests()
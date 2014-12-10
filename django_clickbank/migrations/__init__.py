from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

"""
Django migrations for django_clickbank app

This package does not contain South migrations.  South migrations can be found
in the ``south_migrations`` package.
"""

SOUTH_ERROR_MESSAGE = """\n
For South support, customize the SOUTH_MIGRATION_MODULES setting like so:

    SOUTH_MIGRATION_MODULES = {
        'django_clickbank': 'django_clickbank.south_migrations',
    }
"""

# Ensure the user is not using Django 1.6 or below with South
try:
    from django.db import migrations  # noqa
except ImportError:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured(SOUTH_ERROR_MESSAGE)

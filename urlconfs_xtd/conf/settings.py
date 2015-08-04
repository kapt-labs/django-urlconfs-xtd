# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

# Third party imports
from django.conf import settings

# Local application / specific library imports


DEFAULT_SCHEME = getattr(settings, 'URLCONFS_XTD_DEFAULT_SCHEME', 'http')

# The following setting should define the url configuration modules
# to use in order to perform url resolutions using them.
# It should contains a dictionary defining each urlconf:
#
# URLCONFS_XTD_URL_CONFIGS = {
#     'site_a': {
#         'domain': 'a.example.com',
#         'urlconf': 'project.app.a.urls',
#      },
#     'site_b': {
#         'domain': 'b.example.com',
#         'urlconf': 'project.app.b.urls',
#      },
# }
URL_CONFIGS = getattr(settings, 'URLCONFS_XTD_URL_CONFIGS', {})

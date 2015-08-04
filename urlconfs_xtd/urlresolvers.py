# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

# Third party imports
from django.core.urlresolvers import NoReverseMatch
from django.core.urlresolvers import reverse
from six.moves.urllib.parse import urlunparse

# Local application / specific library imports
from urlconfs_xtd.conf import settings as urlconfs_settings


def external_reverse(
        viewname, external, args=None, kwargs=None, current_app=None):
    """
    Reverses an external URL from the given parameters.

    :param viewname: the name of the URL
    :param external: the external id whose url config will be used for URL reversing
    :param args: positional arguments used for reversing the URL
    :param kwargs: named arguments used for reversing the URL
    :param current_app: hint for the currently executing application
    """
    try:
        external_conf = urlconfs_settings.URL_CONFIGS.get(external)
        domain = external_conf.get('domain')
        urlconf = external_conf.get('urlconf')
    except KeyError:
        raise NoReverseMatch('Error fetching external url config')
    scheme = external_conf.get('scheme', urlconfs_settings.DEFAULT_SCHEME)

    path = reverse(
        viewname, urlconf=urlconf, args=args, kwargs=kwargs,
        current_app=current_app)
    return urlunparse((scheme, domain, path or '', None, None, None))

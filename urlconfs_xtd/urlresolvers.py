# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

# Third party imports
from django.core.urlresolvers import NoReverseMatch
from django.core.urlresolvers import reverse
from six.moves.urllib.parse import urlunparse

# Local application / specific library imports
from urlconfs_xtd.conf import settings as urlconfs_settings


def xtd_reverse(
        external, viewname=None, args=None, kwargs=None, current_app=None):
    """
    Reverses an external URL from the given parameters. Returns only the domain
    URL if the view name is not defined.

    :param external: the external id whose url config will be used for URL reversing
    :param viewname: the name of the URL
    :param args: positional arguments used for reversing the URL
    :param kwargs: named arguments used for reversing the URL
    :param current_app: hint for the currently executing application
    """
    try:
        external_conf = urlconfs_settings.URL_CONFIGS.get(external)
        domain = external_conf.get('domain')
        urlconf = external_conf.get('urlconf')
    except KeyError:
        raise NoReverseMatch('Error fetching external url config: \'{}\''.format(external))
    scheme = external_conf.get('scheme', urlconfs_settings.DEFAULT_SCHEME)

    path = reverse(
        viewname, urlconf=urlconf, args=args, kwargs=kwargs,
        current_app=current_app) if viewname else ''
    return urlunparse((scheme, domain, path, None, None, None))

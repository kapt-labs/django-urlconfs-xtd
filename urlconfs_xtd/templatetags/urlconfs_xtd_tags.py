# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

# Third party imports
from django import template

# Local application / specific library imports
from urlconfs_xtd.urlresolvers import xtd_reverse


register = template.Library()


@register.simple_tag(takes_context=True)
def xtd_url(context, external, view, *args, **kwargs):
    """
    Resolves an external URL in a template.
    Usage::
        {% load urlconfs_xtd_tags %}
        {% xtd_url 'urlconf-id' 'view-reverse-name' %}
    """
    return xtd_reverse(external, view, args=args, kwargs=kwargs)


@register.simple_tag(takes_context=True)
def xtd_domain(context, external):
    """
    Resolves an external domain in a template.
    Usage::
        {% load urlconfs_xtd_tags %}
        {% xtd_domain 'urlconf-id' %}
    """
    return xtd_reverse(external)

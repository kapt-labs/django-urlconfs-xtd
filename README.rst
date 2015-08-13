===================
django-urlconfs-xtd
===================

*Django helpers for resolving external urls using multiple urlconfs..*

.. contents:: :local:

Installation
-------------

Just run:

::

  pip install git+git://github.com/kapt-labs/django-urlconfs-xtd.git

Once installed you just need to add ``urlconfs_xtd`` to ``INSTALLED_APPS`` in your project's settings module:

::

  INSTALLED_APPS = (
      # other apps
      'urlconfs_xtd',
  )

Configuration
-------------

The url configuration modules you wish to use must be defined in the ``URLCONFS_XTD_URL_CONFIGS`` setting. It allows you to define the Python path of urls modules and the domain to use when resolving urls using these configurations:

::

  URLCONFS_XTD_URL_CONFIGS = {
    'site_a': {
      'domain': 'a.example.com',
      'urlconf': 'project.app.a.urls',
    },
    'site_b': {
      'domain': 'b.example.com',
      'urlconf': 'project.app.b.urls',
      'scheme': 'https',
    },
  }

The first-level keys of this dictionary (eg. ``site_a``) define the identifier of each url configuration. It will be used to specifically resolve urls from each of these configurations. The ``domain`` and the ``urlconf`` Python path are the two values that are really required when defining url configurations.

The ``scheme`` value is optional and defaults to ``http``. You can override this default behavior using the ``URLCONFS_XTD_DEFAULT_SCHEME`` setting:

::

  URLCONFS_XTD_DEFAULT_SCHEME = 'https'

Usage
-------

*Django-urlconfs-xtd* provides a new URL resolver that you can use to resolve urls using the configuration modules defined in your ``URLCONFS_XTD_URL_CONFIGS`` setting. To do this, simply import the ``external_reverse`` function and use it as follows:

::

  >> from urlconfs_xtd.urlresolvers import external_reverse
  >> external_reverse('view-name', 'site_a', kwargs={'slug': 'test'})

``site_a`` defines the URL configuration module to use in order to resolve the ``view-name`` URL with the considered arguments.

As you may need to resolve these URLs inside one your Django template, this URL resolver can be used as a templatetag after loading ``urlconfs_xtd_tags``:

::

  {% load urlconfs_xtd_tags %}
  {% xtd_url 'site_a' 'view-name' slug='test' %}
  {% xtd_domain 'site_a' %}

The ``xtd_url`` templatetag acts like the Django ``url`` tag, you just need to specify the URL configuration to use as its first argument. The ``xtd_domain`` templatetag allows you to retrieve only the domain (and its scheme) related to a specific URL configuration.

Authors
-------

Kapt and Contributors <dev@kapt.mobi>

License
-------

BSD. See ``LICENSE`` for more details.

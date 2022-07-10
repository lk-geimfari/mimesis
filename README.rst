Mimesis: The Fake Data Generator
--------------------------------

|

.. image:: https://raw.githubusercontent.com/lk-geimfari/mimesis/master/.github/images/logo-white-bg.png
     :target: https://github.com/lk-geimfari/mimesis

|

Description
-----------

.. image:: https://github.com/lk-geimfari/mimesis/actions/workflows/test.yml/badge.svg?branch=master
     :target: https://github.com/lk-geimfari/mimesis/actions/workflows/test.yml?query=branch%3Amaster
     :alt: Github Actions Test

.. image:: https://readthedocs.org/projects/mimesis/badge/?version=latest
     :target: https://mimesis.name/en/latest/
     :alt: Documentation Status

.. image:: https://codecov.io/gh/lk-geimfari/mimesis/branch/master/graph/badge.svg
     :target: https://codecov.io/gh/lk-geimfari/mimesis
     :alt: Code Coverage

.. image:: https://www.codefactor.io/repository/github/lk-geimfari/mimesis/badge
   :target: https://www.codefactor.io/repository/github/lk-geimfari/mimesis
   :alt: CodeFactor

.. image:: https://img.shields.io/pypi/v/mimesis?color=bright-green
     :target: https://pypi.org/project/mimesis/
     :alt: PyPi Version

.. image:: https://img.shields.io/pypi/dm/mimesis
     :target: https://pypi.org/project/mimesis/
     :alt: PyPI - Downloads

.. image:: https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%20pypy-brightgreen
     :target: https://pypi.org/project/mimesis/
     :alt: Python version

Mimesis (/mɪˈmiːsɪs) is a high-performance fake data generator for Python,
which provides data for a variety of purposes in a variety of languages. The fake data could be used to populate
a testing database, create fake API endpoints, create JSON and XML files of arbitrary structure, anonymize data taken
from production and etc.

Installation
------------


To install mimesis, simply use pip:

.. code:: bash

    pip install mimesis


Python compatibility
---------------------

Mimesis supports Python 3.8 (also PyPy 3.8), 3.9, and 3.10.

The Mimesis 4.1.3 is the last to support Python 3.6 and 3.7.

Supported Features
------------------

- **Easy**: Designed to be easy to use and learn.
- **Multilingual**: Supports data for `a lot of languages <https://mimesis.name/en/latest/getting_started.html#supported-locales>`_.
- **Performance**: The `fastest <https://mimesis.name/en/latest/about.html#performance>`_ data generator available for Python.
- **Data variety**: Supports `a lot of data providers <https://mimesis.name/en/latest/api.html>`_ for a variety of purposes.
- **Country-specific data providers**: Provides data specific only for `some countries <https://mimesis.name/en/latest/api.html#builtin-data-providers>`_.
- **Extensibility**: You can create your own data providers and use them with Mimesis.
- **Generic data provider**: The `simplified <https://mimesis.name/en/latest/getting_started.html#generic-provider>`_ access to all the providers from a single object.
- **Zero hard dependencies**: Does not require any modules other than the Python standard library.
- **Schema-based generators**: Provides an easy mechanism to generate data by the schema of any complexity.


Documentation
-------------

You can find the complete documentation on the `Read the Docs <https://mimesis.name/en/latest/>`_.

It is divided into several sections:

-  `About Mimesis <https://mimesis.name/en/latest/about.html>`_
-  `Getting Started <https://mimesis.name/en/latest/getting_started.html>`_
-  `Tips and Tricks <https://mimesis.name/en/latest/tips.html>`_
-  `API Reference <https://mimesis.name/en/latest/api.html>`_
-  `Contributing <https://mimesis.name/en/latest/contributing.html>`_
-  `Changelog <https://mimesis.name/en/latest/changelog.html>`_

You can improve it by sending pull requests to this repository.

Usage
-----

This library is really easy to use and everything you need is just import an object which
represents a type of data you need (we call such object a *Provider*).

In the example below we import provider `Person <https://mimesis.name/en/latest/api.html#person>`_,
which represents data related to personal information, such as name, surname, email and etc:

.. code:: python

    >>> from mimesis import Person
    >>> from mimesis.locales import Locale
    >>> person = Person(Locale.EN)

    >>> person.full_name()
    'Brande Sears'

    >>> person.email(domains=['example.com'])
    'roccelline1878@example.com'

    >>> person.email(domains=['mimesis.name'], unique=True)
    'f272a05d39ec46fdac5be4ac7be45f3f@mimesis.name'

    >>> person.telephone(mask='1-4##-8##-5##3')
    '1-436-896-5213'


More about the other providers you can read in our `documentation`_.

.. _documentation: https://mimesis.name/en/latest/getting_started.html#data-providers


Locales
-------

Mimesis currently includes support for 34 different `locales`_. You can
specify a locale when creating providers and they will return data that
is appropriate for the language or country associated with that locale.

Let's take a look how it works:

.. code:: python

    >>> from mimesis import Person
    >>> from mimesis.locales import Locale
    >>> from mimesis.enums import Gender

    >>> de = Person(locale=Locale.DE)
    >>> en = Person(locale=Locale.EN)

    >>> de.full_name(gender=Gender.FEMALE)
    'Sabrina Gutermuth'

    >>> en.full_name(gender=Gender.MALE)
    'Layne Gallagher'


.. _locales: https://mimesis.name/en/latest/getting_started.html#supported-locales

Providers
---------

Mimesis support over twenty different data providers available,
which can produce data related to people, food, computer hardware,
transportation, addresses, internet and more.


You can generate a lot of extremely detailed data:

.. code:: python

    >>> from mimesis import Internet
    >>> from mimesis.enums import URLScheme
    >>> internet = Internet()
    >>> internet.url(scheme=URLScheme.WSS, subdomains=["chat"])
    'wss://chat.system.io/'


See `API Reference <https://mimesis.name/en/latest/api.html>`_ and `Data Providers <https://mimesis.name/en/latest/getting_started.html#data-providers>`_ for more info.

How to Contribute
-----------------

1. Take a look at `contributing guidelines`_.
2. Check for open issues or open a fresh issue to start a discussion
   around a feature idea or a bug.
3. Fork the repository on GitHub to start making your changes to the
   *your_branch* branch.
4. Add yourself to the list of `contributors`_.
5. Send a pull request and bug the maintainer until it gets merged and
   published.

.. _contributing guidelines: https://github.com/lk-geimfari/mimesis/blob/master/CONTRIBUTING.rst
.. _contributors: https://github.com/lk-geimfari/mimesis/blob/master/CONTRIBUTORS.rst


Useful links
------------

I have a Telegram channel where I daily post news, announces and all the open-source
goodies I found, so subscribe: `@software_dev_channel <https://t.me/software_dev_channel>`_.

Disclaimer
----------

The authors of `Mimesis` do not assume any responsibility for how you use it or how you use data generated with it.
This library was designed with good intentions to make testing easier. Do not use the data generated with Mimesis for illegal purposes.

License
-------

Mimesis is licensed under the MIT License. See `LICENSE`_ for more
information.

.. _LICENSE: https://github.com/lk-geimfari/mimesis/blob/master/LICENSE

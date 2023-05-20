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

.. image:: https://img.shields.io/pypi/v/mimesis?color=bright-green
     :target: https://pypi.org/project/mimesis/
     :alt: PyPi Version

.. image:: https://img.shields.io/pypi/dm/mimesis
     :target: https://pypi.org/project/mimesis/
     :alt: PyPI - Downloads

.. image:: https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%20pypy-brightgreen
     :target: https://pypi.org/project/mimesis/
     :alt: Python version


Mimesis (`/mɪˈmiːsɪs <https://mimesis.name/en/master/about.html#what-does-name-mean>`_) is a robust data generator for Python that can produce a wide range of fake data in various languages. This tool is useful for populating testing databases, creating fake API endpoints, generating JSON and XML files with custom structures, and anonymizing production data, among other purposes.

Installation
------------


To install mimesis, simply use pip:

.. code:: bash

    pip install mimesis


Python compatibility
---------------------

Mimesis is compatible with Python, including PyPy, version 3.8 or higher. The Mimesis 4.1.3 is the last release that accommodates Python 3.6 and 3.7.

To prevent unintended upgrades, it is highly advisable to always specify the version of mimesis that you are using by pinning it.

Supported Features
------------------

- **Easy**: A simple design and clear documentation for easy and swift data generation.
- **Multilingual**: Mimesis generates data in a vast range of `languages <https://mimesis.name/en/latest/getting_started.html#supported-locales>`_.
- **Performance**: Mimesis has excellent performance and is widely regarded as the fastest data generator among all Python solutions available.
- **Data variety**: Mimesis supports a broad range of data providers, including names, addresses, phone numbers, email addresses, dates, times, and more, enabling users to generate data for various purposes.
- **Country-specific data providers**: Mimesis supports country-specific data providers for generating country-specific data.
- **Extensibility**: Mimesis is extensible, allowing developers to create and integrate their own data providers with the library.
- **Generic data provider**: Mimesis provides a generic data provider that offers easy access to all the available data providers within the library from a single object.
- **Zero hard dependencies**: Mimesis has zero hard dependencies and does not require the installation of any thrid-party libraries.
- **Schema-based generators**: Mimesis provides schema-based data generators, offering an effortless way to produce data by the schema of any complexity.

Documentation
-------------

You can find the complete documentation on the `Read the Docs <https://mimesis.name/en/latest/>`_.

It is divided into several sections:

-  `About Mimesis <https://mimesis.name/en/latest/about.html>`_
-  `Quickstart <https://mimesis.name/en/master/quickstart.html>`_
-  `Locales <https://mimesis.name/en/master/locales.html>`_
-  `Data Providers <https://mimesis.name/en/master/providers.html>`_
-  `Structured Data Generation <https://mimesis.name/en/master/schema.html>`_
-  `Random and Seed <https://mimesis.name/en/master/random_and_seed.html>`_
-  `Tricks and Tips <https://mimesis.name/en/master/tips.html>`_
-  `API Reference <https://mimesis.name/en/master/index.html#api-reference>`_
-  `Additional Information <https://mimesis.name/en/master/index.html#additional-information>`_
-  `Changelog <https://mimesis.name/en/master/index.html#changelog>`_

You can improve it by sending pull requests to this repository.

Usage
-----

The library is exceptionally user-friendly, and it only requires you to import a **Data Provider** object that corresponds to the desired data type.

For instance, the `Person <https://mimesis.name/en/latest/api.html#person>`_ provider can be imported to access personal information, including name, surname, email, and other related fields:

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

Mimesis presently encompasses 34 distinct `locales`_, enabling users to specify the desired region and language when creating providers.

Here's how it operates practically:

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

Mimesis provides more than twenty data providers which can generate a broad range of data related to food, transportation, computer hardware, people, internet, addresses, and more.

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


Disclaimer
----------

The creators of `Mimesis` do not hold themselves accountable for how you employ the library's functionalities or the data generated with it.
Mimesis is designed to facilitate testing and with good intentions. Mimesis should not be used for illicit purposes.

License
-------

Mimesis is licensed under the MIT License. See `LICENSE`_ for more
information.

.. _LICENSE: https://github.com/lk-geimfari/mimesis/blob/master/LICENSE

Mimesis: The Fake Data Generator
--------------------------------

|

.. image:: https://raw.githubusercontent.com/lk-geimfari/mimesis/master/.github/images/logo.png
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

.. image:: https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%20pypy-brightgreen
     :target: https://pypi.org/project/mimesis/
     :alt: Python version


Mimesis (`/mɪˈmiːsɪs <https://mimesis.name/en/master/about.html#what-does-name-mean>`_) is a robust data generator for Python that can produce a wide range of fake data in various languages. This tool is useful for populating testing databases, creating fake API endpoints, filling pandas ``DataFrames``, generating JSON and XML files with custom structures, and anonymizing production data, among other purposes.

Installation
------------


To install mimesis, simply use pip:

.. code:: bash

    pip install mimesis

To work with Mimesis on Python versions 3.8 and 3.9, the final compatible version is Mimesis 11.1.0.
Install this specific version to ensure compatibility.

Features
--------

- **Multilingual**: Supports 35 different locales.
- **Extensibility**: Supports custom data providers and custom field handlers.
- **Ease of use**: Features a simple design and clear documentation for straightforward data generation.
- **Performance**: Widely recognized as the fastest data generator among Python solutions.
- **Data variety**: Includes various data providers designed for different use cases.
- **Schema-based generators**: Offers schema-based data generators to effortlessly produce data of any complexity.
- **Intuitive**: Great editor support. Fully-typed, thus autocompletion almost everywhere.

Documentation
-------------

You can find the complete documentation on the `Read the Docs`_.

It is divided into several sections:

-  `About Mimesis`_
-  `Quickstart`_
-  `Locales`_
-  `Data Providers`_
-  `Structured Data Generation`_
-  `Random and Seed`_
-  `Integration with Pytest`_
-  `Integration with factory_boy`_
-  `Tricks and Tips`_
-  `API Reference`_
-  `Additional Information`_
-  `Changelog`_

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


You can learn more about other providers and locales in our `documentation`_.


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


License
-------

Mimesis is licensed under the MIT License. See `LICENSE`_ for more
information.

.. _Locales: https://mimesis.name/en/master/locales.html
.. _LICENSE: https://github.com/lk-geimfari/mimesis/blob/master/LICENSE
.. _API Reference: https://mimesis.name/en/master/api.html
.. _Data Providers: https://mimesis.name/en/master/getting_started.html#data-providers
.. _Read the Docs: https://mimesis.name/en/master/
.. _About Mimesis: https://mimesis.name/en/latest/about.html
.. _Quickstart: https://mimesis.name/en/master/quickstart.html
.. _Structured Data Generation: https://mimesis.name/en/master/schema.html
.. _Random and Seed: https://mimesis.name/en/master/random_and_seed.html
.. _Tricks and Tips: https://mimesis.name/en/master/tips.html
.. _Additional Information: https://mimesis.name/en/master/index.html#additional-information
.. _Changelog: https://mimesis.name/en/master/index.html#changelog
.. _documentation: https://mimesis.name/en/latest/getting_started.html#data-providers
.. _contributing guidelines: https://github.com/lk-geimfari/mimesis/blob/master/CONTRIBUTING.rst
.. _contributors: https://github.com/lk-geimfari/mimesis/blob/master/CONTRIBUTORS.rst
.. _Integration with Pytest: https://mimesis.name/en/master/pytest_plugin.html
.. _Integration with factory_boy: https://mimesis.name/en/master/factory_plugin.html

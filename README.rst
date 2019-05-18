Mimesis - Fake Data Generator
-----------------------------

|

.. image:: https://raw.githubusercontent.com/lk-geimfari/mimesis/master/media/readme-logo.png
     :target: https://github.com/lk-geimfari/mimesis

|

Description
-----------

.. image:: https://travis-ci.org/lk-geimfari/mimesis.svg?branch=master
     :target: https://travis-ci.org/lk-geimfari/mimesis
     :alt: Travi CI

.. image:: https://ci.appveyor.com/api/projects/status/chj8huslvn6vde18?svg=true
     :target: https://ci.appveyor.com/project/lk-geimfari/mimesis
     :alt: AppVeyor CI

.. image:: https://readthedocs.org/projects/mimesis/badge/?version=latest
     :target: https://mimesis.name/
     :alt: Documentation Status

.. image:: https://codecov.io/gh/lk-geimfari/mimesis/branch/master/graph/badge.svg
     :target: https://codecov.io/gh/lk-geimfari/mimesis
     :alt: Code Coverage

.. image:: https://badge.fury.io/py/mimesis.svg
     :target: https://badge.fury.io/py/mimesis
     :alt: Package version

.. image:: https://img.shields.io/badge/python-3.6%20%7C%203.7-brightgreen.svg
     :target: https://badge.fury.io/py/mimesis
     :alt: Python version



Mimesis is a package for Python, which helps generate big volumes of fake data for a variety of purposes in a variety of languages. The fake data could be used to populate a testing database, create beautiful JSON and XML files, anonymize data taken from production and etc.


Installation
------------

To install mimesis, simply use pip:

.. code:: text

    [env] ~ ⟩ pip install mimesis

Getting started
---------------

This library is really easy to use and everything you need is just import an object which
represents a type of data you need (we call such object *Provider*).

In example below we import provider `Person <https://mimesis.name/api.html#person>`_,
which represents data related to personal information, such as name, surname, email and etc:

.. code:: python

    >>> from mimesis import Person
    >>> person = Person('en')

    >>> person.full_name()
    'Antonetta Garrison'

    >>> person.occupation()
    'Backend Developer'
    
    >>> person.telephone()
    '1-408-855-5063'


More about the other providers you can read in our `documentation`_.

.. _documentation: https://mimesis.name/getting_started.html#providers


Locales
-------

Mimesis currently includes support for 33 different `locales`_. You can
specify a locale when creating providers and they will return data that
is appropriate for the language or country associated with that locale.

Let's take a look how it works:

.. code:: python

    >>> from mimesis import Person
    >>> from mimesis.enums import Gender

    >>> de = Person('de')
    >>> en = Person('en')

    >>> de.full_name(gender=Gender.FEMALE)
    'Sabrina Gutermuth'

    >>> en.full_name(gender=Gender.MALE)
    'Layne Gallagher'

.. _locales: https://mimesis.name/getting_started.html#locales

Providers
---------

Mimesis support over twenty different data providers available,
which can produce data related to people, food, computer hardware,
transportation, addresses, and more.

See `API Reference <https://mimesis.name/api.html>`_ for more info.


Documentation
-------------

You can find the complete documentation on the `Read the Docs`_.

It is divided into several sections:

-  `Foreword`_
-  `Getting Started`_
-  `Tips and Tricks`_
-  `API Reference`_
-  `Contributing`_
-  `Changelog`_

You can improve it by sending pull requests to this repository.

.. _Read the Docs: https://mimesis.name
.. _Foreword: https://mimesis.name/foreword.html
.. _Getting Started: https://mimesis.name/getting_started.html
.. _Tips and Tricks: https://mimesis.name/tips.html
.. _API Reference: https://mimesis.name/api.html
.. _Contributing: https://mimesis.name/contributing.html
.. _Changelog: https://mimesis.name/changelog.html


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


License
-------

Mimesis is licensed under the MIT License. See `LICENSE`_ for more
information.

.. _LICENSE: https://github.com/lk-geimfari/mimesis/blob/master/LICENSE

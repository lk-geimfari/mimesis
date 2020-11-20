Mimesis - Fake Data Generator
-----------------------------

|

.. image:: https://raw.githubusercontent.com/lk-geimfari/mimesis/master/media/readme-logo.png
     :target: https://github.com/lk-geimfari/mimesis

|

Description
-----------

.. image:: https://github.com/lk-geimfari/mimesis/workflows/test/badge.svg?branch=master
     :target: https://github.com/lk-geimfari/mimesis/actions
     :alt: Github Actions Test

.. image:: https://readthedocs.org/projects/mimesis/badge/?version=latest
     :target: https://mimesis.name/
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

.. image:: https://img.shields.io/badge/python-3.6+-brightgreen.svg
     :target: https://badge.fury.io/py/mimesis
     :alt: Python version

Mimesis is a high-performance fake data generator for Python, which provides data for a variety of
purposes in a variety of languages. The fake data could be used to populate a testing database,
create fake API endpoints, create JSON and XML files of arbitrary structure, anonymize data taken
from production and etc.

The key features are:

- **Performance**: The `fastest <https://mimesis.name/foreword.html#performance>`_ data generator available for Python.
- **Extensibility**: You can create your own data providers and use them with Mimesis.
- **Generic data provider**: The `simplified <https://mimesis.name/getting_started.html#generic-provider>`_ access to all the providers from a single object.
- **Multilingual**: Supports data for `a lot of languages <https://mimesis.name/getting_started.html#locales>`_.
- **Data variety**: Supports `a lot of data providers <https://mimesis.name/api.html>`_ for a variety of purposes.
- **Schema-based generators**: Provides an easy mechanism to generate data by the schema of any complexity.
- **Country-specific data providers**: Provides data specific only for `some countries <https://mimesis.name/api.html#builtin-data-providers>`_.


Installation
------------


To install mimesis, simply use pip:

.. code:: text

    [venv] ~ ⟩ pip install mimesis

Usage
-----

This library is really easy to use and everything you need is just import an object which
represents a type of data you need (we call such object *Provider*).

In example below we import provider `Person <https://mimesis.name/api.html#person>`_,
which represents data related to personal information, such as name, surname, email and etc:

.. code:: python

    >>> from mimesis import Person
    >>> person = Person('en')

    >>> person.full_name()
    'Brande Sears'

    >>> person.email(domains=['mimesis.name'])
    'roccelline1878@mimesis.name'

    >>> person.email(domains=['mimesis.name'], unique=True)
    'f272a05d39ec46fdac5be4ac7be45f3f@mimesis.name'

    >>> person.telephone(mask='1-4##-8##-5##3')
    '1-436-896-5213'


More about the other providers you can read in our `documentation`_.

.. _documentation: https://mimesis.name/getting_started.html#providers


Locales
-------

Mimesis currently includes support for 34 different `locales`_. You can
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
transportation, addresses, internet and more.

See `API Reference <https://mimesis.name/api.html>`_ for more info.

The data providers are **heavy objects** since each instance of provider keeps in memory all
the data from the provider's JSON file so you **should not** construct too many providers.


Generating structured data
--------------------------

You can generate dictionaries which can be easily converted to any
the format you want (JSON/XML/YAML etc.)  with any structure you want.

Let's build dummy API endpoint, using Flask to illustrate the idea:

.. code:: python

     from flask import Flask, jsonify, request
     from mimesis.schema import Field, Schema
     from mimesis.enums import Gender

     app = Flask(__name__)


     @app.route('/apps', methods=('GET',))
     def apps_view():
         locale = request.args.get('locale', default='en', type=str)
         count = request.args.get('count', default=1, type=int)

         _ = Field(locale)

         schema = Schema(schema=lambda: {
             'id': _('uuid'),
             'name': _('text.word'),
             'version': _('version', pre_release=True),
             'timestamp': _('timestamp', posix=False),
             'owner': {
                 'email': _('person.email', domains=['test.com'], key=str.lower),
                 'token': _('token_hex'),
                 'creator': _('full_name', gender=Gender.FEMALE)},
         })
         data = schema.create(iterations=count)
         return jsonify(data)

Below, on the screenshot, you can see a response from this fake API (``/apps``):

.. image:: https://user-images.githubusercontent.com/15812620/84743283-64e92400-afba-11ea-8252-76e2ea168972.png
     :target: https://mimesis.name/getting_started.html#schema-and-fields
     :alt: Schema and Fields

See `Schema and Fields <https://mimesis.name/getting_started.html#schema-and-fields>`_ for more info.

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



Thanks
------

Supported by `JetBrains <https://www.jetbrains.com/?from=mimesis>`_.


Disclaimer
----------

The authors of `Mimesis` do not assume any responsibility for how you use it or how you use data generated with it. This library was designed with good intentions to make testing easier. Do not use the data generated with Mimesis for illegal purposes.

License
-------

Mimesis is licensed under the MIT License. See `LICENSE`_ for more
information.

.. _LICENSE: https://github.com/lk-geimfari/mimesis/blob/master/LICENSE

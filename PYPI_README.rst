.. image:: https://raw.githubusercontent.com/lk-geimfari/mimesis/master/media/large-logo.png
    :target: https://github.com/lk-geimfari/mimesis



Mimesis
-------

|Build Status| |Build status on Windows| |codecov| |PyPI version|
|Python|

**Mimesis** is a fast and easy to use library for Python programming
language, which helps generate mock data for a variety of purposes (see
"`Data providers <#data-providers>`__") in a variety of languages (see
"`Locales <#locales>`__"). This data can be particularly useful during
software development and testing. For example, it could be used to
populate a testing database for a web application with user information
such as email addresses, usernames, first names, last names, etc.

Mimesis offers a number of advantages over other similar libraries, such
as Faker:

-  Performance. Mimesis is significantly
   `faster <http://i.imgur.com/pCo6yPA.png>`__ than other similar
   libraries.
-  Completeness. Mimesis strives to provide many detailed providers that
   offer a variety of data generators.
-  Simplicity. Mimesis does not require any modules other than the
   Python standard library.

See
`here <https://gist.github.com/lk-geimfari/461ce92fd32379d7b73c9e12164a9154>`__
for an example of how we compare performance with other libraries.

Documentation
-------------

Mimesis is very simple to use, and the below examples should help you
get started. Complete documentation for Mimesis is available on `Read
the Docs <http://mimesis.readthedocs.io/>`__.

Installation
------------

To install mimesis, simply:

.. code:: zsh

    ➜  ~ pip install mimesis

**Note**: Version ``1.0.0`` has suffered significant
changes, so there is no backwards
compatibility with earlier versions of this library.

Getting started
---------------

As we said above, this library is really easy to use. A simple usage
example is given below:

.. code:: python

    >>> from mimesis import Personal
    >>> from mimesis.enums import Gender
    >>> person = Personal('en')

    >>> person.full_name(gender=Gender.FEMALE)
    'Antonetta Garrison'

    >>> person.occupation()
    'Backend Developer'

    >>> templates = ['U_d', 'U-d', 'l_d', 'l-d']
    >>> for template in templates:
    ...     person.username(template=template)

    'Adders_1893'
    'Abdel-1888'
    'constructor_1884'
    'chegre-2051'

Locales
-------

You can specify a locale when creating providers and they will return
data that is appropriate for the language or country associated with
that locale:

.. code:: python

    >>> from mimesis import Personal

    >>> de = Personal('de')
    >>> fr = Personal('fr')
    >>> pl = Personal('pl')

    >>> de.full_name()
    'Sabrina Gutermuth'

    >>> fr.full_name()
    'César Bélair

    >>> pl.full_name()
    'Światosław Tomankiewicz'

Mimesis currently includes support for 33 different locales. See `details <http://mimesis.readthedocs.io/locales.html>`__ for more information.

When you only need to generate data for a single locale, use the
``Generic()`` provider, and you can access all providers of Mimesis from
one object.

.. code:: python

    >>> from mimesis import Generic
    >>> from mimesis.enums import TLDType
    >>> g = Generic('es')

    >>> g.datetime.month()
    'Agosto'

    >>> g.food.fruit()
    'Limón'

    >>> g.internet.top_level_domain(TLDType.GEOTLD)
    '.moscow'


Data Providers
--------------

Mimesis support over twenty different data providers available, which can produce data related to food, people, computer hardware, transportation, addresses, and more. See `details <http://mimesis.readthedocs.io/providers.html>`__ for more information.


Custom Providers
----------------

You also can add custom provider to ``Generic()``, using
``add_provider()`` method:

.. code:: python

    >>> from mimesis import Generic
    >>> from mimesis.providers import BaseProvider
    >>> generic = Generic('en')

    >>> class SomeProvider(BaseProvider):
    ...     class Meta:
    ...         name = "some_provider"
    ...
    ...     def hello(self):
    ...         return "Hello!"

    >>> class Another(BaseProvider):
    ...     def bye(self):
    ...         return "Bye!"

    >>> generic.add_provider(SomeProvider)
    >>> generic.add_provider(Another)

    >>> generic.some_provider.hello()
    'Hello!'

    >>> generic.another.bye()
    'Bye!'

or multiple custom providers using method ``add_providers()``:

.. code:: python

    >>> generic.add_providers(SomeProvider, Another)


Builtins specific data providers
--------------------------------

Some countries have data types specific to that country. For example
«Social Security Number» (SSN) in the United States of America (``en``),
and «Cadastro de Pessoas Físicas» (CPF) in Brazil (``pt-br``). If you
would like to use these country-specific providers, then you must import
them explicitly:

.. code:: python

    >>> from mimesis import Generic
    >>> from mimesis.builtins import BrazilSpecProvider

    >>> generic = Generic('pt-br')
    >>> generic.add_provider(BrazilSpecProvider)
    >>> generic.brazil_provider.cpf()
    '696.441.186-00'

You can use specific-provider without adding it to ``Generic()``:

.. code:: python

    >>> BrazilSpecProvider().cpf()
    '712.455.163-37'

Generate data by schema
-----------------------

For generating data by schema, just create an instance of ``Field`` object,
which take any string which represents name of the any method of any
supported data provider and the ``**kwargs`` of the method, after that
you should describe the schema in lambda function and run filling the
schema using method ``fill()``:

.. code:: python

    >>> from mimesis.schema import Field
    >>> from mimesis.enums import Gender
    >>> _ = Field('en')
    >>> app_schema = (
    ...     lambda: {
    ...         "id": _('uuid'),
    ...         "name": _('word'),
    ...         "version": _('version'),
    ...         "owner": {
    ...             "email": _('email'),
    ...             "token": _('token'),
    ...             "creator": _('full_name', gender=Gender.FEMALE),
    ...         },
    ...     }
    ... )
    >>> _.fill(schema=app_schema, iterations=10)

Mimesis support generating data by schema only starting from version
``1.0.0``.

Integration with py.test and factory\_boy
-----------------------------------------

We have created libraries which can help you easily use Mimesis with
``factory_boy`` and ``py.test``.

-  `mimesis-factory <https://github.com/mimesis-lab/mimesis-factory>`__
   - Integration with the ``factory_boy``.
-  `pytest-mimesis <https://github.com/mimesis-lab/pytest-mimesis>`__ -
   Integration with the ``py.test``.

How to Contribute
-----------------

1. Fork it
2. Take a look at contributions `guidelines </CONTRIBUTING.md>`__
3. Create your feature branch (``git checkout -b feature/new_locale``)
4. Commit your changes (``git commit -am 'Add new_locale'``)
5. Add yourself to list of contributors
6. Push to the branch (``git push origin feature/new_locale``)
7. Create a new Pull Request

License
-------

Mimesis is licensed under the MIT License. See
`LICENSE <https://github.com/lk-geimfari/mimesis/blob/master/LICENSE>`__
for more information.

Disclaimer
----------

The authors assume no responsibility for how you use this library data
generated by it. This library is designed only for developers with good
intentions. Do not use the data generated with Mimesis for illegal
purposes.

.. |Build Status| image:: https://travis-ci.org/lk-geimfari/mimesis.svg?branch=master
   :target: https://travis-ci.org/lk-geimfari/mimesis
.. |Build status on Windows| image:: https://ci.appveyor.com/api/projects/status/chj8huslvn6vde18?svg=true
   :target: https://ci.appveyor.com/project/lk-geimfari/mimesis
.. |codecov| image:: https://codecov.io/gh/lk-geimfari/mimesis/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lk-geimfari/mimesis
.. |PyPI version| image:: https://badge.fury.io/py/mimesis.svg
   :target: https://badge.fury.io/py/mimesis
.. |Python| image:: https://img.shields.io/badge/python-3.5%2C%203.6-brightgreen.svg
   :target: https://badge.fury.io/py/mimesis


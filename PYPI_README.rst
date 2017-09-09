.. image:: https://raw.githubusercontent.com/lk-geimfari/mimesis/master/media/logo.png
    :target: https://github.com/lk-geimfari/mimesis


=========================


.. image:: https://travis-ci.org/lk-geimfari/mimesis.svg?branch=master
    :target: https://travis-ci.org/lk-geimfari/mimesis

.. image:: https://readthedocs.org/projects/mimesis/badge/?version=latest
	:target: http://mimesis.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. image:: https://badge.fury.io/py/mimesis.svg
    :target: https://badge.fury.io/py/mimesis

.. image:: https://img.shields.io/badge/python-v3.3%2C%20v3.4%2C%20v3.5%2C%20v3.6-brightgreen.svg
    :target: https://github.com/lk-geimfari/mimesis/


`Mimesis <https://github.com/lk-geimfari/mimesis>`_ is a fast and easy to use Python library for generating dummy data for a variety of purposes. This data can be particularly useful during software development and testing. For example, it could be used to populate a testing database for a web application with user information such as email addresses, usernames, first names, last names, etc.

Mimesis uses a JSON-based datastore and does not require any modules that are not in the Python standard library. There are over nineteen different data providers available, which can produce data related to food, people, computer hardware, transportation, addresses, and more.


Documentation
-------------

Complete documentation for Mimesis is available here: http://mimesis.readthedocs.io/


Installation
------------

To install Mimesis, simply:

.. code-block:: bash

    ➜  ~ pip install mimesis

Basic Usage:

.. code-block:: python

    >>> from mimesis import Personal, Address
    >>> person = Personal('en')
    >>> address = Address('en')

    >>> person.full_name(gender='female')
    'Antonetta Garrison'

    >>> person.email(gender='male')
    'oren5936@live.com'

    >>> person.occupation()
    'Programmer'

    >>> address.address()
    '713 Rock Stravenue'

    >>> address.city()
    'Dumont'

    >>> address.country()
    'Switzerland'

    >>> address.country_iso(fmt='iso2')
    'WF'

    >>> address.country_iso(fmt='iso3')
    'BFA'

    >>> address.country_iso(fmt='numeric')
    '744'

    >>> address.continent()
    'South America'


Locales
-------

You can specify a locale when creating providers and they will return data that is appropriate for the language or country associated with that locale. Mimesis currently includes support for `32 <https://github.com/lk-geimfari/mimesis#locales>`_ different locales.

Using locales:

.. code-block:: python

    >>> from mimesis import Personal

    >>> en = Personal('en')
    >>> de = Personal('de')
    >>> ic = Personal('is')

    >>> en.full_name()
    'Carolin Brady'

    >>> de.full_name()
    'Sabrina Gutermuth'

    >>> ic.full_name()
    'Rósa Þórlindsdóttir'


When you only need to generate data for a single locale, use the `Generic` provider, and you can access all `Mimesis`
providers from one object.

.. code:: python

    >>> from mimesis import Generic
    >>> g = Generic('es')

    >>> g.datetime.month()
    'Agosto'

    >>> g.code.imei()
    '353918052107063'

    >>> g.food.fruit()
    'Limón'


Advantages
----------

Mimesis offers a number of advantages over other similar
libraries, such as Faker:

-  Performance. Mimesis is significantly `faster`_ than other
   similar libraries.
-  Completeness. Mimesis strives to provide many detailed
   providers that offer a variety of data generators.
-  Simplicity. Mimesis does not require any modules other than the
   Python standard library.

See `here`_ for an example of how we compare performance with other
libraries.

.. _faster: http://i.imgur.com/ZqkE1k2.png
.. _here: https://gist.github.com/lk-geimfari/461ce92fd32379d7b73c9e12164a9154


Custom Providers
----------------

You also can add custom provider to ``Generic``.

.. code:: python

    >>> class SomeProvider():
    ...
    ...     class Meta:
    ...         name = "some_provider"
    ...
    ...     @staticmethod
    ...     def one():
    ...         return 1

    >>> class Another():
    ...
    ...     @staticmethod
    ...     def bye():
    ...         return "Bye!"

    >>> generic.add_provider(SomeProvider)
    >>> generic.add_provider(Another)

    >>> generic.some_provider.one()
    1

    >>> generic.another.bye()
    'Bye!'


Builtins specific data providers
--------------------------------

Some countries have data types specific to that country. For example
social security numbers in the United States (``en`` locale), and
cadastro de pessoas físicas (CPF) in Brazil (``pt-br`` locale).

If you would like to use these country-specific providers, then you must
import them explicitly:

.. code:: python

    >>> from mimesis import Generic
    >>> from mimesis.builtins.pt_br import BrazilSpecProvider

    >>> generic = Generic('pt-br')

    >>> class BrazilProvider(BrazilSpecProvider):
    ...
    ...     class Meta:
    ...         name = "brazil_provider"
    ...
    >>> generic.add_provider(BrazilProvider)
    >>> generic.brazil_provider.cpf()
    '696.441.186-00'


Decorators
----------

If your locale is cyrillic, but you need latinized locale-specific data,
then you can use special decorator. At this moment it’s work only for
Russian:

.. code:: python

    >>> from mimesis import Personal
    >>> from mimesis.decorators import romanized

    >>> pr = Personal('ru')

    >>> @romanized('ru')
    ... def get_name_ro():
    ...     return pr.full_name()
    ...

    >>> def get_name_ru():
    ...     return pr.full_name()
    ...

    >>> get_name_ru()
    'Вида Панова'

    >>> get_name_ro()
    'Veronika Denisova'


Disclaimer
----------

The authors assume no responsibility for how you use this library data
generated by it. This library is designed only for developers with good
intentions. Do not use the data generated with ``Mimesis`` for illegal
purposes.

.. _contribution: https://github.com/lk-geimfari/mimesis/blob/master/CONTRIBUTING.md
.. _LICENSE: https://github.com/lk-geimfari/mimesis/blob/master/LICENSE


Author
------

`Likid Geimfari <https://github.com/lk-geimfari>`_ (likid.geimfari@gmail.com)

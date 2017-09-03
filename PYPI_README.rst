.. image:: https://raw.githubusercontent.com/lk-geimfari/mimesis/master/media/logo.png
    :target: https://github.com/lk-geimfari/mimesis


**Mimesis** is a fast and easy to use library for Python, which helps
generate mock data for a variety of purposes (see "Data providers")
in a variety of languages (see "Locales"). This data can be particularly useful during software development and testing.
The library was written with the use of tools from the standard Python library, and therefore, it does not have any side dependencies.

|Build Status| |Build status on Windows| |codecov| |PyPI version|
|Python|

Advantages
----------

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
get started. Complete documentation for Mimesis is available
`here <http://mimesis.readthedocs.io/>`__.

Installation
------------

To install mimesis, simply:

.. code:: zsh

    ➜  ~ pip install mimesis

Basic Usage
-----------

As we said above, this library is really easy to use:

.. code:: python

    >>> import mimesis
    >>> person = mimesis.Personal(locale='en')

    >>> person.full_name(gender='female')
    'Antonetta Garrison'

    >>> person.occupation()
    'Backend Developer'

Locales
-------

You can specify a locale when creating providers and they will return
data that is appropriate for the language or country associated with
that locale:

.. code:: python

    >>> from mimesis import Personal

    >>> de = Personal('de')
    >>> ic = Personal('is')

    >>> de.full_name()
    'Sabrina Gutermuth'

    >>> ic.full_name()
    'Rósa Þórlindsdóttir'

Mimesis currently includes support for 31 different locales. See `here`_.

.. _here: https://github.com/lk-geimfari/mimesis#locales

When you only need to generate data for a single locale, use the
``Generic()`` provider, and you can access all providers of Mimesis from
one object.

.. code:: python

    >>> import mimesis
    >>> g = mimesis.Generic('es')

    >>> g.datetime.month()
    'Agosto'

    >>> g.food.fruit()
    'Limón'

Data providers
--------------

Mimesis support over twenty different data providers available, which
can produce data related to food, people, computer hardware,
transportation, addresses, and more. See details for more information.

+------+-----------------+------------------------------------------------------------------+
| №    | Provider        | Description                                                      |
+======+=================+==================================================================+
| 1    | Address         | *Address data (street name, street suffix etc.)*                 |
+------+-----------------+------------------------------------------------------------------+
| 2    | Business        | *Business data (company, company\_type, copyright etc.)*         |
+------+-----------------+------------------------------------------------------------------+
| 3    | Code            | *Codes (ISBN, EAN, IMEI etc.).*                                  |
+------+-----------------+------------------------------------------------------------------+
| 4    | ClothingSizes   | *Clothing sizes (international sizes, european etc.)*            |
+------+-----------------+------------------------------------------------------------------+
| 5    | Datetime        | *Datetime (day\_of\_week, month, year etc.)*                     |
+------+-----------------+------------------------------------------------------------------+
| 6    | Development     | *Data for developers (version, programming language etc.)*       |
+------+-----------------+------------------------------------------------------------------+
| 7    | File            | *File data (extension etc.)*                                     |
+------+-----------------+------------------------------------------------------------------+
| 8    | Food            | *Information on food (vegetables, fruits, measurements etc.)*    |
+------+-----------------+------------------------------------------------------------------+
| 9    | Games           | *Games data (game, score, pegi\_rating etc.)*                    |
+------+-----------------+------------------------------------------------------------------+
| 10   | Personal        | *Personal data (name, surname, age, email etc.)*                 |
+------+-----------------+------------------------------------------------------------------+
| 11   | Text            | *Text data (sentence, title etc.)*                               |
+------+-----------------+------------------------------------------------------------------+
| 12   | Transport       | *Dummy data about transport (truck model, car etc.)*             |
+------+-----------------+------------------------------------------------------------------+
| 13   | Science         | *Scientific data (scientist, math\_formula etc.)*                |
+------+-----------------+------------------------------------------------------------------+
| 14   | Structured      | *Structured data (html, css etc.)*                               |
+------+-----------------+------------------------------------------------------------------+
| 15   | Internet        | *Internet data (facebook, twitter etc.)*                         |
+------+-----------------+------------------------------------------------------------------+
| 16   | Hardware        | *The data about the hardware (resolution, cpu, graphics etc.)*   |
+------+-----------------+------------------------------------------------------------------+
| 17   | Numbers         | *Numerical data (floats, primes, digit etc.)*                    |
+------+-----------------+------------------------------------------------------------------+
| 18   | Path            | *Provides methods and property for generate paths.*              |
+------+-----------------+------------------------------------------------------------------+
| 19   | UnitSytem       | *Provides names of unit systems in international format*         |
+------+-----------------+------------------------------------------------------------------+
| 20   | Generic         | *All at once*                                                    |
+------+-----------------+------------------------------------------------------------------+
| 21   | Cryptographic   | *Cryptographic data*                                             |
+------+-----------------+------------------------------------------------------------------+


Custom Providers
----------------

You also can add custom provider to ``Generic()``, using
``add_provider()`` method:

.. code:: python

    >>> import mimesis
    >>> generic = mimesis.Generic('en')

    >>> class SomeProvider(object):
    ...     class Meta:
    ...         name = "some_provider"
    ...
    ...     def hello(self):
    ...         return "Hello!"

    >>> class Another(object):
    ...     def bye(self):
    ...         return "Bye!"

    >>> generic.add_provider(SomeProvider)
    >>> generic.add_provider(Another)

    >>> generic.some_provider.hi()
    'Hello!'

    >>> generic.another.bye()
    'Bye!'

or multiple custom providers using method ``add_providers()``:

.. code:: python

    >>> generic.add_providers(SomeProvider, Another)

Builtins specific data providers
--------------------------------

Some countries have data types specific to that country. For example
social security numbers (SSN) in the United States of America (``en``),
and cadastro de pessoas físicas (CPF) in Brazil (``pt-br``). If you
would like to use these country-specific providers, then you must import
them explicitly:

.. code:: python

    >>> from mimesis import Generic
    >>> from mimesis.builtins import BrazilSpecProvider

    >>> generic = Generic('pt-br')
    >>> generic.add_provider(BrazilSpecProvider)
    >>> generic.brazil_provider.cpf()
    '696.441.186-00'

Integration with Web Application Frameworks
-------------------------------------------

You can use Mimesis during development and testing of applications built
on a variety of frameworks. Here is an example of integration with a
Flask application:

.. code:: python

    class Patient(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        full_name = db.Column(db.String(100))
        blood_type = db.Column(db.String(64))

        def __init__(self, **kwargs):
            super(Patient, self).__init__(**kwargs)

        @staticmethod
        def populate(count=500, locale=None):
            import mimesis

            person =  mimesis.Personal(locale=locale)

            for _ in range(count):
                patient = Patient(
                    full_name=person.full_name('female'),
                    blood_type=person.blood_type(),
                )

                db.session.add(patient)
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()

Just run shell mode and do following:

.. code:: python

    >>> Patient().populate(count=1000, locale='en')

Generate data by schema
-----------------------

Mimesis support generating data by schema:

.. code:: python

    >>> from mimesis.schema import Schema
    >>> schema = Schema('en')

    >>> schema.load(schema={
    ...     "id": "cryptographic.uuid",
    ...     "name": "text.word",
    ...     "version": "development.version",
    ...     "owner": {
    ...         "email": "personal.email",
    ...         "token": "cryptographic.token",
    ...         "creator": "personal.full_name"
    ...     }
    ... }).create(iterations=2)

    >>> # or you can load data from json file:
    >>> schema.load(path='schema.json').create(iterations=2)

Result:

::

    [
      {
        "id": "790cce21-5f75-2652-2ee2-f9d90a26c43d",
        "name": "container",
        "owner": {
          "email": "anjelica8481@outlook.com",
          "token": "0bf924125640c46aad2a860f40ec4b7f33a516c497957abd70375c548ed56978",
          "creator": "Ileen Ellis"
        },
        "version": "4.11.6"
      },
      ...
    ]

Decorators
----------

If your locale belongs to the family of Cyrillic languages, but you need
latinized locale-specific data, then you can use special decorator which
help you romanize your data. At this moment it's works only for Russian
and Ukrainian:

.. code:: python

    >>> from mimesis.decorators import romanized

    >>> @romanized('ru')
    ... def russian_name():
    ...     return 'Вероника Денисова'

    >>> russian_name()
    'Veronika Denisova'

Disclaimer
----------

The authors assume no responsibility for how you use this library data
generated by it. This library is designed only for developers with good
intentions. Do not use the data generated with Mimesis for illegal
purposes.

Contributing
------------

Your contributions are always welcome! Please take a look at the
`contribution <https://github.com/lk-geimfari/mimesis/blob/master/CONTRIBUTING.md>`__
guidelines first.
`Here <https://github.com/lk-geimfari/mimesis/blob/master/CONTRIBUTORS.md>`__
you can look at list of our contributors.

License
-------

Mimesis is licensed under the MIT License. See
`LICENSE <https://github.com/lk-geimfari/mimesis/blob/master/LICENSE>`__
for more information.

.. |Build Status| image:: https://travis-ci.org/lk-geimfari/mimesis.svg?branch=master
   :target: https://travis-ci.org/lk-geimfari/mimesis
.. |Build status on Windows| image:: https://ci.appveyor.com/api/projects/status/chj8huslvn6vde18?svg=true
   :target: https://ci.appveyor.com/project/lk-geimfari/mimesis
.. |codecov| image:: https://codecov.io/gh/lk-geimfari/mimesis/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lk-geimfari/mimesis
.. |PyPI version| image:: https://badge.fury.io/py/mimesis.svg
   :target: https://badge.fury.io/py/mimesis
.. |Python| image:: https://img.shields.io/badge/python-3.3%5E-brightgreen.svg
   :target: https://badge.fury.io/py/mimesis


Author
------

`Likid Geimfari <https://github.com/lk-geimfari>`_ (likid.geimfari@gmail.com)

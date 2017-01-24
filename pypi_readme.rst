Elizabeth
=========

|Build Status| |codecov| |Documentation Status| |PyPI version| |Python
Version| |Codacy Badge|


.. figure::  https://raw.githubusercontent.com/lk-geimfari/elizabeth/master/other/elizabeth_1.png
    :width: 200px
    :align: center
    

**Elizabeth** is a fast and easy to use Python library for generating
dummy data for a variety of purposes. This data can be particularly
useful during software development and testing. For example, it could be
used to populate a testing database for a web application with user
information such as email addresses, usernames, first names, last names,
etc. Elizabeth uses a JSON-based datastore and does not require any
modules that are not in the Python standard library. There are over
nineteen different `data
providers <https://github.com/lk-geimfari/elizabeth/blob/master/PROVIDERS.md>`__
available, which can produce data related to food, people, computer
hardware, transportation, addresses, and more.

Documentation
=============

Elizabeth is simple to use, and the below examples should help you get
started. Complete documentation for ``Elizabeth`` is available here:
`http://elizabeth.readthedocs.io/en/latest/ <http://elizabeth.readthedocs.io/>`__

Installation
============

To install ``Elizabeth``, simply:

.. code:: zsh

    ➜  ~ pip install elizabeth

Basic Usage
===========

.. code:: python

    >>> from elizabeth import Personal
    >>> p = Personal('en')
    >>>
    >>> p.full_name(gender='female')
    'Antonetta Garrison'
    >>> p.blood_type()
    'O-'
    >>> p.occupation()
    'Programmer'

Locales
=======

You can specify a locale when creating providers and they will return
data that is appropriate for the language or country associated with
that locale. ``Elizabeth`` currently includes support for 21 different
locales:

+------+--------+-------------+------------------------+------------------------+
| №    | Flag   | Code        | Name                   | Native name            |
+======+========+=============+========================+========================+
| 1    | 🇨🇿     | ``cs``      | Czech                  | Česky                  |
+------+--------+-------------+------------------------+------------------------+
| 2    | 🇩🇰     | ``da``      | Danish                 | Dansk                  |
+------+--------+-------------+------------------------+------------------------+
| 3    | 🇩🇪     | ``de``      | German                 | Deutsch                |
+------+--------+-------------+------------------------+------------------------+
| 4    | 🇺🇸     | ``en``      | English                | English                |
+------+--------+-------------+------------------------+------------------------+
| 5    | 🇬🇧     | ``en-gb``   | British English        | English                |
+------+--------+-------------+------------------------+------------------------+
| 6    | 🇪🇸     | ``es``      | Spanish                | Español                |
+------+--------+-------------+------------------------+------------------------+
| 7    | 🇮🇷     | ``fa``      | Farsi                  | فارسی                  |
+------+--------+-------------+------------------------+------------------------+
| 8    | 🇫🇮     | ``fi``      | Finnish                | Suomi                  |
+------+--------+-------------+------------------------+------------------------+
| 9    | 🇫🇷     | ``fr``      | French                 | Français               |
+------+--------+-------------+------------------------+------------------------+
| 10   | 🇭🇺     | ``hu``      | Hungarian              | Magyar                 |
+------+--------+-------------+------------------------+------------------------+
| 11   | 🇮🇸     | ``is``      | Icelandic              | Íslenska               |
+------+--------+-------------+------------------------+------------------------+
| 12   | 🇮🇹     | ``it``      | Italian                | Italiano               |
+------+--------+-------------+------------------------+------------------------+
| 13   | 🇯🇵     | ``jp``      | Japanese               | 日本語                 |
+------+--------+-------------+------------------------+------------------------+
| 14   | 🇰🇷     | ``ko``      | Korean                 | 한국어                 |
+------+--------+-------------+------------------------+------------------------+
| 15   | 🇳🇱     | ``nl``      | Dutch                  | Nederlands             |
+------+--------+-------------+------------------------+------------------------+
| 16   | 🇳🇴     | ``no``      | Norwegian              | Norsk                  |
+------+--------+-------------+------------------------+------------------------+
| 17   | 🇵🇱     | ``pl``      | Polish                 | Polski                 |
+------+--------+-------------+------------------------+------------------------+
| 18   | 🇵🇹     | ``pt``      | Portuguese             | Português              |
+------+--------+-------------+------------------------+------------------------+
| 19   | 🇧🇷     | ``pt-br``   | Brazilian Portuguese   | Português Brasileiro   |
+------+--------+-------------+------------------------+------------------------+
| 20   | 🇷🇺     | ``ru``      | Russian                | Русский                |
+------+--------+-------------+------------------------+------------------------+
| 21   | 🇸🇪     | ``sv``      | Swedish                | Svenska                |
+------+--------+-------------+------------------------+------------------------+

Using locales:

.. code:: python

    >>> from elizabeth import Text
    >>> en = Text()  # English is Elizabeth's default locale
    >>> de = Text('de')

    >>> en.sentence()
    'Ports are used to communicate with the external world.'
    >>> de.sentence()
    'Wir müssen nicht vergessen Zickler.'
    >>>
    >>> en.color()
    'Blue'
    >>> de.color()
    'Türkis'

When you only need to generate data for a single locale, use the
``Generic`` provider, and you can access all ``Elizabeth`` providers
from one object.

.. code:: python

    >>> from elizabeth import Generic
    >>> g = Generic('es')
    >>>
    >>> g.datetime.month()
    'Agosto'
    >>> g.code.imei()
    '353918052107063'
    >>> g.food.fruit()
    'Limón'

Advantages
==========

``Elizabeth`` offers a number of advantages over other similar
libraries, such as ``Faker``:

-  Performance. ``Elizabeth`` is significantly
   `faster <http://i.imgur.com/ZqkE1k2.png>`__ than other similar
   libraries.
-  Completeness. ``Elizabeth`` strives to provide many detailed
   providers that offer a variety of data generators.
-  Simplicity. ``Elizabeth`` does not require any modules other than the
   Python standard library.

See
`here <https://gist.github.com/lk-geimfari/461ce92fd32379d7b73c9e12164a9154>`__
for an example of how we compare performance with other libraries.

Integration with Web Application Frameworks
===========================================

You can use ``Elizabeth`` during development and testing of applications
built on a variety of frameworks. Here is an example of integration with
a ``Flask`` application:

.. code:: python

    class Patient(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120), unique=True)
        phone_number = db.Column(db.String(25))
        full_name = db.Column(db.String(100))
        weight = db.Column(db.String(64))
        height = db.Column(db.String(64))
        blood_type = db.Column(db.String(64))
        age = db.Column(db.Integer)

        def __init__(self, **kwargs):
            super(Patient, self).__init__(**kwargs)

        @staticmethod
        def _bootstrap(count=2000, locale='en'):
            from elizabeth import Personal

            person = Personal(locale)

            for _ in range(count):
                patient = Patient(
                    email=person.email(),
                    phone_number=person.telephone(),
                    full_name=person.full_name(gender='female'),
                    age=person.age(minimum=18, maximum=45),
                    weight=person.weight(),
                    height=person.height(),
                    blood_type=person.blood_type()
                )

                db.session.add(patient)
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()

Just run shell mode

::

    (venv) ➜ python3 manage.py shell

and do following:

.. code:: python

    >>> db
    <SQLAlchemy engine='sqlite:///db_dev.sqlite'>

    >>> Patient
    <class 'app.models.Patient'>

    >>> Patient()._bootstrap(count=1000, locale='en', gender='female')

Result:

.. figure:: https://raw.githubusercontent.com/lk-geimfari/elizabeth/master/other/screenshots/en_bootstrap.png
   :alt: en

   en

Custom Providers
================

You also can add custom provider to ``Generic``.

.. code:: python

    >>> from elizabeth import Generic
    >>> generic = Generic('en')
    >>>
    >>> class SomeProvider():
    >>>     class Meta:
    >>>         name = 'some_provider'
    >>>
    >>>     def ints(self):
    >>>         return [i for i in range(1, 5)]
    >>>
    >>> class Another():
    >>>     def bye(self):
    >>>         return "Bye!"
    >>>
    >>> generic.add_provider(SomeProvider)
    >>> generic.add_provider(Another)
    >>>
    >>> generic.some_provider.ints()
    [1, 2, 3, 4]
    >>> generic.another.bye()
    'Bye!'

Builtins specific data providers
================================

Some countries have data types specific to that country. For example
social security numbers in the United States (``en`` locale), and
cadastro de pessoas físicas (CPF) in Brazil (``pt-br`` locale).

If you would like to use these country-specific providers, then you must
import them explicitly:

.. code:: python

    >>> from elizabeth import Generic
    >>> from elizabeth.builtins import Brazil
    >>>
    >>> generic = Generic('pt-br')
    >>>
    >>> class BrazilProvider(Brazil):
    >>>     class Meta:
    >>>         name = "brazil_provider"
    >>>
    >>> generic.add_provider(BrazilProvider)
    >>>
    >>> generic.brazil_provider.cpf()
    '001.137.297-40'

Like It?
========

You can say `thanks <https://saythanks.io/to/lk-geimfari>`__!

Contributing
============

Your contributions are always welcome! Please take a look at the
`contribution <https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md>`__
guidelines first.
`Here <https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md#contributors>`__
you can look a list of our contributors.

Testing
=======

.. code:: zsh

    ➜ ~ git clone https://github.com/lk-geimfari/elizabeth.git
    ➜ cd elizabeth/
    ➜ python3 -m unittest discover tests

Change Log
==========

See
`CHANGELOG.md <https://github.com/lk-geimfari/elizabeth/blob/master/CHANGELOG.md>`__.

License
=======

Elizabeth is licensed under the MIT License. See
`LICENSE <https://github.com/lk-geimfari/elizabeth/blob/master/LICENSE>`__
for more information.

Disclaimer
==========

The authors assume no responsibility for how you use this library data
generated by it. This library is designed only for developers with good
intentions. Do not use the data generated with ``Elizabeth`` for illegal
purposes.

.. |Build Status| image:: https://travis-ci.org/lk-geimfari/elizabeth.svg?branch=master
   :target: https://travis-ci.org/lk-geimfari/elizabeth
.. |codecov| image:: https://codecov.io/gh/lk-geimfari/elizabeth/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lk-geimfari/elizabeth
.. |Documentation Status| image:: https://readthedocs.org/projects/elizabeth/badge/?version=latest
   :target: http://elizabeth.readthedocs.io/en/latest/?badge=latest
.. |PyPI version| image:: https://badge.fury.io/py/elizabeth.svg
   :target: https://badge.fury.io/py/elizabeth
.. |Python Version| image:: https://img.shields.io/badge/python-v3.3%2C%20v3.4%2C%20v3.5%2C%20v3.6-brightgreen.svg
   :target: https://github.com/lk-geimfari/elizabeth/
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/d773f20efa67430683bb24fff5af9db8
   :target: https://www.codacy.com/app/likid-geimfari/church

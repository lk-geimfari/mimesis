.. image:: https://raw.githubusercontent.com/lk-geimfari/elizabeth/master/other/logo.png
    :target: http://docs.python-requests.org/



=========================


.. image:: https://travis-ci.org/lk-geimfari/elizabeth.svg?branch=master
    :target: https://travis-ci.org/lk-geimfari/elizabeth

.. image:: https://readthedocs.org/projects/elizabeth/badge/?version=latest
    :target: http://elizabeth.readthedocs.io/en/latest/?badge=latest

.. image:: https://badge.fury.io/py/elizabeth.svg
    :target: https://badge.fury.io/py/elizabeth

.. image:: https://img.shields.io/badge/python-v3.3%2C%20v3.4%2C%20v3.5%2C%20v3.6-brightgreen.svg
    :target: https://github.com/lk-geimfari/elizabeth/

.. image:: https://api.codacy.com/project/badge/Grade/8b2f43d89d774929bb0b7535812f5b08
    :target: https://www.codacy.com/app/likid-geimfari/elizabeth?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lk-geimfari/elizabeth&amp;utm_campaign=Badge_Grade

`Elizabeth <https://github.com/lk-geimfari/elizabeth>`_ is a fast and easy to use Python library for generating dummy data for a variety of purposes. This data can be particularly useful during software development and testing. For example, it could be used to populate a testing database for a web application with user information such as email addresses, usernames, first names, last names, etc.

Elizabeth uses a JSON-based datastore and does not require any modules that are not in the Python standard library. There are over nineteen different data providers available, which can produce data related to food, people, computer hardware, transportation, addresses, and more.


Documentation
-------------
Complete documentation for Elizabeth is available here: http://elizabeth.readthedocs.io/


Installation
------------

To install Elizabeth, simply:

.. code-block:: bash

    ➜  ~ pip install elizabeth

Basic Usage:

.. code-block:: python

    >>> from elizabeth import Personal
    >>> pr = Personal('en')

    >>> pr.full_name(gender='female')
    'Antonetta Garrison'

    >>> pr.email(gender='male)
    'oren5936@live.com'

    >>> pr.occupation()
    'Programmer'

Locales
------------

You can specify a locale when creating providers and they will return data that is appropriate for the language or country associated with that locale. `Elizabeth` currently includes support for `24 <https://github.com/lk-geimfari/elizabeth#locales>`_ different locales.

Using locales:

.. code-block:: python

    >>> from elizabeth import Personal
 
    >>> en = Personal('en')
    >>> de = Personal('de')
    >>> ic = Personal('is')

    >>> en.full_name()
    'Carolin Brady'

    >>> de.full_name()
    'Sabrina Gutermuth'
 
    >>> ic.full_name()
    'Rósa Þórlindsdóttir'


When you only need to generate data for a single locale, use the `Generic` provider, and you can access all `Elizabeth`
providers from one object.

.. code:: python

    >>> from elizabeth import Generic
    >>> g = Generic('es')

    >>> g.datetime.month()
    'Agosto'

    >>> g.code.imei()
    '353918052107063'

    >>> g.food.fruit()
    'Limón'


Advantages
------------

``Elizabeth`` offers a number of advantages over other similar
libraries, such as ``Faker``:

-  Performance. ``Elizabeth`` is significantly `faster`_ than other
   similar libraries.
-  Completeness. ``Elizabeth`` strives to provide many detailed
   providers that offer a variety of data generators.
-  Simplicity. ``Elizabeth`` does not require any modules other than the
   Python standard library.

See `here`_ for an example of how we compare performance with other
libraries.

.. _faster: http://i.imgur.com/ZqkE1k2.png
.. _here: https://gist.github.com/lk-geimfari/461ce92fd32379d7b73c9e12164a9154


Integration with Web Application Frameworks
------------

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
        def _bootstrap(count=500, locale='en', gender):
            from elizabeth import Personal

            person = Personal(locale)

            for _ in range(count):
                patient = Patient(
                    email=person.email(),
                    phone_number=person.telephone(),
                    full_name=person.full_name(gender=gender),
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

    (env) ➜ python3 manage.py shell

and do following:

.. code:: python

    >>> db
    <SQLAlchemy engine='sqlite:///db_dev.sqlite'>

    >>> Patient
    <class 'app.models.Patient'>

    >>> Patient()._bootstrap(count=1000, locale='en', gender='female')

Result: `screenshot`_

.. _screenshot: https://raw.githubusercontent.com/lk-geimfari/elizabeth/master/other/screenshots/en_bootstrap.png


Custom Providers
------------

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
------------

Some countries have data types specific to that country. For example
social security numbers in the United States (``en`` locale), and
cadastro de pessoas físicas (CPF) in Brazil (``pt-br`` locale).

If you would like to use these country-specific providers, then you must
import them explicitly:

.. code:: python

    >>> from elizabeth import Generic
    >>> from elizabeth.builtins import BrazilSpecProvider

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
------------

If your locale is cyrillic, but you need latinized locale-specific data,
then you can use special decorator. At this moment it’s work only for
Russian:

.. code:: python

    >>> from elizabeth import Personal
    >>> from elizabeth.decorators import romanized_russian

    >>> pr = Personal('ru')

    >>> @romanized_russian
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


Contributing
------------

Your contributions are always welcome! Please take a look at the
`contribution`_ guidelines first it is very important. `Here`_ you can
look a list of our contributors.


License
------------

Elizabeth is licensed under the MIT License. See `LICENSE`_ for more
information.


Disclaimer
------------

The authors assume no responsibility for how you use this library data
generated by it. This library is designed only for developers with good
intentions. Do not use the data generated with ``Elizabeth`` for illegal
purposes.

.. _contribution: https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md
.. _Here: https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTORS.md
.. _LICENSE: https://github.com/lk-geimfari/elizabeth/blob/master/LICENSE


Author and Maintainer
------------

`Likid Geimfari <https://github.com/lk-geimfari>`_ <likid.geimfari@gmail.com>

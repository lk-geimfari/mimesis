Mimesis
=======

|Build Status| |Build status on Windows| |PyPI version|
|Python|

.. |Build Status| image:: https://travis-ci.org/lk-geimfari/mimesis.svg?branch=master
	:target: https://travis-ci.org/lk-geimfari/mimesis
.. |Build status on Windows| image:: https://ci.appveyor.com/api/projects/status/chj8huslvn6vde18?svg=true
	:target: https://ci.appveyor.com/project/lk-geimfari/mimesis
.. |PyPI version| image:: https://badge.fury.io/py/mimesis.svg
	:target: https://badge.fury.io/py/mimesis
.. |Python| image:: https://img.shields.io/badge/python-3.5%2C%203.6-brightgreen.svg
	:target: https://badge.fury.io/py/mimesis


**Mimesis** is a fast and easy to use library for Python programming language, which helps generate mock data for a variety of purposes (see «\ `Data providers`_\ ») in a variety of languages (see «\ `Locales`_\ »). This data can be particularly useful during software development and testing. For example, it could be used to populate a testing database, create beautiful JSON/XML/HTML files, anonymize data taken from a production service, etc.

.. _Locales: #id1
.. _Data providers: #id2

This library offers a number of advantages over other similar libraries:

-  Performance. Significantly `faster`_ than other similar libraries.
-  Completeness. Strives to provide many detailed providers that offer a variety of data generators.
-  Simplicity. Does not require any modules other than the Python standard library.

See `here <https://gist.github.com/lk-geimfari/461ce92fd32379d7b73c9e12164a9154>`_ for an example of how we compare performance with other
libraries.

.. _faster: http://i.imgur.com/pCo6yPA.png


Installation
------------

To install mimesis, simply use pip:

.. code-block:: bash

    ➜ pip install mimesis

also you can install it manually:

.. code-block:: bash

    ➜ git clone https://github.com/lk-geimfari/mimesis.git
    ➜ cd mimesis/
    ➜ make install


Basic Usage
-----------

That's library is really easy to use:

.. code:: python

    >>> from mimesis import Personal
    >>> from mimesis.enums import Gender
    >>> person = Personal('en')

    >>> person.full_name(gender=Gender.FEMALE)
    'Antonetta Garrison'

    >>> person.occupation()
    'Backend Developer'

    >>> templates = ('U_d', 'U.d', 'U-d', 'ld',
    ...              'l-d', 'Ud', 'l.d', 'l_d')
    >>>
    >>> for template in templates:
    ...     person.username(template=template)
    ...
    'Cristina_1889'
    'Credenza.1845'
    'Alger-1847'
    'cabral1899'
    'maimed-1856'
    'Chenault1820'
    'cobol.1951'
    'dashed_2006'


Seeded data
-----------

For using seeded data just pass argument ``seed`` to data provider:

.. code-block:: python

    >>> from mimesis import Personal
    >>> personal = Personal('tr', seed=0xFF)
    >>> personal.full_name()
    'Gizem Tekand'


Locales
-------

You can specify a locale when creating providers and they will return data that is appropriate for
the language or country associated with that locale. `Mimesis` currently includes support
for `33 different locales <http://mimesis.readthedocs.io/locales.html>`_.


Usage
~~~~~

.. code-block:: python

    >>> from mimesis import Text
    >>> en = Text('en')
    >>> de = Text('de')

    >>> en.color()
    'Blue'

    >>> de.color()
    'Türkis'

When you only need to generate data for a single locale, use the ``Generic()`` provider, and you can access all Mimesis
providers from one object.

.. code-block:: python

    >>> from mimesis import Generic
    >>> g = Generic('es')

    >>> g.datetime.month()
    'Agosto'

    >>> g.code.imei()
    '353918052107063'

    >>> g.food.fruit()
    'Limón'

    >>> g.science.rna()
    'GCTTTAGACC'


Data Providers
--------------
Mimesis support over twenty different data providers available, which can produce data related to food, people, computer hardware, transportation, addresses, and more.

List of supported data providers available `here <http://mimesis.readthedocs.io/providers.html>`_

Custom Data Providers
---------------------

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

    >>> generic.some_provider.hello()
    'Hello!'

    >>> generic.another.bye()
    'Bye!'

or multiple custom providers using method ``add_providers()``:

.. code:: python

    >>> generic.add_providers(SomeProvider, Another)


Builtins Data Providers
-----------------------

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


Decorators
----------

If your locale belongs to the family of Cyrillic languages, but you need
latinized locale-specific data, then you can use special decorator which
help you romanize your data. At this moment it’s works only for Russian (``ru``),
Ukrainian (``uk``) and Kazakh (``kk``):

.. code:: python

    >>> from mimesis.decorators import romanized

    >>> @romanized('ru')
    ... def russian_name():
    ...     return 'Вероника Денисова'

    >>> russian_name()
    'Veronika Denisova'


Best Practice
-------------
We strongly recommend to read articles which published below. There we are speak about
best practices and a number of most useful features of the library.

.. toctree::
   :maxdepth: 3

   part_1
   part_2



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
                    full_name=person.full_name(),
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



Integration with third-party libraries
--------------------------------------

- `mimesis-factory`_ - Integration with ``factory_boy``.
- `pytest-mimesis`_ - is a pytest plugin that provides pytest fixtures for Mimesis providers.

.. _mimesis-factory: https://github.com/mimesis-lab/mimesis-factory
.. _pytest-mimesis: https://github.com/lk-geimfari/pytest-mimesis

Contributing
------------

The `source code <https://github.com/lk-geimfari/mimesis>`_ and `issue tracker <https://github.com/lk-geimfari/mimesis/issues>`_ are hosted on GitHub.  *Mimesis* is tested against Python 3.5 through 3.6 on `Travis-CI <https://travis-ci.org/lk-geimfari/mimesis>`_.  Test coverage is monitored with `Codecov <https://codecov.io/gh/lk-geimfari/mimesis>`_.

Guidelines
~~~~~~~~~~
Your contributions are always welcome! Please adhere to the contribution guidelines:

- Add one change per one commit.
- Include only commit in each pull request.
- Document your code with comments in English.
- Check your spelling and grammar.
- Check code style with `pycodestyle <https://pycodestyle.readthedocs.io/en/latest/>`_, `pylint <https://www.pylint.org/>`_, or another similar tool.
- `Run the test suite <#running-tests>`_ and ensure all tests pass.
- Write additional tests to cover new functionality.
- Do not write bad code!


Running Tests
~~~~~~~~~~~~~

.. code-block:: bash

    ➜  ~ pip install -r dev_requirements.txt
    ➜  ~ cd mimesis/
    ➜  py.test

or

.. code-block:: bash

    ➜ make test

License and Disclaimer
----------------------

`Mimesis` is distributed under the `MIT License <https://github.com/lk-geimfari/mimesis/blob/master/LICENSE>`_.

The authors do not assume any responsibility for how you use this library or how you use data generated with it.  This library is designed only for developers and only with good intentions. Do not use the data generated with Mimesis for illegal purposes.

Contents
--------

.. toctree::
   :maxdepth: 3

   api


Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

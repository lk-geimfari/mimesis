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
.. _Data providers: #providers

This library offers a number of advantages over other similar libraries:

-  Performance. Significantly `faster`_ than other similar libraries.
-  Completeness. Strives to provide many detailed providers that offer a variety of data generators.
-  Simplicity. Does not require any modules other than the Python standard library.

.. _faster: https://gist.github.com/lk-geimfari/e76c12eb3c9a8afbf796c706d4ba779d


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


Seeded Data
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


Example of usage:

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


Providers
---------
Mimesis support over twenty different data providers available, which can produce data related to food, people, computer hardware, transportation, addresses, and more.

List of supported data providers available `here <http://mimesis.readthedocs.io/providers.html>`_.

Custom Providers
----------------

The library supports a vast amount of data and in most cases this would
be enough. For those who want to create their own providers with more
specific data. This can be done like this:

.. code:: python

    >>> class SomeProvider():
    ...     class Meta:
    ...         name = "some_provider"
    ...
    ...     @staticmethod
    ...     def hello():
    ...         return 'Hello!'

    >>> class Another():
    ...     @staticmethod
    ...     def bye():
    ...         return "Bye!"

    >>> generic.add_provider(SomeProvider)
    >>> generic.add_provider(Another)

    >>> generic.some_provider.hello()
    'Hello!'

    >>> generic.another.bye()
    'Bye!'

You can also add multiple providers:

.. code:: python

    >>> generic.add_providers(SomeProvider, Another)
    >>> generic.some_provider.hello()
    'Hello!'
    >>> generic.another.bye()
    'Bye!'

Everything is pretty easy and self-explanatory here, therefore, we will
only clarify one moment — attribute ``name``, class ``Meta`` is the name
of a class through which access to methods of user-class providers is
carried out. By default class name is the name of the class in the lower
register.

Built-in Providers
------------------

Most countries, where only one language is official, have data typical
only for these particular countries. For example, «CPF» for Brazil
(``pt-br``), «SSN» for USA (``en``). This kind of data can cause
discomfort and meddle with the order (or at least annoy) by being
present in all the objects regardless of the chosen language standard.
You can see that for yourselves by looking at the example (the code
won’t run):

.. code:: python

    >>> from mimesis import Personal
    >>> person = Personal('en')

    >>> person.ssn()
    >>> person.cpf()

We bet everyone would agree that this does not look too good.
Perfectionists, as we are, have taken care of this in a way that some
specific regional provider would not bother other providers for other
regions. For this reason, class providers with locally-specific data are
separated into a special sub-package (``mimesis.builtins``) for keeping
a common class structure for all languages and their objects.

Here’s how it works:

.. code:: python

    >>> from mimesis import Generic
    >>> from mimesis.builtins import BrazilSpecProvider

    >>> generic = Generic('pt-br')
    >>> generic.add_provider(BrazilProvider)
    >>> generic.brazil_provider.cpf()
    '696.441.186-00'

If you want to change default name of built-in provider, just change
value of attribute ``name``, class ``Meta`` of the builtin provider:

.. code:: python

    >>> BrazilSpecProvider.Meta.name = 'brasil'
    >>> generic.add_provider(BrazilSpecProvider)
    >>> generic.brasil.cpf()
    '019.775.929-70'

Or just inherit the class and override the value of attribute ``name``
of class ``Meta`` of the provider (in our case this is
``BrazilSpecProvider()``) :

.. code:: python

    >>> class Brasil(BrazilSpecProvider):
    ...
    ...     class Meta:
    ...         name = "brasil"
    ...
    >>> generic.add_provider(Brasil)
    >>> generic.brasil.cnpj()
    '55.806.487/7994-45'

Generally, you don’t need to add built-it classes to the object
``Generic()``. It was done in the example with the single purpose of
demonstrating in which cases you should add a built-in class provider to
the object ``Generic()``. You can use it directly, as shown below:

.. code:: python

    >>> from mimesis.builtins import RussiaSpecProvider
    >>> from mimesis.enums import Gender
    >>> ru = RussiaSpecProvider()

    >>> ru.patronymic(gender=Gender.FEMALE)
    'Петровна'

    >>> ru.patronymic(gender=Gender.MALE)
    'Бенедиктович'

Generate Data by Schema
-----------------------

For generating data by schema, just create an instance of ``Field``
object, which takes any string which represents the name of data
provider in format ``provider.method_name`` (explicitly defines that the
method belongs to data-provider ``provider``) or ``method`` (will be
chosen the first provider which has a method ``method_name``) and the
``**kwargs``\ of the method ``method_name``, after that you should
describe the schema in lambda function and pass it to the object
``Schema`` and call method ``create()``.

Optionally, you can apply a *key function* to result returned by the
method, to do it, just pass the parameter ``key`` with a callable object
which returns final result.

Example of usage:

.. code:: python

    >>> from mimesis.schema import Field, Schema
    >>> from mimesis.enums import Gender
    >>> _ = Field('en')
    >>> description = (
    ...     lambda: {
    ...         'id': _('uuid'),
    ...         'name': _('text.word'),
    ...         'version': _('version', pre_release=True),
    ...         'timestamp': _('timestamp', posix=False),
    ...         'owner': {
    ...             'email': _('email', key=str.lower),
    ...             'token': _('token'),
    ...             'creator': _('personal.full_name', gender=Gender.FEMALE),
    ...         },
    ...     }
    ... )
    >>> schema = Schema(schema=description)
    >>> schema.create(iterations=1)

Output:

.. code:: json

    [
      {
        "owner": {
          "email": "aisling2032@yahoo.com",
          "token": "cc8450298958f8b95891d90200f189ef591cf2c27e66e5c8f362f839fcc01370",
          "creator": "Veronika Dyer"
        },
        "name": "pleasure",
        "version": "4.3.1-rc.5",
        "id": "33abf08a-77fd-1d78-86ae-04d88443d0e0",
        "timestamp": "2018-07-29T15:25:02Z"
      }
    ]



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

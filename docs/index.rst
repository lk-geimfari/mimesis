Mimesis
=======

|Build Status| |Build status on Windows| |codecov| |PyPI version|
|Python|

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

**Mimesis** is a fast and easy to use Python library for generating dummy data for a variety of purposes.  This data can be particularly useful during software development and testing.  For example, it could be used to populate a testing database for a web application with user information such as email addresses, usernames, first names, last names, etc. There are over eighteen different `data providers <http://mimesis.readthedocs.io/en/latest/providers.html>`_ available, which can produce data related to food, people, computer hardware, transportation, addresses, and more. Mimesis does not require any modules that are not in the Python standard library.

Advantages
-------------

Mimesis offers a number of advantages over other similar libraries, such
as Faker:

-  Performance. Mimesis is significantly `faster`_ than other similar
   libraries.
-  Completeness. Mimesis strives to provide many detailed providers that
   offer a variety of data generators.
-  Simplicity. Mimesis does not require any modules other than the
   Python standard library.

See `here <https://gist.github.com/lk-geimfari/461ce92fd32379d7b73c9e12164a9154>`_ for an example of how we compare performance with other
libraries.

.. _faster: http://i.imgur.com/pCo6yPA.png


Installation
------------

.. code-block:: bash

    ➜ git clone https://github.com/lk-geimfari/mimesis.git
    ➜ cd mimesis/
    ➜ make install

or simply:

.. code-block:: bash

    ➜ pip install mimesis


Basic Usage
-----------

As we said above, this library is really easy to use:

.. code:: python

    >>> import mimesis
    >>> person = mimesis.Personal('en')

    >>> person.full_name(gender='female')
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

You can specify a locale when creating providers and they will return data that is appropriate for
the language or country associated with that locale. `Mimesis` currently includes support
for `33 different locales <http://mimesis.readthedocs.io/en/latest/locales.html>`_.


Usage
~~~~~

.. code-block:: python

    >>> from mimesis import Text
    >>> en = Text('en')
    >>> de = Text('de')

    >>> en.sentence()
    'Ports are used to communicate with the external world.'

    >>> de.sentence()
    'Wir müssen nicht vergessen Zickler.'

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


Data Providers
--------------
List of supported data providers available `here <http://mimesis.readthedocs.io/en/latest/providers.html>`_


Builtins Data Providers
-----------------------

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


Custom Data Providers
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

    >>> generic.some_provider.hello()
    'Hello!'

    >>> generic.another.bye()
    'Bye!'

or multiple custom providers using method ``add_providers()``:

.. code:: python

    >>> generic.add_providers(SomeProvider, Another)


Constants
---------

The constraints will be useful to you, because they allows you to avoid entering parameters manually, and this mean that they help to avoid typos.

.. code:: python

    >>> from mimesis import Personal
    >>> import mimesis.constants as c

    >>> p = Personal(c.EN)
    # Typo in parameter gender, which should be has a value "female"
    >>> f_names = [p.full_name(gender='emale') for _ in range(3)] 
    
    # An exception UnexpectedGender will be raised.
 

The constants helps to avoid similar issues:

.. code:: python

    >>> # Use c.FEMALE instead string "female" 
    >>> f_names = [p.full_name(c.FEMALE) for _ in range(3)]
    ['Nobuko Campos', 'Casimira Ballard', 'Lena Brady']


That's all that constants are for.


Decorators
----------

If your locale belongs to the family of Cyrillic languages, but you need
latinized locale-specific data, then you can use special decorator which
help you romanize your data. At this moment it’s works only for Russian (``ru``),
Ukrainian (``uk``) and Kazakh (``kk``):

.. code:: python

    >>> from mimesis.decorators import romanized
    >>> import mimesis.constants as c

    >>> @romanized(c.RU)
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


Related Libraries
-----------------
- `mimesis-lab`_ - An extra open-source solutions using Mimesis library.
- `elizabeth-cloud`_ - web version of Mimesis using GraphQL and Sanic.
- `pytest-mimesis`_ - is a pytest plugin that provides pytest fixtures for Mimesis providers.

.. _mimesis-lab: https://github.com/mimesis-lab
.. _elizabeth-cloud: https://github.com/wemake-services/elizabeth-cloud
.. _pytest-mimesis: https://github.com/lk-geimfari/pytest-mimesis

Contributing
------------

The `source code <https://github.com/lk-geimfari/mimesis>`_ and `issue tracker <https://github.com/lk-geimfari/mimesis/issues>`_ are hosted on GitHub.  *Mimesis* is tested against Python 3.3 through 3.6 on `Travis-CI <https://travis-ci.org/lk-geimfari/mimesis>`_.  Test coverage is monitored with `Codecov <https://codecov.io/gh/lk-geimfari/mimesis>`_.

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

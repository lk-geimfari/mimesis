Mimesis
=========

**Mimesis** is a fast and easy to use Python library for generating dummy data for a variety of purposes.  This data can be particularly useful during software development and testing.  For example, it could be used to populate a testing database for a web application with user information such as email addresses, usernames, first names, last names, etc.

There are over eighteen different `data providers <https://github.com/lk-geimfari/mimesis/blob/master/PROVIDERS.md>`_ available, which can produce data related to food, people, computer hardware, transportation, addresses, and more.  *Mimesis* does not require any modules that are not in the Python standard library.

Best Practice
------------
We strongly recommend to read articles which published in our blog_ on Medium. There we are speak about best practices and a number of most useful features of the library.

Generating mock data using Mimesis: First_ and Second_ part.

.. _First: https://medium.com/wemake-services/generating-mock-data-using-elizabeth-part-i-ca5a55b8027c
.. _Second: https://medium.com/wemake-services/generating-mock-data-with-elizabeth-part-ii-bb16a3f3106f
.. _blog: https://medium.com/wemake-services


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

.. code-block:: python

    >>> from mimesis import Personal
    >>> p = Personal()

    >>> p.full_name(gender='female')
    'Antonetta Garrison'

    >>> p.blood_type()
    'O-'

    >>> p.occupation()
    'Programmer'

Locales
-------

You can specify a locale when creating providers and they will return data that is appropriate for the language or country associated with that locale.  `Mimesis` currently includes support for 30 different locales:

=======  ====================  ====================
Code     Name                  Native Name
=======  ====================  ====================
`cs`     Czech				   Česky
`da`     Danish                Dansk
`de`     German                Deutsch
`de-at`  Austrian german       Deutsch
`de-ch`  Swiss german          Deutsch
`en`     English               English
`en-au`  Australian English    English
`en-ca`  Canadian English      English
`en-gb`  British English       English
`es`     Spanish               Español
`es`     Mexican Spanish       Español
`fa`     Farsi                 فارسی
`fi`     Finnish               Suomi
`fr`     French                Français
`hu`     Hungarian             Magyar
`is`     Icelandic             Íslenska
`it`     Italian               Italiano
`ja`     Japanese              日本語
`ko`	 Korean                한국어
`nl`     Dutch                 Nederlands
`nl-be`  Belgium Dutch         Nederlands
`no`     Norwegian             Norsk
`pl`     Polish                Polski
`pt`     Portuguese            Português
`pt-br`  Brazilian Portuguese  Português Brasileiro
`ru`     Russian               Русский
`sv`     Swedish               Svenska
`tr`     Turkish               Türkçe
`uk`     Ukrainian             Український
`zh`     Chinese               汉语
=======  ====================  ====================

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

When you only need to generate data for a single locale, use the `Generic` provider, and you can access all Mimesis
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

Related Libraries
-----------------

- `elizabeth-cloud`_ - web version of Mimesis using GraphQL and Sanic.
- `pytest-elizabeth`_ - is a pytest plugin that provides pytest fixtures for Mimesis providers.

.. _elizabeth-cloud: https://github.com/wemake-services/elizabeth-cloud
.. _pytest-elizabeth: https://github.com/lk-geimfari/pytest-elizabeth

Contributing
------------

The `source code <https://github.com/lk-geimfari/mimesis>`_ and `issue tracker <https://github.com/lk-geimfari/mimesis/issues>`_ are hosted on GitHub.  *Mimesis* is tested against Python 3.2 through 3.6 on `Travis-CI <https://travis-ci.org/lk-geimfari/mimesis>`_.  Test coverage is monitored with `Codecov <https://codecov.io/gh/lk-geimfari/mimesis>`_.

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

    cd mimesis/
    py.test --cov=mimesis/ --cov-report=term-missing

or

.. code-block:: bash

    make test

License and Disclaimer
----------------------

`Mimesis` is distributed under the `MIT License <https://github.com/lk-geimfari/church/blob/master/LICENSE>`_.

The authors do not assume any responsibility for how you use this library or how you use data generated with it.  This library is designed only for developers and only with good intentions. Do not use the data generated with Mimesis for illegal purposes.

Contents
--------

.. toctree::
   :maxdepth: 3

   guide
   api

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

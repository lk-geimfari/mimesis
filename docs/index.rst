Elizabeth
=========

**Elizabeth** is a fast and easy to use Python library for generating dummy data for a variety of purposes.  This data can be particularly useful during software development and testing.  For example, it could be used to populate a testing database for a web application with user information such as email addresses, usernames, first names, last names, etc.

There are over eighteen different `data providers <https://github.com/lk-geimfari/elizabeth/blob/master/PROVIDERS.md>`_ available, which can produce data related to food, people, computer hardware, transportation, addresses, and more.  *Elizabeth* does not require any modules that are not in the Python standard library.

Installation
------------

.. code-block:: bash

    git clone https://github.com/lk-geimfari/elizabeth.git
    cd elizabeth/
    python3 setup.py install

or simply:

.. code-block:: bash

    pip install elizabeth

Basic Usage
-----------

.. code-block:: python

    >>> from elizabeth import Personal
    >>> p = Personal()
    >>>
    >>> p.full_name(gender='female')
    'Antonetta Garrison'
    >>> p.blood_type()
    'O-'
    >>> p.occupation()
    'Programmer'

Locales
-------

You can specify a locale when creating providers and they will return data that is appropriate for the language or country associated with that locale.  `Elizabeth` currently includes support for 18 different locales:

=======  ====================  ====================
Code     Name                  Native Name
=======  ====================  ====================
`da`     Danish                Dansk
`de`     German                Deutsch
`en`     English               English
`en-gb`  British English       English
`es`     Spanish               Español
`fa`     Farsi                 فارسی
`fi`     Finnish               Suomi
`fr`     French                Français
`hu`     Hungarian             Magyar
`is`     Icelandic             Íslenska
`it`     Italian               Italiano
`nl`     Dutch                 Nederlands
`no`     Norwegian             Norsk
`pl`     Polish                Polski
`pt`     Portuguese            Português
`pt-br`  Brazilian Portuguese  Português Brasileiro
`ru`     Russian               Русский
`sv`     Swedish               Svenska
=======  ====================  ====================

Usage
~~~~~

.. code-block:: python

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

When you only need to generate data for a single locale, use the `Generic` provider, and you can access all `Elizabeth`
providers from one object.

.. code-block:: python

    >>> from elizabeth import Generic
    >>> g = Generic('es')
    >>> g.datetime.month()
    'Agosto'
    >>> g.code.imei()
    '353918052107063'
    >>> g.food.fruit()
    'Limón'

Related Libraries
-----------------

- `Flask-church`_ - an extension for Flask based on Elizabeth.
- `Presturinn`_ - a fake API based on Falcon and Elizabeth v0.2.0.

.. _Flask-church: https://github.com/lk-geimfari/flask_church
.. _Presturinn: https://github.com/lk-geimfari/presturinn

Contributing
------------

The `source code <https://github.com/lk-geimfari/elizabeth>`_ and `issue tracker <https://github.com/lk-geimfari/elizabeth/issues>`_ are hosted on GitHub.  *Elizabeth* is tested against Python 3.2 through 3.6 on `Travis-CI <https://travis-ci.org/lk-geimfari/elizabeth>`_.  Test coverage is monitored with `Codecov <https://codecov.io/gh/lk-geimfari/elizabeth>`_, and code quality checks are automated with `Codacy <https://www.codacy.com/app/wikkiewikkie/elizabeth/dashboard>`_.

Guidelines
~~~~~~~~~~
Your contributions are always welcome! Please adhere to the contribution guidelines:

- Make one change per one commit.
- Include only commit in each pull request.
- Document your code with comments in English.
- Check your spelling and grammar.
- Check code style with `pycodestyle <https://pycodestyle.readthedocs.io/en/latest/>`_, `pylint <https://www.pylint.org/>`_, or another similar tool.
- `Run the test suite <#running-tests>`_ and ensure all tests pass.
- Write additional tests to cover new functionality.


Running Tests
~~~~~~~~~~~~~

.. code-block:: bash

    cd elizabeth/
    python3 -m unittest discover tests

or

.. code-block:: bash

    run_tests.sh

License and Disclaimer
----------------------

`Elizabeth` is distributed under the `MIT License <https://github.com/lk-geimfari/church/blob/master/LICENSE>`_.

The authors do not assume any responsibility for how you use this library or how you use data generated with it.  This library is designed only for developers and only with good intentions.  Do not use the data generated with `Elizabeth` for illegal purposes.

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

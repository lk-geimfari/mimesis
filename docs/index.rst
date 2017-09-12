Mimesis
=======

**Mimesis** is a fast and easy to use Python library for generating dummy data for a variety of purposes.  This data can be particularly useful during software development and testing.  For example, it could be used to populate a testing database for a web application with user information such as email addresses, usernames, first names, last names, etc. There are over eighteen different `data providers <https://github.com/lk-geimfari/mimesis/blob/master/PROVIDERS.md>`_ available, which can produce data related to food, people, computer hardware, transportation, addresses, and more.  *Mimesis* does not require any modules that are not in the Python standard library.

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

See `here`_ for an example of how we compare performance with other
libraries.

.. _faster: http://i.imgur.com/pCo6yPA.png
.. _here: https://gist.github.com/lk-geimfari/461ce92fd32379d7b73c9e12164a9154



Best Practice
-------------
We strongly recommend to read articles which published in blog_ of our friends on Medium. There we are speak about best practices and a number of most useful features of the library.

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

You can specify a locale when creating providers and they will return data that is appropriate for the language or country associated with that locale.  `Mimesis` currently includes support for 33 different locales:

=======  ====================  ====================
Code     Name                  Native Name
=======  ====================  ====================
`cs`     Czech                 Česky
`da`     Danish                Dansk
`de`     German                Deutsch
`de-at`  Austrian german       Deutsch
`de-ch`  Swiss german          Deutsch
`el`	 Greek                 Ελληνικά
`en`     English               English
`en-au`  Australian English    English
`en-ca`  Canadian English      English
`en-gb`  British English       English
`es`     Spanish               Español
`es-mx`  Mexican Spanish       Español
`et`     Estonian              Eesti
`fa`     Farsi                 فارسی
`fi`     Finnish               Suomi
`fr`     French                Français
`hu`     Hungarian             Magyar
`is`     Icelandic             Íslenska
`it`     Italian               Italiano
`ja`     Japanese              日本語
`kk`     Kazakh                Қазақша
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
	
	
Data providers
--------------
+------+-----------------+------------------------------------------------------------------+
| №    | Provider        | Description                                                      |
+======+=================+==================================================================+
| 1    | Address         | Address data (street name, street suffix etc.)                   |
+------+-----------------+------------------------------------------------------------------+
| 2    | Business        | Business data (company, company\_type, copyright etc.)           |
+------+-----------------+------------------------------------------------------------------+
| 3    | Code            | Codes (ISBN, EAN, IMEI etc.).                                    |
+------+-----------------+------------------------------------------------------------------+
| 4    | ClothingSizes   | Clothing sizes (international sizes, european etc.)              |
+------+-----------------+------------------------------------------------------------------+
| 5    | Datetime        | Datetime (day\_of\_week, month, year etc.)                       |
+------+-----------------+------------------------------------------------------------------+
| 6    | Development     | Data for developers (version, programming language etc.)         |
+------+-----------------+------------------------------------------------------------------+
| 7    | File            | File data (extension etc.)                                       |
+------+-----------------+------------------------------------------------------------------+
| 8    | Food            | Information on food (vegetables, fruits, measurements etc.)      |
+------+-----------------+------------------------------------------------------------------+
| 9    | Games           | Games data (game, score, pegi\_rating etc.)                      |
+------+-----------------+------------------------------------------------------------------+
| 10   | Personal        | Personal data (name, surname, age, email etc.)                   |
+------+-----------------+------------------------------------------------------------------+
| 11   | Text            | Text data (sentence, title etc.)                                 |
+------+-----------------+------------------------------------------------------------------+
| 12   | Transport       | Dummy data about transport (truck model, car etc.)               |
+------+-----------------+------------------------------------------------------------------+
| 13   | Science         | Scientific data (scientist, math\_formula etc.)                  |
+------+-----------------+------------------------------------------------------------------+
| 14   | Structured      | Structured data (html, css etc.)                                 |
+------+-----------------+------------------------------------------------------------------+
| 15   | Internet        | Internet data (facebook, twitter etc.)                           |
+------+-----------------+------------------------------------------------------------------+
| 16   | Hardware        | The data about the hardware (resolution, cpu, graphics etc.)     |
+------+-----------------+------------------------------------------------------------------+
| 17   | Numbers         | Numerical data (floats, primes, digit etc.)                      |
+------+-----------------+------------------------------------------------------------------+
| 18   | Path            | Provides methods and property for generate paths.                |
+------+-----------------+------------------------------------------------------------------+
| 19   | UnitSytem       | Provides names of unit systems in international format           |
+------+-----------------+------------------------------------------------------------------+
| 20   | Generic         | All at once                                                      |
+------+-----------------+------------------------------------------------------------------+
| 21   | Cryptographic   | Cryptographic data                                               |
+------+-----------------+------------------------------------------------------------------+


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

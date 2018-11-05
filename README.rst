.. image:: https://raw.githubusercontent.com/lk-geimfari/mimesis/master/media/logo_media.png
     :target: https://github.com/lk-geimfari/mimesis

--------------


.. image:: https://travis-ci.org/lk-geimfari/mimesis.svg?branch=master
     :target: https://travis-ci.org/lk-geimfari/mimesis

.. image:: https://ci.appveyor.com/api/projects/status/chj8huslvn6vde18?svg=true
     :target: https://ci.appveyor.com/project/lk-geimfari/mimesis

.. image:: https://readthedocs.org/projects/mimesis/badge/?version=latest
     :target: http://mimesis.readthedocs.io/?badge=latest

.. image:: https://codecov.io/gh/lk-geimfari/mimesis/branch/master/graph/badge.svg
     :target: https://codecov.io/gh/lk-geimfari/mimesis

.. image:: https://badge.fury.io/py/mimesis.svg
     :target: https://badge.fury.io/py/mimesis

.. image:: https://img.shields.io/badge/python-3.6%20%7C%203.7-brightgreen.svg
     :target: https://badge.fury.io/py/mimesis


**Mimesis** (/maɪˈmiːsəs/; Ancient Greek: μίμησις (mīmēsis), from μιμεῖσθαι (mīmeisthai), “to imitate”, from μῖμος (mimos), “imitator, actor”) is a fast and easy to use Python programming library, 
which helps generate synthetic data for a variety of purposes
in a variety of languages. This data can be particularly useful during development, 
testing, prototyping and a lot where else. For example, it could be used то populate a testing database, create complex structured JSON/XML files, anonymize data taken from a production service, etc. Basically 

Advantages
----------

This library offers a number of advantages over other similar libraries:

-  Performance. Significantly `faster`_ than other similar libraries.
-  Completeness. Strives to provide many detailed providers that offer a
   variety of data generators.
-  Simplicity. Does not require any modules other than the Python
   standard library.

.. _faster: https://mimesis.readthedocs.io/foreword.html#comparison


Installation
------------

To install mimesis, simply use pip:

.. code:: text

    [env] ~ ⟩ pip install mimesis

also you can install it manually:

.. code:: text

    [env] ⟩ git clone git@github.com:lk-geimfari/mimesis.git
    [env] ⟩ cd mimesis/
    [env] ⟩ make install


Getting started
---------------

This library is really easy to use and everyting you need is just import an object which represents type of data you need (we call such object *Provider*). In example below we import provider `Person <https://mimesis.readthedocs.io/api.html#person>`_, which represents data related to personal information, such as name, surname, email and etc:

.. code:: python

    >>> from mimesis import Person
    >>> person = Person('en')

    >>> person.full_name()
    'Antonetta Garrison'

    >>> person.occupation()
    'Backend Developer'
    
    >>> person.telephone()
    '1-408-855-5063'
    
    >>> person.identifier(mask='####/##-#')
    '2714/48-4'


More about the other providers you can read in `here`_.

.. _here: https://mimesis.readthedocs.io/quickstart.html#providers


Locales
-------

Mimesis currently includes support for 33 different `locales`_. You can
specify a locale when creating providers and they will return data that
is appropriate for the language or country associated with that locale:

.. code:: python

    >>> from mimesis import Person
    >>> from mimesis.enums import Gender

    >>> de = Person('de')
    >>> pl = Person('pl')

    >>> de.full_name(gender=Gender.FEMALE)
    'Sabrina Gutermuth'

    >>> pl.full_name(gender=Gender.MALE)
    'Światosław Tomankiewicz'

.. _locales: http://mimesis.readthedocs.io/quickstart.html#supported-locales


Documentation
-------------

You can find the complete documentation on the `Read the Docs`_.

It is divided into several sections:

-  `Foreword`_
-  `Quickstart`_
-  `Advanced Usage`_
-  `API Reference`_
-  `Contributing`_
-  `Changelog`_

You can improve it by sending pull requests to this repository.

.. _Read the Docs: http://mimesis.readthedocs.io
.. _Foreword: http://mimesis.readthedocs.io/foreword.html
.. _Quickstart: http://mimesis.readthedocs.io/quickstart.html
.. _API Reference: http://mimesis.readthedocs.io/api.html
.. _Advanced Usage: http://mimesis.readthedocs.io/advanced.html
.. _Contributing: http://mimesis.readthedocs.io/contributing.html
.. _Changelog: http://mimesis.readthedocs.io/changelog.html


How to Contribute
-----------------

1. Take a look at `contributing guidelines`_.
2. Check for open issues or open a fresh issue to start a discussion
   around a feature idea or a bug.
3. Fork the repository on GitHub to start making your changes to the
   *your_branch* branch.
4. Add yourself to the list of `contributors`_.
5. Send a pull request and bug the maintainer until it gets merged and
   published.

.. _contributing guidelines: https://github.com/lk-geimfari/mimesis/blob/master/CONTRIBUTING.rst
.. _contributors: https://github.com/lk-geimfari/mimesis/blob/master/CONTRIBUTORS.rst


License
-------

Mimesis is licensed under the MIT License. See `LICENSE`_ for more
information.

.. _LICENSE: https://github.com/lk-geimfari/mimesis/blob/master/LICENSE


Disclaimer
----------

The authors assume no responsibility for how you use this library data
generated by it. This library is designed only for developers with good
intentions. Do not use the data generated with Mimesis for illegal
purposes.

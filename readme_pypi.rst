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

You can specify a locale when creating providers and they will return data that is appropriate for the language or country associated with that locale.  `Elizabeth` currently includes support for 24 different locales.

Table of supported locales:

+------+--------+-------------+------------------------+------------------------+
| №    | Flag   | Code        | Name                   | Native name            |
+======+========+=============+========================+========================+
| 1    | 🇨🇿     | ``cs``      | Czech                  | Česky                  |
+------+--------+-------------+------------------------+------------------------+
| 2    | 🇩🇰     | ``da``      | Danish                 | Dansk                  |
+------+--------+-------------+------------------------+------------------------+
| 3    | 🇩🇪     | ``de``      | German                 | Deutsch                |
+------+--------+-------------+------------------------+------------------------+
| 4    | 🇦🇹     | ``de-at``   | Austrian german        | Deutsch                |
+------+--------+-------------+------------------------+------------------------+
| 5    | 🇺🇸     | ``en``      | English                | English                |
+------+--------+-------------+------------------------+------------------------+
| 6    | 🇦🇺     | ``en-au``   | Australian English     | English                |
+------+--------+-------------+------------------------+------------------------+
| 7    | 🇬🇧     | ``en-gb``   | British English        | English                |
+------+--------+-------------+------------------------+------------------------+
| 8    | 🇪🇸     | ``es``      | Spanish                | Español                |
+------+--------+-------------+------------------------+------------------------+
| 9    | 🇮🇷     | ``fa``      | Farsi                  | فارسی                  |
+------+--------+-------------+------------------------+------------------------+
| 10   | 🇫🇮     | ``fi``      | Finnish                | Suomi                  |
+------+--------+-------------+------------------------+------------------------+
| 11   | 🇫🇷     | ``fr``      | French                 | Français               |
+------+--------+-------------+------------------------+------------------------+
| 12   | 🇭🇺     | ``hu``      | Hungarian              | Magyar                 |
+------+--------+-------------+------------------------+------------------------+
| 13   | 🇮🇸     | ``is``      | Icelandic              | Íslenska               |
+------+--------+-------------+------------------------+------------------------+
| 14   | 🇮🇹     | ``it``      | Italian                | Italiano               |
+------+--------+-------------+------------------------+------------------------+
| 15   | 🇯🇵     | ``jp``      | Japanese               | 日本語                 |
+------+--------+-------------+------------------------+------------------------+
| 16   | 🇰🇷     | ``ko``      | Korean                 | 한국어                 |
+------+--------+-------------+------------------------+------------------------+
| 17   | 🇳🇱     | ``nl``      | Dutch                  | Nederlands             |
+------+--------+-------------+------------------------+------------------------+
| 18   | 🇳🇴     | ``no``      | Norwegian              | Norsk                  |
+------+--------+-------------+------------------------+------------------------+
| 19   | 🇵🇱     | ``pl``      | Polish                 | Polski                 |
+------+--------+-------------+------------------------+------------------------+
| 20   | 🇵🇹     | ``pt``      | Portuguese             | Português              |
+------+--------+-------------+------------------------+------------------------+
| 21   | 🇧🇷     | ``pt-br``   | Brazilian Portuguese   | Português Brasileiro   |
+------+--------+-------------+------------------------+------------------------+
| 22   | 🇷🇺     | ``ru``      | Russian                | Русский                |
+------+--------+-------------+------------------------+------------------------+
| 23   | 🇸🇪     | ``sv``      | Swedish                | Svenska                |
+------+--------+-------------+------------------------+------------------------+
| 24   | 🇹🇷     | ``tr``      | Turkish                | Türkçe                 |
+------+--------+-------------+------------------------+------------------------+


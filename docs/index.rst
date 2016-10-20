.. Church documentation master file, created by
   sphinx-quickstart on Tue Oct 18 14:11:49 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Church's documentation!
==================================

.. image:: https://raw.githubusercontent.com/lk-geimfari/church/master/examples/church.png

.. |build| image:: https://travis-ci.org/lk-geimfari/church.svg?branch=master
    :target: https://travis-ci.org/lk-geimfari/church
    :alt: Build status of the master branch

.. |pypi| image:: https://img.shields.io/badge/python-3.3%2C%203.4%2C%203.5%2C%203.6--dev-blue.svg
    :target: https://pypi.python.org/pypi/church/
    :alt: PyPI Package

.. |pypi-version| image:: https://badge.fury.io/py/church.svg
    :target: https://badge.fury.io/py/church
    :alt: Current PyPI version

.. |code-health| image:: https://landscape.io/github/lk-geimfari/church/master/landscape.svg?style=flat
    :target: https://landscape.io/github/lk-geimfari/church/master
    :alt: Code health status

.. |codacy-badge| image:: https://api.codacy.com/project/badge/Grade/d773f20efa67430683bb24fff5af9db8
    :target: https://www.codacy.com/app/likid-geimfari/church
    :alt: Codacy Badge

.. |issues| image:: https://img.shields.io/github/issues/lk-geimfari/church.svg
    :target: https://github.com/lk-geimfari/church/issues
    :alt: Current bug reports and issues

|build| |pypi| |pypi-version| |code-health| |codacy-badge| |issues|

Church is a library to generate fake data. It's very useful when you need to bootstrap your database. Church doesn't have any dependencies.

At this moment a library has 9 supported locales: 

    - English (en)
    - Español (es)
    - Deutsch (de)
    - Français (fr)
    - Italiano (it)
    - Português (pt-br)
    - Русский  (ru)
    - Norsk (no)
    - Svenska (sv)

Installation
------------

.. code:: bash

	➜  ~ git clone https://github.com/lk-geimfari/church.git
	➜  ~ cd church/
	➜  ~ python3 setup.py install

or

.. code:: bash

	➜  ~  pip install church

Testing
-------

.. code:: bash

	➜  ~ cd church/
	➜  ~ python3 -m unittest

Usage
-----

.. code:: python

    # It's very useful when you need to bootstrap your database.
    # Just create a static method that will generate fake data:

    class Patient(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120), unique=True)
        phone_number = db.Column(db.String(25))
        full_name = db.Column(db.String(100))
        gender = db.Column(db.String(64))
        nationality = db.Column(db.String(64))
        weight = db.Column(db.String(64))
        height = db.Column(db.String(64))
        blood_type = db.Column(db.String(64))

        def __init__(self, **kwargs):
            super(Patient, self).__init__(**kwargs)

        @staticmethod
        def churchify(count=2000):
            from church import Personal

            person = Personal('en')
            for _ in range(count):
                patient = Patient(email=person.email(),
                                  phone_number=person.telephone(),
                                  full_name=person.full_name('f'),
                                  gender=person.gender(),
                                  nationality=person.nationality(),
                                  weight=person.weight(),
                                  height=person.height(),
                                  blood_type=person.blood_type()
                                  )
            try:
                db.session.add(patient)
            except Exception:
                db.session.commit()

When you use only one locale, use following format:

.. code:: python

    from church import Church

    ch = Church('en')


    def patient(sex='f'):
        user = {
                'full_name': ch.personal.full_name(sex),
                'gender': ch.personal.gender(sex),
                'blood_type': ch.person.blood_type(),
                'birthday': ch.datetime.birthday()
                }
        return user


Examples
--------

- `Flask-church`_ - an extension for Flask based on Church.
- `Presturinn`_ - This is a fake API based on Falcon and Church v0.2.0.

.. _Flask-church: https://github.com/lk-geimfari/flask_church)
.. _Presturinn: https://github.com/lk-geimfari/presturinn

Contributing
------------

Your contributions are always welcome! Please take a look at the `contribution`_ guidelines first. `Here`_ you can look a list of contributors.

.. _contribution: https://github.com/lk-geimfari/church/blob/master/CONTRIBUTING.md
.. _Here: https://github.com/lk-geimfari/church/blob/master/CONTRIBUTORS.md

Disclaimer
----------

The author does not assume any responsibility for how you will use this library and how you will use data generated with this library. This library is designed only for developers and only with good intentions. Do not use the data generated with Church for illegal purposes.

Licence 
--------

Church uses the `MIT License <https://github.com/lk-geimfari/church/blob/master/LICENSE>`_.

Why church?
-----------

| Such teachings come through hypocritical liars, whose consciences have been seared as with a hot iron.
| -- Timothy 1:4

Contents
--------

.. toctree::
   :maxdepth: 2

   guide
   church

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

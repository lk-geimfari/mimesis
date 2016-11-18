.. Generic documentation master file, created by
   sphinx-quickstart on Tue Oct 18 14:11:49 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Elizabeth's documentation!
==================================

.. image:: https://raw.githubusercontent.com/lk-geimfari/elizabeth/master/other/elizabeth_1.png

.. |build| image:: https://travis-ci.org/lk-geimfari/elizabeth.svg?branch=master
    :target: https://travis-ci.org/lk-geimfari/elizabeth
    :alt: Build status of the master branch


|build|

Elizabeth is a library to generate dummy data. It's very useful when you need to bootstrap your database. Elizabeth doesn't have any dependencies.

At this moment a library has 14 supported locales:

    - Dansk (da)
    - Deutsch (de)
    - English (en)
    - Español (es)
    - Suomi (fi)
    - Français (fr)
    - Íslenska (is)
    - Italiano (it)
    - Nederlands (nl)
    - Norsk (no)
    - Português (pt)
    - Português (pt-br)
    - Русский  (ru)
    - Svenska (sv)

Installation
------------

.. code:: bash

    ➜  ~ git clone https://github.com/lk-geimfari/elizabeth.git
    ➜  ~ cd elizabeth/
    ➜  ~ python3 setup.py install

or

.. code:: bash

    ➜  ~  pip install elizabeth

Testing
-------

.. code:: bash

    ➜  ~ cd elizabeth/
    ➜  ~ python3 -m unittest
or

.. code:: bash
    ➜  ~ ./run_tests.sh

Usage
-----

.. code:: python
    # ...
    # Model from some Flask project.

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
        def _generate(count=2000):
            from elizabeth import Personal

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

    from elizabeth import Generic

    el = Generic('en')


    def patient(sex='f'):
        user = {
                'full_name': el.personal.full_name(sex),
                'gender': el.personal.gender(sex),
                'blood_type': el.person.blood_type(),
                'birthday': el.datetime.birthday()
                }
        return user


Examples
--------

- `Flask-church`_ - an extension for Flask based on Elizabeth.
- `Presturinn`_ - This is a fake API based on Falcon and Elizabeth v0.2.0.

.. _Flask-church: https://github.com/lk-geimfari/flask_church)
.. _Presturinn: https://github.com/lk-geimfari/presturinn

Contributing
------------

Your contributions are always welcome! Please take a look at the `contribution`_ guidelines first. `Here`_ you can look a list of contributors.

.. _contribution: https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md
.. _Here: https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTORS.md

Disclaimer
----------

The author does not assume any responsibility for how you will use this library and how you will use data generated with this library. This library is designed only for developers and only with good intentions. Do not use the data generated with Generic for illegal purposes.

Licence
--------

Generic uses the `MIT License <https://github.com/lk-geimfari/church/blob/master/LICENSE>`_.

Contents
--------

.. toctree::
   :maxdepth: 2

   guide
   elizabeth

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

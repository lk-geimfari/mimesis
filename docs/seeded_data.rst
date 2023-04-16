.. _seeded_data:

Seeded Data
===========

.. note::
    Keep in mind that some methods of some providers cannot be used with seeded
    providers since their crypto secure nature.

.. note::
    We support ``pytest_randomly`` and its global seed.
    If you use it during ``pytest`` runs,
    ``mimesis`` will have the same seed as shown in your ``pytest`` output:
    ``Using --randomly-seed=XXX``

For using seeded data just pass an argument *seed* (which can be *int*, *str*, *bytes*, *bytearray*)
to data provider:

.. code-block:: python

    from mimesis import Person
    from mimesis.locales import Locale

    person = Person(locale=Locale.TR, seed=0xFF)
    person.full_name()
    # Output: 'Gizem Tekand'



If you want to use the same seed for all your data providers, then using :class:`~mimesis.Generic()` is your option:

.. code-block:: python

    from mimesis import Generic
    from mimesis.locales import Locale

    generic = Generic(Locale.EN, seed='Wow. Much seed. Much random.')

    generic.person.name()
    # Output: 'Donn'
    generic.datetime.date()
    # Output: '2021-09-04'
    generic.text.word()
    # Output: 'platform'

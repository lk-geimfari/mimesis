.. _seeded_data:

Random and Seed
===============

This section describes how to use the random number generator and how to seed it.

Random
------

All of the data providers in this library are subclasses of the :class:`~mimesis.providers.base.BaseProvider`
class, which has a **random** attribute.
This attribute is an instance of the :class:`~mimesis.random.Random` class from module :mod:`~mimesis.random`.

If you are creating your own data provider, you should use this random attribute to access the **random**.

.. code-block:: python

    from mimesis import BaseProvider

    class MyProvider(BaseProvider):

        class Meta:
            name = 'my_provider'

        def my_method(self):
            return self.random.randint(0, 100)

    my_provider = MyProvider()
    my_provider.my_method()
    # Output: 42

See :ref:`providers` for more information about custom providers.


Seeding random
--------------

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


Reseeding random
----------------

To reseed the random number generator, you can use the :meth:`~mimesis.providers.BaseProvider.reseed`
method of the :class:`~mimesis.providers.BaseProvider` class

.. code-block:: python

    from mimesis import Person
    from mimesis.locales import Locale

    person = Person(Locale.EN, seed='Wow.')

    person.name()
    # Output: 'Fausto'

    person.reseed('Wow.')

    person.name()
    # Output: 'Fausto'


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

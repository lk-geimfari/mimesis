.. _seeded_data:

Random and Seed
===============

This section describes how to use the random number generator and how to seed it.

Random
------

All of the data providers in this library are subclasses of the :class:`~mimesis.providers.base.BaseProvider`
class, which has a **random** attribute.
This attribute is an instance of the :class:`~mimesis.random.Random` class from the module :mod:`~mimesis.random`.

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
    providers since their nondeterministic nature.

.. note::
    We support ``pytest_randomly`` and its global seed.
    If you use it during ``pytest`` runs,
    ``mimesis`` will have the same seed as shown in your ``pytest`` output:
    ``Using --randomly-seed=XXX``

For using seeded data just pass an argument *seed* (which can be *int*, *str*, *bytes*, *bytearray*)
to data provider:

.. code-block:: python

    from mimesis import Person, Locale

    person = Person(locale=Locale.TR, seed=0xFF)
    person.full_name()
    # Output: 'Gizem Tekand'


Reseeding random
----------------

To reseed the random number generator, you can use the :meth:`~mimesis.providers.BaseProvider.reseed`
method of the :class:`~mimesis.providers.BaseProvider` class

.. code-block:: python

    from mimesis import Person, Locale

    person = Person(Locale.EN, seed='Wow.')

    person.name()
    # Output: 'Fausto'

    person.reseed('Wow.')

    person.name()
    # Output: 'Fausto'


If you want to use the same seed for all your data providers, then using :class:`~mimesis.Generic()` is your option:

.. code-block:: python

    from mimesis import Generic, Locale

    generic = Generic(Locale.EN, seed='Wow. Much seed. Much random.')

    generic.person.name()
    # Output: 'Donn'
    generic.datetime.date()
    # Output: '2021-09-04'
    generic.text.word()
    # Output: 'platform'


Probability and Weighted Choice
-------------------------------

You might wish to produce data with a specific likelihood of appearing.

To illustrate, suppose you aim to produce random complete names for males
and females, but with a greater likelihood of female names being generated.

Here's one approach to accomplish this:

.. code-block:: python

    from mimesis import Person, Locale, Gender

    person = Person(Locale.EN)

    for _ in range(10):
        full_name = person.full_name(
            gender=person.random.weighted_choice(
                choices={
                    Gender.MALE: 0.2,
                    Gender.FEMALE: 0.8,
                }
            ),
        )
        print(full_name)


Output:

.. code-block:: text

    Chieko Flynn
    Jannet William
    Rozella Church
    Dorotha Flowers
    Annis Garcia
    Trudie Mcclure
    Alfonzo Cox
    Elsy Bridges
    Darby Bates
    Serita Cleveland


.. note::

    We are accessing **random** attribute of the :class:`~mimesis.Person` class to ensure same seed.


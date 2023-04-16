.. _quickstart:

Quickstart
==========


Basic Usage
-----------

A minimal basic usage example looks something like this:

.. code:: python

    from mimesis import Person
    from mimesis.locales import Locale
    from mimesis.enums import Gender
    person = Person(Locale.EN)

    person.full_name(gender=Gender.FEMALE)
    # Output: 'Antonetta Garrison'

    person.full_name(gender=Gender.MALE)
    # Output: 'Jordon Hall'


So what did the code above?

1. First we imported the :class:`~mimesis.Person` provider. An instance of this
   class will be our provider of personal data.
2. We import the object ``Locale`` which provides locale codes (its own attributes) and must
   be used as a parameter for locale-depend data providers.
3. We import object :class:`~mimesis.enums.Gender` which we are used as a
   parameter for the :meth:`~mimesis.Person.full_name`.
4. Next we generate random female full name.
5. The same as above, but for male.

Typical Flow
------------

The usual process for using Mimesis involves importing the necessary provider, locale,
and enums (if required), followed by creating a provider instance and invoking the
desired method with the appropriate parameters.

Consider the following example:

.. code:: python

    from mimesis import Person
    from mimesis.locales import Locale
    from mimesis.enums import Gender

    person = Person(Locale.DE)

    person.full_name(gender=Gender.FEMALE)
    'Amelia Hasek'

    person.full_name(gender=Gender.MALE)
    'Leonard Holzknecht'

    person.email(domains=['gmail.com'])
    'job1953@gmail.com'

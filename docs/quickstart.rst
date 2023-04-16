.. _quickstart:

Quickstart
==========

Basic Usage
-----------

The usual process for using Mimesis involves importing the necessary provider, locale,
and enums (if required), followed by creating a provider instance and invoking the
desired method with the appropriate parameters.

Consider the following example:

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
2. We import the object :class:`~mimesis.enums.Locale` which provides locale codes and must
   be used as a parameter for locale-depend data providers.
3. We import object :class:`~mimesis.enums.Gender` which we are used as a
   parameter for the :meth:`~mimesis.Person.full_name`.
4. Next we generate random female full name.
5. The same as above, but for male.

Creating objects
----------------

If your app requires data in one particular language, it’s preferable to
use class :class:`~mimesis.Generic()`, giving access to all class providers through a
single object, rather than through multiple separate class providers.
Using :class:`~mimesis.Generic()` will allow you to get rid of several extra lines of
code.

Incorrect:

.. code:: python

    from mimesis import Person, Datetime, Text, Code
    from mimesis.locales import Locale

    person = Person(Locale.RU)
    datetime = Datetime(Locale.RU)
    text = Text(Locale.RU)
    code = Code(Locale.RU)


Correct:

.. code:: python

    from mimesis import Generic
    from mimesis.locales import Locale
    generic = Generic(locale=Locale.EN)

    generic.person.username()
    # Output: 'sherley3354'

    generic.datetime.date()
    # Output: '14-05-2007'

Still correct:

.. code:: python

    from mimesis import Person
    from mimesis.locales import Locale

    p_en = Person(Locale.EN)
    p_sv = Person(Locale.SV)


Also correct:

.. code:: python

    from mimesis import Person

    person = Person(Locale.EN)
    with person.override_locale(Locale.SV)
        pass


Importing individual class providers may be useful if you only need access
to the data provided by that specific class. However, if you need access to a
wider range of data, it's recommended to use the :class:`~mimesis.Generic()` class instead.
This will allow you to access data from all available providers within the library.


What's next?
------------

- See :ref:`providers` for a list of all available providers.
- See :ref:`locale` for a list of all available locales.
- See :mod:`mimesis.enums` for a list of all available enums.

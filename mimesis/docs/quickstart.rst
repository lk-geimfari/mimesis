==========
Quickstart
==========

Basic Usage
-----------

The typical process for using Mimesis involves importing the necessary provider,
locale, and enums (if required). Next, create a provider instance and invoke the
desired method with the appropriate parameters.

Consider the following example:

.. code-block:: python

    from mimesis import Person
    from mimesis.locales import Locale
    from mimesis.enums import Gender
    person = Person(Locale.EN)

    person.full_name(gender=Gender.FEMALE)
    # Output: 'Antonetta Garrison'

    person.full_name(gender=Gender.MALE)
    # Output: 'Jordon Hall'


What did the code above do?

1. First we imported the :class:`~mimesis.Person` provider from **mimesis**.
   An instance of this class will serve as our provider of personal data.
2. We imported the :class:`~mimesis.enums.Locale` object, which provides locale codes and must be used as a parameter for locale-dependent data providers.
3. We imported the :class:`~mimesis.enums.Gender` object from the :mod:`mimesis.enums` module, which we use as a parameter for the :meth:`~mimesis.Person.full_name`.
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

.. code-block:: python

    from mimesis import Person, Datetime, Text, Code
    from mimesis.locales import Locale

    person = Person(Locale.RU)
    datetime = Datetime(Locale.RU)
    text = Text(Locale.RU)
    code = Code(Locale.RU)


Correct:

.. code-block:: python

    from mimesis import Generic
    from mimesis.locales import Locale
    generic = Generic(locale=Locale.EN)

    generic.person.username()
    # Output: 'sherley3354'

    generic.datetime.date()
    # Output: '14-05-2007'

Still correct:

.. code-block:: python

    from mimesis import Person
    from mimesis.locales import Locale

    p_en = Person(Locale.EN)
    p_sv = Person(Locale.SV)


Also correct:

.. code-block:: python

    from mimesis import Person

    person = Person(Locale.EN)
    with person.override_locale(Locale.SV)
        pass


Importing individual class providers may be useful if you only need access to the data provided by that specific class.
However, if you require access to a broader range of data, it is recommended to use the :class:`~mimesis.Generic()` class instead.
This will enable you to access data from all available providers within the library.


What's next?
------------

- See :ref:`providers` for a list of all available providers.
- See :ref:`structured_data_generation` for generating structured data.
- See :ref:`locale` for a list of all available locales.
- See :ref:`api-reference` for a list of all available methods, providers, and enums.

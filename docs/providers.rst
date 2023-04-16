.. _providers:

Data Providers
==============

Mimesis support over twenty different data providers available,
which can produce data related to food, people, computer hardware,
transportation, addresses, and more.

See :ref:`api-reference` for more info.

.. warning::
    Data providers are **heavy objects** since each instance of provider keeps in memory all
    the data from the provider's JSON file so you **should not** construct too many providers.

    You can read more about the heaviness of providers in `this issue <https://github.com/lk-geimfari/mimesis/issues/968>`_.

Generic Provider
----------------

When you only need to generate data for a single locale, use the :class:`~mimesis.Generic()` provider,
and you can access all Mimesis providers from one object.

.. code-block:: python

    from mimesis import Generic
    from mimesis.locales import Locale
    g = Generic(locale=Locale.ES)

    g.datetime.month()
    # Output: 'Agosto'

    g.code.imei()
    # Output: '353918052107063'

    g.food.fruit()
    # Output: 'Limón'


Built-in Providers
------------------

Most countries, where only one language is official, have data that is typical
only for these particular countries. For example, «CPF» for Brazil
(**pt-br**), «SSN» for USA (**en**).

This kind of data can be annoying when they are present in all the objects regardless of the
chosen language standard.

You can see that for yourselves by looking at the example (the code won’t run):

.. code:: python

    from mimesis import Person
    from mimesis.locales import Locale
    person = Person(locale=Locale.EN)

    person.ssn()
    person.cpf()

Perfectionists, as we are, have taken care of this in a way that some specific regional providers would
not bother other providers for other regions. For this reason, class providers with locally-specific data are
separated into a special sub-package (**mimesis.builtins**) for keeping a common class structure for
all languages and their objects.

Here’s how it works:

.. code:: python

    from mimesis import Generic
    from mimesis.locales import Locale
    from mimesis.builtins import BrazilSpecProvider

    generic = Generic(locale=Locale.PT_BR)
    generic.add_provider(BrazilSpecProvider)
    generic.brazil_provider.cpf()
    # Output: '696.441.186-00'

If you want to change default name of built-in provider, just change
value of attribute *name*, class *Meta* of the builtin provider:

.. code:: python

    BrazilSpecProvider.Meta.name = 'brasil'
    generic.add_provider(BrazilSpecProvider)
    generic.brasil.cpf()
    # Output: '019.775.929-70'

Or just inherit the class and override the value of attribute *name*
of class *Meta* of the provider (in our case this is :class:`~mimesis.builtins.BrazilSpecProvider`) :

.. code:: python

    class Brasil(BrazilSpecProvider):
        class Meta:
            name = "brasil"

    generic.add_provider(Brasil)
    generic.brasil.cnpj()
    # Output: '55.806.487/7994-45'


Generally, you don’t need to add built-it classes to the object
:class:`~mimesis.Generic`. It was done in the example with the single purpose of
demonstrating in which cases you should add a built-in class provider to
the object :class:`~mimesis.Generic`. You can use it directly, as shown below:

.. code:: python

    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Gender
    ru = RussiaSpecProvider()

    ru.patronymic(gender=Gender.FEMALE)
    # Output: 'Петровна'

    ru.patronymic(gender=Gender.MALE)
    # Output: 'Бенедиктович'


See :ref:`api-reference` for more info about built-in providers.

Custom Providers
----------------

The library supports a vast amount of data and in most cases this would
be enough. For those who want to create their own providers with more
specific data. This can be done like this:

.. code:: python

    from mimesis import Generic
    from mimesis.locales import Locale
    from mimesis.providers.base import BaseProvider


    class SomeProvider(BaseProvider):
        class Meta:
            name = "some_provider"

        @staticmethod
        def hello() -> str:
            return "Hello!"


    class Another(BaseProvider):
        def __init__(self, seed, message: str) -> None:
            super().__init__(seed=seed)
            self.message = message

        def bye(self) -> str:
            return self.message


    generic = Generic(locale=Locale.DEFAULT)
    generic.add_provider(SomeProvider) # or generic += SomeProvider
    generic.add_provider(Another, message="Bye!")

    generic.some_provider.hello()
    # Output: 'Hello!'

    generic.another.bye()
    # Output: 'Bye!'


You can also add multiple providers:

.. code:: python

    generic.add_providers(SomeProvider, Another)
    generic.some_provider.hello()
    # Output: 'Hello!'
    generic.another.bye()
    # Output: 'Bye!'

If you'll try to add provider which does not inherit :class:`~mimesis.BaseProvider`
then you got ``TypeError`` exception:

.. code:: python

    class InvalidProvider:
         @staticmethod
         def hello() -> str:
             return 'Hello!'

    generic.add_provider(InvalidProvider)
    Traceback (most recent call last):
      ...
    TypeError: The provider must be a subclass of mimesis.providers.BaseProvider.


All providers must be subclasses of :class:`~mimesis.BaseProvider`
because of ensuring a single instance of object ``Random``.

Everything is pretty easy and self-explanatory here, therefore, we will
only clarify one moment — attribute *name*, class *Meta* is the name
of a class through which access to methods of user-class providers is
carried out. By default class name is the name of the class in lowercase
letters.

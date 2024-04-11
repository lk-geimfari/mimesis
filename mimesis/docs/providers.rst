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

Types of Providers
------------------

There are two types of providers:

- Locale-dependent providers (These providers offer data that is specific to a particular locale/country).
- Locale-independent providers (These providers offer data that is universal and applicable to all countries).

Here is an example of a locale-dependent provider:

.. code-block:: python

    from mimesis import Person
    from mimesis.locales import Locale

    person = Person(locale=Locale.EN)

    person.name()
    # Output: 'John'

If you don't specify the locale for a provider that is dependent on the locale,
the default locale (i.e. **Locale.EN**) will be used.

Locale-independent providers do not require a locale to be specified:

.. code-block:: python

    from mimesis import Code

    code = Code()

    code.imei()
    # Output: '353918052107063'

Moreover, locale-independent providers raise an exception if you try to specify a locale:

.. code-block:: python

    from mimesis import Code
    from mimesis.locales import Locale

    code = Code(locale=Locale.EN)
    # TypeError: BaseProvider.__init__() got an unexpected keyword argument 'locale'


See :ref:`api-reference` to see which providers are locale-dependent and which are not.

Generic Provider
----------------

If you only require generating data for a specific locale, you may opt to
use the :class:`~mimesis.Generic()` provider. It provides access to all the
other Mimesis providers through a single object, allowing you to generate
a wide range of data types using for the same locale.

Let's take a look at an example:

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


When using :class:`~mimesis.Generic()`, Mimesis automatically detects which provider depends
on the locale and which does not, so you don't have to worry about it.

Built-in Providers
------------------

Typically, in countries where only one language is the official language, there are specific types
of data that are unique to those countries. For instance, in Brazil (**Locale.PT_BR**) the "CPF" is used,
while in the USA (**Locale.EN**) the "SSN" is used.

However, this type of data can become bothersome when it appears in all objects
irrespective of the selected locale.

By examining the example provided (the code won't execute), you can see this for yourself:

.. code-block:: python

    from mimesis import Person
    from mimesis.locales import Locale
    person = Person(locale=Locale.EN)

    person.ssn()
    person.cpf()

As perfectionists, we have addressed this issue by separating class providers with locally-specific
data into a special sub-package (mimesis.builtins). This ensures that providers for specific regions
do not cause any inconvenience for providers for other regions. This approach helps to maintain a common
class structure for all languages and their objects.

Here’s how it works:

.. code-block:: python

    from mimesis import Generic
    from mimesis.locales import Locale
    from mimesis.builtins import BrazilSpecProvider

    generic = Generic(locale=Locale.PT_BR)
    generic.add_provider(BrazilSpecProvider)
    generic.brazil_provider.cpf()
    # Output: '696.441.186-00'

To modify the default name of the built-in provider, you can change the value of the attribute **Meta.name**:

.. code-block:: python

    BrazilSpecProvider.Meta.name = 'brasil'
    generic.add_provider(BrazilSpecProvider)
    generic.brasil.cpf()
    # Output: '019.775.929-70'

Or just inherit the class and override the value of attribute *name*
of class *Meta* of the provider (in our case this is :class:`~mimesis.builtins.BrazilSpecProvider`) :

.. code-block:: python

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

.. code-block:: python

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

The library provides support for a wide range of data, which is sufficient
for most use cases. However, for those who wish to create their own providers
with more specific data, this can be achieved as follows:

.. code-block:: python

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


In addition, you can also add multiple providers:

.. code-block:: python

    generic.add_providers(SomeProvider, Another)
    generic.some_provider.hello()
    # Output: 'Hello!'
    generic.another.bye()
    # Output: 'Bye!'

If you attempt to add a provider that does not inherit from :class:`~mimesis.providers.base.BaseProvider`,
you will receive a **TypeError** exception:

.. code-block:: python

    class InvalidProvider:
         @staticmethod
         def hello() -> str:
             return 'Hello!'

    generic.add_provider(InvalidProvider)
      ...
      ...
    TypeError: The provider must be a subclass of mimesis.providers.BaseProvider.


All providers must be subclasses of :class:`~mimesis.providers.base.BaseProvider` to ensure
that only a single instance of the Random object is used.

Everything here is quite straightforward, but we would like to clarify one point:
the **name** attribute in the **Meta** class refers to the name of the class through which access
to methods of user-class providers is carried out. By default, the class name (``cls.__name__``) is used in
lowercase letters.

See :ref:`seeded_data` to learn how to access the :class:`~mimesis.random.Random` object.


Custom Data Providers
---------------------

To create your own **data provider** and store your data
in JSON files, you can follow these steps:

First, create a directory to store your data with the following structure:

.. code-block:: text

    custom_datadir/
    ├── de
    │   └── file_name.json
    ├── en
    │   └── file_name.json
    └── ru
        └── file_name.json

To ensure that your provider supports the desired locale, every custom
**data directory** (datadir) must include a directory with the name of the locale.

Next, you need to populate the files with the relevant data.

For example:

.. code-block:: json

    {
      "key": [
        "value1",
        "value2",
        "value3"
      ]
    }

Afterwards, you will need to create a class that inherits from :class:`~mimesis.providers.base.BaseDataProvider`:

.. code-block:: python

    from pathlib import Path

    from mimesis import BaseDataProvider
    from mimesis.locales import Locale

    class CustomDataProvider(BaseDataProvider):
        class Meta:
            name = 'custom_provider'
            datafile = 'file_name.json'
            datadir = Path(__file__).parent / 'custom_datadir'

        def my_method(self):
            return self.random.choice(self.extract(['key']))

The **Meta** class is required and must contain the following attributes:

- **name** - the name of the provider in lowercase letters.
- **datafile** - the name of the file with data.
- **datadir** - the path to the directory with data (must be an instance of :class:`~pathlib.Path`).

That’s it! Now you can use your custom data provider:

.. code-block:: python

    >>> from mimesis.locales import Locale
    >>> cdp = CustomDataProvider(Locale.EN)
    >>> cdp.my_method()
    'value3'

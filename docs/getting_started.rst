.. _getting_started:

Getting Started
===============

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

Locale
------

You can specify a locale when creating providers and they will return data that
is appropriate for the language or country associated with that locale:

.. code-block:: python

    from mimesis import Address
    from mimesis.locales import Locale

    de = Address(locale=Locale.DE)
    ru = Address(locale=Locale.RU)

    de.region()
    # Output: 'Brandenburg'

    ru.federal_subject()
    # Output: 'Алтайский край'

    de.address()
    # Output: 'Mainzer Landstraße 912'

    >>> ru.address()
    # Output: 'ул. Пехотная 125'


See the table below for more details.

Supported locales
~~~~~~~~~~~~~~~~~

Mimesis currently includes support for 34 different locales:

=======  ====================  ====================  ====================
Code     Associated attribute  Name                  Native Name
=======  ====================  ====================  ====================
`cs`     ``Locale.CS``         Czech                 Česky
`da`     ``Locale.DA``         Danish                Dansk
`de`     ``Locale.DE``         German                Deutsch
`de-at`  ``Locale.DE_AT``      Austrian german       Deutsch
`de-ch`  ``Locale.DE_CH``      Swiss german          Deutsch
`el`	 ``Locale.EL``         Greek                 Ελληνικά
`en`     ``Locale.EN``         English               English
`en-au`  ``Locale.EN_AU``      Australian English    English
`en-ca`  ``LocALE.EN_CA``      Canadian English      English
`en-gb`  ``Locale.EN_GB``      British English       English
`es`     ``Locale.ES``         Spanish               Español
`es-mx`  ``Locale.ES_MX``      Mexican Spanish       Español
`et`     ``Locale.ET``         Estonian              Eesti
`fa`     ``Locale.FA``         Farsi                 فارسی
`fi`     ``Locale.FI``         Finnish               Suomi
`fr`     ``Locale.FR``         French                Français
`hu`     ``Locale.HU``         Hungarian             Magyar
`is`     ``Locale.IS``         Icelandic             Íslenska
`it`     ``Locale.IT``         Italian               Italiano
`ja`     ``Locale.JA``         Japanese              日本語
`kk`     ``Locale.KK``         Kazakh                Қазақша
`ko`	 ``Locale.KO``         Korean                한국어
`nl`     ``Locale.NL``         Dutch                 Nederlands
`nl-be`  ``Locale.NL_BE``      Belgium Dutch         Nederlands
`no`     ``Locale.NO``         Norwegian             Norsk
`pl`     ``Locale.PL``         Polish                Polski
`pt`     ``Locale.PT``         Portuguese            Português
`pt-br`  ``Locale.PT_BR``      Brazilian Portuguese  Português Brasileiro
`ru`     ``Locale.RU``         Russian               Русский
`sk`     ``Locale.SK``         Slovak                Slovensky
`sv`     ``Locale.SV``         Swedish               Svenska
`tr`     ``Locale.TR``         Turkish               Türkçe
`uk`     ``Locale.UK``         Ukrainian             Українська
`zh`     ``Locale.ZH``         Chinese               汉语
=======  ====================  ====================  ====================

Override locale
~~~~~~~~~~~~~~~

Sometimes you need only some data from other locale and creating an instance for such cases
is not really good,  so it's better just temporarily override current locale for provider's instance:

.. code-block:: python

    from mimesis import Person
    from mimesis.locales import Locale

    person = Person(locale=Locale.EN)
    person.full_name()
    # Output: 'Ozie Melton'

    with person.override_locale(Locale.RU):
        person.full_name()

    # Output: 'Симона Богданова'

    person.full_name()
    # Output: 'Waldo Foster'

You can also use it with :class:`~mimesis.Generic()`:

.. code-block:: python

    from mimesis import Generic
    from mimesis.locales import Locale

    generic = Generic(locale=Locale.EN)
    generic.text.word()
    # Output: 'anyone'

    with generic.text.override_locale(Locale.FR):
        generic.text.word()

    # Output: 'mieux'

    generic.text.word()
    # Output: 'responsibilities'


Data Providers
--------------
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


.. _locales:

Seeded Data
-----------

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

Schema and Fields
-----------------

For generating data by schema, just create an instance of :class:`~mimesis.schema.Field`
object, which takes any string which represents the name of data
provider in format *provider.method_name* (explicitly defines that the
method *method_name* belongs to data-provider *provider*) or *method* (will be
chosen the first provider which has a method *method_name*) and the
**\**kwargs** of the method *method_name*, after that you should
describe the schema in lambda function and pass it to
the object :class:`~mimesis.schema.Schema` and call method :meth:`~mimesis.schema.Schema.create`.

Since **v5.6.0** you can use multiplication, instead of the explicit call of :meth:`~mimesis.schema.Schema.create`.
Please, see :meth:`~mimesis.schema.Schema.__mul__` of :class:`~mimesis.schema.Schema` for more details.

Optionally, you can apply a *key function* to result returned by the
method, to do it, just pass the parameter `key` with a callable object
which returns final result.

Example of usage:

.. code:: python

    from mimesis.enums import Gender
    from mimesis.locales import Locale
    from mimesis.schema import Field, Schema

    _ = Field(locale=Locale.EN)
    schema = Schema(schema=lambda: {
        "pk": _("increment"),
        "uid": _("uuid"),
        "name": _("text.word"),
        "version": _("version", pre_release=True),
        "timestamp": _("timestamp", posix=False),
        "owner": {
            "email": _("person.email", domains=["test.com"], key=str.lower),
            "token": _("token_hex"),
            "creator": _("full_name", gender=Gender.FEMALE),
        },
    })
    schema.create(iterations=3)
    # Since v5.6.0 you can do the same thing using multiplication:
    schema * 3


Output:

.. code:: json

    [
      {
        "pk": 1,
        "uid": "c1b2fda1-762b-4c0b-aef7-e995e19758b6",
        "name": "brother",
        "version": "3.0.6-alpha.9",
        "timestamp": "2016-12-07T13:26:54Z",
        "owner": {
          "email": "tewing1841@test.com",
          "token": "09960ce907dee56a3c4a6730b7e1ff6ad9620b878c68ff978bfe296da09c1b4b",
          "creator": "Travis Burton"
        }
      },
      {
        "pk": 2,
        "uid": "b0f33a7e-0e3e-4bf0-92df-3ba869add555",
        "name": "disney",
        "version": "2.6.0-alpha.11",
        "timestamp": "2017-02-11T10:45:27Z",
        "owner": {
          "email": "cyprus1904@test.com",
          "token": "a087fadffce394141d3e93c895e4da6db906a60fd0886bad909dc179861b4650",
          "creator": "Dot Anderson"
        }
      },
      {
        "pk": 3,
        "uid": "19b782f0-abd3-468c-9fe2-a82d47212d0c",
        "name": "mar",
        "version": "4.7.0-beta.4",
        "timestamp": "2003-08-22T08:22:24Z",
        "owner": {
          "email": "artiller1822@test.com",
          "token": "d35edc15e74c101e3c2fb6a9b8b74bf40ed21d45b984cc5516105f3853e375e9",
          "creator": "Enda Martinez"
        }
      }
    ]


By default, :class:`~mimesis.schema.Field` works only with providers which supported by :class:`~mimesis.Generic`,
to change this behavior should be passed parameter *providers* with a sequence of data providers:

.. code:: python

    from mimesis.schema import Field
    from mimesis.locales import Locale
    from mimesis import builtins

    custom_providers = (
         builtins.RussiaSpecProvider,
         builtins.NetherlandsSpecProvider,
    )
    _ = Field(Locale.EN, providers=custom_providers)

    _('snils')
    # Output: '239-315-742-84'

    _('bsn')
    # Output: '657340522'


You can create infinite lazy schema-based data generators using :meth:`~mimesis.schema.Schema.loop`.:

.. code:: python

    from mimesis import Schema, Field
    from mimesis.locales import Locale

    field = Field(Locale.DE)

    schema = Schema(
        schema=lambda: {
            "pk": field("increment"),
            "name": field("full_name"),
            "email": field("email", domains=["example.org"]),
        }
    )


    for obj in schema.loop():
        pk = obj.get("pk")

        if pk > 100:
            break

        print(obj)

Output:

.. code:: text

    {'pk': 1, 'name': 'Wenzel Feigenbaum', 'email': 'cambridge1883@example.org'}
    ...
    {'pk': 100, 'name': 'Gerard Garber', 'email': 'travelers1947@example.org'}


or create lazy data generator of limited length, using :meth:`~mimesis.schema.Schema.iterator`:


.. code:: python

    from mimesis import Schema, Field
    from mimesis.locales import Locale

    field = Field(Locale.DE)

    schema = Schema(
        schema=lambda: {
            "pk": field("increment"),
            "name": field("full_name"),
            "email": field("email", domains=["example.org"]),
        }
    )


    for obj in schema.iterator(100):
        print(obj)

Output:

.. code:: text

    {'pk': 1, 'name': 'Lea Bohn', 'email': 'best2045@example.org'}
    ...
    {'pk': 100, 'name': 'Karsten Haase', 'email': 'dennis2024@example.org'}


Since **8.0.0** you can use th :class:`~mimesis.schema.Fieldset` for creating set of fields.

See **Fieldset and Pandas** section for more details.

Fieldset and Pandas
-------------------

If your aim is to create synthetic data for your Pandas dataframes,
you can make use of the Mimesis.

With Mimesis, you can create datasets that are similar in structure to your real-world data,
allowing you to perform accurate and reliable testing and analysis:

.. code:: python

    import pandas as pd
    from mimesis.schema import Fieldset
    from mimesis.locales import Locale

    fs = Fieldset(locale=Locale.EN)

    df = pd.DataFrame.from_dict({
        "ID": fs("increment", i=5),
        "Name": fs("person.full_name", i=5),
        "Email": fs("email", i=5),
        "Phone": fs("telephone", mask="+1 (###) #5#-7#9#", i=5),
    })

    # Disable truncation of rows.
    pd.set_option('display.max_rows', None)
    # Disable truncation of columns
    pd.set_option('display.max_columns', None)

    print(df)

Output:

.. code:: text

    ID             Name                          Email              Phone
    1     Jamal Woodard              ford1925@live.com  +1 (202) 752-7396
    2       Loma Farley               seq1926@live.com  +1 (762) 655-7893
    3  Kiersten Barrera      relationship1991@duck.com  +1 (588) 956-7099
    4   Jesus Frederick  troubleshooting1901@gmail.com  +1 (514) 255-7091
    5   Blondell Bolton       strongly2081@example.com  +1 (327) 952-7799


Exporting Data
--------------

You can export data as JSON, CSV or as pickled representations of objects:

.. code:: python

    from mimesis.locales import Locale
    from mimesis.schema import Field, Schema

    _ = Field(locale=Locale.EN)
    schema = Schema(schema=lambda: {
        "pk": _("increment"),
        "name": _("text.word"),
        "version": _("version"),
        "timestamp": _("timestamp", posix=False),
    })
    schema.to_csv(file_path='data.csv', iterations=1000)
    schema.to_json(file_path='data.json', iterations=1000)
    schema.to_pickle(file_path='data.obj', iterations=1000)


Example of the content of ``data.csv`` (truncated):

.. code:: text

    pk,uid,name,version,timestamp
    1,save,6.8.6-alpha.3,2018-09-21T21:30:43Z
    2,sponsors,6.9.6-rc.7,2015-03-02T06:18:44Z
    3,after,4.5.6-rc.8,2022-03-31T02:56:15Z
    4,queen,9.0.6-alpha.11,2008-07-22T05:56:59Z


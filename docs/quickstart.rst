.. _quickstart:

Quickstart
==========

This page gives a good introduction to Mimesis. It
assumes you already have Mimesis installed.
If you do not, head over to the :ref:`installation` section.


Basic Usage
-----------

A minimal usage example:

.. code:: python

    >>> from mimesis import Person
    >>> from mimesis.enums import Gender
    >>> person = Person('en')

    >>> person.full_name(gender=Gender.FEMALE)
    'Antonetta Garrison'

    >>> person.full_name(gender=Gender.MALE)
    'Jordon Hall'


So what did the code above?

1. First we imported the :class:`~mimesis.Person` class. An instance of this
   class will be our provider of personal data.
2. We import object :class:`~mimesis.enums.Gender` which we are used as a
   parameter for the :meth:`~mimesis.Person.full_name`.
3. Next we generate random female full name for locale **en**.
4. The same as above, but for male.


Seeded Data
-----------

For using seeded data just pass an argument *seed* (which can be *int*, *str*, *bytes*, *bytearray*)
to data provider:

.. code-block:: python

    >>> from mimesis import Person

    >>> person = Person('tr', seed=0xFF)
    >>> person.full_name()
    'Gizem Tekand'



.. _locales:

Locales
-------

You can specify a locale when creating providers and they will return data that is appropriate for
the language or country associated with that locale:

.. code-block:: python

    >>> from mimesis import Address

    >>> de = Address('de')
    >>> ru = Address('ru')

    >>> de.region()
    'Brandenburg'

    >>> ru.federal_subject()
    'Алтайский край'

    >>> de.address()
    'Mainzer Landstraße 912'

    >>> ru.address()
    'ул. Пехотная 125'



Supported locales
~~~~~~~~~~~~~~~~~

Mimesis currently includes support for 33 different locales:

=======  ====================  ====================
Code     Name                  Native Name
=======  ====================  ====================
`cs`     Czech                 Česky
`da`     Danish                Dansk
`de`     German                Deutsch
`de-at`  Austrian german       Deutsch
`de-ch`  Swiss german          Deutsch
`el`	 Greek                 Ελληνικά
`en`     English               English
`en-au`  Australian English    English
`en-ca`  Canadian English      English
`en-gb`  British English       English
`es`     Spanish               Español
`es-mx`  Mexican Spanish       Español
`et`     Estonian              Eesti
`fa`     Farsi                 فارسی
`fi`     Finnish               Suomi
`fr`     French                Français
`hu`     Hungarian             Magyar
`is`     Icelandic             Íslenska
`it`     Italian               Italiano
`ja`     Japanese              日本語
`kk`     Kazakh                Қазақша
`ko`	 Korean                한국어
`nl`     Dutch                 Nederlands
`nl-be`  Belgium Dutch         Nederlands
`no`     Norwegian             Norsk
`pl`     Polish                Polski
`pt`     Portuguese            Português
`pt-br`  Brazilian Portuguese  Português Brasileiro
`ru`     Russian               Русский
`sv`     Swedish               Svenska
`tr`     Turkish               Türkçe
`uk`     Ukrainian             Український
`zh`     Chinese               汉语
=======  ====================  ====================


Providers
---------
Mimesis support over twenty different data providers available,
which can produce data related to food, people, computer hardware,
transportation, addresses, and more. List of supported data providers
available in the tables below.

Usual Providers
~~~~~~~~~~~~~~~

+------+----------------------------------+------------------------------------------------------------------+
| №    | Provider                         | Description                                                      |
+======+==================================+==================================================================+
| 1    | :class:`~mimesis.Address`        | Address data (street name, street suffix etc.)                   |
+------+----------------------------------+------------------------------------------------------------------+
| 2    | :class:`~mimesis.Business`       | Business data (company, company\_type, copyright etc.)           |
+------+----------------------------------+------------------------------------------------------------------+
| 3    | :class:`~mimesis.Code`           | Codes (ISBN, EAN, IMEI etc.).                                    |
+------+----------------------------------+------------------------------------------------------------------+
| 4    | :class:`~mimesis.ClothingSize`   | Clothing sizes (international sizes, european etc.)              |
+------+----------------------------------+------------------------------------------------------------------+
| 5    | :class:`~mimesis.Datetime`       | Datetime (day of week, month, year etc.)                         |
+------+----------------------------------+------------------------------------------------------------------+
| 6    | :class:`~mimesis.Development`    | Data for developers (version, programming language etc.)         |
+------+----------------------------------+------------------------------------------------------------------+
| 7    | :class:`~mimesis.File`           | File data (extension etc.)                                       |
+------+----------------------------------+------------------------------------------------------------------+
| 8    | :class:`~mimesis.Food`           | Information on food (vegetables, fruits, measurements etc.)      |
+------+----------------------------------+------------------------------------------------------------------+
| 9    | :class:`~mimesis.Games`          | Games data (game, score, pegi\_rating etc.)                      |
+------+----------------------------------+------------------------------------------------------------------+
| 10   | :class:`~mimesis.Person`         | Personal data (name, surname, age, email etc.)                   |
+------+----------------------------------+------------------------------------------------------------------+
| 11   | :class:`~mimesis.Text`           | Text data (sentence, title etc.)                                 |
+------+----------------------------------+------------------------------------------------------------------+
| 12   | :class:`~mimesis.Transport`      | Dummy data about transport (truck model, car etc.)               |
+------+----------------------------------+------------------------------------------------------------------+
| 13   | :class:`~mimesis.Science`        | Scientific data (rna sequence dna sequence, etc.)                |
+------+----------------------------------+------------------------------------------------------------------+
| 14   | :class:`~mimesis.Structure`      | Structured data (html, css etc.)                                 |
+------+----------------------------------+------------------------------------------------------------------+
| 15   | :class:`~mimesis.Internet`       | Internet data (facebook, twitter etc.)                           |
+------+----------------------------------+------------------------------------------------------------------+
| 16   | :class:`~mimesis.Hardware`       | The data about the hardware (resolution, cpu, graphics etc.)     |
+------+----------------------------------+------------------------------------------------------------------+
| 17   | :class:`~mimesis.Numbers`        | Numerical data (floats, primes, digit etc.)                      |
+------+----------------------------------+------------------------------------------------------------------+
| 18   | :class:`~mimesis.Path`           | Provides methods and property for generate paths.                |
+------+----------------------------------+------------------------------------------------------------------+
| 19   | :class:`~mimesis.Payment`        | Payment data (credit_card, credit_card_network, etc.)            |
+------+----------------------------------+------------------------------------------------------------------+
| 20   | :class:`~mimesis.UnitSystem`     | Provides names of unit systems in international format.          |
+------+----------------------------------+------------------------------------------------------------------+
| 21   | :class:`~mimesis.Generic`        | All at once.                                                     |
+------+----------------------------------+------------------------------------------------------------------+
| 22   | :class:`~mimesis.Cryptographic`  | Cryptographic data.                                              |
+------+----------------------------------+------------------------------------------------------------------+


Generating by schema
~~~~~~~~~~~~~~~~~~~~

+------+----------------------------------------+----------------------------------------------+
| №    | Provider                               | Description                                  |
+======+========================================+==============================================+
|  1   | :class:`~mimesis.schema.AbstractField` | Can represent any method of any provider.    |
+------+----------------------------------------+----------------------------------------------+
|  2   | :class:`~mimesis.schema.Field`         | Alias for schema.AbstractField.              |
+------+----------------------------------------+----------------------------------------------+



Builtin data providers
~~~~~~~~~~~~~~~~~~~~~~

+------+----------------------------------------------------+--------------------------------------------+
| №    | Provider                                           | Description                                |
+======+====================================================+============================================+
|  1   | :class:`~mimesis.builtins.RussiaSpecProvider`      | Specific data provider for Russia          |
+------+----------------------------------------------------+--------------------------------------------+
|  2   | :class:`~mimesis.builtins.BrazilSpecProvider`      | Specific data provider for Brazil          |
+------+----------------------------------------------------+--------------------------------------------+
|  3   | :class:`~mimesis.builtins.JapanSpecProvider`       | Specific data provider for Japan           |
+------+----------------------------------------------------+--------------------------------------------+
|  4   | :class:`~mimesis.builtins.USASpecProvider`         | Specific data provider for USA             |
+------+----------------------------------------------------+--------------------------------------------+
|  5   | :class:`~mimesis.builtins.NetherlandsSpecProvider` | Specific data provider for Netherlands     |
+------+----------------------------------------------------+--------------------------------------------+
|  6   | :class:`~mimesis.builtins.GermanySpecProvider`     | Specific data provider for Germany         |
+------+----------------------------------------------------+--------------------------------------------+
|  7   | :class:`~mimesis.builtins.UkraineSpecProvider`     | Specific data provider for Ukraine         |
+------+----------------------------------------------------+--------------------------------------------+
|  8   | :class:`~mimesis.builtins.PolandSpecProvider`      | Specific data provider for Poland          |
+------+----------------------------------------------------+--------------------------------------------+

Generic Provider
----------------

When you only need to generate data for a single locale, use the :class:`~mimesis.Generic` provider,
and you can access all Mimesis providers from one object.

.. code-block:: python

    >>> from mimesis import Generic
    >>> g = Generic('es')

    >>> g.datetime.month()
    'Agosto'

    >>> g.code.imei()
    '353918052107063'

    >>> g.food.fruit()
    'Limón'

    >>> g.science.rna()
    'GCTTTAGACC'



Custom Providers
----------------

The library supports a vast amount of data and in most cases this would
be enough. For those who want to create their own providers with more
specific data. This can be done like this:

.. code:: python

    >>> from mimesis.providers.base import BaseProvider

    >>> class SomeProvider(BaseProvider):
    ...     class Meta:
    ...         name = "some_provider"
    ...
    ...     @staticmethod
    ...     def hello():
    ...         return 'Hello!'

    >>> class Another(BaseProvider):
    ...     @staticmethod
    ...     def bye():
    ...         return "Bye!"

    >>> generic.add_provider(SomeProvider)
    >>> generic.add_provider(Another)

    >>> generic.some_provider.hello()
    'Hello!'

    >>> generic.another.bye()
    'Bye!'

You can also add multiple providers:

.. code:: python

    >>> generic.add_providers(SomeProvider, Another)
    >>> generic.some_provider.hello()
    'Hello!'
    >>> generic.another.bye()
    'Bye!'

Everything is pretty easy and self-explanatory here, therefore, we will
only clarify one moment — attribute *name*, class *Meta* is the name
of a class through which access to methods of user-class providers is
carried out. By default class name is the name of the class in lowercase 
letters.


Built-in Providers
------------------

Most countries, where only one language is official, have data typical
only for these particular countries. For example, «CPF» for Brazil
(**pt-br**), «SSN» for USA (**en**). This kind of data can cause
discomfort and meddle with the order (or at least annoy) by being
present in all the objects regardless of the chosen language standard.
You can see that for yourselves by looking at the example (the code
won’t run):

.. code:: python

    >>> from mimesis import Person
    >>> person = Person('en')

    >>> person.ssn()
    >>> person.cpf()

We bet everyone would agree that this does not look too good.
Perfectionists, as we are, have taken care of this in a way that some
specific regional provider would not bother other providers for other
regions. For this reason, class providers with locally-specific data are
separated into a special sub-package (**mimesis.builtins**) for keeping
a common class structure for all languages and their objects.

Here’s how it works:

.. code:: python

    >>> from mimesis import Generic
    >>> from mimesis.builtins import BrazilSpecProvider

    >>> generic = Generic('pt-br')
    >>> generic.add_provider(BrazilSpecProvider)
    >>> generic.brazil_provider.cpf()
    '696.441.186-00'

If you want to change default name of built-in provider, just change
value of attribute *name*, class *Meta* of the builtin provider:

.. code:: python

    >>> BrazilSpecProvider.Meta.name = 'brasil'
    >>> generic.add_provider(BrazilSpecProvider)
    >>> generic.brasil.cpf()
    '019.775.929-70'

Or just inherit the class and override the value of attribute *name*
of class *Meta* of the provider (in our case this is :class:`~mimesis.builtins.BrazilSpecProvider`) :

.. code:: python

    >>> class Brasil(BrazilSpecProvider):
    ...
    ...     class Meta:
    ...         name = "brasil"
    ...
    >>> generic.add_provider(Brasil)
    >>> generic.brasil.cnpj()
    '55.806.487/7994-45'

Generally, you don’t need to add built-it classes to the object
:class:`~mimesis.Generic`. It was done in the example with the single purpose of
demonstrating in which cases you should add a built-in class provider to
the object :class:`~mimesis.Generic`. You can use it directly, as shown below:

.. code:: python

    >>> from mimesis.builtins import RussiaSpecProvider
    >>> from mimesis.enums import Gender
    >>> ru = RussiaSpecProvider()

    >>> ru.patronymic(gender=Gender.FEMALE)
    'Петровна'

    >>> ru.patronymic(gender=Gender.MALE)
    'Бенедиктович'


Generating by Schema
--------------------

For generating data by schema, just create an instance of :class:`~mimesis.schema.Field`
object, which takes any string which represents the name of data
provider in format *provider.method_name* (explicitly defines that the
method *method_name* belongs to data-provider *provider*) or *method* (will be
chosen the first provider which has a method *method_name*) and the
**\**kwargs** of the method *method_name*, after that you should
describe the schema in lambda function and pass it to
the object :class:`~mimesis.schema.Schema` and call method :meth:`~mimesis.schema.Schema.create`.

Optionally, you can apply a *key function* to result returned by the
method, to do it, just pass the parameter `key` with a callable object
which returns final result.

Example of usage:

.. code:: python

    >>> from mimesis.schema import Field, Schema
    >>> from mimesis.enums import Gender
    >>> _ = Field('en')
    >>> description = (
    ...     lambda: {
    ...         'id': _('uuid'),
    ...         'name': _('text.word'),
    ...         'version': _('version', pre_release=True),
    ...         'timestamp': _('timestamp', posix=False),
    ...         'owner': {
    ...             'email': _('person.email', key=str.lower),
    ...             'token': _('token'),
    ...             'creator': _('full_name', gender=Gender.FEMALE),
    ...         },
    ...     }
    ... )
    >>> schema = Schema(schema=description)
    >>> schema.create(iterations=1)

Output:

.. code:: json

    [
      {
        "owner": {
          "email": "aisling2032@yahoo.com",
          "token": "cc8450298958f8b95891d90200f189ef591cf2c27e66e5c8f362f839fcc01370",
          "creator": "Veronika Dyer"
        },
        "name": "pleasure",
        "version": "4.3.1-rc.5",
        "id": "33abf08a-77fd-1d78-86ae-04d88443d0e0",
        "timestamp": "2018-07-29T15:25:02Z"
      }
    ]

By default, :class:`~mimesis.schema.Field` works only with providers which supported by :class:`~mimesis.Generic`,
to change this behavior should be passed parameter *providers* with a sequence of data providers:

.. code:: python

    >>> from mimesis.schema import Field
    >>> from mimesis import builtins as b

    >>> extra = (
    ...     b.RussiaSpecProvider,
    ...     b.NetherlandsSpecProvider,
    ... )
    >>> _ = Field('en', providers=extra)

    >>> _('snils')
    '239-315-742-84'

    >>> _('bsn')
    '657340522'


Decorators
----------

If your locale belongs to the family of Cyrillic languages, but you need
latinized locale-specific data, then you can use decorator :func:`~mimesis.decorators.romanized` which
help you romanize your data.

Example of usage for romanization of Russian full name:

.. code:: python

    >>> from mimesis.decorators import romanized

    >>> @romanized('ru')
    ... def russian_name():
    ...     return 'Вероника Денисова'

    >>> russian_name()
    'Veronika Denisova'

At this moment it works only for Russian (**ru**),
Ukrainian (**uk**) and Kazakh (**kk**):

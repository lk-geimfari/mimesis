.. _getting_started:

Getting Started
===============

Installation
------------

Within the pre-activated environment, use the following command to install Mimesis:

.. code-block:: sh

    (env) ➜ pip install mimesis

Use the following command to install Mimesis in Jupyter Notebook:

.. code-block:: sh

    (env) ➜ ! pip install mimesis

Installation using *Pipenv* is pretty same:

.. code-block:: sh

    (env) ➜ pipenv install --dev mimesis


If you want to work with the latest Mimesis code before it's released, install or
update the code from the master branch:

.. code-block:: sh

    (env) ➜ git clone git@github.com:lk-geimfari/mimesis.git
    (env) ➜ cd mimesis/
    (env) ➜ make install


Basic Usage
-----------

A minimal basic usage example looks something like this:

.. code:: python

    >>> from mimesis import Person
    >>> from mimesis.enums import Gender
    >>> person = Person('en')

    >>> person.full_name(gender=Gender.FEMALE)
    'Antonetta Garrison'

    >>> person.full_name(gender=Gender.MALE)
    'Jordon Hall'


So what did the code above?

1. First we imported the :class:`~mimesis.Person` provider. An instance of this
   class will be our provider of personal data.
2. We import object :class:`~mimesis.enums.Gender` which we are used as a
   parameter for the :meth:`~mimesis.Person.full_name`.
3. Next we generate random female full name.
4. The same as above, but for male.


Data Providers
--------------
Mimesis support over twenty different data providers available,
which can produce data related to food, people, computer hardware,
transportation, addresses, and more.

See :ref:`api-reference` for more info.

.. attention::
    Data providers are **heavy objects** since each instance of provider keeps in memory all
    the data from the provider's JSON file so you **should not** construct too many providers.

    You can read more about the heaviness of providers in `this issue <https://github.com/lk-geimfari/mimesis/issues/968>`_.

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


.. _locales:

Locales
-------

You can specify a locale when creating providers and they will return data that
is appropriate for the language or country associated with that locale:

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

Override locale
~~~~~~~~~~~~~~~

Sometimes you need only some data from other locale and creating an instance for such cases
is not really good,  so it's better just temporarily override current locale for provider's instance:

.. code-block:: python

    >>> from mimesis import Person
    >>> from mimesis import locales

    >>> person = Person(locales.EN)
    >>> person.full_name()
    'Ozie Melton'

    >>> with person.override_locale(locales.RU):
    ...     person.full_name()

    'Симона Богданова'

    >>> person.full_name()
    'Waldo Foster'

You can also use it with :class:`~mimesis.Generic()`:

.. code-block:: python

    >>> from mimesis import Generic
    >>> from mimesis import locales

    >>> generic = Generic(locales.EN)
    >>> generic.text.word()
    'anyone'

    >>> with generic.text.override_locale(locales.FR):
    ...     generic.text.word()

    'mieux'

    >>> generic.text.word()
    'responsibilities'

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
`sk`     Slovak                Slovensky
`sv`     Swedish               Svenska
`tr`     Turkish               Türkçe
`uk`     Ukrainian             Українська
`zh`     Chinese               汉语
=======  ====================  ====================

Seeded Data
-----------

.. note::
    Keep in mind that some methods of some providers cannot be used with seeded
    providers since their crypto secure nature.

For using seeded data just pass an argument *seed* (which can be *int*, *str*, *bytes*, *bytearray*)
to data provider:

.. code-block:: python

    >>> from mimesis import Person

    >>> person = Person('tr', seed=0xFF)
    >>> person.full_name()
    'Gizem Tekand'



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


See :ref:`api-reference` for more info about built-in providers.

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

If you'll try to add provider which does not inherit :class:`~mimesis.BaseProvider`
then you got ``TypeError`` exception:

.. code:: python

    >>> class InvalidProvider(object):
    ...     @staticmethod
    ...     def hello():
    ...         return 'Hello!'

    >>> generic.add_provider(InvalidProvider)
    Traceback (most recent call last):
      ...
    TypeError: The provider must inherit BaseProvider.


All providers must be subclasses of :class:`~mimesis.BaseProvider`
because of ensuring a single instance of object ``Random``.

Everything is pretty easy and self-explanatory here, therefore, we will
only clarify one moment — attribute *name*, class *Meta* is the name
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
    ...             'email': _('person.email', domains=['test.com'], key=str.lower),
    ...             'token': _('token_hex'),
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
          "email": "aisling2032@test.com",
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
    >>> from mimesis import builtins

    >>> custom_providers = (
    ...     builtins.RussiaSpecProvider,
    ...     builtins.NetherlandsSpecProvider,
    ... )
    >>> _ = Field('en', providers=custom_providers)

    >>> _('snils')
    '239-315-742-84'

    >>> _('bsn')
    '657340522'

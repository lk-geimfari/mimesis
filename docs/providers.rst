.. _providers:

Data Providers
==============

Mimesis supports over twenty different data providers,
which can produce data related to food, people, computer hardware,
transportation, addresses, and more.

See :ref:`api-reference` for more info.

.. warning::
    Data providers are **heavy objects**, since each instance of a provider keeps in memory all
    the data from the provider's JSON file, so you **should not** construct too many providers.

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

If you don't specify a locale for a locale-dependent provider,
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
a wide range of data types for the same locale.

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

Custom Providers
----------------

Built-in providers cover most cases. When you need domain-specific methods,
subclass :class:`~mimesis.providers.base.BaseProvider` (or
:class:`~mimesis.providers.base.BaseDataProvider` for JSON datasets — see
:ref:`custom_data_providers`).

Requirements
~~~~~~~~~~~~

1. Inherit from :class:`~mimesis.providers.base.BaseProvider`.
2. Define a nested ``Meta`` class with at least ``name`` (attribute used to
   access the provider, e.g. ``generic.some_provider``).
3. Decide how the provider is attached — see the next subsection.

All custom providers must subclass ``BaseProvider`` so they share Mimesis’s
:class:`~mimesis.random.Random` instance. See :ref:`seeded_data` for seeded
access to ``self.random``.

Choosing how to attach the provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a subclass defines ``Meta.name``, Mimesis may register it in
:class:`~mimesis.providers.base.ProviderRegistry` at **class definition** time.
:class:`~mimesis.Generic` builds its attributes from that registry, and
:class:`~mimesis.schema.Field` uses ``Generic`` internally — so registration
affects both.

Control this with ``Meta.auto_register``:

+--------------------------+-----------------------------------------------------+
| Setting                  | Use when                                            |
+==========================+=====================================================+
| ``auto_register = False``| **Recommended for application code and tests.**     |
|                          | You attach the provider yourself with               |
|                          | ``add_provider()`` on specific ``Generic``          |
|                          | instances. Nothing leaks into unrelated             |
|                          | ``Generic`` / ``Field`` objects.                    |
+--------------------------+-----------------------------------------------------+
| ``auto_register = True`` | **For reusable plugins / shared libraries.**        |
| (default if omitted)     | After the class is imported, every **new**          |
|                          | ``Generic()`` and ``Field()`` exposes the provider  |
|                          | automatically — no ``add_provider()`` call.         |
+--------------------------+-----------------------------------------------------+

.. note::
   Auto-registration only affects instances created **after** the provider
   class is defined. Existing ``Generic`` objects are unchanged; call
   ``add_provider()`` on them if you need the provider there too.

Step by step: explicit attachment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**1.** Define the provider with ``auto_register = False``:

.. code-block:: python

    from mimesis.providers.base import BaseProvider


    class SomeProvider(BaseProvider):
        class Meta:
            name = "some_provider"
            auto_register = False

        @staticmethod
        def hello() -> str:
            return "Hello!"


    class Another(BaseProvider):
        class Meta:
            name = "another"
            auto_register = False

        def __init__(self, seed, message: str) -> None:
            super().__init__(seed=seed)
            self.message = message

        def bye(self) -> str:
            return self.message

**2.** Create a ``Generic`` and attach the classes:

.. code-block:: python

    from mimesis import Generic
    from mimesis.locales import Locale

    generic = Generic(locale=Locale.DEFAULT)
    generic.add_provider(SomeProvider)  # or: generic += SomeProvider
    generic.add_provider(Another, message="Bye!")

Extra keyword arguments (except ``seed``, which is always taken from
``Generic``) are passed to the provider’s ``__init__``.

**3.** Call your methods:

.. code-block:: python

    generic.some_provider.hello()
    # 'Hello!'

    generic.another.bye()
    # 'Bye!'

Attach several providers at once with
:meth:`~mimesis.providers.generic.Generic.add_providers`:

.. code-block:: python

    generic.add_providers(SomeProvider, Another)

If ``Meta.name`` is omitted, ``add_provider()`` falls back to the class name
in lowercase (``SomeProvider`` → ``generic.someprovider``). Prefer setting
``Meta.name`` explicitly.

A class that does not inherit from ``BaseProvider`` raises ``TypeError``:

.. code-block:: python

    class InvalidProvider:
        @staticmethod
        def hello() -> str:
            return "Hello!"

    generic.add_provider(InvalidProvider)
    # TypeError: The provider must be a subclass of mimesis.providers.BaseProvider

Step by step: automatic registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when shipping a provider that should appear everywhere after import.

**1.** Define the provider with ``Meta.name`` (leave ``auto_register`` at its
default ``True``, or set it explicitly):

.. code-block:: python

    from mimesis.providers.base import BaseProvider


    class Greeting(BaseProvider):
        class Meta:
            name = "greeting"
            # auto_register = True  (default)

        def hello(self) -> str:
            return "Hello!"

**2.** Construct ``Generic`` or ``Field`` **after** the class is defined:

.. code-block:: python

    from mimesis import Field, Generic

    generic = Generic()
    generic.greeting.hello()
    # 'Hello!'

    field = Field()
    field("greeting.hello")
    # 'Hello!'

Prefer ``auto_register = False`` in apps and tests so custom providers do not
appear on unrelated ``Generic`` / ``Field`` instances.


.. _custom_data_providers:

Custom Data Providers
---------------------

Use :class:`~mimesis.providers.base.BaseDataProvider` when your fake data lives
in **locale-specific JSON files** (the same pattern as built-in providers like
:class:`~mimesis.Person`).

Step 1: Create a data directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Layout one folder per locale; each locale folder contains the same JSON
filename:

.. code-block:: text

    custom_datadir/
    ├── de/
    │   └── items.json
    ├── en/
    │   └── items.json
    └── ru/
        └── items.json

Every locale you plan to use must have its own directory (locale codes match
:class:`~mimesis.locales.Locale`, e.g. ``en``, ``ru``, ``de``).

Step 2: Add JSON data
~~~~~~~~~~~~~~~~~~~~~

Example ``en/items.json``:

.. code-block:: json

    {
      "items": [
        "value1",
        "value2",
        "value3"
      ]
    }

Step 3: Subclass ``BaseDataProvider``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Meta`` must include:

- ``name`` — attribute name on ``Generic`` / field prefix for ``Field``
- ``datafile`` — JSON filename inside each locale folder
- ``datadir`` — :class:`~pathlib.Path` to the directory that contains the
  locale folders

Read values with ``_extract()`` — pass a list of keys into the loaded JSON:

.. code-block:: python

    from pathlib import Path

    from mimesis import BaseDataProvider
    from mimesis.locales import Locale


    class ItemsProvider(BaseDataProvider):
        class Meta:
            name = "items"
            datafile = "items.json"
            datadir = Path(__file__).parent / "custom_datadir"
            auto_register = False  # recommended unless this is a shared plugin

        def item(self) -> str:
            return self.random.choice(self._extract(["items"]))

Step 4: Use the provider
~~~~~~~~~~~~~~~~~~~~~~~~

Instantiate it directly:

.. code-block:: python

    >>> provider = ItemsProvider(Locale.EN)
    >>> provider.item()
    'value2'

Or attach it to ``Generic``. Pass ``locale=`` explicitly —
:meth:`~mimesis.providers.generic.Generic.add_provider` does **not** copy
``Generic.locale`` into the provider:

.. code-block:: python

    >>> from mimesis import Generic
    >>> from mimesis.locales import Locale

    >>> generic = Generic(locale=Locale.RU)
    >>> generic.add_provider(ItemsProvider, locale=Locale.RU)
    >>> generic.items.item()
    'value1'

If you set ``auto_register = True`` instead, any **new** ``Generic(locale=...)``
constructed after the class is defined will expose ``generic.items`` and load
JSON for that locale automatically (same as built-in locale-dependent
providers).

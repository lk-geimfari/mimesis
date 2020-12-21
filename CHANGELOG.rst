Version 4.1.3
-------------

**Added**:

- Added ``py.typed`` file to the package
- Added ``Python 3.9`` support


Version 4.1.2
-------------

**Fix**:

- Fixed type hint issue for ``schema.Schema`` (`#928 <https://github.com/lk-geimfari/mimesis/issues/928>`_)


Version 4.1.1
-------------

**Fix**:

- Fixed issue with non-unique uuid

Version 4.1.0
-------------

**Added**:

- Added method ``manufacturer()`` for class ``Transport()``
- Added ``sk`` (Slovak) locale support
- Added new parameter ``unique`` for method ``Person().email()``
- Added new parameter ``as_object`` for method ``Cryptographic().uuid()``

**Updated**:

- Updated parameter ``end`` for some methods of provider ``Datetime()`` (Fix #870)
- Updated ``.price()`` to make it supported locales (Fix #875)

**Rename**:

- Renamed ``decorators.romanized`` to ``decorators.romanize``
- Renamed ``Random.schoice`` to ``Random.generate_string``
- Renamed ``BaseDataProvider.pull`` to ``BaseDataProvider._pull``

**Removed**:

- Removed the deprecated ``download_image()`` function from the ``shortcuts`` module, use your own custom downloader instead.
- Removed parameter ``version`` for method ``Cryptographic().uuid()``

Version 4.0.0
-------------

.. warning:: This release (4.0.0) contains some insignificant but breaking changes in API, please be careful.

**Added**:

- Added an alias ``first_name(*args, **kwargs)`` for the method ``Person().name()``
- Added an alias ``sex(*args, **kwargs)`` for the method ``Person().gender()``
- Added method ``randstr()`` for class ``Random()``
- Added method ``complexes()`` for the provider ``Numbers()``
- Added method ``matrix`` for the provider ``Numbers()``
- Added method ``integer_number()`` for the provider ``Numbers()``
- Added method ``float_number()`` for the provider ``Numbers()``
- Added method ``complex_number()`` for the provider ``Numbers()``
- Added method ``decimal_number()`` for the provider ``Numbers()``
- Added method ``ip_v4_object()`` and ``ip_v6_object`` for the provider ``Internet()``. Now you can generate IP objects, not just strings.
- Added new parameter ``port_range`` for method ``ip_v4()``
- Added new parameter ``separator`` for method ``Cryptographic().mnemonic_phrase()``

**Fixed**:

- Fixed issue with invalid email addresses on using custom domains without ``@`` for ``Person().email()``

**Updated**:

- Updated names and surnames for locale ``ru``
- The ``floats()`` function in the ``Numbers`` provider now accepts arguments about the range of the generated float numbers and the rounding used. By default, it generates a list of ``n`` float numbers instead of a list of 10^n elements.
- The argument ``length`` of the function ``integers`` is renamed to ``n``.

**Removed**:

- Removed the ``rating()`` method from the ``Numbers`` provider. It can be replaced with ``float_number()``.
- Removed the ``primes()`` method from the ``Numbers`` provider.
- Removed the ``digit()`` method from the ``Numbers`` provider. Use ``integer_number()`` instead.
- Removed the ``between()`` method from the ``Numbers`` provider. Use ``integer_number()`` instead.
- Removed the ``math_formula()`` method from the ``Science`` provider.
- Removed ``rounding`` argument from ``floats()``. Now it's ``precision``.

Version 3.3.0
-------------

**Fixed**:

- ``country()`` from the ``Address()`` provider now by default returns the country name of the current locale.
- Separated Europe and Asia continents in Italian locale.


**Removed**:

- Removed duplicated names in the countries of ``et`` locale.

Version 3.2.0
-------------

**Added**:

- Added built-in provider DenmarkSpecProvider
- Added meta classes for providers for internal usage (see `#621 <https://github.com/lk-geimfari/mimesis/issues/621>`_.)
- Added support for custom templates in ``Person().username()``
- Added ``ItalianSpecProvider()``

**Fixed**:

- Support of seed for custom providers
- ``currency_iso_code`` from the ``Business()`` provider now by default returns the currency code of the current locale.

**Removed**:

- Removed ``multiple_choice()`` in the ``random`` module because it was unused and it could be replaced with ``random.choices``.
- Removed legacy method ``child_count()`` from provider ``Person()``

Version 3.1.0
-------------

**Fixed**:

- Fixed ``UnsupportedField`` on using field ``choice``, `#619 <https://github.com/lk-geimfari/mimesis/issues/619>`_


Version 3.0.0
-------------

.. warning:: This release (3.0.0) contains some breaking changes in API

.. warning:: In this release (3.0.0) we've reject support of Python 3.5


**Added**:

- Added provider ``Choice()``
- Added method ``formatted_time()`` for ``Datetime()`` provider
- Added method ``formatted_date()`` for ``Datetime()`` provider
- Added method ``formatted_datetime()`` for ``Datetime()`` provider
- Added support of timezones (optional) for ``Datetime().datetime()``
- Added method to bulk create datetime objects: ``Datetime().bulk_create_datetimes()``
- Added ``kpp`` for ``RussiaSpecProvider``
- Added ``PolandSpecProvider`` builtin data provider
- Added context manager to temporarily overriding locale - ``BaseDataProvider.override_locale()``
- Added method ``token_urlsafe()`` for ``Cryptographic`` provider
- Added 6k+ username words


**Updated**:

- Updated documentation
- Updated data for ``pl`` and ``fr``
- Updated SNILS algorithm for ``RussiaSpecProvider``
- Updated method ``Datetime().time()`` to return only ``datetime.time`` object
- Updated method ``Datetime().date()`` to return only ``datetime.date`` object
- Completely annotated all functions
- Locale independent providers inherit ``BaseProvider`` instead of ``BaseDataProvider`` (it's mean that locale independent providers does not support parameter ``locale`` anymore)
- Now you can add to Generic only providers which are subclasses of ``BaseProvider`` to ensure a single instance of ``random.Random()`` for all providers


**Renamed**:

- Renamed provider ``ClothingSizes`` to ``Clothing``, so now it can contain any data related to clothing, not sizes only
- Renamed ``Science().dna()`` to ``Science().dna_sequence()``
- Renamed ``Science().rna()`` to ``Science().rna_sequence()``
- Renamed module ``helpers.py`` to ``random.py``
- Renamed module ``config.py`` to ``locales.py``
- Renamed module ``utils.py`` to ``shortcuts.py``
- Renamed ``Cryptographic().bytes()`` to ``Cryptographic.token_bytes()``
- Renamed ``Cryptographic().token()`` to ``Cryptographic.token_hex()``


**Removed**:

- Removed deprecated argument ``fmt`` for ``Datetime().date()``, use ``Datetime().formatted_date()`` instead
- Removed deprecated argument ``fmt`` for ``Datetime().time()``, use ``Datetime().formatted_time()`` instead
- Removed deprecated argument ``humanize`` for ``Datetime().datetime()``, use ``Datetime().formatted_datetime()`` instead
- Removed deprecated method ``Science.scientific_article()``
- Removed deprecated providers ``Games``
- Removed deprecated method ``Structure().json()``, use ``schema.Schema()`` and ``schema.Field`` instead
- Removed deprecated and useless method: ``Development().backend()``
- Removed deprecated and useless method: ``Development().frontend()``
- Removed deprecated and useless method: ``Development().version_control_system()``
- Removed deprecated and useless method: ``Development().container()``
- Removed deprecated and useless method: ``Development().database()``
- Removed deprecated method ``Internet().category_of_website()``
- Removed duplicated method ``Internet().image_by_keyword()``, use ``Internet().stock_image()`` with ``keywords`` instead
- Removed deprecated JapanSpecProvider (it didn't fit the definition of the data provider)
- Removed deprecated method ``Internet().subreddit()``
- Removed ``Cryptographic().salt()`` use ``Cryptographic().token_hex()`` or  ``Cryptographic().token_bytes()`` instead
- Removed methods ``Person.favorite_movie()``, ``Person.favorite_music_genre()``, ``Person.level_of_english()`` because they did not related to ``Person`` provider

**Fixed**:

- Fixed bug with seed
- Fixed issue with names on downloading images
- Fixed issue with ``None`` in username for ``Person().username()``
- Other minor improvements and fix


Version 2.1.0
-------------

**Added**:

- Added a list of all supported locales as ``mimesis/locales.py``

**Updated**:

- Changed how ``Internet`` provider works with ``stock_image``
- Changed how ``random`` module works, now exposing global ``Random`` instance
- Updated dependencies
- Updated ``choice`` to make it a provider with more output types

**Fixed**:

- Prevents ``ROMANIZED_DICT`` from mutating
- Fixed ``appveyour`` builds
- Fixed ``flake8-builtins`` checks
- Fixed some ``mypy`` issues with strict mode
- Fixed number of elements returned by ``choice`` with ``unique=True``


Version 2.0.1
-------------

**Removed**:

- Removed internal function ``utils.locale_info`` which duplicate ``utils.setup_locale``


Version 2.0.0
-------------

.. note:: This release (2.0.0) contains some breaking changes and this means that you should update names of classes and methods in your code.

**Added**:

- Added items ``IOC`` and ``FIFA`` for enum object ``CountryCode``
- Added support of custom providers for ``schema.Field``
- Added support of parameter ``dms`` for ``coordinates, longitude, latitude``
- Added method ``Text.rgb_color``

- Added support of parameter ``safe`` for method ``Text.hex_color``
- Added an alias ``zip_code`` for ``Address.postal_code``

**Optimizations**:

- Significantly improved performance of ``schema.Field``
- Other minor improvements

**Updated/Renamed**:

- Updated method ``integers``
- Renamed provider ``Personal`` to ``Person``
- Renamed provider ``Structured`` to ``Structure``
- Renamed provider ``ClothingSizes`` to ``Clothing``
- Renamed json file ``personal.json`` to ``person.json`` for all locales
- Renamed ``country_iso_code`` to ``country_code`` in ``Address`` data provider


Version 1.0.5
-------------

**Added**:

- Added method ``RussiaSpecProvider.inn``

**Fixed**:

- Fixed issue with seed for ``providers.Cryptographic.bytes``
- Fixed issue `#375 <https://github.com/lk-geimfari/mimesis/issues/375>`__

**Optimizations**:

- Optimized method ``Text.hex_color``
- Optimized method ``Address.coordinates``
- Optimized method ``Internet.ip_v6``

**Tests**:

- Grouped tests in classes
- Added tests for seeded data providers
- Other minor optimizations and improvements


Version 1.0.4
-------------

**Added**:

- Added function for multiple choice ``helpers.Random.multiple_choice``

**Fixed**:

- Fixed issue with ``seed`` `#325 <https://github.com/lk-geimfari/mimesis/issues/325>`__

**Optimizations**:

- Optimized method ``username()``


Version 1.0.3
-------------

**Mover/Removed**:

- Moved ``custom_code`` to ``helpers.Random``

**Optimizations**:

- Optimized function ``custom_code`` and it works faster by ≈ 50%
- Other minor optimizations in data providers


Version 1.0.2
-------------

**Added**:

- Added method ``ethereum_address`` for ``Payment``
- Added method ``get_current_locale`` for ``BaseProvider``
- Added method ``boolean`` for ``Development`` which returns random boolean value
- Added method ``integers`` for ``Numbers``
- Added new built in specific provider ``UkraineSpecProvider``
- Added support of ``key functions`` for the object ``schema.Field``
- Added object ``schema.Schema`` which helps generate data by schema

**Fixed**:

- Fixed issue ``full_name`` when method return female surname for male name and vice versa
- Fixed bug with improper handling of attributes that begin with an underscore for class ``schema.Field``

**Updated**:

- Updated method ``version`` for supporting pre-releases and calendar versioning
- Renamed methods ``international``, ``european`` and ``custom`` to ``international_size``, ``european_size`` and ``custom_size``


Version 1.0.1
-------------

**Updated**:

- Fixed #304


Version 1.0.0
-------------

This is a first major version of ``mimesis`` and here are **breaking
changes** (including changes related to support for only the latest
versions of ``Python``, i.e ``Python 3.5`` and ``Python 3.6``), so there
is no backwards compatibility with early versions of this library.

**Added**:

- Added ``Field`` for generating data by schema
- Added new module ``typing.py`` for custom types
- Added new module ``enums.py`` and support of enums in arguments of methods
- Added ``category_of_website`` and ``port`` to ``Internet`` data provider
- Added ``mnemonic_phrase`` for ``Cryptography`` data provider
- Added ``price_in_btc`` and ``currency_symbol`` to ``Business`` data provider
- Added ``dna``, ``rna`` and ``atomic_number`` to ``Science`` data provider
- Added ``vehicle_registration_code`` to ``Transport`` data provider
- Added ``generate_string`` method for ``Random``
- Added alias ``last_name`` for ``surname`` in ``Personal`` data provider
- Added alias ``province``, ``region``, ``federal_subject`` for ``state`` in ``Address`` data provider
- Added annotations for all methods and functions for supporting type hints
- Added new data provider ``Payment``
- Added new methods to ``Payment``: ``credit_card_network``, ``credit_card_owner``

**Fixed**:

- Fixed issue with ``primes`` in ``Numbers`` data provider
- Fixed issue with repeated output on using ``Code().custom code``
- Other minor fix and improvements

**Mover/Removed**:

- Moved ``credit_card``, ``credit_card_expiration_date``, ``cid``, ``cvv``, ``paypal`` and ``bitcoin`` to ``Payment`` from ``Personal``

- Moved ``custom_code`` to ``utils.py`` from ``providers.code.Code``
- Removed some useless methods
- Removed module ``constants``, in view of adding more convenient and useful module ``enums``
- Removed non informative custom exception ``WrongArgument`` and replaced one with ``KeyError`` and ``NonEnumerableError``
- Parameter ``category`` of method ``hashtags`` is deprecated and was removed
- Removed all methods from ``UnitSystem`` and replaced ones with ``unit()``.

**Updated/Renamed**:

- Updated data for ``de-at``, ``en``, ``fr``, ``pl``, ``pt-br``, ``pt``, ``ru``, ``uk``
- Other minor updates in other languages
- Renamed ``currency_iso`` to ``currency_iso_code`` ``in Business`` data provider

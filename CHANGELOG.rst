Version 3.0.0
-------------

.. note:: This release (3.0.0) contains some breaking changes in API.

.. note:: In this release (3.0.0) we've reject support of Python 3.5.

.. note:: Work still in progress and this version will be released only in December 2018.

**Added**:

- Added method ``formatted_time()``
- Added method ``formatted_date()``
- Added method ``formatted_datetime()``
- Added support of timezones for ``Datetime().datetime()``
- Added method to bulk create datetime objects: ``Datetime().bulk_create_datetimes()``
- Added generate KPP for ``RussiaSpecProvider``
- Added ``PolandSpecProvider`` builtin data provider for Poland
- Added context manager for overriding locales - ``locales.override()``
- Added 6k+ username words
- Different superclasses for different types of data provider


**Updated**:

- Updated data for ``pl`` and ``fr``
- Updated snils algorithm for ``RussiaSpecProvider``
- Updated method ``Datetime().time()`` to return only ``datetime.time`` object
- Updated method ``Datetime().date()`` to return only ``datetime.date`` object
- Completely annotated all functions
- Locale independent providers inherit ``BaseProvider`` instead of ``BaseDataProvider``
- Now you can add to Generic only providers which are subclasses of ``BaseProvider`` to ensure a single instance of ``random.Random()`` for all providers


**Renamed**:

- Renamed ``Science().dna()`` to ``Science().dna_sequence()``
- Renamed ``Science().rna()`` to ``Science().rna_sequence()``
- Renamed module ``helpers.py`` to ``random.py``
- Renamed module ``config.py`` to ``locales.py``
- Renamed module ``utils.py`` to ``shortcuts.py``


**Removed**:

- Locale independent providers does not support parameter ``locale`` anymore
- Removed deprecated argument ``fmt`` for ``Datetime().date()``, use ``Datetime().formatted_date()`` instead
- Removed deprecated argument ``fmt`` for ``Datetime().time()``, use ``Datetime().formatted_time()`` instead
- Removed deprecated argument ``humanize`` for ``Datetime().datetime()``, use ``Datetime().formatted_datetime()`` instead
- Removed deprecated method ``Science.scientific_article()``
- Removed deprecated method ``Structure().json()``, use ``schema.Schema()`` instead
- Removed deprecated and useless method: ``Development().backend()``
- Removed deprecated and useless method: ``Development().frontend()``
- Removed deprecated and useless method: ``Development().version_control_system()``
- Removed deprecated and useless method: ``Development().container()``
- Removed deprecated and useless method: ``Development().database()``
- Removed duplicated method ``Internet().image_by_keyword()``, use ``Internet().stock_image()`` with ``keywords`` instead
- Removed deprecated JapanSpecProvider


**Fixed**:

- Fixed bug with seed
- Fixed issue with names on downloading images
- Fixed issue with ``None`` in username for ``Person().username()``


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
- Renamed provider ``ClothingSizes`` to ``ClothingSize``
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
- Added ``schoice`` method for ``Random``
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

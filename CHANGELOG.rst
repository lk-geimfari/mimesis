Version 12.0.0
--------------

- Improve validation for custom field names.
- Added method ``calver`` for ``Development``.
- Added method ``stage`` for ``Development``.
- Added decorator ``@register`` for ``Field`` and ``Fieldset`` to register custom fields.
- Removed parameter ``providers`` for ``Field`` and ``Fieldset``. Use custom fields instead.
- Removed parameters ``pre_release`` and ``calver`` for ``Development.version``. Use methods ``stage`` and ``calver`` instead.


Version 11.0.0
--------------

**Added**:

- Added support for registering custom fields for ``Schema``. This allows you to use your own fields in schemas. See docs for more information.


Version 10.2.0
--------------

**Added**:

- Added a new method ``system_quality_attribute()`` (and its alias ``ility()``) for ``Development``.


Version 10.1.0
--------------

**Added**:

- Added a new enum ``TimestampFormat`` for the ``timestamp()`` method.

**Updated**:

- The method ``timestamp()`` for ``Datetime()`` now expects one of the following timestamp formats: `TimestampFormat.POSIX`, `TimestampFormat.RFC_3339`, or `TimestampFormat.ISO_8601`.
- The ``datetime()`` method now has default parameters start and end set to the current year.

**Removed**:

- The method `timestamp()` no longer accepts the ``posix`` parameter.


Version 10.0.0
--------------

**Updated**:

- ``romanize()`` is a key function now. See docs for more information.


**Removed**:

- Removed method ``swear_word()`` of ``Text()``. This method is inappropriate and lacks practical utility.


Version 9.0.0
-------------
.. note::

    This release contains some breaking changes in Schema's API.

**Updated**:

- Key functions now may accept additional ``random`` as a parameter. See docs for more information.

**Removed**:

- The ``loop`` method for the ``Schema``, which was considered deprecated and unsafe, has been removed.
- The ``iterations`` parameter for all methods of ``Schema`` has been removed. Instead, you now have to specify the number of iterations on instantiation of ``Schema`` passing the ``iterations`` parameter.
- The ``iterator`` method for ``Schema`` has been removed. Instead, you can now use an instance of ``Schema`` directly as an iterator.
- The multiplication is no longer supported for ``Schema``. Instead, you can use the ``iterations`` parameter on instantiation of ``Schema``.

**Added**:

- Add ``weighted_choice()`` method for ``Random()``. See docs for more information.
- Add module ``keys`` for generating key functions.

Version 8.0.0
-------------

**Added**

- ``Fieldset()`` to generate a set of fields at once. See docs for more information.
- ``bank()`` method for ``Finance()``.
- ``default_country`` for ``Address()``, which always returns the country associated with the current locale (i.e ``United States`` for ``en``, ``Россия`` for ``ru``).

**Removed**:

- Removed parameter ``allow_random`` for ``country()``. Now method returns random country by default.

Version 7.1.0
-------------

**Added**

- ``pytest-randomly`` integration, not by default it will set the global seed for every provider and all fields. This can still be reseeded as usual.
- ``http_request_headers()`` and ``http_response_headers()`` methods for ``Internet`` provider. These methods return a dictionary of common headers.
- ``reseed()`` method for ``Field``.

**Removed**:

- ``stock_image()`` method which required an active HTTP connection. Use ``stock_image_url`` instead.

Version 7.0.0
-------------

**Updated**:

- Actualized data
- Removed outdated data

**Removed**:

- Removed parameter ``model_mask`` for ``airplane()``
- Removed method ``truck()`` of ``Transport()``, use ``menufacturer()`` instead.
- Removed method ``cpu_model()`` of ``Hardware()``.

Version 6.1.1
-------------

- Improve random sampling performance.


Version 6.1.0
-------------

- Make field support different delimiters for ``provider.method``.


Version 6.0.0
-------------

**Fixed**:

- Fixed memory leak on using ``Field``.

**Optimizations**:

- Improved performance of ``_load_data()``.


Version 5.6.1
-------------

**Fixed**:

- Fixed ``ValidationFailure`` for ``Internet().uri()``.

**Removed**:

- Removed support of ``port`` parameter in ``Internet().uri()``.

Version 5.6.0

**Added**:

- Multiplication support for schemas. Now you can use `*` on the schema to specify the number of iterations. See docs for more information.
- Method ``dsn()`` for ``Development()``
- Method ``public_dns()`` for ``Internet()``

Version 5.5.0
-------------

**Fixed**:

- Fixed infinite loop on using ``Datetime.bulk_create_datetimes()``.
- Fixed some typing issues

Version 5.4.0
-------------

**Fixed**:

- Fixed TypeError: 'Datetime' object is not callable error on using ``Field`` (See `#1139 <https://github.com/lk-geimfari/mimesis/issues/1139>`_).

**Added**:

- Added items ``Algorithm.BLAKE2B`` and ``Algorithm.BLAKE2S``.


**Removed**:

- Removed deprecated method ``image_placeholder()`` from ``Internet()``



Version 5.3.0
-------------

**Added**:

- Added method ``to_pickle()``, ``to_json()`` and ``to_csv()`` for ``schema.Schema``.


**Optimizations**:

- Significantly improved performance of ``shortcuts.romanize()``
- Use ``random.choices()`` to generate random strings instead of ``random.choice()`` for selecting individual characters. This can lead to a significant speed up, but will also change the reproducibility of values when upgrading to this version as the two methods use different algorithms.
- Optimized ``Address.latitude()``, ``Address.longitude()``, and ``Address.coordinates()`` when passing ``dms=True``.
- Optimized ``Development.version()``.

**Fixed**:

- Fix duplication of parameter name on using ``Internet.query_parameter()`` (See `#1177 <https://github.com/lk-geimfari/mimesis/issues/1177>`_).
- Fix reseeding of the random generator of ``Generic``. This was a regression in v5.1.0. (See `#1150 <https://github.com/lk-geimfari/mimesis/issues/1150>`_).
- ``Development.version()`` now supports use of both the ``calver`` and ``pre_release`` flags together.
- Providers now have an isolated ``random`` instance when using a seed of ``None``.


Version 5.2.1
-------------

**Removed**:

- Removed all params of ``mnemonic_phrase()``


Version 5.1.1
-------------

**Added**:

- Added parameter ``region`` for ``Datetime().timezone()`` and enum object ``enums.TimezoneRegion``

Version 5.1.0
-------------

**Fixed**:

- Fix mechanism of reseeding of the internal providers of ``Generic`` (See `#1115 <https://github.com/lk-geimfari/mimesis/issues/1115>`_).

**Removed**:

- Removed inappropriate words from ``mimesis.data.int.USERNAMES``.

Version 5.0.0
-------------

**Warning**: This release contains some breaking changes in API.

**Python compatibility**:

Mimesis 5.0 supports Python 3.8, 3.9, and 3.10.

The Mimesis 4.1.3 is the last to support Python 3.6 and 3.7.

**Reworked**:

- A method ``Person().username()``, now it accepts a parameters ``mask`` and ``drange``.

**Renamed**:

- Renamed ``enums.UnitName`` to ``enums.MeasureUnit``
- Renamed ``enums.PrefixSign`` to ``enums.MetricPrefixSign``
- Renamed ``Business()`` to ``Finance()``
- Renamed ``BaseDataProvider.pull`` to ``BaseDataProvider._load_datafile``
- Renamed ``mimesis.providers.numbers.Numbers`` to ``mimesis.providers.numeric.Numeric``
- Renamed ``fmt`` argument of ``Address().country_code()`` to ``code``

**Fixed**:

- Fix inheritance issues for ``Generic``, now it inherits ``BaseProvider`` instead of ``BaseDataProvider``
- Fix locale-independent provider to make them accepts keyword-only arguments
- Fix DenmarkSpecProvider CPR to generate valid CPR numbers.
- Fix ``.cvv()`` to make it return string
- Fix ``.cid()`` to make it return string
- Fix ``.price()`` of ``Finance`` to make it return float.

**Added**:

- Added method ``hostname()`` for ``Internet`` data provider
- Added support of ``**kwargs`` for a method ``add_provider`` of ``Generic()`` provider
- Added enum ``Locale`` to ``mimesis.enums`` and ``mimesis.locales``
- Added ``measure_unit`` and ``metric_prefix`` methods for the ``Science`` provider.
- Added ``.iterator()`` for ``schema.Schema``
- Added methods ``.slug()`` and ``ip_v4_with_port()`` for ``Internet()``
- Added ``increment()`` method for ``Numbers()``
- Added methods ``.stock_ticker()``, ``.stock_name()`` and ``.stock_exchange()`` for ``Finance()``
- Added ``BinaryFile`` data provider which provides binary data files, such as ``.mp3``, ``.mp4``, ``.png``, etc.

**Removed**:

- Removed module ``decorators``. Use ``shortcuts.romanize`` to romanize Cyrillic strings.
- Removed ``as_object`` parameter for ``.uuid()``. Now it returns string by default, if you need uuid4 object then use ``.uuid_object()``
- Removed invalid names and surnames from ``person.json`` for ``ru`` locale
- Removed data provider ``UnitSystem()``, use ``Science()`` instead
- Removed data provider ``Structure()``, use ``schema.Schema`` instead
- Removed builtin provider ``GermanySpecProvider``
- Removed data provider ``Clothing``, use ``Numbers`` instead
- Removed method ``copyright()`` of ``Finance()``
- Removed method ``network_protocol()`` of ``Internet()``
- Removed params ``with_port`` and ``port_range`` for ``ip_v4()`` of ``Internet()``. Use ``ip_v4_with_port()`` instead.
- Removed methods ``sexual_orientation``, ``social_media_profile`` and ``avatar`` of the ``Person()`` provider.
- Removed a bunch of useless custom exceptions and replaced them with ``FieldError``.
- Removed completely useless ``chemical_element`` and ``atomic_number`` methods of ``Science`` data provider and made it locale-independent.


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

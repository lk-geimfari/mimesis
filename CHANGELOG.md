## Version 1.0.2

**Added**:

- Added method `ethereum_address` for `Payment`
- Added method `get_current_locale` for `BaseProvider`
- Added method `boolean` for `Development` which returns random boolean value
- Added method `integers` for `Numbers`
- Added new built in specific provider `UkraineSpecProvider`
- Added support of `key functions` for the object `schema.Field`
- Added object `schema.Schema` which helps generate data by schema

**Fixed**:

- Fixed issue `full_name` when method return female surname for male name and vice versa
- Fixed bug with improper handling of attributes that begin with an underscore for class `schema.Field`

**Updated**:

- Updated method `version` for supporting pre-releases and calendar versioning
- Renamed methods `international`, `european` and `custom` to `international_size`, `european_size` and `custom_size`

---

## Version 1.0.1

**Updated**:

- Fixed #304

---

## Version 1.0.0

This is a first major version of `mimesis` and here are **breaking changes** (including changes related to support for only the latest versions of `Python`, i.e `Python 3.5` and `Python 3.6`), so there is no backwards compatibility with early versions of this library.

**Added**:

- Added `Field` for generating data by schema
- Added new module `typing.py` for custom types
- Added new module `enums.py` and support of enums in arguments of methods
- Added `category_of_website` and `port` to `Internet` data provider
- Added `mnemonic_code` for `Cryptography` data provider
- Added `price_in_btc` and `currency_symbol` to `Business` data provider
- Added `dna`, `rna` and `atomic_number` to `Science` data provider
- Added `vehicle_registration_code` to `Transport` data provider
- Added `schoice` method for `Random`
- Added alias `last_name` for `surname` in `Personal` data provider
- Added alias `province`, `region`, `federal_subject` for `state` in `Address` data provider
- Added annotations for all methods and functions for supporting type hints
- Added new data provider `Payment`
- Added new methods to `Payment`: `credit_card_network`, `bitcoin_addres` (previously `bitcoin`), `credit_card_owner`

**Fixed**:
- Fixed issue with `primes` in `Numbers` data provider
- Fixed issue with repeated output on using `Code().custom code`
- Other minor fix and improvements


**Mover/Removed**:
- Moved `credit_card`, `credit_card_expiration_date`, `cid`, `cvv`, `paypal` and `bitcoin` to `Payment` from `Personal`
- Moved `custom_code` to `utils.py` from `providers.code.Code`
- Removed some useless methods
- Removed module `constants`, in view of adding more convenient and useful module `enums`
- Removed non informative custom exception `WrongArgument` and replaced one with `KeyError` and `NonEnumerableError`
- Parameter `category` of method `hashtags` is deprecated and was removed
- Removed all methods from `UnitSystem` and replaced ones with `unit()`.

**Updated/Renamed**:
- Updated data for `de-at`, `en`, `fr`, `pl`, `pt-br`, `pt`, `ru`, `uk`
- Other minor updates in other languages
- Renamed `country_iso` to `country_iso_code` in `Address` data provider
- Renamed `currency_iso` to `currency_iso_code` `in Business` data provider

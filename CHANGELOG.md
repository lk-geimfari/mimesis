
## Version 1.0.0

**Added**:

- Added `Field` for generating data by schema
- Added `category_of_website` and `port` to `Internet` data provider
- Added new module `enums.py` and support of enums in arguments of methods
- Added `dna`, `rna` and `atomic_number` to `Science` data provider
- Added `schoice` method for `Random`
- Added alias `last_name` for `surname` in `Personal` data provider
- Added alias `province`, `region`, `federal_subject` for `state` in `Address` data provider
- Added annotations for all methods and functions for supporting type hints
- Added module `typing.py` for custom types
- Added new data provider `Payment`
- Added new methods to `Payment`: `credit_card_network`, `bitcoin_addres`, `credit_card_owner`

**Fixed**:
- Fixed issue with `primes` in `Nimbers` data provider
- Fixed issue with repeated output on using `Code().custom code`
- Other minor fix and improvements


**Mover/Removed**:
- Moved `credit_card`, `credot_card_expiration_date`, `cid`, `cvv`, `paypal` and `bitcoin` to `Payment` from `Personal`
- Moved `custom_code` to `utils.py` from `providers.code.Code`
- Removed useless methods

**Updated/Renamed**:
- Updated data for `de-at`, `en`, `fr`, `pl`, `pt-br`, `pt`, `ru`, `uk`
- Other minor updates in other languages

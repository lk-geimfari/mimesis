<p align="center">
  <a href="https://github.com/lk-geimfari/mimesis">
    <img src="https://raw.githubusercontent.com/lk-geimfari/mimesis/master/.github/images/logo.png" width="300" alt="Mimesis">
  </a>
</p>

<p align="center">
    <em>Mimesis: The Fake Data Generator</em>
</p>

<p align="center">
<a href="https://github.com/lk-geimfari/mimesis/actions/workflows/test.yml?query=branch%3Amaster" target="_blank">
    <img src="https://github.com/lk-geimfari/mimesis/actions/workflows/test.yml/badge.svg?branch=master" alt="Test">
</a>
<a href="https://mimesis.name/en/latest/" target="_blank">
    <img src="https://readthedocs.org/projects/mimesis/badge/?version=latest" alt="Coverage">
</a>
<a href="https://pypi.org/project/mimesis/" target="_blank">
    <img src="https://img.shields.io/pypi/v/mimesis?color=bright-green" alt="Package version">
</a>
<a href="https://pypi.org/project/mimesis/" target="_blank">
    <img src="https://img.shields.io/pypi/dm/mimesis" alt="Package version">
</a>
<a href="https://pypi.org/project/mimesis/" target="_blank">
    <img src="https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14%20%7C%20pypy-brightgreen" alt="Supported Python versions">
</a>
</p>

---

**Documentation**: <a href="https://mimesis.name/" target="_blank">https://mimesis.name/</a>

---

Mimesis ([/mɪˈmiːsɪs](https://mimesis.name/master/about.html#what-does-name-mean)) is a Python library for generating fake but realistic data in multiple languages and locales. It can generate names, addresses, dates, phone numbers, emails, financial data, and many other types of values.

It is commonly used to populate test databases, mock API responses, generate JSON or XML fixtures, create sample datasets, and anonymize production data. Mimesis provides a simple, consistent API that makes it easy to generate realistic data for development and testing.

The key features are:

- **Multilingual**: Supports 47 different locales.
- **Extensibility**: Supports custom data providers and custom field handlers.
- **Ease of use**: Features a simple design and clear documentation for straightforward data generation.
- **Performance**: Widely recognized as the fastest data generator among Python solutions.
- **Data variety**: Includes various data providers designed for different use cases.
- **Schema-based generators**: Offers schema-based data generators to effortlessly produce data of any complexity.
- **Relational data**: Supports generating related datasets with foreign keys and nested schemas.
- **Intuitive**: Great editor support. Fully typed, so you get autocompletion almost everywhere.

## Installation

To install Mimesis, use pip:

```
~ pip install mimesis
```

## Documentation

You can find the complete documentation on the [Read the Docs](https://mimesis.name/).

It is divided into several sections:

-  [About Mimesis](https://mimesis.name/latest/about.html)
-  [Quickstart](https://mimesis.name/latest/quickstart.html)
-  [Locales](https://mimesis.name/latest/locales.html)
-  [Data Providers](https://mimesis.name/latest/providers.html)
-  [Structured Data Generation](https://mimesis.name/latest/schema.html)
-  [Relational Data Generation](https://mimesis.name/latest/relational.html)
-  [Random and Seed](https://mimesis.name/latest/random_and_seed.html)
-  [Integration with factory_boy](https://mimesis.name/latest/factory_plugin.html)
-  [API Reference](https://mimesis.name/latest/api.html)
-  [Changelog](https://mimesis.name/latest/index.html#changelog)

You can improve it by sending pull requests to this repository.

## Usage

Import a data provider that corresponds to the data type you need.

For example, the [Person](https://mimesis.name/latest/api.html#person) provider gives access to personal information,
including name, surname, email, and other related fields:

```python
from mimesis import Person
from mimesis.locales import Locale

person = Person(Locale.EN)

person.full_name()
# Output: 'Brande Sears'

person.email(domains=['example.com'])
# Output: 'roccelline1878@example.com'

person.email(domains=['mimesis.name'], unique=True)
# Output: 'f272a05d39ec46fdac5be4ac7be45f3f@mimesis.name'

person.telephone(mask='1-4##-8##-5##3')
# Output: '1-436-896-5213'
```

## License

Mimesis is licensed under the MIT License. See [LICENSE](https://github.com/lk-geimfari/mimesis/blob/master/LICENSE) for more information.

<p align="center">
  <a href="https://github.com/lk-geimfari/mimesis"><img src="https://raw.githubusercontent.com/lk-geimfari/mimesis/master/.github/images/logo.png" alt="Mimesis"></a>
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
    <img src="https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%20pypy-brightgreen" alt="Supported Python versions">
</a>
</p>

---

**Documentation**: <a href="https://mimesis.name/" target="_blank">https://mimesis.name/</a>

---

Mimesis ([/mɪˈmiːsɪs](https://mimesis.name/en/master/about.html#what-does-name-mean)) is a robust data generator for
Python that can produce a wide range of fake data in various languages.

The key features are:

- **Multilingual**: Supports 35 different locales.
- **Extensibility**: Supports custom data providers and custom field handlers.
- **Ease of use**: Features a simple design and clear documentation for straightforward data generation.
- **Performance**: Widely recognized as the fastest data generator among Python solutions.
- **Data variety**: Includes various data providers designed for different use cases.
- **Schema-based generators**: Offers schema-based data generators to effortlessly produce data of any complexity.
- **Intuitive**: Great editor support. Fully typed, thus autocompletion almost everywhere.

## Installation

To install mimesis, use pip:

```
~ pip install mimesis
```

To work with Mimesis on Python versions 3.8 and 3.9, the final compatible version is Mimesis 11.1.0.
Install this specific version to ensure compatibility.

## Documentation

You can find the complete documentation on the [Read the Docs](https://mimesis.name/).

It is divided into several sections:

-  [About Mimesis](https://mimesis.name/en/latest/about.html)
-  [Quickstart](https://mimesis.name/en/master/quickstart.html)
-  [Locales](https://mimesis.name/en/master/locales.html)
-  [Data Providers](https://mimesis.name/en/master/getting_started.html#data-providers)
-  [Structured Data Generation](https://mimesis.name/en/master/schema.html)
-  [Random and Seed](https://mimesis.name/en/master/random_and_seed.html)
-  [Integration with Pytest](https://mimesis.name/en/master/pytest_plugin.html)
-  [Integration with factory_boy](https://mimesis.name/en/master/factory_plugin.html)
-  [API Reference](https://mimesis.name/en/master/api.html)
-  [Changelog](https://mimesis.name/en/master/index.html#changelog)

You can improve it by sending pull requests to this repository.

## Usage

The library is exceptionally user-friendly, and it only requires you to import a **Data Provider** object that
corresponds to the desired data type.

For instance, the [Person](https://mimesis.name/en/latest/api.html#person) provider can be imported to access personal information,
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

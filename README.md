## Mimesis

[![Build Status](https://travis-ci.org/lk-geimfari/mimesis.svg?branch=master)](https://travis-ci.org/lk-geimfari/mimesis)
[![Build status on Windows](https://ci.appveyor.com/api/projects/status/chj8huslvn6vde18?svg=true)](https://ci.appveyor.com/project/lk-geimfari/mimesis)
[![codecov](https://codecov.io/gh/lk-geimfari/mimesis/branch/master/graph/badge.svg)](https://codecov.io/gh/lk-geimfari/mimesis)
[![PyPI version](https://badge.fury.io/py/mimesis.svg)](https://badge.fury.io/py/mimesis)
[![Python](https://img.shields.io/badge/python-3.5%2C%203.6-brightgreen.svg)](https://badge.fury.io/py/mimesis)


[![](/media/large-logo.png)](https://github.com/lk-geimfari/mimesis)

**Mimesis** is a fast and easy to use library for Python programming language, which helps generate mock (dummy) data for a variety of purposes (see "[Data providers](#data-providers)") in a variety of languages (see "[Locales](#locales)"). This data can be particularly useful during software development and testing. For example, it could be used to populate a testing database for a web application with user information such as email addresses, usernames, first names, last names, etc. 

Mimesis offers a number of advantages over other similar libraries, such as Faker:

* Performance. Mimesis is significantly [faster](http://i.imgur.com/pCo6yPA.png) than other similar libraries.
* Completeness. Mimesis strives to provide many detailed providers that offer a variety of data generators.
* Simplicity. Mimesis does not require any modules other than the Python standard library.

See [here](https://gist.github.com/lk-geimfari/461ce92fd32379d7b73c9e12164a9154) for an example of how we compare
performance with other libraries.

## Documentation
Mimesis is very simple to use, and the below examples should help you get started. Complete documentation for Mimesis is available on [Read the Docs](http://mimesis.readthedocs.io/).

## Installation
To install mimesis, simply:

```zsh
➜  ~ pip install mimesis
```

Also you can install it manually:
```zsh
(env) ➜ python3 setup.py install
# or
(env) ➜ make install
```

## Getting started

As we said above, this library is really easy to use. A simple usage example is given below:

```python
>>> from mimesis import Personal
>>> person = Personal('en')

>>> person.full_name(gender='female')
'Antonetta Garrison'

>>> person.occupation()
'Backend Developer'

>>> templates = ['U_d', 'U-d', 'l_d', 'l-d']
>>> for template in templates:
...     person.username(template=template)

'Adders_1893'
'Abdel-1888'
'constructor_1884'
'chegre-2051'
```

## Locales

You can specify a locale when creating providers and they will return data that is appropriate for the language or country associated with that locale:

```python
>>> from mimesis import Personal

>>> de = Personal('de')
>>> fr = Personal('fr')
>>> pl = Personal('pl')

>>> de.full_name()
'Sabrina Gutermuth'

>>> fr.full_name()
'César Bélair

>>> pl.full_name()
'Światosław Tomankiewicz'
```

Mimesis currently includes support for 33 different locales. See details for more information.

<details>
<!-- toc -->

| №  | Flag  | Code       | Name                 | Native name |
|--- |---   |---       |---                 |---         |
| 1  | 🇨🇿   |  `cs`      | Czech                | Česky       |
| 2  | 🇩🇰   |  `da`      | Danish               | Dansk       |
| 3  | 🇩🇪   |  `de`      | German               | Deutsch     |
| 4  | 🇦🇹   |  `de-at`   | Austrian German      | Deutsch     |
| 5  | 🇨🇭   |  `de-ch`   | Swiss German         | Deutsch     |
| 6  | 🇬🇷   |  `el`      | Greek                | Ελληνικά    |
| 7  | 🇺🇸   |  `en`      | English              | English     |
| 8  | 🇦🇺   |  `en-au`   | Australian English   | English     |
| 9  | 🇨🇦   |  `en-ca`   | Canadian English     | English     |
| 10 | 🇬🇧   |  `en-gb`   | British English      | English     |
| 11 | 🇪🇸   |  `es`      | Spanish              | Español     |
| 12 | 🇲🇽   |  `es-mx`   | Mexican Spanish      | Español     |
| 13 | 🇪🇪   |  `et`      | Estonian             | Eesti       |
| 14 | 🇮🇷   |  `fa`      | Farsi                | فارسی       |
| 15 | 🇫🇮   |  `fi`      | Finnish              | Suomi       |
| 16 | 🇫🇷   |  `fr`      | French               | Français    |
| 17 | 🇭🇺   |  `hu`      | Hungarian            | Magyar      |
| 18 | 🇮🇸   |  `is`      | Icelandic            | Íslenska    |
| 19 | 🇮🇹   |  `it`      | Italian              | Italiano    |
| 20 | 🇯🇵   |  `ja`      | Japanese             | 日本語       |
| 21 | 🇰🇿   |  `kk`      | Kazakh               | Қазақша     |
| 22 | 🇰🇷   |  `ko`      | Korean               | 한국어       |
| 23 | 🇳🇱   |  `nl`      | Dutch                | Nederlands  |
| 24 | 🇧🇪   |  `nl-be`   | Belgium Dutch        | Nederlands  |
| 25 | 🇳🇴   |  `no`      | Norwegian            | Norsk       |
| 26 | 🇵🇱   |  `pl`      | Polish               | Polski      |
| 27 | 🇵🇹   |  `pt`      | Portuguese           | Português   |
| 28 | 🇧🇷   |  `pt-br`   | Brazilian Portuguese | Português Brasileiro |
| 29 | 🇷🇺   |  `ru`      | Russian              | Русский     |
| 30 | 🇸🇪   |  `sv`      | Swedish              | Svenska     |
| 31 | 🇹🇷   |  `tr`      | Turkish              | Türkçe      |
| 32 | 🇺🇦   |  `uk`      | Ukrainian            | Український |
| 33 | 🇨🇳   |  `zh`      | Chinese              | 汉语         |

<!-- tocstop -->
</details>

<br>

## Data providers

Mimesis support over twenty different data providers available, which can produce data related to food, people, computer hardware, transportation, addresses, and more. See details for more information.

| №   | Provider        | Description                                                  |
|---  | ------------- |:-------------                                                  |
| 1   | Address         | Address data (street name, street suffix etc.)               |
| 2   | Business        | Business data (company, company_type, copyright etc.)        |
| 3   | Code            | Codes (ISBN, EAN, IMEI etc.)                                 |
| 4   | ClothingSizes   | Clothing sizes (international sizes, european etc.)          |
| 5   | Cryptographic   | Cryptographic data                                           |
| 6   | Datetime        | Datetime (day_of_week, month, year etc.)                     |
| 7   | Development     | Data for developers (version, programming language etc.)     |
| 8   | File            | File data (extension etc.)                                   |
| 9   | Food            | Information on food (vegetables, fruits, measurements etc.)  |
| 10  | Games           | Games data (game, score, pegi_rating etc.)                   |
| 11  | Personal        | Personal data (name, surname, age, email etc.)               |
| 12  | Text            | Text data (sentence, title etc.)                             |
| 13  | Transport       | Dummy data about transport (truck model, car etc.)           |
| 14  | Science         | Scientific data (scientist, math_formula etc.)               |
| 15  | Structured      | Structured data (html, css etc.)                             |
| 16  | Internet        | Internet data (facebook, twitter etc.)                       |
| 17  | Hardware        | The data about the hardware (resolution, cpu, graphics etc.) |
| 18  | Numbers         | Numerical data (floats, primes, digit etc.)                  |
| 19  | Path            | Provides methods and property for generate paths             |
| 20  | UnitSytem       | Provides names of unit systems in international format       |
| 21  | Generic         | All at once                                                  |

When you only need to generate data for a single locale, use the `Generic()` provider, and you can access all providers of Mimesis from one object.

```python
>>> from mimesis import Generic
>>> g = Generic('es')

>>> g.datetime.month()
'Agosto'

>>> g.food.fruit()
'Limón'

>>> g.internet.top_level_domain('GeoTLD')
'.moscow'
```

## Custom Providers
You also can add custom provider to `Generic()`, using `add_provider()` method:

```python
>>> from mimesis import Generic
>>> from mimesis.providers import BaseProvider
>>> generic = Generic('en')

>>> class SomeProvider(BaseProvider):
...     class Meta:
...         name = "some_provider"
...
...     def hello(self):
...         return "Hello!"

>>> class Another(BaseProvider):
...     def bye(self):
...         return "Bye!"

>>> generic.add_provider(SomeProvider)
>>> generic.add_provider(Another)

>>> generic.some_provider.hello()
'Hello!'

>>> generic.another.bye()
'Bye!'
```

or multiple custom providers using method `add_providers()`:

```python
>>> generic.add_providers(SomeProvider, Another)
```

Too lazy to search for data? No problem, we found them for you and collected them here: [mimesis-extra-data](https://github.com/mimesis-lab/mimesis-extra-data).


## Builtins specific data providers

Some countries have data types specific to that country. For example social security numbers (SSN) in the United States of America (`en`), and cadastro de pessoas físicas (CPF) in Brazil (`pt-br`).
If you would like to use these country-specific providers, then you must import them explicitly:

```python
>>> from mimesis import Generic
>>> from mimesis.builtins import BrazilSpecProvider

>>> generic = Generic('pt-br')
>>> generic.add_provider(BrazilSpecProvider)
>>> generic.brazil_provider.cpf()
'696.441.186-00'
```

You can use specific-provider without adding it to `Generic()`:

```python
>>> BrazilSpecProvider().cpf()
'712.455.163-37'
```

## Integration with Web Application Frameworks

You can use Mimesis during development and testing of applications built on a variety of frameworks. Here is an
example of integration with a Flask application:

```python
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    blood_type = db.Column(db.String(64))

    def __init__(self, **kwargs):
        super(Patient, self).__init__(**kwargs)

    @staticmethod
    def populate(count=500, locale=None):
        import mimesis

        person =  mimesis.Personal(locale=locale)

        for _ in range(count):
            patient = Patient(
                full_name=person.full_name('female'),
                blood_type=person.blood_type(),
            )

            db.session.add(patient)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
```

Just run shell mode and do following:

```python
>>> Patient().populate(count=1000, locale='en')
```

## Generate data by schema
Mimesis support generating data by schema:

```python
>>> from mimesis.schema import Schema
>>> schema = Schema('en')

>>> schema.load(schema={
...     "id": "cryptographic.uuid",
...     "name": "text.word",
...     "version": "development.version",
...     "owner": {
...         "email": "personal.email",
...         "token": "cryptographic.token",
...         "creator": "personal.full_name"
...     }
... }).create(iterations=2)

>>> # or you can load data from json file:
>>> schema.load(path='schema.json').create(iterations=2)
```

Result:

```
[
  {
    "id": "790cce21-5f75-2652-2ee2-f9d90a26c43d",
    "name": "container",
    "owner": {
      "email": "anjelica8481@outlook.com",
      "token": "0bf924125640c46aad2a860f40ec4b7f33a516c497957abd70375c548ed56978",
      "creator": "Ileen Ellis"
    },
    "version": "4.11.6"
  },
  ...
]
```

## Decorators
If your locale belongs to the family of Cyrillic languages, but you need latinized locale-specific data, then you can use special decorator which help you romanize your data.
At this moment it's works only for Russian and Ukrainian:
```python
>>> from mimesis.decorators import romanized

>>> @romanized('ru')
... def russian_name():
...     return 'Вероника Денисова'

>>> russian_name()
'Veronika Denisova'
```

## How to Contribute

1. Fork it
2. Take a look at contributions [guidelines](/CONTRIBUTING.md)
3. Create your feature branch (`git checkout -b feature/new_locale`)
4. Commit your changes (`git commit -am 'Add new_locale'`)
5. Add yourself to list of contributors
6. Push to the branch (`git push origin feature/new_locale`)
7. Create a new Pull Request


## License
Mimesis is licensed under the MIT License. See [LICENSE](https://github.com/lk-geimfari/mimesis/blob/master/LICENSE) for more information.

## Disclaimer
The authors assume no responsibility for how you use this library data generated by it. This library is designed only for developers with good intentions. Do not use the data generated with Mimesis for illegal purposes.

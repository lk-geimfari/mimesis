<a href="https://github.com/lk-geimfari/mimesis/">
    <p align="center">
      <img src="https://raw.githubusercontent.com/lk-geimfari/elizabeth/feature-new-strucutre/media/logo.png">
    </p>
</a>

---

[![Build Status](https://travis-ci.org/lk-geimfari/elizabeth.svg?branch=master)](https://travis-ci.org/lk-geimfari/elizabeth)
[![codecov](https://codecov.io/gh/lk-geimfari/elizabeth/branch/master/graph/badge.svg)](https://codecov.io/gh/lk-geimfari/elizabeth)
[![PyPI version](https://badge.fury.io/py/elizabeth.svg)](https://badge.fury.io/py/elizabeth)


**Mimesis** is a fast and easy to use library for Python, which helps generate mock data for a variety of purposes. This data can be particularly useful during software development and testing. For example, it could be used to populate a testing database for a web application (Django, Flask, etc.) with user information such as email addresses, usernames, first names, last names, etc. The library was written with the use of tools from the standard Python library, and therefore, it does not have any side dependencies. Currently the library supports 30 languages and 20 class providers, supplying various data.

## Documentation
Mimesis is very simple to use, and the below examples should help you get started. Complete documentation for Mimesis is available [here](http://elizabeth.readthedocs.io/).

## Installation
To install Mimesis, simply:

```zsh
➜  ~ pip install mimesis
```

Also you can install it manually:
```zsh
(env) ➜  python3 setup.py install
```

## Basic Usage

```python
>>> from mimesis import Personal
>>> person = Personal(locale='en')

>>> person.full_name(gender='female')
'Antonetta Garrison'

>>> person.email(gender='male')
'john7893@live.com'

>>> person.occupation()
'Backend Developer'
```

## Locales

You can specify a locale when creating providers and they will return data that is appropriate for the language or country associated with that locale. Mimesis currently includes support for 30 different locales. See details for more information.

<details>
<!-- toc -->

| №  | Flag  | Code       | Name                 | Native name |
|--- |---   |---       |---                 |---         |
| 1  | 🇨🇿   |  `cs`      | Czech                | Česky       |
| 2  | 🇩🇰   |  `da`      | Danish               | Dansk       |
| 3  | 🇩🇪   |  `de`      | German               | Deutsch     |
| 4  | 🇦🇹   |  `de-at`   | Austrian German      | Deutsch     |
| 5  | 🇨🇭   |  `de-ch`   | Swiss German         | Deutsch     |
| 6  | 🇺🇸   |  `en`      | English              | English     |
| 7  | 🇦🇺   |  `en-au`   | Australian English   | English     |
| 8  | 🇨🇦   |  `en-ca`   | Canadian English     | English     |
| 9  | 🇬🇧   |  `en-gb`   | British English      | English     |
| 10 | 🇪🇸   |  `es`      | Spanish              | Español     |
| 11 | 🇲🇽   |  `es-mx`   | Mexican Spanish      | Español     |
| 12 | 🇮🇷   |  `fa`      | Farsi                |      فارسی  |
| 13 | 🇫🇮   |  `fi`      | Finnish              | Suomi       |
| 14 | 🇫🇷   |  `fr`      | French               | Français    |
| 15 | 🇭🇺   |  `hu`      | Hungarian            | Magyar      |
| 16 | 🇮🇸   |  `is`      | Icelandic            | Íslenska    |
| 17 | 🇮🇹   |  `it`      | Italian              | Italiano    |
| 18 | 🇯🇵   |  `ja`      | Japanese             | 日本語       |
| 19 | 🇰🇷   |  `ko`      | Korean               | 한국어       |
| 20 | 🇳🇱   |  `nl`      | Dutch                | Nederlands  |
| 21 | 🇧🇪   |  `nl-be`   | Belgium Dutch        | Nederlands  |
| 22 | 🇳🇴   |  `no`      | Norwegian            | Norsk       |
| 23 | 🇵🇱   |  `pl`      | Polish               | Polski      |
| 24 | 🇵🇹   |  `pt`      | Portuguese           | Português   |
| 25 | 🇧🇷   |  `pt-br`   | Brazilian Portuguese | Português Brasileiro |
| 26 | 🇷🇺   |  `ru`      | Russian              | Русский     |
| 27 | 🇸🇪   |  `sv`      | Swedish              | Svenska     |
| 28 | 🇹🇷   |  `tr`      | Turkish              | Türkçe      |
| 29 | 🇺🇦   |  `uk`      | Ukrainian            | Український |
| 30 | 🇨🇳   |  `zh`      | Chinese              | 汉语         |

<!-- tocstop -->
</details>

Using locales:

```python
>>> import mimesis

>>> en = mimesis.Personal('en')
>>> de = mimesis.Personal('de')
>>> ic = mimesis.Personal('is')

>>> en.full_name()
'Carolin Brady'

>>> de.full_name()
'Sabrina Gutermuth'

>>> ic.full_name()
'Rósa Þórlindsdóttir'
```

When you only need to generate data for a single locale, use the `Generic()` provider, and you can access all providers of Mimesis from one object.

```python
>>> from mimesis import Generic
>>> g = Generic('es')

>>> g.datetime.month()
'Agosto'

>>> g.code.imei()
'353918052107063'

>>> g.food.fruit()
'Limón'
```

Keep in mind that the library supports more than twenty data providers and it's means that you can generate data for almost anything you want (really):
```python
>>> from mimesis import UnitSystem

>>> us = UnitSystem()

>>> '23 %s%s' % (us.prefix(), us.magnetic_flux())
'23 exaweber'

>>> '678 %s%s' % (us.prefix(sign='negative'), us.radioactivity())
'678 millibecquerel'
```

## Advantages

Mimesis offers a number of advantages over other similar libraries, such as Faker:

* Performance. Mimesis is significantly [faster](http://i.imgur.com/ZqkE1k2.png) than other similar libraries.
* Completeness. Mimesis strives to provide many detailed providers that offer a variety of data generators.
* Simplicity. Mimesis does not require any modules other than the Python standard library.

See [here](https://gist.github.com/lk-geimfari/461ce92fd32379d7b73c9e12164a9154) for an example of how we compare
performance with other libraries.

## Integration with Web Application Frameworks

You can use Mimesis during development and testing of applications built on a variety of frameworks. Here is an
example of integration with a Flask application:

```python
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    weight = db.Column(db.String(64))
    height = db.Column(db.String(64))
    blood_type = db.Column(db.String(64))

    def __init__(self, **kwargs):
        super(Patient, self).__init__(**kwargs)

    @staticmethod
    def bootstrap(count=500, locale='en', gender=None):
        from mimesis import Personal

        person = Personal(locale)

        for _ in range(count):
            patient = Patient(
                full_name=person.full_name(gender=gender),
                weight=person.weight(),
                height=person.height(),
                blood_type=person.blood_type(),
            )

            db.session.add(patient)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
```

Just run shell mode
```
(env) ➜ python3 manage.py shell
```

and do following:

```python
>>> Patient().bootstrap(count=1000, locale='en', gender='female')
```

## Custom Providers
You also can add custom provider to `Generic()`, using `add_provider()` method:

```python
>>> class SomeProvider():
...
...     class Meta:
...         name = "some_provider"
...
...     @staticmethod
...     def one():
...         return 1

>>> class Another():
...
...     @staticmethod
...     def bye():
...         return "Bye!"

>>> generic.add_provider(SomeProvider)
>>> generic.add_provider(Another)

>>> generic.some_provider.one()
1

>>> generic.another.bye()
'Bye!'
```

or multiple custom providers using method `add_providers()`:

```python
>>> generic.add_providers(SomeProvider, Another)
```

## Builtins specific data providers

Some countries have data types specific to that country. For example social security numbers (SSN) in the United States of America (`en`), and cadastro de pessoas físicas (CPF) in Brazil (`pt-br`).
If you would like to use these country-specific providers, then you must import them explicitly:

```python
>>> from mimesis import Generic
>>> from mimesis.builtins import BrazilSpecProvider

>>> generic = Generic('pt-br')

>>> class BrazilProvider(BrazilSpecProvider):
...     class Meta:
...         name = "brazil_provider"

>>> generic.add_provider(BrazilProvider)
>>> generic.brazil_provider.cpf()
'696.441.186-00'
```


## Decorators
If your locale belongs to the family of Cyrillic languages, but you need latinized locale-specific data, then you can use special decorator which help you romanize your data.
At this moment it's works only for Russian and Ukrainian:
```python
>>> import mimesis.decorators

>>> @mimesis.decorators.romanized('ru')
... def russian_name():
...     return 'Вероника Денисова'

>>> russian_name()
'Veronika Denisova'
```

## Disclaimer
The authors assume no responsibility for how you use this library data generated by it. This library is designed only for developers with good intentions. Do not use the data generated with Mimesis for illegal purposes.

## Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/mimesis/blob/master/CONTRIBUTING.md) guidelines first. [Here](https://github.com/lk-geimfari/mimesis/blob/master/CONTRIBUTORS.md) you can look at list of our contributors.

## License
Mimesis is licensed under the MIT License. See [LICENSE](https://github.com/lk-geimfari/mimesis/blob/master/LICENSE) for more information.

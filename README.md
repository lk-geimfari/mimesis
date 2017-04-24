<a href="https://github.com/lk-geimfari/elizabeth/">
    <p align="center">
      <img src="https://raw.githubusercontent.com/lk-geimfari/elizabeth/master/other/logo.png" alt="Elizabeth">
    </p>
</a>

---

[![Build Status](https://travis-ci.org/lk-geimfari/elizabeth.svg?branch=master)](https://travis-ci.org/lk-geimfari/elizabeth)
[![codecov](https://codecov.io/gh/lk-geimfari/elizabeth/branch/master/graph/badge.svg)](https://codecov.io/gh/lk-geimfari/elizabeth)
[![PyPI version](https://badge.fury.io/py/elizabeth.svg)](https://badge.fury.io/py/elizabeth)
[![Python Version](https://img.shields.io/badge/python-v3.3%2C%20v3.4%2C%20v3.5%2C%20v3.6-brightgreen.svg)](https://github.com/lk-geimfari/elizabeth/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8b2f43d89d774929bb0b7535812f5b08)](https://www.codacy.com/app/likid-geimfari/elizabeth?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lk-geimfari/elizabeth&amp;utm_campaign=Badge_Grade)

## Description

**Elizabeth** is a fast and easy to use Python library for generating dummy data for a variety of purposes.  This data can be particularly useful during software development and testing.  For example, it could be used to populate a testing database for a web application with user information such as email addresses, usernames, first names, last names, etc.

Elizabeth uses a JSON-based datastore and does not require any modules that are not in the Python standard library. There are over nineteen different [data providers](https://github.com/lk-geimfari/elizabeth/blob/master/PROVIDERS.md) available, which can produce data related to food, people, computer hardware, transportation, addresses, and more.

## Documentation
Elizabeth is simple to use, and the below examples should help you get started.  Complete documentation for Elizabeth is available here: [http://elizabeth.readthedocs.io/](http://elizabeth.readthedocs.io/)

## Installation
To install `Elizabeth`, simply:

```zsh
➜  ~ pip install elizabeth
```

Also you can install it manually (pre-activated virtualenv):
```zsh
(env) ➜  cd elizabeth/
(env) ➜  make test
(env) ➜  make install
```


## Basic Usage

```python
>>> from elizabeth import Personal
>>> person = Personal('en')

>>> person.full_name(gender='female')
'Antonetta Garrison'

>>> person.email(gender='male)
'oren5936@live.com'

>>> person.occupation()
'Programmer'
```

## Locales

You can specify a locale when creating providers and they will return data that is appropriate for the language or country associated with that locale.  `Elizabeth` currently includes support for 30 different locales. See details for more information.

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
>>> from elizabeth import Personal

>>> en = Personal('en')
>>> de = Personal('de')
>>> ic = Personal('is')

>>> en.full_name()
'Carolin Brady'

>>> de.full_name()
'Sabrina Gutermuth'

>>> ic.full_name()
'Rósa Þórlindsdóttir'

```

When you only need to generate data for a single locale, use the `Generic` provider, and you can access all `Elizabeth`
providers from one object.

```python
>>> from elizabeth import Generic
>>> g = Generic('es')

>>> g.datetime.month()
'Agosto'

>>> g.code.imei()
'353918052107063'

>>> g.food.fruit()
'Limón'

>>> g.internet.network_protocol(layer='application')
'AMQP'

>>> g.science.math_formula()
'(a/b)/(c/d) = (a/b) * (d/c)'
```

Keep in mind that the library supports more than nineteen data providers and it's means that you can create data for almost anything you want:
```python
>>> from elizabeth import UnitSystem

>>> us = UnitSystem()

>>> '23 %s%s' % (us.prefix(), us.magnetic_flux())
'23 exaweber'

>>> '678 %s%s' % (us.prefix(sign='negative'), us.radioactivity())
'678 millibecquerel'
```

## Advantages

`Elizabeth` offers a number of advantages over other similar libraries, such as `Faker`:

* Performance. `Elizabeth` is significantly [faster](http://i.imgur.com/ZqkE1k2.png) than other similar libraries.
* Completeness. `Elizabeth` strives to provide many detailed providers that offer a variety of data generators.
* Simplicity. `Elizabeth` does not require any modules other than the Python standard library.

See [here](https://gist.github.com/lk-geimfari/461ce92fd32379d7b73c9e12164a9154) for an example of how we compare
performance with other libraries.

## Integration with Web Application Frameworks

You can use `Elizabeth` during development and testing of applications built on a variety of frameworks. Here is an
example of integration with a `Flask` application:

```python
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(25))
    full_name = db.Column(db.String(100))
    weight = db.Column(db.String(64))
    height = db.Column(db.String(64))
    blood_type = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super(Patient, self).__init__(**kwargs)

    @staticmethod
    def _bootstrap(count=500, locale='en', gender):
        from elizabeth import Personal

        person = Personal(locale)

        for _ in range(count):
            patient = Patient(
                email=person.email(),
                phone_number=person.telephone(),
                full_name=person.full_name(gender=gender),
                age=person.age(minimum=18, maximum=45),
                weight=person.weight(),
                height=person.height(),
                blood_type=person.blood_type()
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
>>> db
<SQLAlchemy engine='sqlite:///db_dev.sqlite'>

>>> Patient
<class 'app.models.Patient'>

>>> Patient()._bootstrap(count=1000, locale='en', gender='female')
```

Result: [screenshot](https://raw.githubusercontent.com/lk-geimfari/elizabeth/master/other/screenshots/en_bootstrap.png)

## Custom Providers
You also can add custom provider to `Generic`.

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

## Builtins specific data providers

Some countries have data types specific to that country. For example social security numbers in the United States (`en` locale), and cadastro de pessoas físicas (CPF) in Brazil (`pt-br` locale).

If you would like to use these country-specific providers, then you must import them explicitly:

```python
>>> from elizabeth import Generic
>>> from elizabeth.builtins import BrazilSpecProvider

>>> generic = Generic('pt-br')

>>> class BrazilProvider(BrazilSpecProvider):
...
...     class Meta:
...         name = "brazil_provider"
...

>>> generic.add_provider(BrazilProvider)
>>> generic.brazil_provider.cpf()
'696.441.186-00'
```


## Decorators
If your locale is cyrillic, but you need latinized locale-specific data, then you can use special decorator.
At this moment it's works only for Russian and Ukrainian:
```python
>>> from elizabeth.decorators import romanized

>>> @romanized('ru')
... def name_ru():
...     return 'Вероника Денисова'
...

>>> @romanized('uk')
>>> def name_uk():
...     return 'Емілія Акуленко'
...

>>> name_ru()
'Veronika Denisova'

>>> name_uk()
'Emіlіja Akulenko'
```


## Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md) guidelines first it is very important. [Here](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTORS.md) you can look a list of our contributors.

## License
Elizabeth is licensed under the MIT License. See [LICENSE](https://github.com/lk-geimfari/elizabeth/blob/master/LICENSE) for more information.

## Disclaimer
The authors assume no responsibility for how you use this library data generated by it.  This library is designed only for developers with good intentions. Do not use the data generated with Elizabeth for illegal purposes.

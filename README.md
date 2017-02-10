## Elizabeth
[![Build Status](https://travis-ci.org/lk-geimfari/elizabeth.svg?branch=master)](https://travis-ci.org/lk-geimfari/elizabeth)
[![codecov](https://codecov.io/gh/lk-geimfari/elizabeth/branch/master/graph/badge.svg)](https://codecov.io/gh/lk-geimfari/elizabeth)
[![Documentation Status](https://readthedocs.org/projects/elizabeth/badge/?version=latest)](http://elizabeth.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/elizabeth.svg)](https://badge.fury.io/py/elizabeth)
[![Python Version](https://img.shields.io/badge/python-v3.3%2C%20v3.4%2C%20v3.5%2C%20v3.6-brightgreen.svg)](https://github.com/lk-geimfari/elizabeth/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d773f20efa67430683bb24fff5af9db8)](https://www.codacy.com/app/likid-geimfari/church)

<p align="center">
  <img src="https://raw.githubusercontent.com/lk-geimfari/elizabeth/master/other/elizabeth_1.png">
  <br>
</p>

**Elizabeth** is a fast and easy to use Python library for generating dummy data for a variety of purposes.  This data can be particularly useful during software development and testing.  For example, it could be used to populate a testing database for a web application with user information such as email addresses, usernames, first names, last names, etc.  Elizabeth uses a JSON-based datastore and does not require any modules that are not in the Python standard library. There are over nineteen different [data providers](https://github.com/lk-geimfari/elizabeth/blob/master/PROVIDERS.md) available, which can produce data related to food, people, computer hardware, transportation, addresses, and more.

## Documentation
Elizabeth is simple to use, and the below examples should help you get started.  Complete documentation for `Elizabeth` is available here: [http://elizabeth.readthedocs.io/en/latest/](http://elizabeth.readthedocs.io/)

## Installation
To install `Elizabeth`, simply:

```zsh
➜  ~ pip install elizabeth
```

Also you can install it manually:
```zsh
➜  ~ git clone https://github.com/lk-geimfari/elizabeth.git
➜  ~ cd elizabeth
➜  python3 setup.py install
```


## Basic Usage

```python
>>> from elizabeth import Personal
>>> p = Personal('en')
>>>
>>> p.full_name(gender='female')
'Antonetta Garrison'
>>> p.blood_type()
'O-'
>>> p.occupation()
'Programmer'
```

## Locales

You can specify a locale when creating providers and they will return data that is appropriate for the language or country associated with that locale.  `Elizabeth` currently includes support for 22 different [locales](https://github.com/lk-geimfari/elizabeth/blob/master/LOCALES.md)

Using locales:

```python
>>> from elizabeth import Text
>>> en = Text()  # English is Elizabeth's default locale
>>> de = Text('de')

>>> en.sentence()
'Ports are used to communicate with the external world.'
>>> de.sentence()
'Wir müssen nicht vergessen Zickler.'
>>>
>>> en.color()
'Blue'
>>> de.color()
'Türkis'
```

When you only need to generate data for a single locale, use the `Generic` provider, and you can access all `Elizabeth`
providers from one object.

```python
>>> from elizabeth import Generic
>>> g = Generic('es')
>>>
>>> g.datetime.month()
'Agosto'
>>> g.code.imei()
'353918052107063'
>>> g.food.fruit()
'Limón'
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
    def _bootstrap(count=2000, locale='en'):
        from elizabeth import Personal

        person = Personal(locale)

        for _ in range(count):
            patient = Patient(
                email=person.email(),
                phone_number=person.telephone(),
                full_name=person.full_name(gender='female'),
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
(venv) ➜ python3 manage.py shell
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
>>> from elizabeth import Generic
>>> generic = Generic('en')
>>>
>>> class SomeProvider():
>>>     class Meta:
>>>         name = 'some_provider'
>>>
>>>     def ints(self):
>>>         return [i for i in range(1, 5)]
>>>
>>> class Another():
>>>     def bye(self):
>>>         return "Bye!"
>>>
>>> generic.add_provider(SomeProvider)
>>> generic.add_provider(Another)
>>>
>>> generic.some_provider.ints()
[1, 2, 3, 4]
>>> generic.another.bye()
'Bye!'
```

## Builtins specific data providers

Some countries have data types specific to that country. For example social security numbers in the United States (`en` locale), and cadastro de pessoas físicas (CPF) in Brazil (`pt-br` locale).

If you would like to use these country-specific providers, then you must import them explicitly:

```python
>>> from elizabeth import Generic
>>> from elizabeth.builtins import BrazilSpecProvider
>>>
>>> generic = Generic('pt-br')
>>>
>>> class BrazilProvider(BrazilSpecProvider):
>>>     class Meta:
>>>         name = "brazil_provider"
>>>
>>> generic.add_provider(BrazilProvider)
>>>
>>> generic.brazil_provider.cpf()
'001.137.297-40'
```

## Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md) guidelines first. [Here](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTORS.md) you can look a list of our contributors.

## Testing
```zsh
➜ ~ git clone https://github.com/lk-geimfari/elizabeth.git
➜ cd elizabeth/
➜ python3 -m unittest discover tests
```

## License
Elizabeth is licensed under the MIT License. See [LICENSE](https://github.com/lk-geimfari/elizabeth/blob/master/LICENSE) for more information.

## Like It?
You can say [thanks](https://saythanks.io/to/lk-geimfari)!

## Disclaimer
The authors assume no responsibility for how you use this library data generated by it.  This library is designed only for developers with good intentions. Do not use the data generated with `Elizabeth` for illegal purposes.

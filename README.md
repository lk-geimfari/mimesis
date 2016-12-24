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

**Elizabeth** is a fast and easier to use Python library for generating dummy data. These data are very useful when you need to bootstrap the database in the testing phase of your software. A great example of how you can use the library are web applications on Flask or Django which need a data, such as users (email, username, name, surname etc.), posts (tags, text, title, publishing date and etc.) and so forth. The library uses the JSON files as a datastore and doesn’t have any dependencies. The library offers more than 18 different data providers (from personal ones to transport and more).


## Documentation
Elizabeth is a pretty simple library and all you need to start is the small documentation. See Elizabeth's Sphinx-generated documentation here: [http://elizabeth.readthedocs.io/en/latest/](http://elizabeth.readthedocs.io/)

## Locales

At this moment a library has 16 supported locales:

| №  | Flag  | Code       | Name                 | Native name |
|--- |---   |---        |---                |---         |
| 1  | 🇩🇰   |  `da`      | Danish               | Dansk       |
| 2  | 🇩🇪   |  `de`      | German               | Deutsch     |
| 3  | 🇺🇸   |  `en`      | English              | English     |
| 4  | 🇪🇸   |  `es`      | Spanish              | Español     |
| 5  | 🇮🇷   |  `fa`      | Farsi                |      فارسی  |
| 6  | 🇫🇮   |  `fi`      | Finnish              | Suomi       |
| 7  | 🇫🇷   |  `fr`      | French               | Français    |
| 8  | 🇮🇸   |  `is`      | Icelandic            | Íslenska    |
| 9  | 🇮🇹   |  `it`      | Italian              | Italiano    |
| 10 | 🇳🇱   |  `nl`      | Dutch                | Nederlands  |
| 11 | 🇳🇴   |  `no`      | Norwegian            | Norsk       |
| 12 | 🇵🇱   |  `pl`      | Polish               | Polski      |
| 13 | 🇵🇹   |  `pt`      | Portuguese           | Português   |
| 14 | 🇧🇷   |  `pt-br`   | Brazilian Portuguese | Português Brasileiro |
| 15 | 🇷🇺   |  `ru`      | Russian              | Русский     |
| 16 | 🇸🇪   |  `sv`      | Swedish              | Svenska     |




## Installation
```zsh
➜  ~ pip install elizabeth
```

## Testing
```zsh
➜  ~ git clone https://github.com/lk-geimfari/elizabeth.git
➜  ~ cd elizabeth/
➜  ~ python3 -m unittest discover tests
```

## Using with Flask

You can use `Elizabeth` with your Flask-application (or with any another Web-framwrork that suppor ORM).

```python
# Some logic
# ...
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

Result:

![en](https://raw.githubusercontent.com/lk-geimfari/elizabeth/master/other/screenshots/en_bootstrap.png)


## A common use

Import a provider that you need

```python
>>>> from elizabeth import Personal
```
and create instance of provider that was be imported:

```python
>>> personal = Personal('en')
```
and call the one from methods:

```python
>>> for _ in range(0, 5):
       personal.full_name(gender='female')
```

Output:
```
Antonetta Garrison
Taneka Dickerson
Jackelyn Stafford
Tashia Olsen
Rachal Hartman
```

For other locales, exactly the same way (Icelandic) :

```python
>>> personal = Personal('is')
```

```python
>>> for _ in range(0, 5):
        personal.full_name(gender='male')
```

Output:
```
Þórgrímur Garibaldason
Zóphanías Bergfinnsson
Vésteinn Ríkharðsson
Hallvarður Valgarðsson
Baltasar Hlégestsson
```

When you use only one locale you can use the `Generic` , that provides all providers at one class.

```python
>>> from elizabeth import Generic

>>> g = Generic('ru')

>>> for _ in range(0, 5):
        name = g.personal.full_name()
        birthday = g.datetime.birthday(readable=True)
        print(name, '-', birthday)

```
Output:
```
Гера Исакова - Май 31, 1981
Лидия Воронцова - Апрель 11, 1990
Пелагея Исаева - Август 7, 1983
Евфросинья Ермакова - Март 12, 1992
Веселина Зыкова - Октябрь 18, 1996
```

## Data providers
Elizabeth support more than [18](https://github.com/lk-geimfari/elizabeth/blob/master/PROVIDERS.md) data providers, such as Personal, Datetime, Internet and [another](https://github.com/lk-geimfari/elizabeth/blob/master/PROVIDERS.md).

## Like it?
You can say [thanks](https://saythanks.io/to/lk-geimfari)!


## Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md) guidelines first. [Here](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md#contributors) you can look a list of contributors


## Disclaimer
The author does not assume any responsibility for how you will use this library and how you will use data generated with this library. This library is designed only for developers and only with good intentions. Do not use the data generated with `Elizabeth` for illegal purposes.


## Licence
Elizabeth is licensed under the MIT License. See [LICENSE](https://github.com/lk-geimfari/elizabeth/blob/master/LICENSE)  for the full license text.

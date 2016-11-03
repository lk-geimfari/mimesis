# Church
[![Build Status](https://travis-ci.org/lk-geimfari/church.svg?branch=master)](https://travis-ci.org/lk-geimfari/church)
[![Documentation Status](https://readthedocs.org/projects/church/badge/?version=latest)](http://church.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/church.svg)](https://badge.fury.io/py/church)
[![HitCount](https://hitt.herokuapp.com/lk-geimfar/church.svg)](https://github.com/lk-geimfari/church)
[![Code Health](https://landscape.io/github/lk-geimfari/church/master/landscape.svg?style=flat)](https://landscape.io/github/lk-geimfari/church/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d773f20efa67430683bb24fff5af9db8)](https://www.codacy.com/app/likid-geimfari/church)
[![Issues](https://img.shields.io/github/issues/lk-geimfari/church.svg)](https://github.com/lk-geimfari/church/issues)


![alt text](https://raw.githubusercontent.com/lk-geimfari/church/master/examples/logo.png)



Church is a library to generate fake data. It's very useful when you need to bootstrap your database. Church doesn't have any dependencies.

At this moment a library has 14 supported locales:

|   F   |  Code   |   Name              |
|--:    |---      |    ---              |
| 🇩🇰  | da      |  Dansk               |
| 🇩🇪  | de      |  Deutsch             |
| 🇺🇸  | en      |  English             |
| 🇪🇸  | es      |  Español             |
| 🇫🇮  | fi      |  Suomi               |
| 🇫🇷  | fr      |  Français            |
| 🇮🇸  | is      |  Íslenska*           |
| 🇮🇹  | it      |  Italiano            |
| 🇳🇱  | nl      |  Nederlands*         |
| 🇳🇴  | no      |  Norsk               |
| 🇸🇪  | sv      |  Svenska             |
| 🇷🇺  | ru      |  Русский             |
| 🇵🇹  | pt      | Português            |
| 🇧🇷  | pt-br   |  Português Brasileiro|

`* - not completely`


## Documentation
Church is a pretty simple library and all you need to start is the small documentation. See church's Sphinx-generated documentation here: [http://church.readthedocs.io](http://church.readthedocs.io)



## Installation
```zsh
➜  ~ git clone https://github.com/lk-geimfari/church.git
➜  ~ cd church/
➜  ~ python3 setup.py install

```
or
```zsh
➜  ~  pip install church
```

## Testing
```zsh
➜  ~ cd church/
➜  ~ python3 -m unittest discover tests
```


## Usage

```python
# It's very useful when you need to bootstrap your database.
# Just create a static method that will generate fake data:


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(25))
    full_name = db.Column(db.String(100))
    gender = db.Column(db.String(64))
    nationality = db.Column(db.String(64))
    weight = db.Column(db.String(64))
    height = db.Column(db.String(64))
    blood_type = db.Column(db.String(64))

    def __init__(self, **kwargs):
        super(Patient, self).__init__(**kwargs)

    @staticmethod
    def churchify(count=2000):
        from church import Personal

        person = Personal('en')
        for _ in range(count):
            patient = Patient(email=person.email(),
                              phone_number=person.telephone(),
                              full_name=person.full_name(gender='female'),
                              gender=person.gender(),
                              nationality=person.nationality(),
                              weight=person.weight(),
                              height=person.height(),
                              blood_type=person.blood_type()
                              )
        try:
            db.session.add(patient)
        except Exception:
            db.session.commit()
```
When you use only one locale, use following format:
```python
from church import Church

ch = Church('en')


def patient(sex='female'):
    user = {
        'full_name': ch.personal.full_name(sex),
        'gender': ch.personal.gender(sex),
        'blood_type': ch.person.blood_type(),
        'birthday': ch.datetime.birthday()
    }
    return user
```


## Examples
- [flask_church](https://github.com/lk-geimfari/flask_church) - An extension for `Flask` based on `Church`.
- [presturinn](https://github.com/lk-geimfari/presturinn) - This is a fake API based on `Falcon` and `Church v0.2.0` .


## Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/church/blob/master/CONTRIBUTING.md) guidelines first. [Here](https://github.com/lk-geimfari/church/blob/master/CONTRIBUTORS.md) you can look a list of contributors


## Disclaimer
The author does not assume any responsibility for how you will use this library and how you will use data generated with this library. This library is designed only for developers and only with good intentions. Do not use the data generated with `church` for illegal purposes.


## Licence
[MIT License](https://github.com/lk-geimfari/church/blob/master/LICENSE)

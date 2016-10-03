# Church
[![Build Status](https://travis-ci.org/lk-geimfari/church.svg?branch=master)](https://travis-ci.org/lk-geimfari/church)
[![PyPI version](https://badge.fury.io/py/church.svg)](https://badge.fury.io/py/church)
[![HitCount](https://hitt.herokuapp.com/lk-geimfar/church.svg)](https://github.com/lk-geimfari/church)
[![Code Health](https://landscape.io/github/lk-geimfari/church/master/landscape.svg?style=flat)](https://landscape.io/github/lk-geimfari/church/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d773f20efa67430683bb24fff5af9db8)](https://www.codacy.com/app/likid-geimfari/church)
[![Issues](https://img.shields.io/github/issues/lk-geimfari/church.svg)](https://github.com/lk-geimfari/church/issues)


![alt text](https://raw.githubusercontent.com/lk-geimfari/church/master/examples/church.png)

Church is a library to generate fake data. It's very useful when you need to bootstrap your database.

## Installation

```zsh
➜  ~  pip install church
```

## Usage

```python
# At this moment a library has 4 supported locales: en_us, de_de, fr_fr, ru_ru
#
# It's very useful when you need to bootstrap your database.
# Just create a static method that will generate fake data:

@staticmethod
def _bootstrap(count=2000):
    from church import Personal

    person = Personal('en_us')
    for _ in range(count):
        user = User(username=person.username(),
                    email=person.email(),
                    user_twitter=person.twitter()
                    name=person.name('m'),
                    surname=person.surname(),
                    credit_card=person.credit_card_number(),
                    home_page=person.home_page(),
                    password=person.password(algorithm='sha1'),
                    gender=person.gender(abbreviated=True),
                    profession=person.profession(),
                    nationality=person.nationality()
               )
        try:
            db.session.add(user)
        except Exception:
            db.session.commit()

# ...
```

## Example
[presturinn](https://github.com/lk-geimfari/presturinn) - This is a fake API based on `Falcon` and `Church`.

## Docs
Church is a pretty simple library. All you need to start is a small [guidebook.](https://github.com/lk-geimfari/church/blob/master/docs/README.md)

## Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/church/blob/master/CONTRIBUTING.md) guidelines first.

## Requirements
No requirements, no dependencies

## Runtime
[![PyPI](https://img.shields.io/badge/python-3.4%2C%203.5-blue.svg?maxAge=2592000)](https://pypi.python.org/pypi/church/)

## Licence 
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://github.com/lk-geimfari/church/blob/master/LICENSE)   

## Why church?
«Such teachings come through hypocritical liars, whose consciences have been seared as with a hot iron.» Timothy 1:4

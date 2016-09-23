# Church
[![Build Status](https://travis-ci.org/lk-geimfari/church.svg?branch=master)](https://travis-ci.org/lk-geimfari/church)
[![PyPI version](https://badge.fury.io/py/church.svg)](https://badge.fury.io/py/church)
[![HitCount](https://hitt.herokuapp.com/lk-geimfar/church.svg)](https://github.com/lk-geimfari/church)
[![Code Health](https://landscape.io/github/lk-geimfari/church/master/landscape.svg?style=flat)](https://landscape.io/github/lk-geimfari/church/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d773f20efa67430683bb24fff5af9db8)](https://www.codacy.com/app/likid-geimfari/church?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lk-geimfari/church&amp;utm_campaign=Badge_Grade)
[![Issues](https://img.shields.io/github/issues/lk-geimfari/church.svg)](https://github.com/lk-geimfari/church/issues)


![alt text](https://raw.githubusercontent.com/lk-geimfari/church/master/examples/church.png)

Church - is a library to generate fake data. It's very useful if you need to bootstrap your database.

## Installation
```zsh
➜  ~  pip install church

```

## Usage
```python
#  It's very useful if you need to bootstrap your database.
# Just create static method that will generate fake data.
# ...

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
## Docs
Church is pretty simple library. All that you need is small [guidebook.](https://github.com/lk-geimfari/church/blob/master/docs/README.md)


## Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/church/blob/master/CONTRIBUTING.md) guidelines first.

## Runtime
[![PyPI](https://img.shields.io/badge/python-3.4%2C%203.5-blue.svg?maxAge=2592000)](https://pypi.python.org/pypi/church/)


## Licence 
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://github.com/lk-geimfari/church/blob/master/LICENSE)   


## Why church?
«Such teachings come through hypocritical liars, whose consciences have been seared as with a hot iron.» Timothy 1:4

`If you offended by name of this library then you may don't use it.` [`Do Not Use!`](https://github.com/lk-geimfari/church/issues/6)

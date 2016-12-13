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

**Elizabeth** is a fast and easier to use Python library for generate dummy data. These data are very useful when you need to bootstrap the database in the testing phase of your software. A great example of how you can use the library is a web applications on Flask or Django which need a data, such as users (email, username, name, surname etc.), posts (tags, text, title, publishing date and etc.) asf. The library use the JSON files as a datastore and doesn't have any dependencies.


## Documentation
Elizabeth is a pretty simple library and all you need to start is the small documentation. See Elizabeth's Sphinx-generated documentation here: [http://elizabeth.readthedocs.io/en/latest/](http://elizabeth.readthedocs.io/)

## Locales

At this moment a library has 16 supported locales:

| №  | Flag  | Code       | Name                 | Native name |
|--- |---    |---         |---                   |---          |
| 1  | 🇩🇰   |  `da`      | Danish               | Dansk       |
| 2  | 🇩🇪   |  `de`      | German               | Deutsch     |
| 3  | 🇺🇸   |  `en`      | English              | English     |
| 4  | 🇪🇸   |  `es`      | Spanish              | Español     |
| 5  | 🇮🇷   |  `fa`      | Farsi                | فارسی       |
| 6  | 🇫🇮   |  `fi`      | Finnish              | Suomi       |
| 7  | 🇫🇷   |  `fr`      | French               | Français    |
| 8  | 🇮🇸   |  `is`      | Icelandic            | Íslenska    |
| 9  | 🇮🇹   |  `it`      | Italian              | Italiano    |
| 10 | 🇳🇱   |  `nl`      | Dutch                | Nederlands  |
| 11 | 🇳🇴   |  `no`      | Norwegian            | Norsk       |
| 12 | 🇸🇪   |  `sv`      | Swedish              | Svenska     |
| 13 | 🇷🇺   |  `ru`      | Russian              | Русский     |
| 14 | 🇵🇹   |  `pt`      | Portuguese           | Português   |
| 15 | 🇧🇷   |  `pt-br`   | Brazilian Portuguese | Português Brasileiro |
| 16 | 🇵🇱   |  `pl`      | Polish               | Polski      |



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

## Examples

Below you can see, how to generate fake paths using `Elizabeth`:
```python
>>> from elizabeth import Path
>>> path = Path()

>>> path.root
'/'

>>> path.home
'/home/'

>>> path.user(gender='female')
'/home/chieko'

>>> path.users_folder(user_gender='male')
'/home/lyndon/Documents'

>>> path.dev_dir(user_gender='female')
'/home/edra/Development/Ruby'

>>> path.project_dir(user_gender='female')
'/home/katharina/Development/C Shell/litany'
```
or how to generate dummy model of transport:
```python
>>> from elizabeth import Transport
>>> transport = Transport()

>>> transport.truck()
'Union-0632 FX'

>>> transport.truck(model_mask="##/@")
'Jiaotong-78/P'

>>> transport.car()
'Pontiac Grand Am'

>>> transport.airplane()
'Boeing 575'

>>> transport.airplane(model_mask="7##")
'Airbus 778'
```

When you use only one locale you can use the `Generic` , that provides all providers at one class.

This is a contrived example, but it illustrates how this works.

```python
from elizabeth import Generic

el = Generic('en')


def patient(gender='female'):
    patient_card = {
        'full_name': el.personal.full_name(gender=gender),
        'gender': el.personal.gender(gender=gender),
        'blood_type': el.person.blood_type(),
        'birthday': el.datetime.birthday()
    }
return patient_card
```

## Data providers
Elizabeth support more than [18](https://github.com/lk-geimfari/elizabeth/blob/master/PROVIDERS.md) data providers, such as Personal, Datetime, Internet and [another](https://github.com/lk-geimfari/elizabeth/blob/master/PROVIDERS.md).


## Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md) guidelines first. [Here](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md#contributors) you can look a list of contributors


## Disclaimer
The author does not assume any responsibility for how you will use this library and how you will use data generated with this library. This library is designed only for developers and only with good intentions. Do not use the data generated with `Elizabeth` for illegal purposes.


## Licence
Elizabeth is licensed under the MIT License. See [LICENSE](https://github.com/lk-geimfari/elizabeth/blob/master/LICENSE)  for the full license text.

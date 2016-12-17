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

How to generate user data:

```python
from elizabeth import Personal

personal = Personal('en')

for _ in range(0, 15):
    print(personal.full_name(gender='female'))
```

Output:
```
Sixta Cantu
Antonetta Garrison
Caroll Mcgee
Helaine Mendoza
Taneka Dickerson
Jackelyn Stafford
Tashia Olsen
Reiko Lynn
Roberto Baxter
Rachal Hartman
Susann Hogan
Natashia Klein
Delora Conrad
Britteny Valdez
Sunni Strickland
```

For other locales, exactly the same way (Icelandic) :

```python
personal = Personal('is')

for _ in range(0, 15):
    print(personal.full_name(gender='male'))
```

Output:
```
Karl Brynjúlfsson
Þórgrímur Garibaldason
Rögnvald Eiðsson
Zóphanías Bergfinnsson
Vésteinn Ríkharðsson
Friðleifur Granason
Fjarki Arngarðsson
Hafsteinn Þrymsson
Hallvarður Valgarðsson
Baltasar Hlégestsson
Sívar Kakalason
Sigurjón Tómasson
Grímnir Unason
Gýmir Þórðsson
```

How to work tith datetime:

```python
from elizabeth import Datetime

dt = Datetime('no') # Norwegian

for _ in range(0, 10):
    print(dt.birthday())
```

Output:
```
Mai 17, 1982
August 13, 1984
September 6, 1999
Februar 8, 1998
April 8, 1985
August 5, 1990
Mai 23, 1997
April 25, 1987
November 5, 1980
Mars 27, 1990
```

When you use only one locale you can use the `Generic` , that provides all providers at one class.

```python
from elizabeth import Generic

g = Generic('ru')

for _ in range(0, 5):
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


## Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md) guidelines first. [Here](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md#contributors) you can look a list of contributors


## Disclaimer
The author does not assume any responsibility for how you will use this library and how you will use data generated with this library. This library is designed only for developers and only with good intentions. Do not use the data generated with `Elizabeth` for illegal purposes.


## Licence
Elizabeth is licensed under the MIT License. See [LICENSE](https://github.com/lk-geimfari/elizabeth/blob/master/LICENSE)  for the full license text.

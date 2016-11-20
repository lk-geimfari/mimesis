# Elizabeth
[![Build Status](https://travis-ci.org/lk-geimfari/elizabeth.svg?branch=master)](https://travis-ci.org/lk-geimfari/elizabeth)
[![Documentation Status](https://readthedocs.org/projects/elizabeth/badge/?version=latest)](http://elizabeth.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/elizabeth.svg)](https://badge.fury.io/py/elizabeth)
[![HitCount](https://hitt.herokuapp.com/lk-geimfar/church.svg)](https://github.com/lk-geimfari/elizabeth)
[![Code Health](https://landscape.io/github/lk-geimfari/elizabeth/master/landscape.svg?style=flat)](https://landscape.io/github/lk-geimfari/elizabeth/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d773f20efa67430683bb24fff5af9db8)](https://www.codacy.com/app/likid-geimfari/church)
[![Issues](https://img.shields.io/github/issues/lk-geimfari/church.svg)](https://github.com/lk-geimfari/elizabeth/issues)


<p align="center">
  <img src="https://raw.githubusercontent.com/lk-geimfari/elizabeth/master/other/elizabeth_1.png">
  <br>
</p>


**Elizabeth** is a library to generate dummy data. It's very useful when you need to bootstrap your database. Elizabeth doesn't have any dependencies.

At this moment a library has 15 supported locales:

| F     |🇩🇰 |🇩🇪|🇺🇸|🇪🇸 |🇫🇮|🇫🇷|🇮🇸|🇮🇹|🇳🇱|🇳🇴|🇸🇪|🇷🇺|🇵🇹 |🇧🇷 |🇵🇱|
|---    |--- |--- |---|--- |--- |--- |---|---|--- |---|--- |---|---|---  |---  |
| Code  |[da](http://bit.ly/2g50Hpf)|[de](http://bit.ly/2fDVsPl)|[en](http://bit.ly/2g3wYfe)|[es](http://bit.ly/2grHSRg)*|[fi](http://bit.ly/2g3tzxe)*|[fr](http://bit.ly/2fpp7cc)|[is](http://bit.ly/2f8Lem2)*|[it](http://bit.ly/2g4DAOl)|[nl](http://bit.ly/2fNqFNF)*|[no](http://bit.ly/2eOUErG)|[sv](http://bit.ly/2eOZV2D)|[ru](http://bit.ly/2fNsUk5)|[pt](http://bit.ly/2fNpopS)* |[pt-br](http://bit.ly/2grKChn)|[pl](http://bit.ly/2ffwDbO)|

`* - not completely`


## Documentation
Elizabeth is a pretty simple library and all you need to start is the small documentation. See Elizabeth's Sphinx-generated documentation here: [http://elizabeth.readthedocs.io/en/latest/](http://elizabeth.readthedocs.io/en/latest/)



## Installation
```zsh
➜  ~ git clone https://github.com/lk-geimfari/elizabeth.git
➜  ~ cd elizabeth/
➜  ~ python3 setup.py install

# or

➜  ~ pip install elizabeth
```

## Testing
```zsh
➜  ~ cd elizabeth/
➜  ~ python3 -m unittest discover tests

# or
➜  ~ ./run_tests.sh
```

## Usage

```python
# ...
# Model from some Flask project.

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
    def _bootstrap(count=2000):
        from elizabeth import Personal

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
When you use only one locale, then you can use the `Generic` class.
```python
from elizabeth import Generic

el = Generic('en')


def patient(gender='female'):
    patient_card = {
        'full_name': el.personal.full_name(sex),
        'gender': el.personal.gender(gender=gender),
        'blood_type': el.person.blood_type(),
        'birthday': el.datetime.birthday()
    }
return patient_card
```

## Available data providers

| Provider          | Description                                                  |
| -------------     |:-------------                                                |
| `Address`         | *Address data (street name, street suffix etc.)*             |
| `Business`        | *Business data (company, company_type, copyright etc.)*      |
| `Code`            | *Codes (ISBN, EAN, IMEI etc.).*                              |
| `ClothingSizes`   | *Clothing sizes (international sizes, european etc.)*        |
| `Datetime`        | *Datetime (day_of_week, month, year etc.)*                   |
| `Development`     | *Data for developers (version, programming language etc.)*   |
| `File`            | *File data (extension etc.)*                                 |
| `Food`            | *Information on food (vegetables, fruits, measurements etc.)*|
| `Personal`        | *Personal data (name, surname, age, email etc.)*             |
| `Text`            | *Text data (sentence, title etc.)*                           |
| `Transport`       | *Dummy data about transport (truck model, car etc.)*         |
| `Network`         | *Network data (IPv4, IPv6, MAC address) etc*                 |
| `Science`         | *Scientific data (scientist, math_formula etc.)*             |
| `Internet`        | *Dummy internet data (facebook, twitter etc.)*                |
| `Hardware`        | *The data about the hardware (resolution, cpu, graphics etc.)*|
| `Numbers`         | *Numerical data (floats, primes, digit etc.)*                 |
| `Generic`         | *All at one*                                                  |


## Examples
- [flask_church](https://github.com/lk-geimfari/flask_church) - An extension for `Flask` based on `Elizabeth`.
- [presturinn](https://github.com/lk-geimfari/presturinn) - This is a fake API based on `Falcon` and `Elizabeth v0.2.0` .


## Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTING.md) guidelines first. [Here](https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTORS.md) you can look a list of contributors


## Disclaimer
The author does not assume any responsibility for how you will use this library and how you will use data generated with this library. This library is designed only for developers and only with good intentions. Do not use the data generated with `elizabeth` for illegal purposes.


## Licence
[MIT License](https://github.com/lk-geimfari/elizabeth/blob/master/LICENSE)

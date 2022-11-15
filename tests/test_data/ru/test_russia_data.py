import re
import typing

import pytest

from mimesis import Person
from mimesis.locales import Locale

NON_RU_LETTERS = re.compile(r"(?:(?![а-яё\d])[\w])+", re.IGNORECASE)


def params(data: typing.Dict):
    def extract_data(data: typing.Dict, result: typing.List, key: str = '') -> None:
        for k, v in data.items():
            name = f"{key}_{k}" if key else k
            if isinstance(v, list):
                result.append((name, v))
            else:
                extract_data(v, result, name)

    result = []
    data.pop("occupation")  # mixed language data
    extract_data(data, result)

    return result


@pytest.mark.parametrize("name, data", params(Person(Locale.RU)._data))
def test_person_data(name, data):
    for string in data:
        result = NON_RU_LETTERS.search(string)
        assert not result, f"{name} data '{string}' contains non cyrillic character!"


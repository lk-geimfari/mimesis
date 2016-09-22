from functools import lru_cache
from os.path import (
    join,
    dirname,
    abspath
)

PATH = abspath(join(dirname(__file__), 'data'))

__all__ = ['priest']


@lru_cache(maxsize=None)
def pull(filename, lang='en_us'):
    """
    Function for getting data from text files in data/
    1. de_de - Folder for Germany.
    2. en_us - Folder for United States
    3. ru_ru - Folder for Russian Federation.
    """
    with open(join(PATH + '/' + lang, filename), 'r') as f:
        _result = f.readlines()

    return _result


def priest():
    """
    Get a random quote from Bible.
    :return: quote.
    """
    from random import choice
    _quo = choice(pull('data', 'ch_path')).strip()
    return "My child, " + _quo

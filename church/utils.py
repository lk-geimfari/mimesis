from os.path import join, dirname, abspath

PATH = abspath(join(dirname(__file__), 'data'))

_cache = {}


def pull(filename, lang='en_us'):
    """
    Function for getting data from text files in data/
    """
    if filename not in _cache:
        with open(join(PATH + '/' + lang, filename), 'r') as f:
            _cache[filename] = f.readlines()

    return _cache[filename]
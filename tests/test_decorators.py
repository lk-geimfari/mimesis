import pytest

import mimesis.decorators


def test_romanization_dict_is_unchanged():
    from copy import deepcopy
    from mimesis.data import ROMANIZATION_DICT

    old_data = deepcopy(ROMANIZATION_DICT)

    @mimesis.decorators.romanize('ru')
    def some_name():
        return 'Абырвалг Аристархович'

    some_name()
    assert ROMANIZATION_DICT == old_data


@pytest.fixture
@mimesis.decorators.romanize('ru')
def russian_name():
    return 'Ликид Геимфари'


def test_russian(russian_name):
    assert russian_name == 'Likid Geimfari'


@pytest.fixture
@mimesis.decorators.romanize('ru')
def mixed_text():
    return 'Что-то там_4352-!@#$%^&*()_+?"<>"'


def test_russian_mixed_text(mixed_text):
    assert mixed_text == 'Chto-to tam_4352-!@#$%^&*()_+?"<>"'


@pytest.fixture
@mimesis.decorators.romanize('ru')
def russian_alphabet():
    return ' '.join('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                    'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')


def test_romanize_russian_alphabet(russian_alphabet):
    result = 'A B V G D E Yo Zh Z I Ye K L M N O P R S T U F Kh Ts ' \
             'Ch Sh Shch  Y  E Yu Ja a b v g d e yo zh z i ye k l m n' \
             ' o p r s t u f kh ts ch sh shch  y  e yu ja'

    assert russian_alphabet == result


@pytest.fixture
@mimesis.decorators.romanize('uk')
def ukrainian_text():
    return 'Українська мова!'


def test_ukrainian(ukrainian_text):
    assert ukrainian_text == 'Ukrayins’ka mova!'


@pytest.fixture
@mimesis.decorators.romanize('kk')
def kazakh_text():
    return 'Python - ең жақсы бағдарламалау тілі!'


def test_kazakh(kazakh_text):
    expected_result = 'Python - eñ zhaqsy bağdarlamalau tili!'
    assert kazakh_text == expected_result


def test_not_implemented_error():
    @mimesis.decorators.romanize('nil')
    def user():
        return 'Mimesis'

    with pytest.raises(KeyError):
        user()

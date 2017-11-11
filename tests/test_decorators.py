import pytest

import mimesis.decorators


# --- romanized() ---

@pytest.fixture
@mimesis.decorators.romanized('ru')
def russian_name():
    return 'Ликид Геимфари'


def test_russian(russian_name):
    assert russian_name == 'Likid Geimfari'


@pytest.fixture
@mimesis.decorators.romanized('ru')
def mixed_text():
    return 'Что-то там_4352-!@#$%^&*()_+?"<>"'


def test_russian_mixed_text(mixed_text):
    assert mixed_text == 'Chto-to tam_4352-!@#$%^&*()_+?"<>"'


@pytest.fixture
@mimesis.decorators.romanized('ru')
def russian_alphabet():
    return ' '.join('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                    'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')


def test_romanized_russian_alphabet(russian_alphabet):
    result = 'A B V G D E Yo Zh Z I Ye K L M N O P R S T U F Kh Ts ' \
             'Ch Sh Shch  Y  E Yu Ja a b v g d e yo zh z i ye k l m n' \
             ' o p r s t u f kh ts ch sh shch  y  e yu ja'

    assert russian_alphabet == result


@pytest.fixture
@mimesis.decorators.romanized('uk')
def ukrainian_text():
    return 'Українська мова!'


def test_ukrainian(ukrainian_text):
    assert ukrainian_text == 'Ukrayins’ka mova!'


@pytest.fixture
@mimesis.decorators.romanized('kk')
def kazakh_text():
    return 'Python - ең жақсы бағдарламалау тілі!'


def test_kazakh(kazakh_text):
    expected_result = 'Python - eñ zhaqsy bağdarlamalau tili!'
    assert kazakh_text == expected_result


def test_not_implemented_error():
    @mimesis.decorators.romanized('nil')
    def user():
        return 'Mimesis'

    with pytest.raises(KeyError):
        user()


# --- type_to() ---

@mimesis.decorators.type_to(tuple)
def fixture_list():
    return ['this', 'is', 'a', 'list']


@mimesis.decorators.type_to(list)
def fixture_tuple():
    return 'this', 'is', 'a', 'list'


@mimesis.decorators.type_to(list, check_len=True)
def fixture_check_len():
    return ['one element']


@pytest.mark.parametrize(
    'fixture, fixture_type', [
        (fixture_list(), tuple),
        (fixture_tuple(), list),
    ],
)
def test_type_to(fixture, fixture_type):
    assert isinstance(fixture, fixture_type)
    # When we use check_len=True and length of returned object == 1,
    # decorator just returns first element.
    assert isinstance(fixture_check_len(), str)

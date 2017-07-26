import pytest

import mimesis.decorators


@mimesis.decorators.romanized('ru')
def russian_user():
    return 'Ликид Геимфари'


@mimesis.decorators.romanized('ru')
def russian_mixed_text():
    return 'Что-то там_4352-!@#$%^&*()_+?"<>"'


@mimesis.decorators.romanized('uk')
def ukrainian_text():
    return 'Українська мова!'


def test_russian():
    assert 'Likid Geimfari' == russian_user()


def test_russian_mixed_text():
    assert 'Chto-to tam_4352-!@#$%^&*()_+?"<>"' == russian_mixed_text()


def test_ukrainian():
    assert 'Ukrayins’ka mova!' == ukrainian_text()


def test_not_implemented_error():
    @mimesis.decorators.romanized('nil')
    def user():
        return 'Mimesis'

    with pytest.raises(KeyError):
        user()


def test_type_to():
    @mimesis.decorators.type_to(tuple)
    def fixture_list():
        return ['this', 'is', 'a', 'list']

    @mimesis.decorators.type_to(list)
    def fixture_tuple():
        return ['this', 'is', 'a', 'list']

    assert isinstance(fixture_list(), tuple)
    assert isinstance(fixture_tuple(), list)

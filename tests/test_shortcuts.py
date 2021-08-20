# -*- coding: utf-8 -*-

import pytest
from mimesis import shortcuts
from mimesis.exceptions import LocaleError
from mimesis.locales import Locale


@pytest.mark.parametrize(
    "number, check_sum",
    [
        ("5563455651", "2"),
        ("7992739871", "3"),
        ("5161675549", "5"),
    ],
)
def test_luhn_checksum(number, check_sum):
    assert shortcuts.luhn_checksum(number) == check_sum


def test_russian_to_roma():
    assert shortcuts.romanize("Ликид Геимфари", locale=Locale.RU) == "Likid Geimfari"


def test_russian_mixed_text():
    assert (
        shortcuts.romanize("Что-то там_4352-!@", locale=Locale.RU)
        == "Chto-to tam_4352-!@"
    )


def test_romanize_russian_alphabet():
    result = (
        "A B V G D E Yo Zh Z I Ye K L M N O P R S T U F Kh Ts "
        "Ch Sh Shch  Y  E Yu Ja a b v g d e yo zh z i ye k l m n"
        " o p r s t u f kh ts ch sh shch  y  e yu ja"
    )

    russian_alphabet = " ".join(
        "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    )

    assert shortcuts.romanize(russian_alphabet, locale=Locale.RU) == result


def test_ukrainian():
    assert (
        shortcuts.romanize("Українська мова!", locale=Locale.UK) == "Ukrayins’ka mova!"
    )


def test_kazakh():
    expected_result = "Python - eñ zhaqsy bağdarlamalau tili!"
    assert (
        shortcuts.romanize("Python - ең жақсы бағдарламалау тілі!", locale=Locale.KK)
        == expected_result
    )


def test_not_implemented_error():
    with pytest.raises(LocaleError):
        shortcuts.romanize("Mimesis", locale="sdsdsd")


# TODO: Fix me
def test_error():
    assert shortcuts.romanize("Mimesis", locale=Locale.DE)

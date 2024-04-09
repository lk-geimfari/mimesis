import pytest

from mimesis.exceptions import LocaleError
from mimesis.keys import maybe, romanize
from mimesis.locales import Locale
from mimesis.random import random

ROMANIZE_INPUT_PARAMETERS = [
    (Locale.RU, "Ликид Геимфари", "Likid Geimfari"),
    (Locale.RU, "Что-то там_4352-!@", "Chto-to tam_4352-!@"),
    (
        Locale.RU,
        " ".join("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
        (
            "A B V G D E Yo Zh Z I Ye K L M N O P R S T U F Kh Ts "
            "Ch Sh Shch  Y  E Yu Ja a b v g d e yo zh z i ye k l m n"
            " o p r s t u f kh ts ch sh shch  y  e yu ja"
        ),
    ),
    (Locale.UK, "Українська мова!", "Ukrayins’ka mova!"),
    (Locale.UK, "Щось там_4352-!@", "Shchos’ tam_4352-!@"),
    (
        Locale.KK,
        "Python - ең жақсы бағдарламалау тілі!",
        "Python - eñ zhaqsy bağdarlamalau tili!",
    ),
]


def test_maybe():
    key = maybe(None, probability=1)
    assert key("foo", random) is None

    key = maybe(None, probability=0.0)
    assert key("foo", random) is not None


@pytest.mark.parametrize(
    "locale, string, expected",
    ROMANIZE_INPUT_PARAMETERS,
)
def test_romanize_cyrillic_string(locale, string, expected):
    assert romanize(locale)(string) == expected


def test_romanize_invalid_locale():
    with pytest.raises(LocaleError):
        romanize(locale="sindarin")  # type: ignore


def test_romanize_unsupported_locale():
    with pytest.raises(ValueError):
        romanize(locale=Locale.DE)


def test_romanize_missing_positional_arguments():
    with pytest.raises(TypeError):
        romanize()  # type: ignore

    with pytest.raises(TypeError):
        romanize(locale=Locale.RU)()  # type: ignore

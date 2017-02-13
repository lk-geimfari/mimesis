import pytest
from elizabeth.decorators import romanized_russian


@romanized_russian
def russian_user():
    return 'Ликид Геимфари'


def test_romanize():
    user = russian_user()
    assert user == 'Likid Geimfari'

    username = russian_user()
    username = username.replace(' ', '_').lower()
    assert username == 'likid_geimfari'

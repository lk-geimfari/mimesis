from elizabeth.decorators import romanized_russian


@romanized_russian
def russian_user():
    return 'Ликид Геимфари'


def test_romanize():
    assert 'Likid Geimfari' == russian_user()

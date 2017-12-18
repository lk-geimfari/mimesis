import pytest

from mimesis import Games
from mimesis.data import GAMES, GAMING_PLATFORMS, GENRES, SCORE_PHRASES


@pytest.fixture
def games():
    return Games()


def test_gaming_platform(games):
    platform = games.gaming_platform()
    assert platform in GAMING_PLATFORMS


def test_score(games):
    result = games.score(minimum=5.5, maximum=10)
    assert isinstance(result, float)
    assert (result >= 5.5) and (result <= 10)


def test_pegi_rating(games):
    result = games.pegi_rating().split(' ')[1]
    standard = [3, 7, 12, 16, 18]

    assert int(result) in standard

    result = games.pegi_rating(pt=True).split(' ')[1]
    assert int(result) <= 18


def test_genre(games):
    result = games.genre()
    assert result in GENRES


def test_score_phrase(games):
    result = games.score_phrase()
    assert result in SCORE_PHRASES


def test_game(games):
    result = games.game()
    assert result in GAMES

import pytest

from mimesis import Games
from mimesis.data import GAMES, GAMING_PLATFORMS, GENRES, SCORE_PHRASES


@pytest.fixture
def games():
    return Games()


@pytest.fixture
def _seeded_games():
    return Games(seed=42)


def test_gaming_platform(games):
    platform = games.gaming_platform()
    assert platform in GAMING_PLATFORMS


def test_seeded_gaming_platform(_seeded_games):
    result = _seeded_games.gaming_platform()
    assert result == 'Xbox One X'
    result = _seeded_games.gaming_platform()
    assert result == 'Nintendo Switch'


def test_score(games):
    result = games.score(minimum=5.5, maximum=10)
    assert isinstance(result, float)
    assert (result >= 5.5) and (result <= 10)


def test_seeded_score(_seeded_games):
    result = _seeded_games.score(minimum=5.5, maximum=10)
    assert result == 9.5
    result = _seeded_games.score()
    assert result == 2.4
    result = _seeded_games.score()
    assert result == 1.3


def test_pegi_rating(games):
    result = games.pegi_rating().split(' ')[1]
    standard = [3, 7, 12, 16, 18]

    assert int(result) in standard

    result = games.pegi_rating(pt=True).split(' ')[1]
    assert int(result) <= 18


def test_seeded_pegi_rating(_seeded_games):
    result = _seeded_games.pegi_rating(pt=True)
    assert result == 'PEGI 4'
    result = _seeded_games.pegi_rating()
    assert result == 'PEGI 3'
    result = _seeded_games.pegi_rating()
    assert result == 'PEGI 12'


def test_genre(games):
    result = games.genre()
    assert result in GENRES


def test_seeded_genre(_seeded_games):
    result = _seeded_games.genre()
    assert result == 'Adventure, RPG'
    result = _seeded_games.genre()
    assert result == 'Action, Platformer'


def test_score_phrase(games):
    result = games.score_phrase()
    assert result in SCORE_PHRASES


def test_seeded_score_phrase(_seeded_games):
    result = _seeded_games.score_phrase()
    assert result == 'Unbearable'
    result = _seeded_games.score_phrase()
    assert result == 'Awful'


def test_game(games):
    result = games.game()
    assert result in GAMES


def test_seeded_game(_seeded_games):
    result = _seeded_games.game()
    assert result == 'Dead Space Extraction'
    result = _seeded_games.game()
    assert result == 'Apotheon'

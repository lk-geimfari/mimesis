import pytest

from elizabeth.data.int import *


def test_gaming_platform(games):
    platform = games.gaming_platform()
    assert platform in GAMING_PLATFORMS


def test_score(games):
    score = games.score(minimum=5.5, maximum=10)
    assert isinstance(score, float)
    assert (score >= 5.5) and (score <= 10)


def test_pegi_rating(games):
    rating = games.pegi_rating().split(' ')[1]
    standard = [3, 7, 12, 16, 18]

    assert int(rating) in standard

    rating_pt = games.pegi_rating(pt=True).split(' ')[1]
    standard[0], standard[1] = 4, 6

    assert int(rating_pt) in standard


def test_genre(games):
    genre = games.genre()
    assert genre in GENRES


def test_score_phrase(games):
    phrase = games.score_phrase()
    assert phrase in SCORE_PHRASES


def test_game(games):
    assert games.game() in GAMES

import pytest

from mimesis import Games
from mimesis.data import GAMES, GAMING_PLATFORMS, GENRES, SCORE_PHRASES


class TestGames(object):
    @pytest.fixture
    def games(self):
        return Games()

    def test_gaming_platform(self, games):
        platform = games.gaming_platform()
        assert platform in GAMING_PLATFORMS

    def test_score(self, games):
        result = games.score(minimum=5.5, maximum=10)
        assert isinstance(result, float)
        assert (result >= 5.5) and (result <= 10)

    def test_pegi_rating(self, games):
        result = games.pegi_rating().split(' ')[1]
        standard = [3, 7, 12, 16, 18]
        assert int(result) in standard

    def test_genre(self, games):
        result = games.genre()
        assert result in GENRES

    def test_score_phrase(self, games):
        result = games.score_phrase()
        assert result in SCORE_PHRASES

    def test_game(self, games):
        result = games.game()
        assert result in GAMES


class TestSeededGames(object):
    TIMES = 5

    @pytest.fixture
    def _gameses(self, seed):
        return Games(seed=seed), Games(seed=seed)

    def test_gaming_platform(self, _gameses):
        g1, g2 = _gameses
        for _ in range(self.TIMES):
            assert g1.gaming_platform() == g2.gaming_platform()

    def test_score(self, _gameses):
        g1, g2 = _gameses
        for _ in range(self.TIMES):
            assert g1.score() == g2.score()

    def test_pegi_rating(self, _gameses):
        g1, g2 = _gameses
        for _ in range(self.TIMES):
            assert g1.pegi_rating() == g2.pegi_rating()

    def test_genre(self, _gameses):
        g1, g2 = _gameses
        for _ in range(self.TIMES):
            assert g1.genre() == g2.genre()

    def test_score_phrase(self, _gameses):
        g1, g2 = _gameses
        for _ in range(self.TIMES):
            assert g1.score_phrase() == g2.score_phrase()

    def test_game(self, _gameses):
        g1, g2 = _gameses
        for _ in range(self.TIMES):
            assert g1.game() == g2.game()

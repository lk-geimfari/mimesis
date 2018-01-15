"""Provides data related to gaming and games."""

from mimesis.data import GAMES, GAMING_PLATFORMS, GENRES, SCORE_PHRASES
from mimesis.providers.base import BaseDataProvider

__all__ = ['Games']


class Games(BaseDataProvider):
    """Class for generating data related to the games."""

    def gaming_platform(self) -> str:
        """Get random gaming platform.

        :return: Gaming platform

        :Example:
            PlayStation 4 Pro
        """
        return self.random.choice(GAMING_PLATFORMS)

    def score(self, minimum: int = 1, maximum: int = 10) -> float:
        """Score of game.

        :param minimum: Maximum value.
        :param maximum: Minimum value.
        :return: Score.
        """
        return self.random.randint(minimum * 10, maximum * 10) / 10

    def pegi_rating(self) -> str:
        """Get a random PEGI rating.

        :return: PEGI rating.

        :Example:
            PEGI 18
        """
        standard = [3, 7, 12, 16, 18]
        digit = self.random.choice(standard)
        return '{0} {1}'.format('PEGI', digit)

    def genre(self) -> str:
        """Get a random genre of game.

        :return: Genre.

        :Example:
            Shooter
        """
        return self.random.choice(GENRES)

    def score_phrase(self) -> str:
        """Get a random score phrase.

        :return: Score phrase.

        :Example:
            Great
        """
        return self.random.choice(SCORE_PHRASES)

    def game(self) -> str:
        """Get a random game from list of games.

        :return: Name of the game.

        :Example:
            Battlefield 1
        """
        return self.random.choice(GAMES)

from mimesis.data import GAMES, GAMING_PLATFORMS, GENRES, SCORE_PHRASES
from mimesis.providers import BaseProvider

__all__ = ['Games']


class Games(BaseProvider):
    def gaming_platform(self):
        """Get random gaming platform.

        :return: Gaming platform
        :Example:
            PlayStation 4 Pro
        """
        return self.random.choice(GAMING_PLATFORMS)

    def score(self, minimum=1, maximum=10):
        return self.random.randint(minimum * 10, maximum * 10) / 10

    def pegi_rating(self, pt=False):
        """Get a random PEGI rating.

        :param pt: PEGI rating for Portugal.
        :return: PEGI rating.
        :Example:
            PEGI 18
        """
        standard = [3, 7, 12, 16, 18]

        # In Portugal, two of the PEGI categories were aligned with the age
        # ratings of the film classification system to avoid confusion;
        # 3 was changed to 4 and 7 was changed to 6.
        if pt:
            standard[0] = 4
            standard[1] = 6

        return '{0} {1}'.format('PEGI',
                                self.random.choice(standard))

    def genre(self):
        """Get a random genre of game.

        :return: Genre.
        :Example:
            Shooter
        """
        return self.random.choice(GENRES)

    def score_phrase(self):
        """Get a random score phrase.

        :return: Score phrase.
        :Example:
            Great
        """
        return self.random.choice(SCORE_PHRASES)

    def game(self):
        """Get a random game from list of games.

        :return: Name of the game.
        :Example:
            Battlefield 1
        """
        return self.random.choice(GAMES)

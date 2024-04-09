"""Provides data related to text."""
import typing as t

from mimesis.datasets import SAFE_COLORS
from mimesis.enums import EmojyCategory
from mimesis.providers.base import BaseDataProvider

__all__ = ["Text"]


class Text(BaseDataProvider):
    """Class for generating text data."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes."""
        super().__init__(*args, **kwargs)
        self._emojis = self._read_global_file("emojis.json")

    class Meta:
        name = "text"
        datafile = f"{name}.json"

    def alphabet(self, lower_case: bool = False) -> list[str]:
        """Returns an alphabet for current locale.

        :param lower_case: Return alphabet in lower case.
        :return: Alphabet.
        """
        case = "uppercase" if not lower_case else "lowercase"

        alpha: list[str] = self._extract(["alphabet", case])
        return alpha

    def level(self) -> str:
        """Generates a word that indicates a level of something.

        :return: Level.

        :Example:
            critical.
        """
        levels: list[str] = self._extract(["level"])
        return self.random.choice(levels)

    def text(self, quantity: int = 5) -> str:
        """Generates the text.

        :param quantity: Quantity of sentences.
        :return: Text.
        """
        text = self._extract(["text"])
        return " ".join(self.random.choices(text, k=quantity))

    def sentence(self) -> str:
        """Generates a random sentence from the text.

        :return: Sentence.
        """
        return self.text(quantity=1)

    def title(self) -> str:
        """Generates a random title.

        :return: The title.
        """
        return self.text(quantity=1)

    def words(self, quantity: int = 5) -> list[str]:
        """Generates a list of random words.

        :param quantity: Quantity of words. Default is 5.
        :return: Word list.

        :Example:
            [science, network, god, octopus, love]
        """
        words = self._extract(["words"])
        return self.random.choices(words, k=quantity)

    def word(self) -> str:
        """Generates a random word.

        :return: Single word.

        :Example:
            Science.
        """
        return self.words(quantity=1)[0]

    def quote(self) -> str:
        """Generates a random quote.

        :return: Random quote.

        :Example:
            "Bond... James Bond."
        """
        quotes: list[str] = self._extract(["quotes"])
        return self.random.choice(quotes)

    def color(self) -> str:
        """Generates a random color name.

        :return: Color name.

        :Example:
            Red.
        """
        colors: list[str] = self._extract(["color"])
        return self.random.choice(colors)

    @staticmethod
    def _hex_to_rgb(color: str) -> tuple[int, ...]:
        """Converts hex color to RGB format.

        :param color: Hex color.
        :return: RGB tuple.
        """
        color = color.lstrip("#") if color.startswith("#") else color
        return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))

    def hex_color(self, safe: bool = False) -> str:
        """Generates a random HEX color.

        :param safe: Get safe Flat UI hex color.
        :return: Hex color code.

        :Example:
            #d8346b
        """
        if safe:
            return self.random.choice(SAFE_COLORS)

        return f"#{self.random.randint(0x000000, 0xFFFFFF):06x}"

    def rgb_color(self, safe: bool = False) -> tuple[int, ...]:
        """Generates a random RGB color tuple.

        :param safe: Get safe RGB tuple.
        :return: RGB tuple.

        :Example:
            (252, 85, 32)
        """
        color = self.hex_color(safe)
        return self._hex_to_rgb(color)

    def answer(self) -> str:
        """Generates a random answer in the current language.

        :return: An answer.

        :Example:
            No
        """
        answers: list[str] = self._extract(["answers"])
        return self.random.choice(answers)

    def emoji(self, category: EmojyCategory | None = EmojyCategory.DEFAULT) -> str:
        """Generates a random emoji from the specified category.

        Generates a random emoji from the specified category.
        If the category is not specified, a random emoji
        from any category will be returned.

        :param category: :class:`~mimesis.enums.EmojyCategory`.
        :raises NonEnumerableError: When category is not supported.
        :return: Emoji code.
        :example:
            😟
        """
        category = self.validate_enum(category, EmojyCategory)
        symbol = self.random.choice(self._emojis[category])

        base = 16
        # Some emoji consist of multiple Unicode characters.
        if isinstance(symbol, list):
            return "".join([chr(int(s, base)) for s in symbol])
        return chr(int(symbol, base))

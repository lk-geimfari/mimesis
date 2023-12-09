"""Provides data related to food."""
import typing as t

from mimesis.providers.base import BaseDataProvider

__all__ = ["Food"]


class Food(BaseDataProvider):
    """Class for generating data related to food."""

    class Meta:
        name = "food"
        datafile = f"{name}.json"

    def _choice_from(self, key: str) -> str:
        """Choice random element."""
        data: t.List[str] = self.extract([key])
        return self.random.choice(data)

    def vegetable(self) -> str:
        """Get a random vegetable.

        :return: Vegetable name.

        :Example:
            Tomato.
        """
        return self._choice_from("vegetables")

    def fruit(self) -> str:
        """Get a random fruit or berry.

        :return: Fruit name.

        :Example:
            Banana.
        """
        return self._choice_from("fruits")

    def dish(self) -> str:
        """Get a random dish.

        :return: Dish name.

        :Example:
            Ratatouille.
        """
        return self._choice_from("dishes")

    def spices(self) -> str:
        """Get a random spices or herbs.

        :return: The name of the spices or herbs.

        :Example:
            Anise.
        """
        return self._choice_from("spices")

    def drink(self) -> str:
        """Get a random drink.

        :return: The name of the alcoholic beverage.

        :Example:
            Vodka.
        """
        return self._choice_from("drinks")

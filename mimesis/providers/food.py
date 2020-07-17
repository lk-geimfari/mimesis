# -*- coding: utf-8 -*-

"""Provides data related to food."""

from mimesis.providers.base import BaseDataProvider

__all__ = ['Food']


class Food(BaseDataProvider):
    """Class for generating data related to food."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self._datafile = 'food.json'
        self._pull(self._datafile)

    class Meta:
        """Class for metadata."""

        name = 'food'

    def _choice_from(self, key: str) -> str:
        """Choice random element."""
        data = self._data[key]
        return self.random.choice(data)

    def vegetable(self) -> str:
        """Get a random vegetable.

        :return: Vegetable name.

        :Example:
            Tomato.
        """
        return self._choice_from('vegetables')

    def fruit(self) -> str:
        """Get a random fruit or berry.

        :return: Fruit name.

        :Example:
            Banana.
        """
        return self._choice_from('fruits')

    def dish(self) -> str:
        """Get a random dish.

        :return: Dish name.

        :Example:
            Ratatouille.
        """
        return self._choice_from('dishes')

    def spices(self) -> str:
        """Get a random spices or herbs.

        :return: Spices or herbs.

        :Example:
            Anise.
        """
        return self._choice_from('spices')

    def drink(self) -> str:
        """Get a random drink.

        :return: Alcoholic drink.

        :Example:
            Vodka.
        """
        return self._choice_from('drinks')

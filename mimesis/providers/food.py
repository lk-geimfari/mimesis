from mimesis.providers.base import BaseDataProvider
from mimesis.utils import pull


class Food(BaseDataProvider):
    """Class for Food, i.e fruits, vegetables, berries and other."""

    def __init__(self, *args, **kwargs):
        """
        :param str locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self._data = pull('food.json', self.locale)

    def _choice_from(self, key: str) -> str:
        """Choice random element from self._data[key].
        """
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
        """Get a random name of fruit or berry .

        :return: Fruit name.

        :Example:
            Banana.
        """
        return self._choice_from('fruits')

    def dish(self) -> str:
        """Get a random dish for current locale.

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

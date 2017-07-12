from mimesis.providers import BaseProvider
from mimesis.utils import pull


class Food(BaseProvider):
    """Class for Food, i.e fruits, vegetables, berries and other."""

    def __init__(self, *args, **kwargs):
        """
        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self._data = pull('food.json', self.locale)

    def vegetable(self):
        """Get a random vegetable.

        :return: Vegetable.
        :Example:
            Tomato.
        """
        vegetables = self._data['vegetables']
        return self.random.choice(vegetables)

    def fruit(self):
        """Get a random name of fruit or berry .

        :return: Fruit.
        :Example:
            Banana.
        """
        fruits = self._data['fruits']
        return self.random.choice(fruits)

    def dish(self):
        """Get a random dish for current locale.

        :return: Dish name.
        :Example:
            Ratatouille.
        """
        dishes = self._data['dishes']
        return self.random.choice(dishes)

    def spices(self):
        """Get a random spices or herbs.

        :return: Spices or herbs.
        :Example:
            Anise.
        """
        spices = self._data['spices']
        return self.random.choice(spices)

    def drink(self):
        """Get a random drink.

        :return: Alcoholic drink.
        :Example:
            Vodka.
        """
        drinks = self._data['drinks']
        return self.random.choice(drinks)

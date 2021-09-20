# -*- coding: utf-8 -*-

"""Implements classes for generating data by schema."""
from typing import Any, Callable, Iterator, List, Optional, Sequence

from mimesis.exceptions import FieldError, SchemaError
from mimesis.locales import Locale
from mimesis.providers.generic import Generic
from mimesis.typing import JSON, Seed

__all__ = ["BaseField", "Field", "Schema"]


class BaseField:
    """
    BaseField is a class for generating data by the name of the method.

    Instance of this object takes any string which represents the name
    of any method of any supported data provider (:class:`~mimesis.Generic`)
    and the ``**kwargs`` of the method.

    See :class:`~mimesis.schema.BaseField.perform` for more details.
    """

    class Meta:
        base = True

    def __init__(
        self,
        locale: Locale = Locale.DEFAULT,
        seed: Optional[Seed] = None,
        providers: Optional[Sequence[Any]] = None,
    ) -> None:
        """Initialize field.

        :param locale: Locale
        :param seed: Seed for random.
        """
        self._gen = Generic(locale, seed)

        if providers:
            self._gen.add_providers(*providers)

        self._table = {}  # type: ignore

    def perform(
        self,
        name: Optional[str] = None,
        key: Optional[Callable[[Any], Any]] = None,
        **kwargs: Any
    ) -> Any:
        """Performs the value of the field by its name.

        It takes any string which represents the name of any method of
        any supported data provider and the ``**kwargs`` of this method.

        .. note:: Some data providers have methods with the same names
            and in such cases, you can explicitly define that the method
            belongs to data-provider ``name='provider.name'`` otherwise
            it will return the data from the first provider which
            has a method ``name``.

        You can apply a *key function* to the result returned by
        the method, bt passing a parameter **key** with a callable
        object which returns the final result.

        :param name: Name of the method.
        :param key: A key function (or any other callable object)
            which will be applied to result.
        :param kwargs: Kwargs of method.
        :return: Value which represented by method.
        :raises ValueError: if provider not
            supported or if field not defined.
        """
        if name is None:
            raise FieldError()

        def tail_parser(tails: str, obj: Any) -> Any:
            """Return method from end of tail.

            :param tails: Tail string
            :param obj: Search tail from this object
            :return last tailed method
            """
            provider_name, method_name = tails.split(".", 1)

            if "." in method_name:
                raise FieldError(name)

            attr = getattr(obj, provider_name)
            if attr is not None:
                try:
                    return getattr(attr, method_name)
                except AttributeError:
                    raise FieldError(name)

        try:
            if name not in self._table:
                if "." not in name:
                    # Fix https://github.com/lk-geimfari/mimesis/issues/619
                    if name == self._gen.choice.Meta.name:
                        self._table[name] = self._gen.choice
                    else:
                        for provider in dir(self._gen):
                            provider = getattr(self._gen, provider)
                            if name in dir(provider):
                                self._table[name] = getattr(provider, name)
                else:
                    self._table[name] = tail_parser(name, self._gen)

            result = self._table[name](**kwargs)
            if key and callable(key):
                return key(result)
            return result
        except KeyError:
            raise FieldError(name)

    def __str__(self) -> str:
        return "{} <{}>".format(self.__class__.__name__, self._gen.locale)


class Field(BaseField):
    """Greedy field.

    The field whcih evaluates immediately.

    Example:
        >>> _ = Field()
        >>> _('username')
        Dogtag_1836
    """

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.perform(*args, **kwargs)


class Schema:
    """Class which return list of filled schemas."""

    def __init__(self, schema: Callable[[], JSON]) -> None:
        """Initialize schema.

        :param schema: A schema (must be a callable object).
        """
        if schema and callable(schema):
            self.schema = schema
        else:
            raise SchemaError()

    def create(self, iterations: int = 1) -> List[JSON]:
        """Creates a list of a fulfilled schemas.

        .. note::
            This method evaluates immediately, so be careful on creating
            large datasets otherwise you're risking running out of memory.

            If you need a lazy version of this method, see
            :meth:`iterator`

        :param iterations: Number of iterations.
        :return: List of fulfilled schemas.
        """

        if iterations < 1:
            raise ValueError("The number of iterations must be greater than 0.")

        return [self.schema() for _ in range(iterations)]

    def iterator(self, iterations: int = 1) -> Iterator[JSON]:
        """Fulfills schema in a lazy way.

        :param iterations: Number of iterations.
        :return: List of fulfilled schemas.
        """

        if iterations < 1:
            raise ValueError("The number of iterations must be greater than 0.")

        for item in range(iterations):
            yield self.schema()

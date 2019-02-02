# -*- coding: utf-8 -*-

"""Implements classes for generating data by schema."""

from types import LambdaType
from typing import Any, Callable, List, Optional

from mimesis.exceptions import (
    UnacceptableField,
    UndefinedField,
    UndefinedSchema,
    UnsupportedField,
)
from mimesis.providers.generic import Generic
from mimesis.typing import JSON, Seed

__all__ = ['AbstractField', 'Field', 'Schema']


class AbstractField(object):
    """
    AbstractField is a class for generating data by the name of the method.

    Instance of this object takes any string which represents name
    of any method of any supported data provider (:class:`~mimesis.Generic`)
    and the ``**kwargs`` of the method:

    >>> _ = AbstractField('en', 0xf)
    >>> surname = _('surname')
    >>> isinstance(surname, str)
    True
    """

    def __init__(self, locale: str = 'en',
                 seed: Optional[Seed] = None,
                 providers: Optional[Any] = None) -> None:
        """Initialize field.

        :param locale: Locale
        :param seed: Seed for random.
        """
        self.locale = locale
        self.seed = seed
        self._gen = Generic(self.locale, self.seed)

        if providers:
            self._gen.add_providers(*providers)

        self._table = {}  # type: ignore

    def __call__(self, name: Optional[str] = None,
                 key: Optional[Callable] = None, **kwargs) -> Any:
        """Override standard call.

        This magic method override standard call so it's take any string which
        represents name of the any method of any supported data provider
        and the ``**kwargs`` of this method.

        ..note:: Some data providers have methods with the same name and
        in such cases, you can explicitly define that the method belongs to
        data-provider ``name='provider.name'``.

        You can apply a *key function* to result returned by the method,
        to do it, just pass parameter **key** with a callable object which
        returns final result.

        :param name: Name of the method.
        :param key: A key function (or other callable object)
            which will be applied to result.
        :param kwargs: Kwargs of method.
        :return: Value which represented by method.
        :raises ValueError: if provider is not
            supported or if field is not defined.
        """
        if name is None:
            raise UndefinedField()

        def tail_parser(tails: str, obj: Any) -> Any:
            """Return method from end of tail.

            :param tails: Tail string
            :param obj: Search tail from this object
            :return last tailed method
            """
            provider_name, method_name = tails.split('.', 1)

            if '.' in method_name:
                raise UnacceptableField()

            attr = getattr(obj, provider_name)
            if attr is not None:
                return getattr(attr, method_name)

        try:
            if name not in self._table:
                if '.' not in name:
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
            raise UnsupportedField(name)

    def __str__(self):
        return '{} <{}>'.format(
            self.__class__.__name__, self.locale)


class Schema(object):
    """Class which return list of filled schemas."""

    def __init__(self, schema: LambdaType) -> None:
        """Initialize schema.

        :param schema: A schema.
        """
        if isinstance(schema, LambdaType):
            self.schema = schema
        else:
            raise UndefinedSchema()

    def create(self, iterations: int = 1) -> List[JSON]:
        """Return filled schema.

        Create a list of a filled schemas with elements in
        an amount of **iterations**.

        :param iterations: Amount of iterations.
        :return: List of willed schemas.
        """
        return [self.schema() for _ in range(iterations)]


# Alias for AbstractField
Field = AbstractField

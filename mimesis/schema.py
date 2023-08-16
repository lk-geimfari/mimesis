"""Implements classes for generating data by schema."""

import csv
import json
import pickle
import re
import typing as t

from mimesis.exceptions import FieldError, FieldsetError, SchemaError
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider
from mimesis.random import Random
from mimesis.providers.generic import Generic
from mimesis.types import (
    JSON,
    CallableSchema,
    FieldCache,
    Key,
    MissingSeed,
    Seed,
)

__all__ = ["BaseField", "Field", "Fieldset", "Schema"]

RegisterableFieldHandler = t.Callable[[Random, t.Any], t.Any]
RegisterableField = t.Tuple[str, RegisterableFieldHandler]
RegisterableFields = t.Sequence[RegisterableField]


class BaseField:
    def __init__(
        self,
        locale: Locale = Locale.DEFAULT,
        seed: Seed = MissingSeed,
        providers: t.Optional[t.Sequence[t.Any]] = None,
    ) -> None:
        """Initialize field.

        :param locale: Locale
        :param seed: Seed for random.
        """
        self._gen = Generic(locale, seed)

        if providers:
            self._gen.add_providers(*providers)

        self._cache: FieldCache = {}
        self._custom_fields: t.Dict[str, t.Callable[[Random, t.Any], t.Any]] = {}

    def reseed(self, seed: Seed = MissingSeed) -> None:
        """Reseed the random generator.

        :param seed: Seed for random.
        """
        self._gen.reseed(seed)

    def get_random_instance(self) -> Random:
        """Get random object from Generic.

        :return: Random object.
        """
        return self._gen.random

    def _explicit_lookup(self, name: str) -> t.Any:
        """An explicit method lookup.

        This method is called when the field
        defined explicitly, like this: ``provider.method``

        :param name: The field name.
        :return: Callable object.
        :raise FieldError: When field is invalid.
        """
        provider_name, method_name = name.split(".", 1)
        try:
            provider = getattr(self._gen, provider_name)
            return getattr(provider, method_name)
        except AttributeError:
            raise FieldError(name)

    def _fuzzy_lookup(self, name: str) -> t.Any:
        """A fuzzy method lookup.

        This method is called when the field definition
        is fuzzy, like this: ``method``

        :param name: The field name.
        :return: Callable object.
        :raise FieldError: When field is invalid.
        """
        for provider in dir(self._gen):
            provider = getattr(self._gen, provider)
            if isinstance(provider, BaseProvider):
                if name in dir(provider):
                    return getattr(provider, name)

        raise FieldError(name)

    def _lookup_method(self, name: str) -> t.Any:
        """Lookup method by the field name.

        :param name: The field name.
        :return: Callable object.
        :raise FieldError: When field is invalid.
        """
        # Support additional delimiters
        name = re.sub(r"[/:\s]", ".", name)

        if name.count(".") > 1:
            raise FieldError(name)

        if name not in self._cache:
            if "." not in name:
                method = self._fuzzy_lookup(name)
            else:
                method = self._explicit_lookup(name)
            self._cache[name] = method

        return self._cache[name]

    def perform(
        self,
        name: t.Optional[str] = None,
        key: Key = None,
        **kwargs: t.Any,
    ) -> t.Any:
        """Performs the value of the field by its name.

        It takes any string which represents the name of any method of
        any supported data provider and the ``**kwargs`` of this method.

        .. note:: Some data providers have methods with the same names
            and in such cases, you can explicitly define that the method
            belongs to data-provider ``name='provider.name'`` otherwise
            it will return the data from the first provider which
            has a method ``name``.

            Allowed delimiters: ``.``, ``:``, ``/`` and space:

            - ``provider.name``
            - ``provider:name``
            - ``provider/name``
            - ``provider name``

        You can apply a *key function* to the result returned by
        the method, by passing a parameter **key** with a callable
        object which returns the final result.

        The key function has the option to accept two parameters: **result**
        and **random**. In case you require access to a random instance within
        the key function, you must modify the function to accept both of them,
        where the first corresponds to the method result and the second
        corresponds to the instance of random.

        :param name: Name of the method.
        :param key: A key function (any callable object)
            which will be applied to result.
        :param kwargs: Kwargs of method.
        :return: Value which represented by method.
        :raises ValueError: if provider not supported or if field not defined.
        """
        if name is None:
            raise FieldError()

        random = self.get_random_instance()

        if name in self._custom_fields:
            result = self._custom_fields[name](random, **kwargs)
        else:
            result = self._lookup_method(name)(**kwargs)

        if key and callable(key):
            try:
                # If key function accepts two parameters
                # then pass random instance to it.
                return key(result, random)  # type: ignore
            except TypeError:
                return key(result)

        return result

    def __str__(self) -> str:
        return f"{self.__class__.__name__} <{self._gen.locale}>"

    def register_field(self, field_name: str, handler: RegisterableFieldHandler) -> None:
        """Register a new field handler.

        :param field_name: Name of the field.
        :param handler: Callable object.
        """

        if not callable(handler):
            raise TypeError(
                f"Handler must be a callable object, "
                f"but {handler.__class__.__name__} given."
            )

        if field_name not in self._custom_fields:
            self._custom_fields[field_name] = handler

    def register_fields(self, fields: RegisterableFields) -> None:
        """Register a new field handlers.

        :param fields: A sequence of tuples with field name and handler.
        :return: None.
        """
        for name, handler in fields:
            self.register_field(name, handler)

    def unregister_field(self, field_name: str) -> None:
        """Unregister a field handler.

        :param field_name: Name of the field.
        """
        if field_name in self._custom_fields:
            del self._custom_fields[field_name]

    def unregister_fields(self, field_names: t.Union[t.Sequence[str], ...]) -> None:
        """Unregister a field handlers with given names.

        Unregisters all custom fields if ``field_names`` is ``...`` (aka Ellipsis).

        :param field_names: Names of the fields.
        :return: None.
        """

        if field_names is ...:
            self._custom_fields.clear()
        else:
            for name in field_names:
                self.unregister_field(name)


class Field(BaseField):
    """Greedy field.

    The field whcih evaluates immediately.

    .. warning::

        There is no case when you need to instance **field** in loops.

        If you doing this:

        >>> for i in range(1000):
        ...     field = Field()

        You doing it **wrong**! It is a terrible idea that will lead to a memory leak.

        Forewarned is forearmed.

    Here is usage example:

        >>> _ = Field()
        >>> _('username')
        Dogtag_1836
    """

    def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
        return self.perform(*args, **kwargs)


class Fieldset(BaseField):
    """Greedy fieldset (evaluates immediately).

    Works like a field, but returns a list of values.

    Here is usage example:

        >>> fieldset = Fieldset(i=100)
        >>> fieldset('username')
        ['pot_1821', 'vhs_1915', ..., 'reviewed_1849']

    You may also specify the number of iterations by passing the **i** keyword
    argument to the callable instance of fieldset:

        >>> fieldset = Fieldset()
        >>> fieldset('username', i=2)
        ['pot_1821', 'vhs_1915']

    When **i** is not specified, the reasonable default is used — **10**.

    See "Field vs Fieldset" section of documentation for more details.

    :cvar fieldset_default_iterations: Default iterations. Default is **10**.
    :cvar fieldset_iterations_kwarg: Keyword argument for iterations. Default is **i**.
    """

    fieldset_default_iterations: int = 10
    fieldset_iterations_kwarg: str = "i"

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize fieldset.

        Accepts additional keyword argument **i** which is used
        to specify the number of iterations.

        The name of the keyword argument can be changed by
        overriding **fieldset_iterations_kwarg** attribute of this class.
        """
        self._iterations = kwargs.pop(
            self.fieldset_iterations_kwarg,
            self.fieldset_default_iterations,
        )
        super().__init__(*args, **kwargs)

    def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.List[t.Any]:
        """Perform fieldset.

        :param args: Arguments for field.
        :param kwargs: Keyword arguments for field.
        :raises FieldsetError: If iterations less than 1.
        :return: List of values.
        """
        min_iterations = 1
        iterations = kwargs.pop(
            self.fieldset_iterations_kwarg,
            self._iterations,
        )

        if iterations < min_iterations:
            raise FieldsetError()

        return [self.perform(*args, **kwargs) for _ in range(iterations)]


class Schema:
    """Class which return list of filled schemas."""

    __slots__ = (
        "_count",
        "_schema",
        "iterations",
        "_min_iterations",
    )

    def __init__(self, schema: CallableSchema, iterations: int = 10) -> None:
        """Initialize schema.

        :param iterations: Number of iterations.
            This parameter is keyword-only. The default value is 10.
        :param schema: A schema (must be a callable object).
        """
        if schema and callable(schema):  # type: ignore[truthy-function]
            self._schema = schema
            self._count = 0
            self._min_iterations = 1
            if iterations >= self._min_iterations:
                self.iterations = iterations
            else:
                raise ValueError(
                    f"Iterations must be greater than {self._min_iterations}"
                )
        else:
            # This is just a better error message
            raise SchemaError()

    def to_csv(self, file_path: str, **kwargs: t.Any) -> None:
        """Export a schema as a CSV file.

        :param file_path: File path.
        :param kwargs: The keyword arguments for :py:class:`csv.DictWriter` class.

        *New in version 5.3.0*
        """
        data = self.create()
        with open(file_path, "w", encoding="utf-8", newline="") as fp:
            fieldnames = list(data[0])
            dict_writer = csv.DictWriter(fp, fieldnames, **kwargs)
            dict_writer.writeheader()
            dict_writer.writerows(data)

    def to_json(self, file_path: str, **kwargs: t.Any) -> None:
        """Export a schema as a JSON file.

        :param file_path: File path.
        :param kwargs: Extra keyword arguments for :py:func:`json.dump` class.

        *New in version 5.3.0*
        """
        with open(file_path, "w", encoding="utf-8") as fp:
            json.dump(self.create(), fp, **kwargs)

    def to_pickle(self, file_path: str, **kwargs: t.Any) -> None:
        """Export a schema as the pickled representation of the object to the file.

        :param file_path: File path.
        :param kwargs: Extra keyword arguments for :py:func:`pickle.dump` class.

        *New in version 5.3.0*
        """
        with open(file_path, "wb") as fp:
            pickle.dump(self.create(), fp, **kwargs)

    def create(self) -> t.List[JSON]:
        """Creates a list of a fulfilled schemas.

        .. note::
            This method evaluates immediately, so be careful on creating
            large datasets otherwise you're risking running out of memory.

            If you need a lazy version of this method, see :meth:`iterator`.

        :return: List of fulfilled schemas.
        """
        return [self._schema() for _ in range(self.iterations)]

    def __next__(self) -> JSON:
        """Return the next item from the iterator."""
        if self._count < self.iterations:
            self._count += 1
            return self._schema()
        raise StopIteration

    def __iter__(self) -> "Schema":
        """Return the iterator object itself."""
        self._count = 0
        return self

"""Implements classes for generating data by schema."""

import csv
import inspect
import json
import pickle
import re
from typing import Any, Callable, Sequence

from mimesis.exceptions import (
    AliasesTypeError,
    FieldArityError,
    FieldError,
    FieldNameError,
    FieldsetError,
    SchemaError,
)
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider
from mimesis.providers.generic import Generic
from mimesis.random import Random
from mimesis.types import JSON, CallableSchema, Key, MissingSeed, Seed

__all__ = [
    "BaseField",
    "Field",
    "Fieldset",
    "Schema",
    "FieldHandler",
    "RegisterableFieldHandler",
    "RegisterableFieldHandlers",
]

FieldCache = dict[str, Callable[[Any], Any]]
FieldHandler = Callable[[Random, Any], Any]
RegisterableFieldHandler = tuple[str, FieldHandler]
RegisterableFieldHandlers = Sequence[RegisterableFieldHandler]


class BaseField:
    def __init__(
        self,
        locale: Locale = Locale.DEFAULT,
        seed: Seed = MissingSeed,
    ) -> None:
        """Base class for fields.

        This class is used as a base class for :class:`Field` and :class:`Fieldset`.

        :attr: aliases: A dictionary of aliases for standard fields.
        :param locale: Locale.
        :param seed: Seed for random.
        """
        self._generic = Generic(locale, seed)
        self._cache: FieldCache = {}
        self._handlers: dict[str, FieldHandler] = {}
        self.aliases: dict[str, str] = {}

    def reseed(self, seed: Seed = MissingSeed) -> None:
        """Reseed the random generator.

        :param seed: Seed for random.
        """
        self._generic.reseed(seed)

    def get_random_instance(self) -> Random:
        """Get a random object from Generic.

        :return: Random object.
        """
        return self._generic.random

    def _explicit_lookup(self, name: str) -> Any:
        """An explicit method lookup.

        This method is called when the field
        defined explicitly, like this: ``provider.method``

        :param name: The field name.
        :return: Callable object.
        :raise FieldError: When field is invalid.
        """
        provider_name, method_name = name.split(".", 1)
        try:
            provider = getattr(self._generic, provider_name)
            return getattr(provider, method_name)
        except AttributeError:
            raise FieldError(name)

    def _fuzzy_lookup(self, name: str) -> Any:
        """A fuzzy method lookup.

        This method is called when the field definition
        is fuzzy, like this: ``method``

        :param name: The field name.
        :return: Callable object.
        :raise FieldError: When field is invalid.
        """
        for provider in dir(self._generic):
            provider = getattr(self._generic, provider)
            if isinstance(provider, BaseProvider):
                if name in dir(provider):
                    return getattr(provider, name)

        raise FieldError(name)

    def _lookup_method(self, name: str) -> Any:
        """Lookup method by the field name.

        :param name: The field name.
        :return: Callable object.
        :raise FieldError: When field is invalid.
        """
        # Check if the field is defined in aliases
        name = self.aliases.get(name, name)

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

    def _validate_aliases(self) -> bool:
        """Validate aliases."""
        if not isinstance(self.aliases, dict) or any(
            not isinstance(key, str) or not isinstance(value, str)
            for key, value in self.aliases.items()
        ):
            # Reset to valid state
            self.aliases = {}
            raise AliasesTypeError()
        return True

    def perform(
        self,
        name: str | None = None,
        key: Key = None,
        **kwargs: Any,
    ) -> Any:
        """Performs the value of the field by its name.

        It takes any string that represents the name of any method of
        any supported data provider and the ``**kwargs`` of this method.

        .. note:: Some data providers have methods with the same names,
            and in such cases, you can explicitly define that the method
            belongs to data-provider ``field(name='provider.name')`` otherwise
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
        :return: The result of method.
        :raises ValueError: if provider is not supported or if field is not defined.
        """
        # Validate aliases before lookup
        self._validate_aliases()

        if name is None:
            raise FieldError()

        random = self.get_random_instance()

        # First, try to find a custom field handler.
        if name in self._handlers:
            result = self._handlers[name](random, **kwargs)  # type: ignore
        else:
            result = self._lookup_method(name)(**kwargs)

        if key and callable(key):
            try:
                # If a key function accepts two parameters
                # then pass random instance to it.
                return key(result, random)  # type: ignore
            except TypeError:
                return key(result)

        return result

    def register_handler(self, field_name: str, field_handler: FieldHandler) -> None:
        """Register a new field handler.

        :param field_name: Name of the field.
        :param field_handler: Callable object.
        """

        if not isinstance(field_name, str):
            raise TypeError("Field name must be a string.")

        if not field_name.isidentifier():
            raise FieldNameError(field_name)

        if not callable(field_handler):
            raise TypeError("Handler must be a callable object.")

        callable_signature = inspect.signature(field_handler)

        if len(callable_signature.parameters) <= 1:
            raise FieldArityError()

        if field_name not in self._handlers:
            self._handlers[field_name] = field_handler

    def handle(
        self, field_name: str | None = None
    ) -> Callable[[FieldHandler], FieldHandler]:
        """Decorator for registering a custom field handler.

        You can use this decorator only for functions,
        not for any other callables.

        .. versionadded:: 12.0.0

        :param field_name: Name of the field.
            If not specified, the name of the function is used.
        :return: Decorator.
        """

        def decorator(field_handler: FieldHandler) -> FieldHandler:
            _field_name = field_name or field_handler.__name__
            self.register_handler(_field_name, field_handler)
            return field_handler

        return decorator

    def register_handlers(self, fields: RegisterableFieldHandlers) -> None:
        """Register the new field handlers.

        :param fields: A sequence of sequences with field name and handler.
        :return: None.
        """
        for name, handler in fields:
            self.register_handler(name, handler)

    def unregister_handler(self, field_name: str) -> None:
        """Unregister a field handler.

        :param field_name: Name of the field.
        """

        self._handlers.pop(field_name, None)

    def unregister_handlers(self, field_names: Sequence[str] = ()) -> None:
        """Unregister a field handlers with given names.

        :param field_names: Names of the fields.
        :return: None.
        """

        for name in field_names:
            self.unregister_handler(name)

    def unregister_all_handlers(self) -> None:
        """Unregister all custom field handlers.

        :return: None.
        """
        self._handlers.clear()

    def __str__(self) -> str:
        return f"{self.__class__.__name__} <{self._generic.locale}>"


class Field(BaseField):
    """Greedy field (evaluates immediately).

    .. warning::

        There is no case when you need to instance **field** in loops.

        If you are doing this:

        >>> for i in range(1000):
        ...     field = Field()

        You're doing it **wrong**! It is a terrible idea that will lead to a memory leak.

        Forewarned is forearmed.

    Here is an example of how to use it:

        >>> _ = Field()
        >>> _('username')
        Dogtag_1836
    """

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.perform(*args, **kwargs)


class Fieldset(BaseField):
    """Greedy fieldset (evaluates immediately).

    Works like a field, but returns a list of values.

    Here is an example:

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

    def __init__(self, *args: Any, **kwargs: Any) -> None:
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

    def __call__(self, *args: Any, **kwargs: Any) -> list[Any]:
        """Perform fieldset.

        :param args: Arguments for field.
        :param kwargs: Keyword arguments for field.
        :raises FieldsetError: If parameter **i** is less than 1.
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
        "__counter",
        "__schema",
        "iterations",
    )

    def __init__(self, schema: CallableSchema, iterations: int = 10) -> None:
        """Initialize schema.

        :param iterations: Number of iterations.
            This parameter is keyword-only. The default value is 10.
        :param schema: A schema (must be a callable object).
        """
        if iterations < 1:
            raise ValueError("Number of iterations should be greater than 1.")

        self.iterations = iterations
        if schema and callable(schema):  # type: ignore[truthy-function]
            self.__schema = schema
            self.__counter = 0
        else:
            raise SchemaError()

    def to_csv(self, file_path: str, **kwargs: Any) -> None:
        """Export a schema as a CSV file.

        :param file_path: The file path.
        :param kwargs: The keyword arguments for :py:class:`csv.DictWriter` class.
        """
        data = self.create()
        with open(file_path, "w", encoding="utf-8", newline="") as fp:
            fieldnames = list(data[0])
            dict_writer = csv.DictWriter(fp, fieldnames, **kwargs)
            dict_writer.writeheader()
            dict_writer.writerows(data)

    def to_json(self, file_path: str, **kwargs: Any) -> None:
        """Export a schema as a JSON file.

        :param file_path: File a path.
        :param kwargs: Extra keyword arguments for :py:func:`json.dump` class.
        """
        with open(file_path, "w", encoding="utf-8") as fp:
            json.dump(self.create(), fp, **kwargs)

    def to_pickle(self, file_path: str, **kwargs: Any) -> None:
        """Export a schema as the pickled representation of the object to the file.

        :param file_path: The file path.
        :param kwargs: Extra keyword arguments for :py:func:`pickle.dump` class.
        """
        with open(file_path, "wb") as fp:
            pickle.dump(self.create(), fp, **kwargs)

    def create(self) -> list[JSON]:
        """Creates a list of a fulfilled schemas.

        .. note::
            This method evaluates immediately, so be careful when creating
            large datasets otherwise you're risking running out of memory.

            If you need a lazy version of this method, see :meth:`iterator`.

        :return: List of fulfilled schemas.
        """
        return [self.__schema() for _ in range(self.iterations)]

    def __next__(self) -> JSON:
        """Return the next item from the iterator."""
        if self.__counter < self.iterations:
            self.__counter += 1
            return self.__schema()
        raise StopIteration

    def __iter__(self) -> "Schema":
        """Return the iterator object itself."""
        self.__counter = 0
        return self

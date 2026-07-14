"""Lazy evaluation types for SchemaBuilder."""

from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from mimesis.types import Key


if TYPE_CHECKING:
    from mimesis.builder.core import SchemaBuilder

__all__ = [
    "FieldRef",
    "LazyChoice",
    "LazyField",
    "LazyWeightedChoice",
    "NestedSchema",
    "Resolvable",
    "SchemaRefProxy",
]


class Resolvable(ABC):
    """Abstract base class for resolving values from a schema."""

    __slots__ = ()

    @abstractmethod
    def _resolve(self, builder: "SchemaBuilder") -> Any:
        """Resolve the lazy value to an actual value.

        :param builder: The SchemaBuilder instance.
        :return: The resolved value.
        """
        raise NotImplementedError


class LazyField(Resolvable):
    """A field that evaluates lazily during schema generation.

    Example::

        sb.f("username")
        sb.f("email", key=str.lower)
        sb.f("integer_number", start=1, end=100)
    """

    __slots__ = ("_key", "_kwargs", "_name")

    def __init__(
        self,
        name: str,
        key: Key = None,
        **kwargs: Any,
    ) -> None:
        self._name = name
        self._key = key
        self._kwargs = kwargs

    def _resolve(self, builder: "SchemaBuilder") -> Any:
        return builder._resolve_field(self._name, self._key, **self._kwargs)

    def __repr__(self) -> str:
        return f"LazyField({self._name!r})"


class LazyChoice(Resolvable):
    """Lazy random choice from a list of items.

    Example::

        sb.choice(["active", "inactive", "pending"])
    """

    __slots__ = ("_items",)

    def __init__(self, items: Sequence[Any]) -> None:
        self._items = items

    def _resolve(self, builder: "SchemaBuilder") -> Any:
        return builder._random.choice(self._items)

    def __repr__(self) -> str:
        return f"LazyChoice({self._items!r})"


class LazyWeightedChoice(Resolvable):
    """Lazy weighted random choice.

    Example::

        sb.weighted_choice(["common", "rare"], [0.9, 0.1])
    """

    __slots__ = ("_items", "_weights")

    def __init__(
        self,
        items: Sequence[Any],
        weights: Sequence[float],
    ) -> None:
        if len(items) != len(weights):
            raise ValueError("items and weights must have the same length")
        if not items:
            raise ValueError("items must not be empty")
        self._items = items
        self._weights = weights

    def _resolve(self, builder: "SchemaBuilder") -> Any:
        return builder._random.choices(self._items, weights=self._weights)[0]

    def __repr__(self) -> str:
        return f"LazyWeightedChoice({self._items!r})"


class FieldRef(Resolvable):
    """Reference to a specific field in another schema.

    Resolves to a random value from the referenced schema's field.

    Example::

        sb.ref(users).id  # Returns FieldRef
    """

    __slots__ = ("_field_name", "_schema_name")

    def __init__(self, schema_name: str, field_name: str) -> None:
        self._schema_name = schema_name
        self._field_name = field_name

    def _resolve(self, builder: "SchemaBuilder") -> Any:
        return builder._pick_from(self._schema_name, self._field_name)

    def __repr__(self) -> str:
        return f"FieldRef({self._schema_name!r}.{self._field_name!r})"


class SchemaRefProxy(Resolvable):
    """Reference to an entire schema record.

    When used without field access, resolves to a random complete record.

    Example::

        sb.ref(users)  # Returns SchemaRefProxy (whole record)
        sb.ref(users).id  # Returns FieldRef (specific field)
    """

    __slots__ = ("_schema_name",)

    def __init__(self, schema_name: str) -> None:
        self._schema_name = schema_name

    def __getattr__(self, field_name: str) -> FieldRef:
        """Access a specific field from the referenced schema.

        :param field_name: Name of the field to reference.
        :return: A FieldRef that resolves to a random value from this field.
        """
        if field_name.startswith("_"):
            raise AttributeError(field_name)
        return FieldRef(self._schema_name, field_name)

    def _resolve(self, builder: "SchemaBuilder") -> Any:
        """Resolve to a random complete record from the schema."""
        return builder._pick_record(self._schema_name)

    def __repr__(self) -> str:
        return f"SchemaRefProxy({self._schema_name!r})"


class NestedSchema(Resolvable):
    """Embed N generated items from another schema definition.

    Example::

        addresses = sb.schema("addresses", {"city": sb.f("city")})
        users = sb.schema(
            "users",
            {
                "name": sb.f("full_name"),
                "addresses": addresses(count=3),
            },
        )
    """

    __slots__ = ("_count", "_definition", "_schema_name")

    def __init__(
        self,
        schema_name: str,
        definition: dict[str, Any],
        count: int,
    ) -> None:
        if count < 1:
            raise ValueError("count must be >= 1")
        self._schema_name = schema_name
        self._definition = definition
        self._count = count

    def _resolve(self, builder: "SchemaBuilder") -> list[Any]:
        if self._schema_name in builder._generating:
            raise ValueError(
                f"Circular nesting detected involving '{self._schema_name}'"
            )

        builder._generating.add(self._schema_name)
        try:
            return [
                builder._resolve_value(self._definition) for _ in range(self._count)
            ]
        finally:
            builder._generating.discard(self._schema_name)

    def __repr__(self) -> str:
        return f"NestedSchema({self._schema_name!r}, count={self._count})"

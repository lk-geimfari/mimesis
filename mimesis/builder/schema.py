"""Schema reference types for SchemaBuilder."""

from typing import Any

from mimesis.builder.resolver import NestedSchema


__all__ = ["SchemaRef"]


class SchemaRef:
    """Reference to a defined schema.

    Returned by ``sb.schema()``. Used for:

    1. Foreign keys via ``sb.ref(schema_ref).field``
    2. Nesting via ``schema_ref(count=N)``

    Example::

        users = sb.schema("users", {"id": sb.f("increment")})

        posts = sb.schema(
            "posts",
            {
                "user_id": sb.ref(users).id,  # Foreign key
            },
        )

        companies = sb.schema(
            "companies",
            {
                "name": sb.f("company"),
                "employees": users(count=5),  # Nested users
            },
        )
    """

    __slots__ = ("_definition", "_name")

    def __init__(self, name: str, definition: dict[str, Any]) -> None:
        """Initialize schema reference.

        :param name: The schema name.
        :param definition: The schema definition dict.
        """
        self._name = name
        self._definition = definition

    @property
    def name(self) -> str:
        """Return the schema name."""
        return self._name

    def __call__(self, *, count: int = 1) -> NestedSchema:
        """Create a nested embedding of this schema.

        :param count: Number of items to generate and embed.
        :return: A NestedSchema that resolves to a list of items.
        """
        return NestedSchema(self._name, self._definition, count)

    def __repr__(self) -> str:
        return f"SchemaRef({self._name!r})"

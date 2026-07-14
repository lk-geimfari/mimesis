"""SchemaBuilder — unified API for related fake data generation."""

from collections.abc import Sequence
from typing import Any

from mimesis.builder.resolver import (
    FieldRef,
    LazyChoice,
    LazyField,
    LazyWeightedChoice,
    NestedSchema,
    Resolvable,
    SchemaRefProxy,
)
from mimesis.builder.schema import SchemaRef
from mimesis.locales import Locale
from mimesis.schema import Field
from mimesis.types import JSON, Key, MissingSeed, Seed


__all__ = ["SchemaBuilder"]


class SchemaBuilder:
    """Unified builder for generating related fake data.

    Example::

        from mimesis import SchemaBuilder
        from mimesis.locales import Locale

        sb = SchemaBuilder(Locale.EN, seed=0xFF)

        users = sb.schema(
            "users",
            {
                "id": sb.f("increment"),
                "username": sb.f("username"),
                "email": sb.f("email"),
            },
        )

        posts = sb.schema(
            "posts",
            {
                "id": sb.f("increment"),
                "title": sb.f("sentence"),
                "user_id": sb.ref(users).id,
            },
        )

        data = sb.create(users=10, posts=50)
    """

    __slots__ = (
        "_dependencies",
        "_field",
        "_generated",
        "_generating",
        "_locale",
        "_random",
        "_schemas",
        "_seed",
    )

    def __init__(
        self,
        locale: Locale = Locale.DEFAULT,
        seed: Seed = MissingSeed,
    ) -> None:
        """Initialize the SchemaBuilder.

        :param locale: Locale for data generation.
        :param seed: Seed for reproducible random generation.
        """
        self._locale = locale
        self._seed = seed
        self._field = Field(locale, seed)
        self._random = self._field.get_random_instance()
        self._schemas: dict[str, JSON] = {}
        self._dependencies: dict[str, set[str]] = {}
        self._generated: dict[str, list[JSON]] = {}
        self._generating: set[str] = set()

    def reseed(self, seed: Seed = MissingSeed) -> None:
        """Reseed all random generators.

        :param seed: New seed value.
        """
        self._seed = seed
        self._field.reseed(seed)
        self._random = self._field.get_random_instance()

    def f(self, name: str, key: Key = None, **kwargs: Any) -> LazyField:
        """Create a lazy field that evaluates during generation.

        :param name: Field name (e.g., "username", "person.email").
        :param key: Optional key function to transform the result.
        :param kwargs: Additional arguments for the field method.
        :return: A lazy field that resolves during data generation.

        Example::

            sb.f("username")
            sb.f("person.email", domains=["example.com"])
            sb.f("full_name", key=str.upper)
        """
        return LazyField(name, key, **kwargs)

    def choice(self, items: Sequence[Any]) -> LazyChoice:
        """Create a lazy random choice from items.

        :param items: Sequence of items to choose from.
        :return: A lazy choice that resolves during data generation.

        Example::

            sb.choice(["active", "inactive", "pending"])
        """
        if not items:
            raise ValueError("items must not be empty")
        return LazyChoice(items)

    def weighted_choice(
        self, items: Sequence[Any], weights: Sequence[float]
    ) -> LazyWeightedChoice:
        """Create a lazy weighted random choice.

        :param items: Sequence of items to choose from.
        :param weights: Weights for each item (must match items length).
        :return: A lazy weighted choice that resolves during data generation.

        Example::

            sb.weighted_choice(["common", "rare", "legendary"], [0.7, 0.25, 0.05])
        """
        return LazyWeightedChoice(items, weights)

    def ref(self, schema: SchemaRef) -> SchemaRefProxy:
        """Create a reference to another schema for foreign keys.

        :param schema: The SchemaRef returned by sb.schema().
        :return: A proxy that allows field access for FK references.

        Example::

            users = sb.schema("users", {"id": sb.f("increment")})

            posts = sb.schema(
                "posts",
                {
                    "user_id": sb.ref(users).id,  # FK to users.id
                    "author": sb.ref(users),  # Whole user record
                },
            )
        """
        if not isinstance(schema, SchemaRef):
            raise TypeError(
                f"ref() expects a SchemaRef, got {type(schema).__name__}. "
                f"Use sb.ref(schema_var) where schema_var = sb.schema(...)."
            )
        return SchemaRefProxy(schema._name)

    def schema(self, name: str, schema: dict[str, Any]) -> SchemaRef:
        """Define a schema and return a reference.

        :param name: Unique name for this schema.
        :param schema: Dictionary defining the schema fields.
        :return: A SchemaRef for FK references and nesting.

        Example::

            users = sb.schema(
                "users",
                {
                    "id": sb.f("increment"),
                    "username": sb.f("username"),
                    "profile": {
                        "bio": sb.f("text"),
                    },
                },
            )
        """
        self._schemas[name] = schema
        self._dependencies[name] = self._extract_dependencies(schema)
        return SchemaRef(name, schema)

    def _extract_dependencies(self, obj: Any) -> set[str]:
        """Extract schema dependencies from a definition.

        :param obj: Object to scan for dependencies.
        :return: Set of schema names this definition depends on.
        """
        deps: set[str] = set()

        if isinstance(obj, (FieldRef, SchemaRefProxy)):
            deps.add(obj._schema_name)
        elif isinstance(obj, NestedSchema):
            deps.update(self._extract_dependencies(obj._definition))
        elif isinstance(obj, dict):
            for value in obj.values():
                deps.update(self._extract_dependencies(value))
        elif isinstance(obj, (list, tuple)):
            for item in obj:
                deps.update(self._extract_dependencies(item))

        return deps

    def _resolve_field(self, name: str, key: Key = None, **kwargs: Any) -> Any:
        """Resolve a field name to its value.

        :param name: Field name.
        :param key: Optional key function.
        :param kwargs: Field arguments.
        :return: Generated value.
        """
        return self._field(name, key=key, **kwargs)

    def _resolve_value(self, value: Any) -> Any:
        """Recursively resolve lazy values to actual values.

        :param value: Value to resolve (may be lazy or nested).
        :return: Resolved value.
        """
        if isinstance(value, Resolvable):
            # Resolve again so choice/weighted_choice can yield nested
            # lazy values (e.g. sb.choice([None, sb.f("sentence")])).
            return self._resolve_value(value._resolve(self))
        if isinstance(value, SchemaRef):
            raise TypeError(
                f"Bare SchemaRef({value._name!r}) cannot be used as a field value. "
                f"Use sb.ref({value._name}) for foreign keys or "
                f"{value._name}(count=N) for nesting."
            )
        if isinstance(value, dict):
            return {k: self._resolve_value(v) for k, v in value.items()}
        if isinstance(value, list):
            return [self._resolve_value(v) for v in value]
        if isinstance(value, tuple):
            return tuple(self._resolve_value(v) for v in value)
        return value

    def _pick_from(self, schema_name: str, field_name: str) -> Any:
        """Pick a random field value from generated data.

        :param schema_name: Name of the schema.
        :param field_name: Name of the field to extract.
        :return: Random value from the specified field.
        :raises ValueError: If schema hasn't been generated yet.
        """
        if schema_name not in self._generated:
            raise ValueError(
                f"Schema '{schema_name}' not yet generated. "
                f"Make sure to include it in create()."
            )

        items = self._generated[schema_name]
        if not items:
            raise ValueError(f"Schema '{schema_name}' has no items")

        item = self._random.choice(items)
        if field_name not in item:
            raise KeyError(f"Field '{field_name}' not found in schema '{schema_name}'")
        return item[field_name]

    def _pick_record(self, schema_name: str) -> JSON:
        """Pick a random complete record from generated data.

        :param schema_name: Name of the schema.
        :return: Random record (dict) from the schema.
        :raises ValueError: If schema hasn't been generated yet.
        """
        if schema_name not in self._generated:
            raise ValueError(
                f"Schema '{schema_name}' not yet generated. "
                f"Make sure to include it in create()."
            )

        items = self._generated[schema_name]
        if not items:
            raise ValueError(f"Schema '{schema_name}' has no items")

        return self._random.choice(items)

    def _topological_sort(self, names: list[str]) -> list[str]:
        """Sort schema names by their dependencies.

        :param names: List of schema names to sort.
        :return: Topologically sorted list.
        :raises ValueError: If circular dependency detected.
        """
        result: list[str] = []
        visited: set[str] = set()
        visiting: set[str] = set()

        def visit(name: str) -> None:
            if name in visited:
                return
            if name in visiting:
                raise ValueError(f"Circular dependency detected involving '{name}'")

            visiting.add(name)

            for dep in self._dependencies.get(name, set()):
                if dep in names:
                    visit(dep)

            visiting.remove(name)
            visited.add(name)
            result.append(name)

        for name in names:
            visit(name)

        return result

    def _generate_schema(self, name: str, count: int) -> list[JSON]:
        """Generate data for a single schema.

        :param name: Schema name.
        :param count: Number of items to generate.
        :return: List of generated items.
        """
        definition = self._schemas[name]
        results: list[JSON] = []

        self._generating.add(name)
        try:
            for _ in range(count):
                item = self._resolve_value(definition)
                results.append(item)
        finally:
            self._generating.discard(name)

        return results

    def create(self, **counts: int) -> dict[str, list[JSON]]:
        """Generate all schemas with specified counts.

        Schemas are automatically sorted by dependencies, so you can
        pass them in any order.

        :param counts: Schema names mapped to their counts.
        :return: Dictionary of schema names to generated data lists.
        :raises ValueError: If a schema name is not defined.

        Example::

            data = sb.create(
                users=10,
                posts=50,
                comments=200,
            )
        """
        self._generated.clear()
        self._generating.clear()

        for name, count in counts.items():
            if name not in self._schemas:
                raise ValueError(f"Schema '{name}' is not defined")
            if count < 0:
                raise ValueError(f"Count for '{name}' must be >= 0")

        ordered_names = self._topological_sort(list(counts.keys()))

        result: dict[str, list[JSON]] = {}
        for name in ordered_names:
            data = self._generate_schema(name, counts[name])
            self._generated[name] = data
            result[name] = data

        return result

    def clear(self) -> None:
        """Clear all generated data (keeps schema definitions)."""
        self._generated.clear()
        self._generating.clear()

    def reset(self) -> None:
        """Reset builder completely (clears schemas and generated data)."""
        self._schemas.clear()
        self._dependencies.clear()
        self._generated.clear()
        self._generating.clear()

    def __repr__(self) -> str:
        schemas = ", ".join(self._schemas.keys()) or "none"
        return f"SchemaBuilder(locale={self._locale}, schemas=[{schemas}])"

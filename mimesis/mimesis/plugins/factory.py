from contextlib import contextmanager
from typing import Any, ClassVar, Iterator

from mimesis.locales import Locale
from mimesis.schema import Field, RegisterableFieldHandlers

try:
    from factory import declarations
    from factory.builder import BuildStep, Resolver
except ImportError:
    raise ImportError("This plugin requires factory_boy to be installed.")

__all__ = ["FactoryField", "MimesisField"]


class FactoryField(declarations.BaseDeclaration):  # type: ignore[misc]
    """
    Mimesis integration with FactoryBoy starts here.

    This class provides a common interface for FactoryBoy,
    but inside it has Mimesis generators.
    """

    _default_locale: ClassVar[Locale] = Locale.EN
    _cached_instances: ClassVar[dict[str, Field]] = {}

    def __init__(
        self,
        field: str,
        locale: Locale | None = None,
        **kwargs: Any,
    ) -> None:
        """
        Creates a field instance.

        The created field is lazy. It also receives build time parameters.
        These parameters are not applied yet.

        :param field: name to be passed to :class:`~mimesis.schema.Field`.
        :param locale: locale to use. This parameter has the highest priority.
        :param kwargs: optional parameters that would be passed to ``Field``.
        """
        super().__init__()
        self.locale = locale
        self.kwargs = kwargs
        self.field = field

    def evaluate(
        self,
        instance: Resolver,
        step: BuildStep,
        extra: dict[str, Any] | None = None,
    ) -> Any:
        """Evaluates the lazy field.

        :param instance: (factory.builder.Resolver): The object holding currently computed attributes.
        :param step: (factory.builder.BuildStep): The object holding the current build step.
        :param extra: Extra call-time added kwargs that would be passed to ``Field``.
        """
        kwargs: dict[str, Any] = {}
        kwargs.update(self.kwargs)
        kwargs.update(extra or {})

        field_handlers = step.builder.factory_meta.declarations.get(
            "field_handlers", []
        )

        _field = self._get_cached_instance(
            locale=self.locale,
            field_handlers=field_handlers,
        )
        return _field(self.field, **kwargs)

    @classmethod
    @contextmanager
    def override_locale(cls, locale: Locale) -> Iterator[None]:
        """
        Overrides unspecified locales.

        Remember that implicit locales would not be overridden.
        """
        old_locale = cls._default_locale
        cls._default_locale = locale
        yield
        cls._default_locale = old_locale

    @classmethod
    def _get_cached_instance(
        cls,
        locale: Locale | None = None,
        field_handlers: RegisterableFieldHandlers | None = None,
    ) -> Field:
        """Returns cached instance.

        :param locale: locale to use.
        :param field_handlers: custom field handlers.
        :return: cached instance of Field.
        """
        if locale is None:
            locale = cls._default_locale

        field_names = "-".join(
            sorted(
                dict(field_handlers if field_handlers else []).keys(),
            )
        )

        key = f"{locale}{field_names}"

        if key not in cls._cached_instances:
            field = Field(locale)

            if field_handlers:
                field.register_handlers(field_handlers)

            cls._cached_instances[key] = field

        return cls._cached_instances[key]


# An alias
MimesisField = FactoryField

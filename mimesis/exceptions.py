# -*- coding: utf-8 -*-

"""Custom exceptions which used in Mimesis."""

from typing import Any, Optional


class UnsupportedAlgorithm(AttributeError):
    """Raised when the user wants to use an unsupported algorithm."""


class UnsupportedLocale(KeyError):
    """Raised when a locale isn't supported."""

    def __init__(self, locale: Optional[str] = None) -> None:
        """Initialize attributes for informative output.

        :param locale: Locale.
        """
        self.locale = locale
        self.message = 'Locale «{}» is not supported'

    def __str__(self) -> str:
        return self.message.format(self.locale)


class UndefinedSchema(ValueError):
    """Raised when schema is empty."""

    def __str__(self) -> str:
        return 'Schema should be defined in lambda.'


class NonEnumerableError(TypeError):
    """Raised when object is not instance of Enum."""

    message = 'You should use one item of: «{}» of the object mimesis.enums.{}'

    def __init__(self, enum_obj: Any) -> None:
        """Initialize attributes for informative output.

        :param enum_obj: Enum object.
        """
        if enum_obj:
            self.name = enum_obj
            self.items = ', '.join([str(i) for i in enum_obj])
        else:
            self.items = ''

    def __str__(self) -> str:
        return self.message.format(self.items,
                                   self.name.__name__)


class UnsupportedField(ValueError):
    """Raises when ``field`` is not supported."""

    def __init__(self, name: Optional[str] = None) -> None:
        """Initialize attributes for more informative output.

        :param name: Name of the field..
        """
        self.name = name
        self.message = 'Field «{}» is not supported.'

    def __str__(self) -> str:
        return self.message.format(self.name)


class UndefinedField(ValueError):
    """Raises when ``field`` is None."""

    def __str__(self) -> str:
        return 'Undefined field. Filed cannot be None.'


class UnacceptableField(ValueError):
    """Raises when the ``field`` has an unacceptable format."""

    def __str__(self) -> str:
        return 'Unacceptable field format, use **provider.method**.'

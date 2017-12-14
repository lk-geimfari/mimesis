from typing import Any, Optional


class UnsupportedAlgorithm(AttributeError):
    """ Raised when the user wants to use an unsupported algorithm. """


class UnsupportedLocale(KeyError):
    """ Raised when a locale isn't supported. """

    def __init__(self, locale: Optional[str] = None) -> None:
        self.locale = locale
        self.message = 'Locale «{}» is not supported'

    def __str__(self) -> str:
        return self.message.format(self.locale)


class UndefinedSchema(ValueError):
    """ Raised when schema is empty. """

    def __str__(self):
        return 'Schema should be defined in lambda.'


class NonEnumerableError(TypeError):
    """ Raised when object is not instance of Enum """

    message = 'You should use one item of: «{}» of the object mimesis.enums.{}'

    def __init__(self, enum_obj: Any) -> None:
        if enum_obj:
            self.name = enum_obj
            self.items = ', '.join([str(i) for i in enum_obj])
        else:
            self.items = ''

    def __str__(self) -> str:
        return self.message.format(self.items,
                                   self.name.__name__)


class UnsupportedField(ValueError):
    def __init__(self, name: Optional[str] = None):
        self.name = name
        self.message = 'Field «{}» is not supported.'

    def __str__(self):
        return self.message.format(self.name)


class UndefinedField(ValueError):
    def __str__(self):
        return 'Undefined field. Filed cannot be None.'

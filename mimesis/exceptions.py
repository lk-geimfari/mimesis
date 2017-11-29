class UnsupportedLocale(KeyError):
    """ Raised when a locale isn't supported. """

    def __init__(self, locale: str) -> None:
        self.locale = locale
        self.message = 'Locale «{}» is not supported'

    def __str__(self) -> str:
        return self.message.format(self.locale)


class UnsupportedAlgorithm(AttributeError):
    """ Raised when the user wants to use an unsupported algorithm. """


class UndefinedSchema(ValueError):
    """ Raised when schema is empty. """


class NonEnumerableError(TypeError):
    """ Raised when object is not instance of Enum """

    message = 'You should use one item of: «{}» of the object mimesis.enums.{}'

    def __init__(self, enum_obj) -> None:
        if enum_obj:
            self.name = enum_obj
            self.items = ', '.join([str(i) for i in enum_obj])
        else:
            self.items = ''

    def __str__(self) -> str:
        return self.message.format(self.items,
                                   self.name.__name__)

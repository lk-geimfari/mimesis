class UnsupportedLocale(KeyError):
    """ Raised when a locale isn't supported. """


class JSONKeyError(KeyError):
    """ Raised when a JSON key doesn't exist. """


class UnexpectedGender(KeyError):
    """ Raised when gender is wrong. """


class UnsupportedAlgorithm(AttributeError):
    """ Raised when the user wants to use an unsupported algorithm. """


class UndefinedSchema(ValueError):
    """ Raised when schema is empty. """


class NonEnumerableError(TypeError):
    """ Raised when object is not instance of Enum """

    def __init__(self, enum_name):
        self.enum_name = enum_name

    def __str__(self):
        return 'You should use item of enum object «{}» ' \
               'from module mimesis.enums'.format(self.enum_name)

class UnsupportedLocale(KeyError):
    """ Raised when a locale isn't supported. """


class JSONKeyError(KeyError):
    """ Raised when a JSON key doesn't exist. """


class WrongArgument(KeyError):
    """ Raised when argument is wrong. """


class UnexpectedGender(WrongArgument):
    """ Raised when gender is wrong. """


class UnsupportedAlgorithm(AttributeError):
    """ Raised when the user wants to use an unsupported algorithm. """


class UndefinedSchema(ValueError):
    """ Raised when schema is empty. """

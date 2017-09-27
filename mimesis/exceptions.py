class UnsupportedLocale(KeyError):
    """An exception that raised when a locale doesn't supported."""


class JSONKeyError(KeyError):
    """An exception that raised when JSON key doesn't exist"""


class WrongArgument(KeyError):
    """An exception that raised when argument is wrong"""


class UnexpectedGender(WrongArgument):
    """An exceptions that raised when gender is wrong"""


class UnsupportedAlgorithm(AttributeError):
    """An exception that raised when user want to use unsupported algorithm"""


class UndefinedSchema(ValueError):
    """An exception that raised when schema if empty"""

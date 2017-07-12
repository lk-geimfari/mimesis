class UnsupportedLocale(KeyError):
    """An exception that raised when a locale doesn't supported."""


class JSONKeyError(KeyError):
    """An exception that raised when JSON key doesn't exist"""


class NotImplementedYet(NotImplementedError):
    """An exception that raised when NotImplementedError"""


class WrongArgument(KeyError):
    """An exception that raised when argument is wrong"""

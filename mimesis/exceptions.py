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

    def __init__(self, enum_obj):
        if enum_obj:
            self.enum_name = str(enum_obj)
            self.items = ', '.join([str(i) for i in enum_obj])
        else:
            self.items = ''

    def __str__(self):
        return 'You should use one item of: «{}» of the object {} ' \
               'from module mimesis.enums'.format(self.items, self.enum_name)

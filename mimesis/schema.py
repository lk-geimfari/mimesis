from typing import Any

from mimesis import Generic

DATA_PROVIDERS = [
    'address',
    'business',
    'clothing_sizes',
    'code',
    'cryptographic',
    'datetime',
    'development',
    'file',
    'food',
    'games',
    'hardware',
    'internet',
    'numbers',
    'path',
    'personal',
    'science',
    'text',
    'transport',
    'unit_system',
]


class Field(object):
    """Field for generating data using Schema().

    >>> field = Field('en')
    >>> field('name', gender='female')
    """

    def __init__(self, locale: str = 'en') -> None:
        self.locale = locale
        self.gen = Generic(self.locale)
        self.SUPPORTED = DATA_PROVIDERS

    def __call__(self, name, **kwargs) -> Any:
        for provider in self.SUPPORTED:
            if hasattr(self.gen, provider):
                provider = getattr(self.gen, provider)

                if name and hasattr(provider, name):
                    return getattr(provider, name)(**kwargs)
        else:
            raise ValueError('Undefined field')

    def __str__(self):
        return '{}:{}'.format(
            self.locale,
            self.__class__.__name__,

        )

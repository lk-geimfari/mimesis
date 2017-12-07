from random import Random

from mimesis.providers.base import ValidateEnumMixin
from mimesis.utils import custom_code


class BaseSpecProvider(ValidateEnumMixin):
    def __init__(self):
        self.random = Random()
        self.code = custom_code

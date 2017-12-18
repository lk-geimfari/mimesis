from mimesis.helpers import Random
from mimesis.providers.base import ValidateEnumMixin


class BaseSpecProvider(ValidateEnumMixin):
    def __init__(self):
        self.random = Random()

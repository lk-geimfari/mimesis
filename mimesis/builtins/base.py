from random import Random

from mimesis.providers.base import Boilerplate
from mimesis.utils import custom_code


class BaseSpecProvider(Boilerplate):
    def __init__(self):
        self.random = Random()
        self.code = custom_code

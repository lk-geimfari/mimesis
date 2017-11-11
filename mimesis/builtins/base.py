from random import Random

from mimesis.utils import custom_code


class BaseSpecProvider(object):
    def __init__(self):
        self.random = Random()
        self.code = custom_code

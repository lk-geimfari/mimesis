from random import Random

from mimesis.providers import Code


class BaseSpecProvider(object):
    def __init__(self):
        self.random = Random()
        self.code = Code().custom_code

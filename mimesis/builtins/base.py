from mimesis.helpers import Random


class BaseSpecProvider(object):
    def __init__(self):
        self.random = Random()

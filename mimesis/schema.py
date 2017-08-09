import json

from mimesis.decorators import type_to
from mimesis.providers import Generic


class Schema(object):
    def __init__(self, locale=None):
        self.schema = {}
        if locale is None:
            self.locale = 'en'
        else:
            self.locale = locale

        self.generic = Generic(self.locale)

    def __generate(self, schema):
        data = dict()
        for k, v in schema.items():
            if isinstance(v, dict):
                data[k] = self.__generate(v)
            elif isinstance(v, list):
                data[k] = [self.__generate(i) for i in v]
            else:
                provider, method = v.split('.')
                data[k] = getattr(
                    getattr(self.generic, provider), method)()
        return data

    def load(self, path=None, schema=None):

        if schema:
            self.schema = schema
        if path:
            try:
                with open(path, 'r') as f:
                    self.schema = json.load(f)
            except ValueError:
                raise ValueError('Invalid json file!')
        return self

    @type_to(list, check_len=True)
    def create(self, iterations=1):
        if self.schema:
            return map(lambda _: self.__generate(self.schema),
                       range(iterations))

from mimesis.decorators import type_to
from mimesis.providers import Generic


# TODO: 1. Saving json in the file (fluent interface)
# TODO: 2. Add tests

class Schema(object):
    def __init__(self, locale=None):
        self.generic = Generic(locale=locale)

    def __generate(self, schema):
        data = dict()
        for key, val in schema.items():
            if isinstance(val, dict):
                data[key] = self.__generate(val)
            elif isinstance(val, list):
                data[key] = [self.__generate(i) for i in val]
            else:
                provider, method = val.split('.')
                data[key] = getattr(
                    getattr(self.generic, provider), method)()
        return data

    @type_to(list)
    def create(self, schema, iterations=1):
        return map(lambda _: self.__generate(schema),
                   range(iterations))

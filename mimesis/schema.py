import json
from typing import Iterator

from mimesis.decorators import type_to
from mimesis.exceptions import UndefinedSchema
from mimesis.providers import BaseProvider, Generic


class Schema(BaseProvider):
    """Class which helps generate data by schema using any
    providers which supported by mimesis.
    """

    schema = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generic = Generic(self.locale)

    def __generate(self, schema: dict) -> dict:
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

    def load(self, path: str=None, schema: dict=None):
        """Load schema from python dict or from json file.

        :param path: Path to file.
        :param schema: Dictionary (schema).
        """

        if schema:
            self.schema = schema
        if path:
            try:
                try:
                    with open(path, 'r') as f:
                        self.schema = json.load(f)
                except FileNotFoundError:
                    raise FileNotFoundError(
                        'File {path} is not found'.format(path=path))
            except ValueError:
                raise ValueError('Invalid json file!')
        return self

    @type_to(list, check_len=True)
    def create(self, iterations: int=1) -> Iterator:
        """Fill schema using data generators of mimesis.

        :param iterations: Count of iterations.
        :return: Filled schema.
        """
        if self.schema:
            return map(lambda _: self.__generate(self.schema),
                       range(iterations))
        else:
            raise UndefinedSchema(
                'The schema is empty or do not loaded.')

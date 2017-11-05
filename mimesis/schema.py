import json
from typing import Optional, Iterator

from mimesis.decorators import type_to
from mimesis.exceptions import UndefinedSchema
from mimesis.providers.base import BaseProvider
from mimesis.providers.generic import Generic
from mimesis.typing import JSON


class Schema(BaseProvider):
    """Class which helps generate data by schema using any
    providers which supported by mimesis.
    """

    schema = {}  # type: dict

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generic = Generic(self.locale)

    def __generate(self, schema: JSON = dict) -> JSON:
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

    def load(self, path: Optional[str] = None,
             schema: Optional[JSON] = None) -> 'Schema':
        """Load schema from python dict or json file.

        :param path: Path to file.
        :param schema: Dictionary (schema).
        """

        if schema:
            self.schema = schema
        if path:
            try:
                with open(path, 'r') as f:
                    self.schema = json.load(f)
            except FileNotFoundError:
                # modify message
                raise FileNotFoundError(
                    'File {path} is not found'.format(path=path))
            except ValueError:
                raise ValueError('Invalid json file!')
        return self

    @type_to(list, check_len=True)
    def create(self, iterations: int = 1) -> Iterator[dict]:
        """Fill schema using data generators of mimesis.

        :param iterations: Count of iterations.
        :return: Filled schema.
        """

        if self.schema:
            return map(lambda _: self.__generate(self.schema),
                       range(iterations))
        else:
            raise UndefinedSchema(
                'The schema is empty or not loaded.')

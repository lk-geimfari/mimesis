from types import LambdaType
from typing import Any, List, Optional

from mimesis.exceptions import UndefinedSchema
from mimesis.providers import Generic
from mimesis.providers.generic import GENERIC_ATTRS
from mimesis.typing import JSON


class Field(object):
    """Field for generating data by schema.

    Instance of this object takes any string which represents name
    of the any method of any supported data provider and the ``**kwargs``
    of the method:

    >>> _ = Field('en')
    >>> _('full_name')
    'Benedict Larson'
    """

    def __init__(self, locale: str = 'en') -> None:
        self.locale = locale
        self.gen = Generic(self.locale)

    def __call__(self, name: Optional[str] = None, **kwargs) -> Any:
        """This magic override standard call so it's take any string which
        represents name of the any method of any supported data provider
        and the ``**kwargs`` of this method.

        :param name: Name of method.
        :param kwargs: Kwargs of method.
        :return: Value which represented by method.
        :raises ValueError: if provider is not
            supported or if field is not defined.
        """
        if name is not None:
            for provider in GENERIC_ATTRS:
                if hasattr(self.gen, provider):
                    provider = getattr(self.gen, provider)
                    if hasattr(provider, name):
                        method = getattr(provider, name)
                        return method(**kwargs)
            else:
                raise ValueError('Field «{}» is not supported'.format(name))
        else:
            raise ValueError('Undefined field')

    def __str__(self) -> str:
        return '{}:{}'.format(
            self.__class__.__name__,
            self.locale,
        )

    @staticmethod
    def fill(schema: LambdaType, iterations: int = 1) -> List[JSON]:
        """Fill schema with data.

        :param lambda schema: Lambda function with schema.
        :param int iterations: Count of iterations.
        :return: Filled schema.
        :raises UndefinedSchema: if schema is empty dict.
        """
        if schema() and isinstance(schema, LambdaType):
            result = map(lambda _: schema(), range(iterations))
            return list(result)
        else:
            raise UndefinedSchema(
                'Schema should be defined in lambda.')

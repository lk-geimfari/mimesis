from typing import Any, List
from types import LambdaType

from mimesis.exceptions import UndefinedSchema
from mimesis.providers import Generic
from mimesis.providers.generic import GENERIC_ATTRS


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

    def __call__(self, name: str, **kwargs) -> Any:
        """Override standard calling.

        :param str name: Name of method.
        :param kwargs: Kwargs of method.
        :return: Value which represented by method.
        :rtype: Any
        :raises ValueError: if providers is not supported.
        :raises ValueError: if field is not defined.
        """
        if name is not None:
            for provider in GENERIC_ATTRS:
                if hasattr(self.gen, provider):

                    provider = getattr(self.gen, provider)
                    if hasattr(provider, name):
                        return getattr(provider, name)(**kwargs)
            else:
                raise ValueError('Unsupported field')
        else:
            raise ValueError('Undefined field')

    def __str__(self):
        return '{}:{}'.format(
            self.locale,
            self.__class__.__name__,

        )

    @staticmethod
    def fill(schema: LambdaType, iterations: int = 1) -> List[Any]:
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

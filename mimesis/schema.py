from types import LambdaType
from typing import Any, Callable, List, Optional

from mimesis.exceptions import (UndefinedField, UndefinedSchema,
                                UnsupportedField)
from mimesis.providers.base import StrMixin
from mimesis.providers.generic import Generic
from mimesis.typing import JSON

__all__ = ['AbstractField', 'Field', 'Schema']


class AbstractField(StrMixin):
    """
    AbstractField is a class for generating data by the name of the method.

    Instance of this object takes any string which represents name
    of the any method of any supported data provider and the ``**kwargs``
    of the method:

    >>> _ = AbstractField('en')
    >>> _('full_name')
    'Benedict Larson'
    """

    def __init__(self, locale: str = 'en', seed: bool = None) -> None:
        self.locale = locale
        self.seed = seed
        self.gen = Generic(self.locale, self.seed)

    def __call__(self, name: Optional[str] = None,
                 key: Optional[Callable] = None, **kwargs) -> Any:
        """This magic override standard call so it's take any string which
        represents name of the any method of any supported data provider
        and the ``**kwargs`` of this method.

        :param name: Name of method.
        :param key: A key function (or other callable object)
            which will be applied to result.
        :param kwargs: Kwargs of method.
        :return: Value which represented by method.
        :raises ValueError: if provider is not
            supported or if field is not defined.
        """
        if name is None:
            raise UndefinedField()

        # TODO: This is a really slow solution. Fix it.
        for provider in dir(self.gen):
            if hasattr(self.gen, provider):
                provider = getattr(self.gen, provider)
                if name in dir(provider):
                    method = getattr(provider, name)
                    result = method(**kwargs)
                    if key and callable(key):
                        return key(result)
                    return result
            else:
                continue
        else:
            raise UnsupportedField(name)


class Schema(object):
    """
    Class which return list of filled schemas.
    """

    def __init__(self, schema: LambdaType) -> None:
        if callable(schema) and isinstance(schema, LambdaType):
            self.schema = schema
        else:
            raise UndefinedSchema()

    def create(self, iterations: int = 1) -> List[JSON]:
        data = map(lambda _: self.schema(), range(iterations))
        return list(data)


Field = AbstractField

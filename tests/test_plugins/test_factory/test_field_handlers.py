import factory
import pytest
from pytest_factoryboy import register

from mimesis.exceptions import FieldError
from mimesis.plugins.factory import MimesisField


class Guest:
    def __init__(self, full_name: str, age: int) -> None:
        self.age = age
        self.full_name = full_name


@register
class FactoryWithoutCustomFieldHandlers(factory.Factory):
    class Meta(object):
        model = Guest

    age = MimesisField("anynum")
    full_name = MimesisField("nickname")


@register
class FactoryWithCustomFieldHandlers(factory.Factory):
    class Meta(object):
        model = Guest

    class Params(object):
        field_handlers = [
            ("anynum", lambda rand, **kwargs: rand.randint(1, 99)),
            ("nickname", lambda rand, **kwargs: rand.choice(["john", "alice"])),
        ]

    age = MimesisField("anynum")
    full_name = MimesisField("nickname")


def test_factory_without_custom_field_handlers(factory_without_custom_field_handlers):
    with pytest.raises(FieldError):
        factory_without_custom_field_handlers()


def test_factory_with_custom_field_handlers(factory_with_custom_field_handlers):
    guest = factory_with_custom_field_handlers()
    assert isinstance(guest, Guest)

    assert 1 <= guest.age <= 99
    assert guest.full_name in ["john", "alice"]

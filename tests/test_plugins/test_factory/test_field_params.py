import factory
import pytest
from pytest_factoryboy import register

from mimesis.enums import Gender
from mimesis.plugins.factory import MimesisField

MIN_AGE = 30
MAX_AGE = 32


class Guest(object):
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age


@register
class GuestFactory(factory.Factory):
    class Meta(object):
        model = Guest

    full_name = MimesisField("full_name", gender=Gender.FEMALE)
    age = MimesisField("integer_number", start=MIN_AGE, end=MAX_AGE)


def test_guest_factory_different_data(guest_factory):
    guest1 = guest_factory()
    guest2 = guest_factory()

    assert isinstance(guest1, Guest)
    assert isinstance(guest2, Guest)
    assert guest1 != guest2
    assert guest1.full_name != guest2.full_name
    assert MIN_AGE <= guest1.age <= MAX_AGE
    assert MIN_AGE <= guest2.age <= MAX_AGE


def test_guest_factory_create_batch(guest_factory):
    guests = guest_factory.create_batch(50)
    names = {guest.full_name for guest in guests}

    assert len(guests) == len(names)

    for guest in guests:
        assert isinstance(guest, Guest)
        assert MIN_AGE <= guest.age <= MAX_AGE


def test_guest_factory_build_batch(guest_factory):
    guests = guest_factory.build_batch(50)
    names = {guest.full_name for guest in guests}

    assert len(guests) == len(names)

    for guest in guests:
        assert isinstance(guest, Guest)
        assert MIN_AGE <= guest.age <= MAX_AGE


def test_guest_instance_data(guest):
    assert isinstance(guest, Guest)
    assert guest.full_name != ""
    assert MIN_AGE <= guest.age <= MAX_AGE


@pytest.mark.parametrize("guest__age", [19])
def test_guest_data_overrides(guest):
    assert isinstance(guest, Guest)
    assert guest.full_name != ""
    assert guest.age == 19

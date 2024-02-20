import factory

from mimesis.plugins.factory import MimesisField


class User(object):
    def __init__(self, uid, email):
        self.uid = uid
        self.email = email


class UserFactory(factory.Factory):
    class Meta(object):
        model = User

    uid = factory.Sequence(lambda order: order)
    email = MimesisField("email")


def test_direct_factory():
    users = UserFactory.create_batch(10)

    uids = {user.uid for user in users}
    emails = {user.email for user in users}

    assert len(users) == len(emails)
    assert len(users) == len(uids)


def test_factory_extras():
    user = UserFactory(email="custom@mail.ru")

    assert user.email == "custom@mail.ru"

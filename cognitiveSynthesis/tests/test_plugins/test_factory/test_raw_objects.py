import factory
import pytest
import validators
from pytest_factoryboy import register

from mimesis.plugins.factory import FactoryField

TEST_USERNAMES = ("sobolevn", "lk-geimfari")


class Account(object):
    def __init__(self, uid, username, email):
        self.uid = uid
        self.username = username
        self.email = email


@register
class AccountFactory(factory.Factory):
    class Meta(object):
        model = Account
        exclude = ("_domain",)

    uid = factory.Sequence(lambda order: order + 1)
    username = FactoryField("username")
    _domain = FactoryField("top_level_domain")
    email = factory.LazyAttribute(
        lambda instance: "{0}@example{1}".format(
            instance.username,
            instance._domain,  # noqa: WPS437
        ),
    )


def test_account_factory_different_data(account_factory):
    account1 = account_factory()
    account2 = account_factory()

    assert isinstance(account1, Account)
    assert isinstance(account2, Account)
    assert account1 != account2
    assert account1.uid != account2.uid
    assert account1.username != account2.username
    assert account1.email != account2.email


def test_account_factory_overrides(account_factory):
    username = "sobolevn"
    desired_id = 190
    account = account_factory(username=username, uid=desired_id)

    assert account.uid == desired_id
    assert account.username == username
    assert account.email.startswith(username)


def test_account_factory_create_batch(account_factory):
    accounts = account_factory.create_batch(10)
    uids = {account.uid for account in accounts}
    usernames = {account.username for account in accounts}

    assert len(accounts) == len(uids)
    assert len(accounts) == len(usernames)

    for account in accounts:
        assert isinstance(account, Account)
        assert account.uid > 0
        assert account.username != ""
        assert account.email.startswith(account.username)


def test_account_factory_build_batch(account_factory):
    accounts = account_factory.build_batch(10)
    uids = {account.uid for account in accounts}
    usernames = {account.username for account in accounts}

    assert len(accounts) == len(uids)
    assert len(accounts) == len(usernames)

    for account in accounts:
        assert isinstance(account, Account)
        assert account.uid > 0
        assert account.username != ""
        assert account.email.startswith(account.username)


def test_account_data(account):
    assert isinstance(account, Account)
    assert account.uid > 0
    assert account.username != ""
    assert validators.email(account.email)

    username, domain = account.email.split("@")
    assert account.username == username
    assert validators.domain(domain)


@pytest.mark.parametrize("account__username", TEST_USERNAMES)
def test_account_data_overrides(account):
    assert account.username in TEST_USERNAMES

    username, _ = account.email.split("@")

    assert account.username == username
    assert username in TEST_USERNAMES


@pytest.mark.parametrize(
    ("account__username", "account__uid"),
    zip(
        TEST_USERNAMES,
        range(10000, 10003),
    ),
)
def test_account_multiple_data_overrides(account):
    assert account.username in TEST_USERNAMES
    assert 10000 <= account.uid < 10003

    username, _ = account.email.split("@")

    assert account.username == username
    assert username in TEST_USERNAMES


def test_account_excluded_data(account):
    with pytest.raises(AttributeError):
        account._domain  # noqa: WPS428, WPS437

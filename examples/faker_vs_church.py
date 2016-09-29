# Test
import cProfile

from faker import Faker

from church import Personal, Address

p = Personal('en_us')
a = Address('en_us')
f = Faker()


def test_faker_full_name():
    """
    Result:
    https://gist.github.com/lk-geimfari/19e92dac7568c1905c1e47d4425bcbf9
    """
    li = []
    for _ in range(4000):
        li.append(f.name())


def test_church_full_name():
    """
    Result:
    https://gist.github.com/lk-geimfari/f09cfc83303cb9f14829d214ad6acccd
    """
    li = []
    for _ in range(4000):
        li.append(p.full_name())


def test_faker_address():
    """
    Result:
    https://gist.github.com/lk-geimfari/7bb4b59bf0041b266f188612d06d94f8
    """
    li = []
    for _ in range(5000):
        li.append(f.address())


def test_church_address():
    """
    Result:
    https://gist.github.com/lk-geimfari/2863431bb969d7cc919e4bb86acd0d5e
    """
    li = []
    for _ in range(5000):
        li.append(a.address())


def test_faker_emails():
    """
    Result:
    https://gist.github.com/lk-geimfari/86536e967bd970727541fd24330050ea
    """
    li = []
    for _ in range(3000):
        li.append(f.email())


def test_church_emails():
    """
    Result:
    https://gist.github.com/lk-geimfari/61b86ddf49d4694eb171294153e3f26f
    """
    li = []
    for _ in range(3000):
        li.append(p.email())


# cProfile.run('test_faker_emails()')
cProfile.run('test_church_emails()')

# It is possible that you find an example an artificial, if so,
# I'll be glad to see the full comparison, but at the moment `church`
# generates data 10 times faster than ` faker`.

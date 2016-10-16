import time

import faker
import church

personal = church.Personal('en')
address = church.Address('en')
f = faker.Faker()


def chronos(func):
    def clock(*args):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, func.__name__, arg_str, result))
        return result

    return clock


@chronos
# [6.08868742s] test_faker_full_name() -> None
def test_faker_full_name():
    """
    Result (using cProfile):
    https://gist.github.com/lk-geimfari/19e92dac7568c1905c1e47d4425bcbf9
    """
    li = []
    for _ in range(4000):
        li.append(f.name())


@chronos
# [0.04863763s] test_church_full_name() -> None
def test_church_full_name():
    """
    Result (using cProfile):
    https://gist.github.com/lk-geimfari/f09cfc83303cb9f14829d214ad6acccd
    """
    li = []
    for _ in range(4000):
        li.append(personal.full_name())


@chronos
# [8.85601449s] test_faker_address() -> None
def test_faker_address():
    """
    Result (using cProfile):
    https://gist.github.com/lk-geimfari/7bb4b59bf0041b266f188612d06d94f8
    """
    li = []
    for _ in range(5000):
        li.append(f.address())


@chronos
# [0.12299252s] test_church_address() -> None
def test_church_address():
    """
    Result (using cProfile):
    https://gist.github.com/lk-geimfari/2863431bb969d7cc919e4bb86acd0d5e
    """
    li = []
    for _ in range(5000):
        li.append(address.address())


@chronos
# [7.57951045s] test_faker_emails() -> None
def test_faker_emails():
    """
    Result (using cProfile):
    https://gist.github.com/lk-geimfari/86536e967bd970727541fd24330050ea
    """
    li = []
    for _ in range(3000):
        li.append(f.email())


@chronos
# [0.02873206s] test_church_emails() -> None
def test_church_emails():
    """
    Result (using cProfile):
    https://gist.github.com/lk-geimfari/61b86ddf49d4694eb171294153e3f26f
    """
    li = []
    for _ in range(3000):
        li.append(personal.email())


if __name__ == '__main__':
    test_church_full_name()
    test_faker_full_name()
    # test_church_emails()
    # test_faker_emails()
    # test_church_address()
    # test_faker_address()

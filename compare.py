import time

from mimesis.providers import Cryptographic


# This function from Fluent Python by Luciano Ramalho.
def clock(func):
    def clocked(*args):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def performance_for(method, count, *args, **kwargs):
    _ = [method(*args, **kwargs) for _ in range(count)]
    del _
    return '{} done.'.format(method.__name__)


if __name__ == '__main__':
    c = Cryptographic()
    performance_for(c.mnemonic_code, 1000)

    c = Cryptographic()
    performance_for(c.new_mnemonic_code, 1000)

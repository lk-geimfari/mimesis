import pytest

from mimesis import Generic, Numeric


@pytest.mark.parametrize("seed", [0, 0x123])
def test_lazy_numeric_uses_latest_seed_and_reseeds_in_place(seed):
    generic = Generic(seed=0xABC)
    assert "numeric" not in generic.__dict__

    generic.reseed(seed)
    assert "numeric" not in generic.__dict__

    numeric = generic.numeric
    expected = Numeric(seed=seed)
    assert numeric.seed == seed
    assert numeric.random.getstate() == expected.random.getstate()
    assert numeric.increment() == 1

    numeric.random.getrandbits(32)
    generic.reseed(seed)

    assert generic.numeric is numeric
    assert numeric.random.getstate() == expected.random.getstate()
    assert numeric.increment() == 2

from pycpp import pycpp


def test_sum():
    assert 6 == pycpp.sum(4, 2)


def test_diff():
    assert 2 == pycpp.diff(4, 2)


def test_product():
    assert 8 == pycpp.product(4, 2)


def test_quotient():
    assert 2 == pycpp.quotient(4, 2)


def test_modulus():
    assert 0 == pycpp.modulus(4, 2)

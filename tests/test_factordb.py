import pytest
from factorizer import FactorDBFactorizer as Factorizer
from factorizer import TimeOutError


def test_ok_simple_case_timeout_empty():
    divider = Factorizer()
    facts = divider.factorize(57)
    assert facts == (3, 19)


def test_ok_simple_case_timeout_None():
    divider = Factorizer(timeout=None)
    facts = divider.factorize(57)
    assert facts == (3, 19)


def test_ok_simple_case_timeout_minus1():
    divider = Factorizer(timeout=-1)
    facts = divider.factorize(57)
    assert facts == (3, 19)


def test_ok_simple_case_timeout_5():
    divider = Factorizer(timeout=5)
    facts = divider.factorize(57)
    assert facts == (3, 19)


def test_ok_0():
    divider = Factorizer()
    facts = divider.factorize(0)
    assert facts == (0, 0)


def test_ok_1():
    divider = Factorizer()
    facts = divider.factorize(1)
    assert facts == (1, 1)


def test_ok_2():
    divider = Factorizer()
    facts = divider.factorize(2)
    assert facts == (1, 2) or facts == (2, 1)


def test_ok_3():
    divider = Factorizer()
    facts = divider.factorize(3)
    assert facts == (1, 3) or facts == (3, 1)


def test_ok_4():
    divider = Factorizer()
    facts = divider.factorize(4)
    assert facts == (2, 2)


def test_ok_6():
    divider = Factorizer()
    facts = divider.factorize(6)
    assert facts == (2, 3) or facts == (3, 2)


def test_ok_both_big():
    divider = Factorizer(timeout=5)
    n = 144483604528043653279487
    facts = divider.factorize(n)
    assert facts == (2147483647, 67280421310721)


def test_ok_even():
    divider = Factorizer(timeout=5)
    n = 2 * 3571
    facts = divider.factorize(n)
    assert facts == (2, 3571)    
    

def test_ok_square():
    divider = Factorizer(timeout=5)
    n = 97**2
    facts = divider.factorize(n)
    assert facts == (97, 97)


def test_ok_prime():
    divider = Factorizer(timeout=5)
    facts = divider.factorize(97)
    assert facts == (1, 97)


def test_ng_timeout():
    divider = Factorizer(timeout=0.0001)
    n = 3
    with pytest.raises(TimeOutError):
        facts = divider.factorize(n)
import pytest
from factorizer import PminusOneFactorizer as Factorizer
from factorizer import TimeOutError

def test_ok_simple_case_timeout_empty_step1():
    divider = Factorizer()
    facts = divider.factorize(57)
    assert facts == (3, 19)


def test_ok_simple_case_timeout_None_step1():
    divider = Factorizer(timeout=None)
    facts = divider.factorize(57)
    assert facts == (3, 19)


def test_ok_simple_case_timeout_minus1_step1():
    divider = Factorizer(timeout=-1)
    facts = divider.factorize(57)
    assert facts == (3, 19)


def test_ok_simple_case_timeout_5_step1():
    divider = Factorizer(timeout=5)
    facts = divider.factorize(57)
    assert facts == (3, 19)


def test_ok_0_step1():
    divider = Factorizer()
    facts = divider.factorize(0)
    assert facts == (0, 0)


def test_ok_1_step1():
    divider = Factorizer()
    facts = divider.factorize(1)
    assert facts == (1, 1)


def test_ok_2_step1():
    divider = Factorizer()
    facts = divider.factorize(2)
    assert facts == (1, 2) or facts == (2, 1)


def test_ok_3_step1():
    divider = Factorizer()
    facts = divider.factorize(3)
    assert facts == (1, 3) or facts == (3, 1)


def test_ok_4_step1():
    divider = Factorizer()
    facts = divider.factorize(4)
    assert facts == (2, 2)


def test_ok_6_step1():
    divider = Factorizer()
    facts = divider.factorize(6)
    assert facts == (2, 3) or facts == (3, 2)


def test_ok_M_1000_step1():
    divider = Factorizer()
    facts = divider.factorize(2885500349, M=1000)
    assert facts == (59359, 48611)


def test_ok_both_big_step1():
    divider = Factorizer(timeout=300)
    n = 144483604528043653279487
    facts = divider.factorize(n)
    assert facts == (2147483647, 67280421310721)


def test_ok_simple_case_timeout_empty_step2():
    divider = Factorizer(step=2)
    facts = divider.factorize(57, M=3, L=100)
    assert facts == (3, 19)


def test_ok_simple_case_timeout_None_step2():
    divider = Factorizer(timeout=None, step=2)
    facts = divider.factorize(57, M=3, L=100)
    assert facts == (3, 19)


def test_ok_simple_case_timeout_minus1_step2():
    divider = Factorizer(timeout=-1, step=2)
    facts = divider.factorize(57, M=3, L=100)
    assert facts == (3, 19)


def test_ok_simple_case_timeout_5_step2():
    divider = Factorizer(timeout=5, step=2)
    facts = divider.factorize(57, M=3, L=100)
    assert facts == (3, 19)


def test_ok_0_step2():
    divider = Factorizer(step=2)
    facts = divider.factorize(0)
    assert facts == (0, 0)


def test_ok_1_step2():
    divider = Factorizer(step=2)
    facts = divider.factorize(1)
    assert facts == (1, 1)


def test_ok_2_step2():
    divider = Factorizer(step=2)
    facts = divider.factorize(2)
    assert facts == (1, 2) or facts == (2, 1)


def test_ok_3_step2():
    divider = Factorizer(step=2)
    facts = divider.factorize(3)
    assert facts == (1, 3) or facts == (3, 1)


def test_ok_4_step2():
    divider = Factorizer(step=2)
    facts = divider.factorize(4)
    assert facts == (2, 2)


def test_ok_6_step2():
    divider = Factorizer(step=2)
    facts = divider.factorize(6)
    assert facts == (2, 3) or facts == (3, 2)


def test_ok_M_1000_step2():
    divider = Factorizer(step=2)
    facts = divider.factorize(2885500349, M=10, step=2)
    assert facts == (48611, 59359)


def test_ok_both_big_step2():
    divider = Factorizer(timeout=300, step=2)
    n = 144483604528043653279487
    facts = divider.factorize(n, M=100)
    assert facts == (2147483647, 67280421310721)
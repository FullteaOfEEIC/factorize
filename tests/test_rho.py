import pytest
from factorizer import PollardsRhoFactorizer as Factorizer
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
    assert facts == (2, 2) or facts == (1, 4)


def test_ok_6():
    divider = Factorizer()
    facts = divider.factorize(6)
    assert facts == (2, 3) or facts == (3, 2)


def test_ok_both_big():
    divider = Factorizer(timeout=300)
    n = 115792089237316195423570985008687907853269984665640564039457584007913129639937
    facts = divider.factorize(n)
    assert facts == (1238926361552897, 93461639715357977769163558199606896584051237541638188580280321)


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


def test_ng_both_big_timeout():
    divider = Factorizer(timeout=1)
    n = 17094896531810236860130284769490321915294047711310368136394905170386978916759334950349117125605720936295486193376534502996558346954298821541237678202872064373159864453975455700275218336138295073109837853052911442982249175483147894454735060228013876333548456070708161754022653432247114865681934678336369669630310417775703125135381535339600363990582556226874678712573925886711666498382111760727570796847908646797570295191362260110871270300928038772025787352463090061558150045455638071691578922379413464004696514186854056461649591756647526422083918100655183395966280798720122926503397649310956601613684952853243575941193
    with pytest.raises(TimeOutError):
        facts = divider.factorize(n)


def test_ok_c_1():
    divider = Factorizer(timeout=5, c=1)
    n = 2 * 3571
    facts = divider.factorize(n)
    assert facts == (2, 3571)    
    

def test_ok_c_minus1():
    divider = Factorizer(timeout=5, c=-1)
    n = 97**2
    facts = divider.factorize(n)
    assert facts == (97, 97)
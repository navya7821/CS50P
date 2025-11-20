from fuel import convert
from fuel import gauge
import pytest
def test_value():
    with pytest.raises(ValueError):
        convert('7/5')
def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('5/0')


def test_val():
    assert convert('1/2') == 50
    assert convert('2/3') == 67
def test_gauge():
    assert gauge(67) == '67%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'




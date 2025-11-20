import pytest
from working import convert
def test_amam():
    assert convert('5 AM to 7 AM') == '05:00 to 07:00'
    assert convert('5:00 AM to 8:00 AM') == '05:00 to 08:00'
def test_ampm():
    assert convert('3 AM to 3 PM') == '03:00 to 15:00'
    assert convert('4:20 AM to 3:24 PM') == '04:20 to 15:24'
def test_pmam():
    assert convert('1:23 PM to 3:28 AM') == '13:23 to 03:28'
    assert convert('2 PM to 8 AM') == '14:00 to 08:00'
def test_pmpm():
    assert convert('2:30 PM to 7:21 PM') == '14:30 to 19:21'
    assert convert('4 PM to 5 PM') == '16:00 to 17:00'
def test_rest():
    with pytest.raises(ValueError):
        convert('4 Am to 7PM')
    with pytest.raises(ValueError):
        convert('3:70 AM to 3:20 PM')
    with pytest.raises(ValueError):
        convert('cat')

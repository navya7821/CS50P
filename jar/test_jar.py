import pytest
from jar import Jar
def test_init():
    with pytest.raises(ValueError):
        Jar(-2)
def test_str():
    jar = Jar(10)
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(4)
    jar.deposit(4)
    with pytest.raises(ValueError):
        jar.deposit(4)
def test_withdraw():
    jar = Jar(5)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)




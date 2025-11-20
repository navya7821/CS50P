from numb3rs import validate
def test_single():
    assert validate("1.2.3.4") == True
    assert validate("1.1.1.1.") == False
def test_double():
    assert validate("12.23.33.45") == True
    assert validate("12.12.23") == False
def test_three():
    assert validate("123.145.180.201") == True
    assert validate("123.231") == False
def test_rule():
    assert validate("201.290.290.290") == False
    assert validate("0.0.0,0") == False
    assert validate("cat") == False
    assert validate("12.12.12.0.1") == False
    assert validate("12") == False

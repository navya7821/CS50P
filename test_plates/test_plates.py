from plates import is_valid
def test_length():
    assert is_valid('AA') == True
    assert is_valid('AAA') == True
    assert is_valid('AAABBBB') == False
    assert is_valid('AAAA') == True

def test_number_placement():
    assert is_valid('AA1') == True
    assert is_valid('1AA') == False
    assert is_valid('A1A') == False
    assert is_valid('AAA') == True
    assert is_valid('AA12') == True
    assert is_valid('12AA') == False
    assert is_valid('1AAA') == False
    assert is_valid('AA1A') == False
    assert is_valid('A1AA') == False


def test_four():
    assert is_valid('AA24') == True
    assert is_valid('AAA3') == True
    assert is_valid('12AB') == False

def test_five():
    assert is_valid('ABC12') == True
    assert is_valid('AAAA1') == True
    assert is_valid('A1234') == False

def test_six():
    assert is_valid('AA1234') == True
    assert is_valid('AAAA23') == True
    assert is_valid('AAAAAB12') == False
    assert is_valid('12AA34') == False

def test_alpha():
    assert is_valid('Abc!') == False
    assert is_valid('Abc@') == False
    assert is_valid('Abc#') == False

def test_zero():
    assert is_valid('AA01') == False
    assert is_valid('AA10') == True

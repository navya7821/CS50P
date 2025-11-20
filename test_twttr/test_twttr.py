from twttr import shorten


def test_upper_case():
    assert shorten('Abcd') == 'bcd'
    assert shorten('EBc') == 'Bc'
def test_lower_case():
    assert shorten('abc') == 'bc'
    assert shorten('peRkS') == 'pRkS'
def test_number():
    assert shorten('CSa50') == 'CS50'
    assert shorten('CSA50') == 'CS50'
def test_punc():
    assert shorten('Hello!') == 'Hll!'
    assert shorten('HELlO!') == 'HLl!'


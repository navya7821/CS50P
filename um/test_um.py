from um import count
def test_cases():
    assert count('um') == 1
    assert count('Heyum') == 0
    assert count('um,..') == 1
    assert count('um, hello!') == 1
    assert count('um! um') == 2
    assert count('UM hi um') == 2




from bank import value

def test_zero():
    assert value('hello') == 0
    assert value('hello!') == 0
def test_punc():
    assert value('Hello, mate') == 0
    assert value('hello mate') == 0
def test_twenty():
    assert value('Homophone') == 20
    assert value('Heeey') == 20

def test_hundred():
    assert value('What') == 100
    assert value("What's ur name?") == 100

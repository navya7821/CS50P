import os
from project import data_retrieval
from project import day_structure
from project import attendance
from project import percentage
def test_day_structure(monkeypatch):
    inputs = iter(['math','1','science','0',''])
    monkeypatch.setattr('builtins.input', lambda _:next(inputs))
    result = day_structure()
    expected = {'math':'1','science':'0'}
    assert result == expected

def test_data_retrieval():
    os.makedirs('Sem',exist_ok=True)
    with open('Sem/Week1','w') as file:
        file.write('math,1\nenglish,0\nscience,1')
    assert data_retrieval('','1') == [{'subject':'math','mark':'1'},
                                      {'subject':'english','mark':'0'},
                                      {'subject':'science','mark':'1'}]
def test_attendance():
    d = [{'subject':'math','mark':'1'},
         {'subject':'english','mark':'0'}]
    f = ([{'name': 'math', 'total': 1, 'attended': 1}, {'name': 'english', 'total': 1, 'attended': 0}] ,2, 1)
    assert attendance(d) == f


def test_percentage():
    a =  ([{'name': 'math', 'total': 1, 'attended': 1}, {'name': 'english', 'total': 1, 'attended': 0}])
    b = (50.0, {'math': 1.0, 'english': 0.0})
    assert percentage(a,2,1) == b



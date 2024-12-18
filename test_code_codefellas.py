
# Test Matrix Hands-On
 
def sum(a, b):
    return a + b
 
def subtraction(a, b):
    return a - b
 
def append_dictionary(dict1, dict2):
    # Added after Python 3.9
    return dict1 | dict2
 
################################
 
def test_sum():
    assert sum(2, 3) == 5 
    assert sum(-1, 1) == 0 
    assert sum(0, 0) == 0
    assert sum(0, 4) == 4
 
 
def test_subtraction():
    assert subtraction(5, 3) == 2 
    assert subtraction(0, 3) == -3 
    assert subtraction(3, 3) == 0  
 
 
def test_append_dictionary():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    result = append_dictionary(dict1, dict2)
    assert result == {"a": 1, "b": 2, "c": 3, "d": 4} 

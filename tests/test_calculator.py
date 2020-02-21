from simple_calculator.calculator import Calculator

calculator = Calculator()

def test_add_two_numbers():
    assert calculator.add(1,2) == 3

def test_add_many_numbers():
    assert calculator.add(1,2,3,4,5) == 15

def test_multiply_two_numbers():
    assert calculator.multiply(1,2) == 2

def test_multiply_many_numbers():
    assert calculator.multiply(2,2,3) == 12
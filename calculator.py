class Calculator:

    def __init__(self):
        pass
    # This function  adds the minimum of two numbers
    def add(self, *args):
        sum = 0
        for val in args:
            number = int(val)
            sum += number
        return sum
    # This function multiplies the minimum of two numbers
    def multiply(self, *args):
        product = 1
        for val in args:
            number = int(val)
            product *= number
        return product
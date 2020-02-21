class Calculator:

    def __init__(self):
        pass

    def add(self, *args):
        sum = 0
        for val in args:
            number = int(val)
            sum += number
        return sum

    def multiply(self, *args):
        product = 1
        for val in args:
            number = int(val)
            product *= number
        return product
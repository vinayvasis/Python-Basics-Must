"""
Closures are nothing but functions that are returned by another function. We use closures to remove code duplication.
In the following example we create a simple closure for adding numbers.
"""


def add_number(num):
    def adder(number):
        """adder is a closure"""
        return num + number

    return adder


a_10 = add_number(10)
print(a_10(21))

print(a_10(34))

a_5 = add_number(5)
print(a_5(3))

"""
Python iterator objects are required to support two methods while following the iterator protocol.

__iter__ returns the iterator object itself. This is used in for and in statements.

__next__ method returns the next value from the iterator. If there is no more items to return then it should raise

StopIteration exception.
"""

"""Example 1"""
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

"""Example 2"""
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

"""Example 3-----Create an iterator that returns numbers, starting with 1, and each sequence will increase by one 
(returning 1,2,3,4,5 etc.):
"""


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

"""Example 5-------Stop after 20 iterations:"""


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

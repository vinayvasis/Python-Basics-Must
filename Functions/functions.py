"""
1.abs()	Returns the absolute value of a number
2.all()	Returns True if all items in an iterable object are true
3.any()	Returns True if any item in an iterable object is true
4.ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
5.bin()	Returns the binary version of a number
6.bool()	Returns the boolean value of the specified object
7.bytearray()	Returns an array of bytes.
8.bytes()	Returns a bytes object
9.callable()	Returns True if the specified object is callable, otherwise False
10.chr()	Returns a character from the specified Unicode code.
11.classmethod()	Converts a method into a class method
12.compile()	Returns the specified source as an object, ready to be executed
13.complex()	Returns a complex number
14.delattr()	Deletes the specified attribute (property or method) from the specified object
15.dict()	Returns a dictionary (Array)
16.dir()	Returns a list of the specified object's properties and DataTypeMethods
17.divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
18.enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
19.eval()	Evaluates and executes an expression
20.exec()	Executes the specified code (or object)
21.filter()	Use a filter function to exclude items in an iterable object
22.float()	Returns a floating point number
23.format()	Formats a specified value
24.frozenset()	Returns a frozenset object
25.getattr()	Returns the value of the specified attribute (property or method)
26.globals()	Returns the current global symbol table as a dictionary
27.hasattr()	Returns True if the specified object has the specified attribute (property/method)
28.hash()	Returns the hash value of a specified object
29.help()	Executes the built-in help system
30.hex()	Converts a number into a hexadecimal value
31.id()	Returns the id of an object
32.input()	Allowing user input
33.int()	Returns an integer number
34.isinstance()	Returns True if a specified object is an instance of a specified object
35.issubclass()	Returns True if a specified class is a subclass of a specified object
36.iter()	Returns an iterator object
37.len()	Returns the length of an object
38.list()	Returns a list
39.locals()	Returns an updated dictionary of the current local symbol table
40.map()	Returns the specified iterator with the specified function applied to each item
41.max()	Returns the largest item in an iterable
42.memoryview()	Returns a memory view object
43.min()	Returns the smallest item in an iterable
44.next()	Returns the next item in an iterable
45.object()	Returns a new object
46.oct()	Converts a number into an octal
47.open()	Opens a file and returns a file object
48.ord()	Convert an integer representing the Unicode of the specified character
49.pow()	Returns the value of x to the power of y
50.print()	Prints to the standard output device
51.property()	Gets, sets, deletes a property
52.range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
53.repr()	Returns a readable version of an object
54.reversed()	Returns a reversed iterator
55.round()	Rounds a numbers
56.set()	Returns a new set object
57.setattr()	Sets an attribute (property/method) of an object
58.slice()	Returns a slice object
59.sorted()	Returns a sorted list
60.@staticmethod()	Converts a method into a static method
61.str()	Returns a string object
62.sum()	Sums the items of an iterator
63.super()	Returns an object that represents the parent class
64.tuple()	Returns a tuple
65.type()	Returns the type of an object
66.vars()	Returns the __dict__ property of an object
67.zip()	Returns an iterator, from two or more iterators
"""

"""1.abs"""
x = -1.23
print(abs(x))

"""2.all"""
l = [1, 2, 3]
print(all(l))
l1 = [1, 2, 3, 0]
print(all(l1))

"""3.any"""
print(any(l1))

"""4.ascii---not to get ascii value only to get readable version"""
a = "My name is Ståle"
print(ascii(a))

"""5.bin"""
x = 3
print(bin(x))

"""6.bool"""
y = 0
print(bool(x))
print(bool(y))

"""7.bytearray"""
print(bytearray(x))

"""8.bytes"""
print(bytes(x))

"""9.callable"""


def fun(z):
    print(z)


cld = fun
print(callable(x))
print(callable(l))
print(callable(cld))

"""10.chr---returns ascii value of a digit"""
print(chr(97))
print(chr(122))

"""11.classmethod"""
print(classmethod(x))

"""12.compile"""
codeInString = 'a = 5\nb=6\nsum1=a+b\nprint("sum =",sum1)'
codeObejct = compile(codeInString, 'sumstring', 'exec')

exec(codeObejct)

"""13.complex"""
print(complex(12))

"""14.delattr"""


class Example:
    def __init__(self, a):
        self.a = a


# creating an object
obj = Example(5)
print(obj.a)

# Now removing attribute x
delattr(obj, 'a')
# print(obj.a) """this gives error becasues attribute has been removed"""

"""15.dict"""
# dict(**kwarg)
# dict([mapping, **kwarg])
# dict([iterable, **kwarg])

# dict(**kwarg)
print(dict(m=10, y=12))

# dict([mapping, **kwarg])
print(dict({'m': 10, 'y': 12}, c=12))

# dict([iterable, **kwarg])
print(dict([(1, 2), (3, 4)], l=12))

"""16.dir"""
print(dir(x))

"""17.divmod"""
print(divmod(10, 5))

"""18.enumerate"""
print(enumerate((1, 2, 3)))

"""19.eval"""
print(eval('10+1'))

"""20.exec"""
prog = 'print("The sum of 5 and 10 is", (5+10))'
exec(prog)

"""21.filter"""
l2 = [1, 2, 3]
x = list(filter(lambda x: x % 2, l2))
print(x)

"""22.float"""
print(float(2))

"""23.format"""
strd = "This article is written in {}"
print(strd.format("Python"))

"""24.frozenset"""
print(frozenset(l2))

"""25.getattr"""


class Example:
    def __init__(self, a):
        self.a = a


# creating an object
obj = Example(5)
print(obj.a)

# Now removing attribute x
print(getattr(obj, 'a'))

"""26.globals"""
print(globals())

"""27.hasattr"""
print(hasattr(obj, 'a'))
print(hasattr(obj, 'y'))

"""28.hash"""
print(hash(12))
print(hash((1, 2, 3)))

"""29.help"""
# print(help())

"""30.hex"""
print(hex(12))

"""31.id"""
print(id(12))

"""32.input"""
# x = input("enter input")
print(x)

"""33.int"""
print(int(13.02))

"""34.isinstance"""


class Foo:
    a = 5


fooInstance = Foo()
print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))
numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers, 'instance of list?', result)

"""35.issubclass"""


class Polygon:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__('triangle')


print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))

"""36.iter"""
l = [1, 2, 3, 4]
it = iter(l)
print(next(it))
print(next(it))

"""37.len"""
print(len({'1': 1, '2': '2'}))

"""38.list"""
x = (1, 2, 3)
y = {'1': 1, '2': '3'}
z = "abc+xyz"
print(list(x))
print(list(y))
print(list(z))

"""39.locals"""
print(locals())

"""40.map"""


# 1
def addition(n):
    return n + n


numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# 2
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# 3
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# 4
l = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, l))
print(test)

"""41.max"""
print(max(1, 2, 3))
print(max([1, 2, 3]))

"""42.memoryview"""
byte_array = bytearray('XYZ', 'utf-8')
print('Before update:', byte_array)
mem_view = memoryview(byte_array)
mem_view[2] = 74
print('After update:', byte_array)

"""43.min"""
print(min(1, 2, 3))
print(min([1, 2, 3]))

"""44.next"""
l = [1, 2, 3, 4]
it = iter(l)
print(next(it))
print(next(it))

"""45.object"""

x = object()
print(type(x))
print(dir(x))

"""46.oct"""
print(oct(12))

"""47.open"""
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test1.txt", "r")
print(f.read())
f.close()

"""48.ord"""
print(ord('a'))
print(ord('V'))

"""49.pow"""
x = 2
print(pow(x, 4))

"""50.print"""
print("HI")

"""51.property"""


class Alphabet:
    def __init__(self, value):
        self._value = value

        # getting the values

    def getValue(self):
        print('Getting value')
        return self._value

        # setting the values

    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

        # deleting the values

    def delValue(self):
        print('Deleting value')
        del self._value

    value = property(getValue, setValue, delValue, )


x = Alphabet('GeeksforGeeks')
print(x.value)
x.value = 'GfG'
del x.value

"""52.range"""
for x in range(1, 10):
    print(x)

"""53.repr"""


class Foo:
    a = 5


fooInstance = Foo()
print(repr(fooInstance))

"""54.reversed"""
l = [1, 2, 3]
x = reversed(l)
for y in x:
    print(y)

"""55.round"""
print(round(1.23456, 2))
print(round(1.23456))

"""56.set"""
lis1 = [3, 4, 1, 4, 5]
tup1 = (3, 4, 1, 4, 5)
print(set(lis1))
print(set(tup1))

"""57.setattr"""


class Person:
    name = 'Adam'


p = Person()
# setting attribute name to None
setattr(p, 'name', None)
print('Name is:', p.name)
# setting an attribute not present
# in Person
setattr(p, 'age', 23)
print('Age is:', p.age)

"""58.slice"""
pyString = 'Python'
sObject = slice(3)
print(pyString[sObject])
sObject = slice(1, 5, 2)
print(pyString[sObject])

"""59.sorted"""
l = [5, 1, 2, 3, 4]
x = sorted(l)
print(x)

"""60.@staticmethod()---unpythonic way instead use decorator"""


class Mathematics:

    def addNumbers(x, y):
        return x + y


# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))

"""61.str"""
x = str('xyz')
y = str(2)
print(x)
print(type(x))

"""62.sum"""
print(sum({1, 2, 3, 4, 5}))

"""63.super"""


class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()

"""64.tuple"""
l = [1, 2, 3, 4, 5]
x = tuple(l)
print(x)

"""65.type"""
print(type(x))

"""66.vars"""


class Geeks:
    def __init__(self, name1="Arun", num2=46, name3="Rishab"):
        self.name1 = name1
        self.num2 = num2
        self.name3 = name3


GeeksforGeeks = Geeks()
print(vars(GeeksforGeeks))

"""67.zip"""
numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting itertor to list
resultList = list(result)
print(resultList)

# Two iterables are passed
result = zip(numberList, strList)

# Converting itertor to set
resultSet = set(result)
print(resultSet)

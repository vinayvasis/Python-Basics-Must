"""
1.count
2.index
"""

"""1.count"""
a = (1, 2, 3, 1)
x = a.count(1)
print(x)

"""2.index---   NOTE::: this syntax does not apply for tuples:: --index(element,start,end)"""
x = a.index(1)
print(x)
y = a.index(1, 1, 3)
print(y)

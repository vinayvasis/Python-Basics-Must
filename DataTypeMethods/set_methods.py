"""
1.add() Adds an element to the set
3.2.clear()	Removes all the elements from the set
4.copy()	Returns a copy of the set
5.difference()	Returns a set containing the difference between two or more sets
6.difference_update()	Removes the items in this set that are also included in another, specified set
7.discard()	Remove the specified item
8.intersection()	Returns a set, that is the intersection of two other sets
9.intersection_update()	Removes the items in this set that are not present in other, specified set(s)
10.isdisjoint()	Returns whether two sets have a intersection or not
11.issubset()	Returns whether another set contains this set or not
12.issuperset()	Returns whether this set contains another set or not
13.pop()	Removes an element from the set
14.remove()	Removes the specified element
15.symmetric_difference()	Returns a set with the symmetric differences of two sets
16.symmetric_difference_update()	inserts the symmetric differences from this set and another
17.union()	Return a set containing the union of sets
18.update()	Update the set with the union of this set and others"""

s = {1, 2, 3}
s1 = {3, 4, 5}

"""1.add"""
print(s.add(4))
print(s)

"""2.clear"""
print(s.clear())
print(s)

"""3.4.copy"""
a = s1.copy()
print(a)

"""5.difference"""
b = {3, 4, 5}
c = {1, 2, 3}
print(s1.difference(b))
print(s1.difference(c))

"""6.difference_update"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
b.difference_update(c)
print(b)

"""7.discard"""
print(x.discard('apple'))
print(x)

"""8.intersection"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"sap", "nam"}
print(x.intersection(y))
print(x)

"""9.intersection_update"""
print(x.intersection_update(y))
print(x)

"""10.isdisjoint"""
print(x.isdisjoint(y))
print(x.isdisjoint(z))

"""11.issubset"""
print(x.issubset(y))

"""12.issuperset"""
print(x.issuperset(y))

"""13.pop"""
print(x)
print(x.pop())
print(x)

"""14.remove"""
print(y)
print(y.remove('microsoft'))
print(y)

"""15.symmetric_difference"""
s = {1, 2, 3}
s1 = {3, 4, 5}
print(s.symmetric_difference(s1))

"""16.symmetric_difference_update"""
s.symmetric_difference_update(s1)
print(s)
print(s1)

"""17.union"""
print(s.union(s1))

"""18.update"""
print(s)
s.update(s1)
print(s)

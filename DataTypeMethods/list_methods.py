"""
1.append
2.clear
3.copy
4.count
5.extend
6.index
7.insert
8.pop
9.remove
10.reverse
11.sort
"""

a = [1, 2, 3]
b = [4, 5, 6]
c = [1, 2, 3]

"""1.append"""
a.append(1)
print(a)
a.append([1, 2, 3])
print(a)

"""2.clear"""
a.clear()
print(a)
a *= 0
print(a)
del a[:]
print(a)

"""3.copy"""
d = c.copy()
print(d)

# shallowcopy  and deepcopy
import copy

# copy of object is copied
li1 = [1, 2, [3, 5], 4]
li2 = copy.deepcopy(li1)
print(li2)
li2[2][0] = 7
print(li2)
print(li1)

# copy of object with reference is copied
li1 = [1, 2, [3, 5], 4]
li2 = copy.copy(li1)
print(li2)
li2[2][0] = 7
print(li2)
print(li1)

"""4.count"""
x = c.count(1)
print(x)
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
print(random.count('a'))
print(random.count(('a', 'b')))
print(random.count([3, 4]))

"""5.extend"""
c.extend(b)
print(c)
c.extend([(1, 2), {1: 2}])
print(c)

"""6.index --index(element,start,end)"""
x = b.index(5)
print(x)
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
print(list1.index(1, 1, 5))

"""7.insert ---insert(index,object)"""
a.insert(1, 2)
print(a)
print(a.index(2))
a.insert(0, 1)
print(a)
print(a.index(1))
print(a.index(2))

"""8.pop"""
a.pop(-1)
print(a)
a.pop()
print(a)
# del if you only want to use one list:
del a[0:]
print(a)

"""9.remove"""
animal = ['cat', 'dog', 'dog', 'rabbit', 'guinea pig']
animal.remove('cat')
print(animal)
animal.remove('dog')
print(animal)

"""10.reverse"""
animal.reverse()
print(animal)
x = animal[::-1]
print(x)

"""11.sort"""
sr = [4, 2, 1, 5, 5, 7, 3, 8, 0]
sr.sort()
print(sr)
sr.sort(reverse=True)
print(sr)

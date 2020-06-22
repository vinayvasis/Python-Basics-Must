"""
1.clear()	Removes all the elements from the dictionary
2.copy()	Returns a copy of the dictionary
3.fromkeys()	Returns a dictionary with the specified keys and values
4.get()	Returns the value of the specified key
5.items()	Returns a list containing a tuple for each key value pair
6.keys()	Returns a list containing the dictionary's keys
7.pop()	Removes the element with the specified key
8.popitem()	Removes the last inserted key-value pair
9.setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
10.update()	Updates the dictionary with the specified key-value pairs
11.values()	Returns a list of all the values in the dictionary
"""

d = {'1': 'a', '2': 'b'}
e = {'1': 'a', '2': 'b'}
"""1.clear"""
print(d.clear())
print(d)

"""2.copy"""
a = d.copy()
print(a)

"""3.fromkeys"""
StarWars = ('Luke', 'Vader', 'Ray', 'Yoda')
StarTrek = ('Spock')
universe = dict.fromkeys(StarWars, StarTrek)
print(universe)
StarWars = ['Luke', 'Vader', 'Ray', 'Yoda']
StarTrek = ['Spock']
universe = dict.fromkeys(StarWars, StarTrek)
print(universe)

"""4.get"""
print(e.get('1'))

"""5.items"""
print(e.items())

"""6.keys"""
print(e.keys())

"""7.pop"""
print(e.pop('1'))
print(e)

"""8.popitem"""
print(e.popitem())
print(e)

"""9.setdefault"""
f = {'1': 'a', '2': 'b'}
print(f.setdefault('1'))
print(f.setdefault('c', '3'))
print(f)

"""10.update"""
o = {'2': 'dfj'}
print(f.update({'1': 'vin'}))
print(f.update(o))
print(f)

"""11.values"""
print(f.values())

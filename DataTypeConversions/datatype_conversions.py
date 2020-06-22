"""
1.List
2.Tuple
3.String
4.Dictionary
5.Set
"""

"""1.List - Tuple"""
l = [1, 2, 3]
t = tuple(l)
print(t)

"""1.List - String"""
# Using join()
s = [str(i) for i in l]
res = str("".join(s))
print(res)
print(type(res))
# Using map()
res = str("".join(map(str, l)))
print(res)
print(type(res))

"""1.List - Dictionary"""
d = dict.fromkeys(l)
print(d)

d = {i: None for i in l}
print(d)

d = {i: l[i] for i in range(0, len(l))}
print(d)

# Convert two lists to a dictionary

l1 = ["hello", "at", "test", "this", "here", "now"]
l2 = [56, 23, 43, 97, 43, 102]

zipbObj = zip(l1, l2)
d = dict(zipbObj)
print(d)

# Convert a list of tuples to dictionary
l3 = [("Riti", 11), ("Aadi", 12), ("Sam", 13), ("John", 22), ("Lucy", 90)]
d = dict(l3)
print(d)

"""1.List - Set"""
st = set(l)
print(st)

"""2.Tuple - List"""
t = (1, 2, 3)
l = list(t)
print(l)
print(type(l))

"""2.Tuple - String"""
# Using join()
s = [str(x) for x in t]
res = str("".join(s))
print(res)
print(type(res))
# Using map()
res = str("".join(map(str, t)))
print(res)
print(type(res))

"""2.Tuple - dictionary """
d = dict.fromkeys(t)
print(d)

# Convert a tuple of tuples to dictionary
t1 = (('a', 1), ('b', 2))
d = dict(t1)
print(d)

# Another method
d = dict((x, y) for x, y in t1)
print(d)

# Another Method
d = dict(map(reversed, t1))
print(d)

"""2.Tuple - set """
st = set()
for x, y in t1:
    st.add(x)
    st.add(y)
print(st)

"""3.String - List """
s = "vinay"
l = list(s)
print(l)

l = list()
l.append(s)
print(l)

"""3.String - Tuple"""
t = tuple(s)
print(t)

t = tuple()
a = list(t)
a.append(s)
t = tuple(a)
print(t)

"""3.String - Dictionary"""
d = dict.fromkeys(s)
print(d)

"""3.String - Set"""
st = set()
for x in s:
    st.add(x)
print(st)

st = set()
st.add(s)
print(st)

"""4.Dictionary - List"""
d = {'a': 1, 'b': 2}
l = list(d)
print(l)

l = list()
for x, y in d.items():
    l.append(x)
    l.append(y)
print(l)

"""4.Dictionary - Tuple """
t = tuple(d)
print(t)

t = tuple()
a = list(t)
for x, y in d.items():
    a.append(x)
    a.append(y)
t = tuple(a)
print(t)

"""4.Dictionary - String"""
s = str(d)
print(s)

"""5.Set - List"""
st = {1, 2, 3, 4}
l = list(st)
print(l)

"""5.Set - Tuple"""
t = tuple(st)
print(t)

"""5.Set - Dictionary"""
d = dict.fromkeys(st)
print(d)

"""5.Set - string"""
s = [str(x) for x in st]
res = str("".join(s))
print(res)

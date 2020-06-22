"""
1.capitalize()	Converts the first character to upper case
2.casefold()	Converts string into lower case
3.center()	Returns a centered string
4.count()	Returns the number of times a specified value occurs in a string
5.encode()	Returns an encoded version of the string
6.endswith()	Returns true if the string ends with the specified value
7.expandtabs()	Sets the tab size of the string
8.find()	Searches the string for a specified value and returns the position of where it was found
9.format()	Formats specified values in a string
10.format_map()	Formats specified values in a string
11.index()	Searches the string for a specified value and returns the position of where it was found
12.isalnum()	Returns True if all characters in the string are alphanumeric
13.isalpha()	Returns True if all characters in the string are in the alphabet
14.isdecimal()	Returns True if all characters in the string are decimals
15.isdigit()	Returns True if all characters in the string are digits
16.isidentifier()	Returns True if the string is an identifier
17.islower()	Returns True if all characters in the string are lower case
18.isnumeric()	Returns True if all characters in the string are numeric
19.isprintable()	Returns True if all characters in the string are printable
20.isspace()	Returns True if all characters in the string are whitespaces
21.istitle()	Returns True if the string follows the rules of a title
22.isupper()	Returns True if all characters in the string are upper case
23.join()	Joins the elements of an iterable to the end of the string
24.ljust()	Returns a left justified version of the string
25.lower()	Converts a string into lower case
26.lstrip()	Returns a left trim version of the string
27.maketrans()	Returns a translation table to be used in translations
28.partition()	Returns a tuple where the string is parted into three parts
29.replace()	Returns a string where a specified value is replaced with a specified value
30.rfind()	Searches the string for a specified value and returns the last position of where it was found
31.rindex()	Searches the string for a specified value and returns the last position of where it was found
32.rjust()	Returns a right justified version of the string
33.rpartition()	Returns a tuple where the string is parted into three parts
34.rsplit()	Splits the string at the specified separator, and returns a list
35.rstrip()	Returns a right trim version of the string
36.split()	Splits the string at the specified separator, and returns a list
37.splitlines()	Splits the string at line breaks and returns a list
38.startswith()	Returns true if the string starts with the specified value
39.strip()	Returns a trimmed version of the string
40.swapcase()	Swaps cases, lower case becomes upper case and vice versa
41.title()	Converts the first character of each word to upper case
42.translate()	Returns a translated string
43.upper()	Converts a string into upper case
44.zfill()	Fills the string with a specified number of 0 values at the beginning
"""

name = "vinayvy{}"
nam = "VINay"
"""1.capitalize"""
print(name.capitalize())

"""2.casefold"""
print(name.casefold())

"""3.center----only to leave spaces"""
print(name.center(50))

"""4.count"""
print(name.count('v'))

"""5.encode"""
print(name.encode())

"""6.endswith---endswith(sting,start,end)"""
print(name.endswith('nay', 0, -1))

"""7.expandtabs---default=8"""
c = "Original\tstring: "
print(c.expandtabs())
print(c.expandtabs(tabsize=12))
print(c.expandtabs(24))

"""8.find"""
print(name.find('v', 1, -1))

"""9.format"""
print(name.format("PYTHON"))

"""10.format_map"""
a = {'x': 'John', 'y': 'Wick'}
print("{x}'s last name is {y}".format_map(a))

"""11.index"""
print(name.index('}'))

"""12.isalnum"""
c = "abc123"
print(c.isalnum())

"""13.isalpha"""
d = "vin"
print(name.isalpha())
print(d.isalpha())

"""14.isdecimal"""
e = "123"
print(name.isdecimal())
print(e.isdecimal())

"""15.isdigit"""
print(e.isdigit())

"""16.isdigit"""
print(e.isdigit())

"""16.isidentifier"""
print(d.isidentifier())
print(e.isidentifier())
print(name.isidentifier())

"""17.islower"""
f = "VINAY"
print(name.islower())
print(f.islower())

"""18.isnumeric"""
print(name.isnumeric())
print(e.isnumeric())

"""19.isprintable"""
g = "`\nvinay"
print(name.isprintable())
print(g.isprintable())

"""20.isspace"""
h = "   \t"
print(name.isspace())
print(h.isspace())

"""21.istitle"""
"""String which has the first character in each word Uppercase and remaining all characters Lowercase alphabets."""
i = "Vinay Is Good"
print(name.istitle())
print(i.istitle())

"""22.isupper"""
print(f.isupper())

"""23.join----join(iterable)"""
l1 = ['1', '2', '3']
s1 = 'abc'
s2 = '123'
test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))
print(name.join(l1))
print(s1.join(s2))
print(s2.join(s1))

"""24.ljust"""
print(name.ljust(50, 'V'))

"""25.lower"""
print(name.lower())
print(f.lower())

"""26.lstrip"""
j = "s  vinay"
print(j.lstrip('s'))

"""27.maketrans"""
dicts = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dicts))
# first string
firstString = "abc"
secondString = "def"
print(string.maketrans(firstString, secondString))

"""28.partition"""
"""If the separator string is not found, then the 3-tuple contains the string itself followed by two empty strings."""
print(name.partition('nay'))
print(name.partition('2018'))

"""29.replace"""
print(name.replace('vin', 'san'))

"""30.rfind---returns last position"""
print(name.rfind('n', 0, -1))

"""31.rindex----returns last position"""
print(name.rindex('v'))

"""32.rjust"""
print(name.rjust(50, "d"))

"""33.rpartition"""
"""Python String rpartition() splits the string at the last occurrence of the separator string. 
If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself."""
print(name.rpartition("n"))
print(name.rpartition('2018'))
s = 'ABCBA'
parts_tuple = s.partition('B')
print(parts_tuple)
parts_tuple = s.rpartition('B')
print(parts_tuple)

"""34.rsplit"""
print(name.rsplit('vin'))
s = 'Python is Awesome'
str_list = s.rsplit(sep=' ')
print(str_list)

str_list = s.rsplit(sep=' ', maxsplit=1)
print(str_list)
s = 'Hi||Hello||Adios'
str_list = s.rsplit('||')
print(str_list)

"""35.rstrip"""
print(name.rstrip())
s1 = '  abc  '
print(s1.rstrip())
print(s1.lstrip())
print(s1.strip())

"""36.split"""
print(name.split(sep='v', maxsplit=2))

"""37.splitlines"""
s2 = 'abc\n123\n234'
print(s2.splitlines())

"""38.startswith"""
print(name.startswith('vin'))

"""39.strip"""
s1 = '  abc  '
print(s1.strip())

"""40.swapcase"""
print(name.swapcase())
print(f.swapcase())

"""41.title"""
print(name.title())
print(f.title())

"""42.translate"""
# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"
string = "abcdef"
print("Original string:", string)
translation = string.maketrans(firstString, secondString, thirdString)
# translate string
print("Translated string:", string.translate(translation))

"""43.upper"""
print(name.upper())
print(firstString.upper())

"""44.zfill"""
print(name.zfill(30))

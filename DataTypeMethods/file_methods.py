"""
1.close()	Closes the file
2.detach()	Returns the separated raw stream from the buffer
3.fileno()	Returns a number that represents the stream, from the operating system's perspective
4.flush()	Flushes the internal buffer
5.isatty()	Returns whether the file stream is interactive or not
6.read()	Returns the file content
7.readable()	Returns whether the file stream can be read or not
8.readline()	Returns one line from the file
9.readlines()	Returns a list of lines from the file
10.seek()	Change the file position
11.seekable()	Returns whether the file allows us to change the file position
12.tell()	Returns the current file position
13.truncate()	Resizes the file to a specified size
14.writeable()	Returns whether the file can be written to or not
15.write()	Writes the specified string to the file
16.writelines()	Writes a list of strings to the file
"""

"""1.close"""
file = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//event.json", "r")
print(file.read())
file.close()

"""2.detach"""
"""Returns the separated raw stream from the buffer"""

"""3.fileno"""
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test.txt", "a")
print(f.fileno())

"""4.flush"""
f.write("Now the file has one more line!")
f.flush()
f.write("...and another one!")

"""5.isatty"""
print(f.isatty())
f.close()

"""6.read"""
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test.txt", "r")
print(f.read())

"""7.readable"""
print(f.readable())
f.close()

"""8.readline"""
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test1.txt", "r")
print(f.readline())
f.close()

"""9.readlines"""
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test1.txt", "r")
print(f.readlines())
f.close()

"""10.seek"""
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test1.txt", "r")
f.seek(2)
print(f.read())

"""11.seekable"""
print(f.seekable())

"""12.tell"""
f.seek(5)
print(f.tell())
f.close()

"""13.truncate"""
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test1.txt", "a")
f.truncate(5)
f.close()

# open and read the file after the truncate:
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test1.txt", "r")
print(f.read())

"""14.writeable"""
print(f.writable())
f.close()
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test1.txt", "a")
print(f.writable())
f.close()

"""15.write"""
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test1.txt", "a")
f.write('"vinay"')
f.close()
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test1.txt", "r")
print(f.read())
f.close()

"""16.writelines"""
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test1.txt", "a")
f.writelines(['"file"', '"bye"'])
print(f.close())
f = open("C://Users//vinay.muralikrishna//PycharmProjects//pytest//test1.txt", "r")
print(f.read())
f.close()


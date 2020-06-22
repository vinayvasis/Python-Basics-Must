f = open("demofile.txt", 'r')
# method one
print(f.read())


# method two
for line in f:
    print(line)


"""  Read Only Parts of the File  """
print(f.read(8))


""" Read Line """
print(f.readline())

""" Read Lines """
print(f.readlines())

""" Read Multiple Lines """
print(f.readline())
print(f.readline())

""" Close Files """
f.close()

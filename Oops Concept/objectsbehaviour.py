class Parrot:
#instance attributes
    def __init__(self,name,age):
        self.name =  name
        self.age  = age

#instance DataTypeMethods
    def sing(self,song):
        return "{} sings a {}".format(self.name,song)

    def dance(self):
        return "{} is now dancing".format(self.name)

blu = Parrot('vin',age=24)

print(blu.sing("'hello'"))
print(blu.dance())


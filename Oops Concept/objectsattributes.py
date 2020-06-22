class Parrot:


    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

blu = Parrot('vin',24)
woo = Parrot('san',28)


print(blu.species)
print("blu is a {}".format(blu.__class__.species))
print("woo is also a {}".format(woo.__class__.species))


print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))

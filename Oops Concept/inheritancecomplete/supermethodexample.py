class Bird():
    def __init__(self,first, last):
        self.first_name = first
        self.last_name = last

    def fly(self):
        return f'{self.first_name}{self.last_name}'

class Parrot(Bird):

    def __init__(self, first, last, middle):
        super().__init__(first, last)
        self.middle_name = middle

object = Parrot('v','i','n')
print(object.__dict__)
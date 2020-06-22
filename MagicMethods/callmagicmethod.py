class Myclass(object):
    def __init__(self, var_1, var_2, var_3):
        self.var_1 = var_1
        self.var_2 = var_2
        self.var_3 = var_3

    # we can use as like this also
    # def __call__(self, var1, var2):
    #     self.var_1 = var1
    #     self.var_2 = var2

    def __call__(self, *args):
        self.var_1, self.var_2 = args


object = Myclass(1,2,3)
print(object.__dict__)
print(id(object))

object.__call__(4,5)
print(object.__dict__)
print(id(object))
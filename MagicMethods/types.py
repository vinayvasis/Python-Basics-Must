"""
https://towardsdatascience.com/magic-methods-in-python-by-example-16b6826cae5c
"""


class MycustomList(list):

    def __getitem__(self, index):
        if index == 0:
            raise ValueError
        index = index - 1
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index == 0:
            raise ValueError
        index = index - 1
        return  list.__setitem__(self,index,value)

    def __delitem__(self, index):
        index = index - 1
        return  list.__delitem__(self, index)

    def __mul__(self, other):
        mul_list = [x * y for x, y in zip(self, other)]
        return MycustomList(mul_list)

lis_one = MycustomList([1,2,3,4,5])

#This will call __getitem__ to get index of that value
print(lis_one[2])


#This will call __setitem__ method which sets first element in a list to 100
lis_one[1] = 100
print(lis_one)

#This will cal __delitem__ method which deletes value by indexing using del keyword.
del lis_one[1]
print(lis_one)

#This will return a multiplication of two list objects one is self, which is lis_one and other is lis_two
lis_one = MycustomList([1,2,3,4,5])
print(lis_one)
lis_two = MycustomList([1,2,3,4,5])
print(lis_two)
lis_three = lis_one * lis_two
print(lis_three)
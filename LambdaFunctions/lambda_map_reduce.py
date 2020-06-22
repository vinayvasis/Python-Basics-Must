""" Use of lambda() """


# def cube(y):
#     return y * y * y
#
#
# g = lambda x: x * x * x
# print(g(7))
#
# print(cube(7))
#
# """ Use of lambda() with filter() """
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(filter(lambda x: (x % 2 != 0), li))
# print(final_list)

""" Use of lambda() with map() """
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(final_list)

# """ Use of lambda() with reduce() """
# from functools import reduce
#
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print(sum)

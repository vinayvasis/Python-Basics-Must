""" syntax::--   output_list = [output_exp for var in input_list if (var satisfies this condition)]  """

""" Example 1"""
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:", list_using_comp)

""" Example 2"""
list_using_comp = [var ** 2 for var in range(1, 10)]

print("Output List using list comprehension:", list_using_comp)


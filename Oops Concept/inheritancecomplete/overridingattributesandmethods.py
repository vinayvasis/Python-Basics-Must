"""
https://medium.com/@rajdhakad/python-the-complete-inheritance-tutorial-786b584475ea

"""

class Rectangle():
    sides = 4
    all_sides_equal = False
    opp_sides_equal = True
    type = 'rectangle'

    def area(self):
        length = int(input("Enter length :"))
        width = int( input( "Enter width : "))
        return length * width

class Square(Rectangle):
    # overriding necessary attributes
    all_sides_equal = True
    type = 'square'

    #overriding area method
    def area(self):
        side = int(input('Enter Sides :'))
        return side ** 2


rect_obj = Rectangle().area()
print(rect_obj)

sqr_obj = Square().area()
print(sqr_obj)
from math import pi


#impure function
def calculate_circle_area1(radius):
    area = pi * (radius)**2
    print('The area of the circle is ', area)
    return area


#pure function
def calculate_circle_area(radius):
    return pi * (radius)**2


calculate_circle_area1(3)

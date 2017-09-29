# Name:
#
# Date:
#
# Period:
#
# Description:  Define the functions described in comments below.
#               Functions should all work with sample input/output
#               as well as other cases
import math


def rect_area(length: float, width: float):
    """returns the area of a rectangle with a given length and width"""

    return length * width


def rect_perimeter(length: float, width: float):
    """returns the perimeter of a rectangle with a given length and width"""

    return 2 * (length + width)


def triangle_area(base: float, height: float):
    """returns the area of a triangle with a given length and width"""

    return base * height / 2


def circle_area(radius: float):
    """returns the area of a circle with a given radius"""

    return radius ** 2 * math.pi


def circle_circumference(radius: float):
    """returns the circumference of a circle  with a given radius"""

    return 2 * math.pi * radius


def calculate_slope(x1: float, y1: float, x2: float, y2: float):
    """Returns the slope between the 2 points (x1, y1) and (x2, y2)"""

    return (y1 - y2) / (x1 - x2)



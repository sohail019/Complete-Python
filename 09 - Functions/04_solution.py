# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle_calculation(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return area, circumference


a , c = circle_calculation(3)

print("Area:", round(a, 2), '- Circumference:', round(c, 2))
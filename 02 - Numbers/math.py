import math

#-------------------------------------------------------------
print('--------------------------Math Built in------------------------')
# Built in Math - Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

# Min and Max
print(min(1, 2, 3))  # 1
print(max(1, 2, 3))  # 3

# Absolute - returns positive numbers
print(abs(-7521))  # 7521

# Power - returns the value of x to the power y
print(pow(3, 2))  # 9

# ----------------------------------------------------------------
print('--------------------------Math Module------------------------')
# Math Module
# import math already imported in line 1

# Square root of a number
print(math.sqrt(4))  # 2.0

# Ceil - Rounds a number upwards to it's nearest integer
print(math.ceil(3.5))  # 4
print(math.ceil(-3.5))  # -3

# Floor - Rounds a number downwards to it's nearest integer
print(math.floor(3.5))  #3
print(math.floor(-3.5))  #-4

# Trunc - Returns the truncated integer parts of a number
print(math.trunc(3.5))  # 3
print(math.trunc(-3.5))  # -3

# PI - returns the value of pi
print(math.pi)

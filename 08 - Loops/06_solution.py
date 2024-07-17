# Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

number = 5
fact = 1

while number > 0:
    fact *= number
    number-= 1

print('Factorial value of Number is', fact)

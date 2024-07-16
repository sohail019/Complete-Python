# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

number = input('Enter a Number: ')
number = int(number)

sum_even = 0

for i in range(1, number+1):
    if i%2 == 0:
        sum_even += i

print('Sum of Even Number upto', number, ' is ', sum_even)
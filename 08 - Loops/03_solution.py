# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.


num = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(num ,'x', i, '=' ,num*i)

# With User Input
print('-----------With User Input------------')
number = input('Enter a Number: ')

number = int(number)

for i in range(1, 11):
    if i == 5:
        continue
    print(number, 'x', i, ' = ', number*i)
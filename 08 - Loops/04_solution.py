# 4. Reverse a String
# Problem: Reverse a string using a loop.

str = 'sohail'
reversed_str = ''

for char in str:
    reversed_str = char + reversed_str

print(reversed_str)

# With User Input
print('-----With User Input-----------')

input_str = input('Enter a String: ')

input_reversed_str = ''

for char in input_str:
    input_reversed_str = char + input_reversed_str

print('Reversed String of', input_str, 'is "',input_reversed_str,'".')
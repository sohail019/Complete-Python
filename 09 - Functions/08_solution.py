# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "sohail", age = 21)
print_kwargs(fullName = "sohail shaikh", age = 21, language = 'python')

print_kwargs(fruit = "banana", color = 'yellow', isRiped = True)
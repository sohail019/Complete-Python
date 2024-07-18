# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name = 'Sohail'):
    greet_template = 'Heyy ' + name + '!'
    return greet_template

print(greet('Sohail Shaikh')) # Heyy Sohail Shaikh
print(greet()) # Hey Sohail
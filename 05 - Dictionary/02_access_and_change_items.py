# ----------------------------------------------------------
myself = {
    'name': 'sohail',
    'age': 21,
    'hobby': 'coding',
    'dob': '28th September',
    'gender': 'male',
}
print(myself)
# Access Dictionary Items
print('')
print('--------------Access Dictionary Items----------------')

# Access dictionary by referring to it's key name, inside square brackets
print(myself['age'])

# By using get method
print(myself.get('name'))

# Get Keys - keys() method will return a list of all the keys in dictionary
print(myself.keys())

# Get Values - values() method will return a list of all the values in the dictionary
print(myself.values())

# Get Items  - items() method will return each item in a dictionary, as tuples in a list
print(myself.items())

my_car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 2020
}
print(my_car)

# Check if Key Exists
if 'brand' in my_car:
    print("Yes, brand in my_car exists")

# --------------------------------------------------------------
# Change Dictionary Items
print('')
print('--------------Change Dictionary Items----------------')

my_favt = {
    'language' : 'python',
    'fruit' : 'watermelon',
    'sports': 'cricket',
    'player': 'rohit sharma'
}

print(my_favt)

# change the value of a specific item by referring to its key name
my_favt['player'] = 'Virat Kohli'
print(my_favt)

# Update Dictionary - update() method will update the dictionary with the items
# The argument must be a dictionary or iterable object with key:value pairs

my_favt.update({'fruit': 'banana'})
print(my_favt)

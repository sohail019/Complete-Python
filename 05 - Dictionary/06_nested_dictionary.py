# --------------------------------------------------------------
# Nested  Dictionary
print('')
print('--------------Nested Dictionary----------------')

# Dictionary contain dictionaries is called nested

my_family = {
    'child1': {
        'name': 'Jack',
        'age': 21
    },
    'child2': {
        'name': 'Mark',
        'age': 14
    },
    'child3': {
        'name': 'Sophie',
        'age': 15
    }
}
print(my_family)

# Access items in nested 
print(my_family['child1']['name']) # Jack


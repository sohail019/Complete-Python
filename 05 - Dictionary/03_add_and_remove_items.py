my_favt = {
    'language' : 'python',
    'fruit' : 'watermelon',
    'sports': 'cricket',
    'player': 'rohit sharma'
}

# --------------------------------------------------------------
# Add Items in Dictionary
print('')
print('--------------Add Items in Dictionary----------------')

# it is done by using a new index key and assigning a value to it
my_favt['color'] = 'black'
print(my_favt)

# update method is used to change but if item does not exist it will add
my_favt.update({'song': 'Love Yourself'})
print(my_favt)

# --------------------------------------------------------------
# Remove Items from Dictionary
print('')
print('--------------Remove Items from Dictionary----------------')

# pop() method : removes the item with specified key name
my_favt.pop('color')
print(my_favt)

# popitem() method: removes the item from the last inserted item
my_favt.popitem()
print(my_favt)

# del keyword -  removes the item with specified key name
del my_favt['language']
print(my_favt)

# clear method -  empties the dictionary
my_favt.clear()
print(my_favt)

# del method also deletes the entire dictionary
del my_favt
# print(my_favt) #my_favt is not defined 

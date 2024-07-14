# --------------------------------------------------------------
my_favt = {
    'language' : 'python',
    'fruit' : 'watermelon',
    'sports': 'cricket',
    'player': 'rohit sharma'
}
print(my_favt)
# Copy a Dictionary
print('')
print('--------------Copy a Dictionary----------------')

# by using built in copy() method
my_favt_copy = my_favt.copy()
print(my_favt_copy)

# by using dict() constructor

my_favt_copy_2 = dict(my_favt_copy)
print(my_favt_copy)

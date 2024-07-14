# --------------------------------------------------------------
# Loop through a Dictionary
print('')
print('--------------Loop through a Dictionary----------------')

#  you can loop through a dictionary using for loop
#  when looping, the return value are the keys of the dictionary, but there are methods to return the values as well

# print all keys name
my_favt = {
    'language' : 'python',
    'fruit' : 'watermelon',
    'sports': 'cricket',
    'player': 'rohit sharma'
}

for key in my_favt:
    print(key)

print('')

# print all values in the dictionary
for values in my_favt:
    print(my_favt[values])

print('')

# we can use values methods as well
for values in my_favt.values():
    print(values)

print('')

# we can use keys method to return keys
for keys in my_favt.keys():
    print(keys)

print('')
# loop through both keys and values by using items method
for key, value in my_favt.items():
    print('KEY:', key , 'Value: ', value)

# Python List

# List are used to store multiple items in a single variable
# List are created using square bracket []

this_list = ['apple', 'mango', 'banana']
print(this_list)

# List items are ordered, changeable and allow duplicate values
# Items are indexed, the first item has index [0], second has [1]

# Ordered means that the items have defined order, and that order will not change, If you add new items to a list, the new items will be placed at the end of the list.

# Changeable means that we can change, add, and remove items in a list after it has been created.

# Allow duplicates means it can have items with same values

this_list2 = ['apple', 'mango', 'apple', 'mango', 'banana']
print(this_list2)

# lenght of list
print(len(this_list2)) #5

# type of list
print(type(this_list2)) # <class 'list'>

# list constructor
fruits = list(('apple', 'mango', 'banana', 'apple', 'watermelon'))
print(fruits)
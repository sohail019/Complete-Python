# Tuples in Python

# Tuples are used to store multiple items in a single variable
# Tuple is a collection which is ordered and unchangeable
# Tuples are written with round brackets()

# Create a Tuple
fruits = ('banana', 'mango', 'orange', 'apple')
print(fruits)

# tuples are unchangeable which means we cannot change, add or remove items after the tuple has created

# Create tuple with one item
veggies = ('potato',) # You have to add a comma after the item, otherwise python will not recognize it as a tuple

print(veggies) 

# Type
print(type(fruits))

# Constructor 
bikes = tuple(('Honda', 'Royal Enfield', 'Suzuki')) # note double brackets
print(bikes)


# -----------------------------------------------
print('')
print('-------------------Access the tuple------------------')

print(bikes[1]) #Royal Enfield
print(bikes[-1]) #Negative Indexing -> Suzuki
print(fruits[2:])

# Check if item is
if 'banana' in fruits:
  print('It has Banana')


# -----------------------------------------------
print('')
print('-------------------Update the tuple------------------')

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there are some workarounds, you can convert the tuple into list, change the list and convert back to tuple

veggies = ('potato', 'tomato', 'onion')
print(veggies, type(veggies))
veggies_list = list(veggies)
print(veggies_list, type(veggies_list))
veggies_list[1] = 'brinjal'
print(veggies_list, type(veggies_list))
veggies = tuple(veggies_list)
print(veggies, type(veggies))


# Add tuple to tuple
shopping = fruits + veggies
print(shopping)

# Remove Items
# Same convert to list, remove item then convert back to tuple

# or del the tuple completely
del shopping
# print(shopping)

# -----------------------------------------------
print('')
print('-------------------Unpack the tuple------------------')

fruits = ('apple', 'banana', 'grapes')

(red , yellow , green) = fruits

print(red)
print(yellow)
print(green)

# NOTE: the number of variable must match with number of values in tuple, if not you must use asterisk(*) to collect the remaining value


fruits = ('apple', 'banana', 'grapes', 'watermelon', 'guava', 'custard apple')

(red , yellow , *green) = fruits

print(red)
print(yellow)
print(green)


print('--------------Access Items----------------')
fruits = ['apple', 'mango', 'banana', 'orange']
print(fruits) 

# Access items
print(fruits[1]) # mango
print(fruits[2]) # banana
print(fruits[0]) # apple

# Change list
fruits[1] = 'grapes'
print(fruits) # ['apple', 'grapes', 'banana', 'apple', 'watermelon']


# Insert item in a list
print(' ')
print('--------------Insert Items----------------')
# To insert a new list item, without replacing any of the existing values, we can use insert() method. it inserts an item at specific index
print('Before Insertion::', fruits)
fruits.insert(2, 'oranges')
print('After Insertion::,', fruits)

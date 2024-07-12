fruits = ['apple', 'mango', 'banana', 'orange']
print(fruits) 


# Access items
print(fruits[1]) # mango

# Change list
fruits[1] = 'grapes'
print(fruits) # ['apple', 'grapes', 'banana', 'apple', 'watermelon']

# Insert item in a list

# To insert a new list item, without replacing any of the existing values, we can use insert() method. it inserts an item at specific index

fruits.insert(2, 'oranges')
print(fruits)

fruits = ['apple', 'mango', 'banana', 'orange']
print(fruits) 

print('----------------------Add Items ------------------------')
# Add Items

# Append Items - To add an item at the end of the list, use append() method
fruits.append('strawberry') # ['apple', 'mango', 'banana', 'orange', 'strawberry']
print(fruits)


# Extend items - To append elements from another list to the current list, use extend()
veggies = ['spinach', 'brocolli', 'tomato', 'potato']
print(veggies) # ['spinach', 'brocolli', 'tomato', 'potato']

fruits.extend(veggies) # veggies will be added to the end of fruits
print(fruits) # ['apple', 'mango', 'banana', 'orange', 'spinach', 'brocolli', 'tomato', 'potato']

# Add any other iterable too like tuples, set, dictionaries
chai = ('masala chai', 'ginger tea', 'lemon tea')
print(chai)

fruits.extend(chai)   
print(fruits) #['apple', 'mango', 'banana', 'orange', 'spinach', 'brocolli', 'tomato', 'potato', 'masala chai', 'ginger tea', 'lemon tea'] 

# Remove
print('----------------------Remove Items ------------------------')
# Remove specified items
cold_drinks = ['thumps up', 'mirinda', 'pepsi', 'coca cola', '7 up']
print(cold_drinks) 

cold_drinks.remove('mirinda') 
print(cold_drinks) # mirinda will be removed

# # Remove specified index
cold_drinks.pop(1)
print(cold_drinks) # pepsi will be removed
# # Note - If you don't specify the index, the pop() method removes the last item

print('----------------------del Keywords ------------------------')
# # del keyword also removes the specified index
print(cold_drinks)
del cold_drinks[2]
print(cold_drinks)

# Delete the entire list
del cold_drinks
# print(cold_drinks)

print('----------------------Clear the list ------------------------')
# # Clear the list
chai = ['lemon tea', 'ginger tea', 'masala tea']
chai.clear()
print(chai)


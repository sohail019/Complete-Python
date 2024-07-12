import random
# ---------------------------------------------------------
print('-------------------Random---------------')
# Random - module imported

print(random.random()) # Returns a random float number between 0 and 1

print(random.randint(1, 10)) # random number in integer 

l1 = [1,2,3,4,5,6]
print(l1)
print(random.choice(l1)) # choice to select random from list

random.shuffle(l1)# shuffle the list
print(l1)
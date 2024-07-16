# 10. Pet Food Recommendation

# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_species = input('Enter Your Pet: ')
age = input("Enter Pet's Age: ")

age = int(age)
food = ''

if (pet_species == "Dog" and age < 2):
    food = 'Puppy Food'
elif (pet_species == 'Cat' and age > 5):
    food = 'Senior cat food'
else:
    print("Sorry, currently I don't have knowledge about this!")
    exit()

print('Your Pet is', pet_species , 'and Age of your pet is', age, ' So I recommend you ', food)
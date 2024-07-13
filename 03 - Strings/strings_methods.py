# ------------------------------------------
print('-----------------Slice---------------------')

name = 'Sohail Shaikh'

# slice sohail from name
print(name[0:6])  # sohail

my_list = "0123456789"
print(my_list[:])  #0123456789
print(my_list[3:])  #3456789
print(my_list[:7])  #0123456
print(my_list[0:7:2])  #0246
print(my_list[0:7:3])  #036

# ----------------------------------------
print('----------------Upper and Lower-------------------')
print(name.upper())
print(name.lower())  #sohail shaikh

# -------------------------------------------
print('--------------Strip-------------')
surname = '     Shaikh        '
print(surname)
print(surname.strip())  # Shaikh

# -------------------------------------------
print('--------------Replace-------------')
print(name.replace('Shaikh', 'Khan'))  # sohail khan
print(name)  # sohail shaikh

# -------------------------------------------
print('--------------List to String Conversion-------------')
fruits = ['apple', 'mango', 'banana']
print(fruits)
print(type(fruits)) # <class 'list'>
print(", ".join(fruits)) # 'apple, mango, banana'
print(type(fruits)) # <class 'list'>

# -------------------------------------------
print('--------------String to List Conversion-------------')
veggies = 'tomato, cauliflower, potato, onion'
print(veggies) 
print(type(veggies)) # <class 'str'>
print(veggies.split(", "))  # ['tomato', 'cauliflower', 'potato', 'onion']
print(type(veggies)) # <class 'str'>

# -------------------------------------------
print('-----------Find index of character or word in string----------')
fullname = 'Sohail Shaikh'
print(fullname)
print(fullname.find('Shaikh')) #7
print(fullname.find('S')) # 0
print(fullname.find('m')) # -1 if not found

# -------------------------------------------
print('------------Count of character or word in srting----------')
fullname = 'Sohail Shaikh Shaikh Shaikh Shaikh'
print(fullname)
print(fullname.count('Shaikh')) # 4
print(fullname.count('S')) # 5
print(fullname.count('M')) # 0 if not found

# -------------------------------------------
print('------------Contains or Not----------')
fullname = 'Sohail Shaikh'
print('Sohail' in fullname) # True
print('sohail' in fullname) # False

# -------------------------------------------
print('------------Find Lenght of a String----------')
print(fullname, '- lenght:', len(fullname)) # 34
print(len('sohail')) # 6

# -------------------------------------------
print('------------Print each character line by line----------')
name = 'sohail'
for letter in name:
    print(letter)

# -------------------------------------------
print('------------Use Backslash for string----------')
# intro = "Hii, My Name is "Sohail Shaikh" and I am 21 years old" it gives error

intro = "Hii, My Name is \"Sohail Shaikh\" and I am 21 years old"
print(intro)

# -------------------------------------------
print('------------Raw String----------')
name = 'Sohail \n Shaikh'
print(name) # it will print sohail in one line and shaikh in next line
# solution???
name = r'Sohail \n Shaikh'
print(name) # 'Sohail \n Shaikh'

# Windows path problem 
# path = 'c:\user\Python' # Error about unicode escape 
path = r'c:\user\Python'
print(path)    


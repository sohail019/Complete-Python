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
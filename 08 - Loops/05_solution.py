# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.


str = input('Enter a String that contains repeater character: ')

for char in str:
    if str.count(char) == 1:
        print('Firsy Non Repeated Char from', str, 'is', char  )
        break

# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

num = 0

while True:
    num = int(input('Enter a Number b/w 1 to 10: '))

    if 1 <= num <= 10:
        print('Thanks')
        break
    else:
        print('Invalid Number!! Try Again') 
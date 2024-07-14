# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit_name = input('Enter Your Fruit Name:: ')


if fruit_name == 'Banana':
  color = input('Enter Color of Your Fruit:: ')
  if color == 'Green':
    print("Offo! You can't eat this, it's still Unripe")
  elif color == 'Yellow':
    print("Wohoooo, You can eat it.. It's Ripe")
  elif color == 'Brown':
    print("Throw it in dustbin, It's Overripe")
  else:
    print("No, Banana can't be this color, You picked up some other fruit I guess")
else:
  print("Sorry, right now I don't have information for this fruit")
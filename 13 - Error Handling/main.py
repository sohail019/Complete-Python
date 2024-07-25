file = open('myFile.txt', 'w')


try:
  file.write('Written through try catch block')
finally:
  file.close()



with open('myFile.txt', 'w') as file:
  file.write('Written through more easy with as syntax')
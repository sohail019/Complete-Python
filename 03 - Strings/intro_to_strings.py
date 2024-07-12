# Strings
# --> Strings in python are surrounded by either single quotation marks or double quotation marks
#  --> 'hello' is same as "hello"

print('hello')
print("hello")

# Quotes inside quotes
print("It's already here")  # It's already here
print('He called "sohail"')  # He called "sohail"

# Multiline strings
print(
    """Virat Kohli was born on 5 November 1988 in Delhi into a Punjabi Hindu family. His father, Prem Nath Kohli, worked as a criminal lawyer, and his mother, Saroj Kohli, served as a housewife. He has an older brother, Vikas, and an older sister, Bhawna.[9] Kohli's formative years were spent in Uttam Nagar. He commenced his early education at Vishal Bharti Public School.[10] According to his family, Kohli exhibited an early affinity for cricket as a three-year-old. He would pick up a cricket bat and request his father to bowl to him.[11]
""")

# Assign to variable
name = 'sohail'
print(name)

# Type of String
print(type(name))  # <class 'str'>

# length of string
print(len(name))  # 6

# check certain phrase or character in string
print('o' in name)  # True
print('z' in name)  # False

# Take out character
print(name[0])  # s
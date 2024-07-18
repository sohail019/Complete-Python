# Closures:
# It is a nested function that allows us to access variables of the outer function even after the outer function is closed

# Let's revise nested function

def greet(name):
    # inner function
    def display_name():
        print('Hii', name)
    
    # call inner function
    display_name()

# call outer function
greet('Sohail') 
# Output : Hii Sohail


# Python closures
print('')
print('----------Python Closure----------')

def greet2():
    # variable defined outside the inner function
    name = 'Sohail'

    # Return a nested anonymous function
    return lambda: 'Hii ' + name

# call the outer function
message = greet2() # the return function is now assigned to the message variable
# At this point the execution of the outer function is completed, so the name variable should be destroyed. However we can call the anonymous function using
# print the inner function
print(message())

# We are able to access the name variable of the outer function

# IT'S POSSIBLE BECAUSE THE NESTED FUNCTION NOW ACTS AS A CLOSURE THAT CLOSES THE OUTER SCOPE VARIABLE WITHIN ITS SCOPE EVEN AFTER THE OUTER FUNCTION IS EXECUTED

# One more Example

# Print odd numbers using python closure
print('')
print('----------Print Odd Numbers using PC----------')
def calculate():
    num = 1

    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

# call the outer function
odd = calculate() # the code executes the outer function calculate() and returns a closure to the odd number
# That's why we can access the num variable of calculate even after completing the outer function.



# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate() # Again when we call the outer function
print(odd2()) # a new closure is returned. Hence we get 3 again when we call odd2()


# WHEN TO USE CLOSURES????????

# It can be used to avoid global values and provide data hiding, and can be an elegant solution for simple cases with one or few methods.

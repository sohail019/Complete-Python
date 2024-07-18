# Scopes

# Scope: A Variable is only available from inside the region it is created


# Local Scope --> A variable created inside a function belongs to the local scope of that function, and can only be used inside the function

# Example
print('------------Local Scope---------------')
def my_func():
    x = 300
    print(x)

my_func()
# print(x) # NameError: x is not defined

# -------------------------------------------------
# Function inside function
print('')
print('------------Function inside Function---------------')

def myfunc():
    x = 10
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# -------------------------------------------------
# Global scope --> A variabe created in the main body of python file and it is available from within any scope, global and local
print('')
print('------------Global Scope---------------')

x = 100

def my_global_func():
    print(x)

my_global_func() # 100

print(x) # 100

# -------------------------------------------------

# Naming Variables
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

print('')
print('------------Naming variables---------------')
x = 300
def func1():
    x = 200
    print(x) # ye local lega -> 200

func1()

print(x) # 300

# ------------------------------------------------------
# global Keyword :-> If you need to create a global variable, but are stuck in local scope, you can use global keyword
# it makes the variable global
print('')
print('------------global Keyword---------------')

def func2():
    global x
    x = 10

func2()
print(x) # 10 from func2() function

# Also use the global keyword if you want to change a global variable inside a function

x = 100

def func3():
    global x
    x = 112

func3()
print(x)





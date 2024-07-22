# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):

    def wrapper(*args, **kwargs):

        args_value = ', '.join(str(arg) for arg in args)

        kwargs_value = ', '.join(f"{k}:{v}" for k,v in kwargs.items())

        print(f"Calling: {func.__name__} function with Arguments: {args_value} and Keyword Arguments: {kwargs_value}")

        return func(*args, **kwargs)
    
    return wrapper

@debug
def print_name(name):
    print(name)

@debug
def greet(greet, name):
    print(greet + name)

print_name('Sohail')

greet('Hello ', 'Sohail')
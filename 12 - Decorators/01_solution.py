# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time() # records the start time

        result = func(*args, **kwargs) # executes the function

        end = time.time() # records the end time

        actual_time = round(end - start, 2) # calculate the function time 
        
        print(f"{func.__name__} ran in ${actual_time} seconds")

        return result # return result of original function
    return wrapper

@timer
def first_function(n):
    time.sleep(n)
    print('Function 1')

first_function(2)

@timer
def second_function(n):
    time.sleep(n)
    print('Function 2')

second_function(6)


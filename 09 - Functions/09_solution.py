# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):

    for i in range(2, limit + 1, 2):
        yield i # yield keyword is used to return a list of values from a function, unlike return keyword which stops further execution of function, yield continues to the end of the function


for num in even_generator(10):
    print(num)

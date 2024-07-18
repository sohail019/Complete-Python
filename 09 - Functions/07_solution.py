# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args): # *args to take multiple arguments
    # print(args) # ye tuple return karta hai arguments ka

    # for i in args:
    #     print(i * 2)
    
    return sum(args)

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6))
print(sum_all(1,2,3,4,5,6,7,8))
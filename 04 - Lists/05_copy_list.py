# List Copy
#  You cannot copy a list by simply typing list1 = list2, because list 2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2


chai = ['masala chai', 'adrak wali chai', 'nimbu wali chai']

# There are 2 ways, by using built in method - copy() or list()

chai_copy = chai.copy()
print(chai_copy)
chai[0] = 'malai chai'
print(chai)

chai_copy_2 = list(chai)
print(chai_copy_2)


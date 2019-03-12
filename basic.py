"""
Python does offer magic methods like sum() and others, please try to write down your algorithms or coding 
instructions clearly without using any shortcuts
"""
# Multiply 3 and any number
def mult(number):
    # complete your code
    product = 3*number
    return product  

# adds two numbers together
def add(a, b):
    # complete with your solution
    return a + b

"""
Using data structures like list, can you find the total or the values in that list.
Do not use a function like sum(someList), that would be cheating ;-)
"""
# Data structure
numbers = [1,2,3,6]
def sumOfList(someList):
    # your solution
    total = 0
    for item in someList:
        total += item
    return total

# Program checker (do not change the lines below)    
assert sumOfList(numbers) == 12
assert mult(3) == 9
assert add(1,3) == 4

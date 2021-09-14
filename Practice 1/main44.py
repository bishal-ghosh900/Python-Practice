# generators

# generators object will only be created if we use comprehension expression inside the parenthesis
# if there is a large number of data, and we don't want to store the data in the memory, then generators are required. It doesn't store all the data, it only generate the data at the time of iteration

from sys import getsizeof 

numbers1 = (i*2 for i in range(1000)) # It is generator , doesn't store the values
print(f"size of this genrator object is {getsizeof(numbers1)}") # size of this genrator object is 112

numbers1 = [i*2 for i in range(1000)] # It is list , stores the values
print(f"size of this list object is {getsizeof(numbers1)}") # size of this list object is 8856



numbers2 = (i*2 for i in range(1000000)) # It is generator , doesn't store the values
print(f"size of this genrator object is {getsizeof(numbers2)}") # size of this genrator object is 112

numbers2 = [i*2 for i in range(1000000)] # It is list , stores the values
print(f"size of this list object is {getsizeof(numbers2)}") # size of this list object is 8448728

# we can't use len() method to know how many elements are stored in generators as generators don't store the elements , it only generates the elements 
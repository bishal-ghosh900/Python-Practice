# array

from array import array

list = [1, 2, 3, 4, 5]

numbers = array("i", list) # here "i" is the typecode, and it is referring signed integer, means this array can only take signed integer, no float , no string , no other types.

print(numbers) 
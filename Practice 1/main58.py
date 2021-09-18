# list comprehension of list of iterable list
arr1 = [[1, 2], [3 , 4]]
arr2 = [[2, 7], [4, 5]]
arr3 = [ r for i in [arr1, arr2] for y in i for r in y]
arr4 = [k for i in arr1 for k in i]
print(arr3)
print(arr4)
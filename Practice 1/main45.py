# unpacking operator

# unpacking operator is same as spread operator in javascript

# list
list1 = [1, 2, 3, 4, 5]
print(*list1) # 1 2 3 4 5
list2 = [5, 6, 7, 8, 9]
list3 = [*list1, *list2]
print(list3) # [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]


# dictionary
obj1 = dict(x = 1, y = 2)
obj2 = dict(m = 4, n = 5, o = 9)
obj3 = {**obj1, **obj2}
print(obj3) # {'x': 1, 'y': 2, 'm': 4, 'n': 5, 'o': 9}
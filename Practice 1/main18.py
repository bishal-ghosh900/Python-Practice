# program to find a largest a number in a list

list  = [1, 5, 2, 6, 9, 6, 2, 7, 10, 22, 30, 5, 11]

max = list[0]
for i in list:
    if i > max:
        max = i
print(max)
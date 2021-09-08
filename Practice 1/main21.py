# Write a program to remove the duplicate in a list

list = [4, 4, 1, 2, 5, 3, 2, 6, 7, 3, 2, 6]

# method 1:

new = []

for i in list:
    if(i not in new) :
        new.append(i)

print(new)


# list methods
numbers = [5, 2, 1, 7, 4]

numbers.append(10) # [5, 2, 1, 7, 4, 10]
print(numbers)

numbers.insert(2, 6) # [5, 2, 6, 1, 7, 4, 10]
print(numbers)

numbers.remove(10) # [5, 2, 6, 1, 7, 4]
print(numbers)

numbers.pop() # [5, 2, 6, 1, 7]
print(numbers)


print(numbers.index(6)) # 2 --> first occurence of 6 is in index 2

print(6 in numbers) # True
print(10 in numbers) # False

numbers.append(6) # [5, 2, 6, 1, 7, 6]
print(numbers)

print(numbers.count(6)) # 2 --> all occurence of 6 in the list

numbers.sort() # [1, 2, 5, 6, 6, 7]
print(numbers)

numbers.reverse() # [7, 6, 6, 5, 2, 1]
print(numbers)

temp_numbers = numbers.copy();
print(temp_numbers)

temp_numbers.append(33)
print(temp_numbers) # [7, 6, 6, 5, 2, 1, 33]
print(numbers) # [7, 6, 6, 5, 2, 1]

del numbers[2: 5] # [7, 6, 1] --> int [2 : 5] -> 2 and 5 both are index, not length of how many numbers we want to delete
print(numbers)

numbers.clear() # []
print(numbers)



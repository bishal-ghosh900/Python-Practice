# zip function

# zip function only take iterable objects --> it is taking every list value with same index item and create a zip object until the smallest length argument exhausted, we can create a list by wrapping list() method around this zip object.

list1 = [1, 2, 3] # iterable
list2 = [4, 5, 6, 7, 8] # iterable
list3 = "abcde" # iterable
list4 = "abcdefgh" # iterable

x = zip(list1, list2, list3, list4)
print(x) # <zip object at 0x00000104CB154680>

print(list(x)) # [(1, 4, 'a', 'a'), (2, 5, 'b', 'b'), (3, 6, 'c', 'c')]
# set
nums = [1, 2, 3, 4, 5]

num_set1 = set(nums)
print(num_set1) 

num_set2 = {4, 5, 6, 7, 8}

# in set there is not any indexing , so we can't use expression like num_set1[0].
# 
# Basically set is used to do mathematics set operations
 
#union
print(num_set1 | num_set2) # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection
print(num_set1 & num_set2) # {4, 5}

# A - B --> Every element of A but not of B
print(num_set1 - num_set2) # {1, 2, 3}

# B - A --> Every element of B but not of A
print(num_set2 - num_set1) # {8, 6, 7}

# symmetric difference --> (A - B) U (B - A) --> Every thing present in A and B but not in both
print(num_set1 ^ num_set2) # {1, 2, 3, 6, 7, 8}

# like list we can also create set comprehension

nums = { i * 2 for i in range(5)}
print(nums) # {0, 2, 4, 6, 8}

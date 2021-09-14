# queue

from collections import deque

list1 = deque([1, 2, 3, 4, 5]);

list1.appendleft(10)
print(list1) # deque([10, 1, 2, 3, 4, 5])

list1.popleft()
print(list1) # deque([1, 2, 3, 4, 5])

list1.append(6)
print(list1) # deque([1, 2, 3, 4, 5, 6])

list1.pop()
print(list1) # deque([1, 2, 3, 4, 5])


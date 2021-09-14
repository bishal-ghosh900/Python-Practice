# Sieve of Eratosthenes
import math;
n = int(input())

def findPrimes(n):
    arr = [1 for i in range(n+1)]
    arr[0] = 0
    arr[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if arr[i] == 1:
            j = 2
            while j * i <= n:
                arr[j*i] = 0
                j += 1
    for index, value in enumerate(arr): # enumerate will give tuples for every iteration which will contain index and value of that particular iteration coming from the list . And in this particular list the tuple is being unpacked in the index and the value variable
    
    # Its something like --> index, value = ("0", 1)
    #                        index, value = ("1", 2) and so on
    # "0", "1", "2" etc are the indexs of the list, and the next argument is the value of that particular index from the list in which we are performing enumerate() operation.
        if value == 1:
            print(index, sep=" ")
        else:
            continue

findPrimes(n)
   


 


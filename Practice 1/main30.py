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
    for i in range(n+1):
        if arr[i] == 1:
            print(i, sep=" ")
        else:
            continue

findPrimes(n)
   


 


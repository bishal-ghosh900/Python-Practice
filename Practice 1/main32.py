# fizz-buzz 

def fizz_buzz(n):
    if n % 15 == 0:
        print("FizzBuzz", end=" ")
    elif n % 3 == 0:
        print("Fizz", end=" ")
    elif n % 5 == 0:
        print("Buzz", end=" ")
    else: 
        print(n, end=" ")

for i in range (1, 31):
    fizz_buzz(i);


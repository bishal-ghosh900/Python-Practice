# Exception handling


try:
    age = int(input("Age: "))
    year = 2000
    print(year/age)
except ValueError:
    print("Age must be a valid number")
except ZeroDivisionError:
    print("Age can't be zero")    

# Functions 

# print(add(1, 2)) --> error 
# 
# -> (why) -> In python everything is being iterpreted line by line, so thats why the functions in python should be define before than the function call

def add(x, y) :
    return x + y

print(add(1, 2)) # 3 -> the way function is called is said positional argument

print(add(x = 1, y = 2)) # 3 -> the way function is called is said keyword argument

print(add(y = 2, x = 1)) # 3 -> we can also call the function with keyword argument this way, Its the same as the upward add(x = 1, y = 2) call

# If we are using positional argument and keyword argument both then first argument should be postional argument else error will occur

# print(add(x = 1, 2)) -> error
print(add(1, y = 2)) # as first argument is positional argument, so that value is being set for x, as x is first parameter in the add(x, y) function, so thats why is the next argument is keyword argument then that argument should not be y,  Ex : add(1, x = 2) --> error
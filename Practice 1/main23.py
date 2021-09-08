# Unpacking

number1 = (1, 2, 3, 4)
a, b, c, d = number1
print(f"a = {a}, b = {b}, c = {c}, d = {d}") # a = 1, b = 2, c = 3, d = 4

number2 = [1, 2, 3, 4, 5, 6]
a, b, c, d, e, f = number2
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}") # a = 1, b = 2, c = 3, d = 4, e = 5, f = 6

# If there is n element then we have to unpack n variables else we will get error
# Ex:
#     nums = (1, 2, 3)
#     a, b = nums -> error

# And we can unpack this way also -->
x, y, z = 5, 6, 7
print(f"x = {x}, y = {y}, z = {z}") # x = 5, y = 6, z = 7
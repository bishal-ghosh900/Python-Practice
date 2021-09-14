# swapping variables

# 1st way
a = 10
b = 20
print(f"a = {a} and b = {b}")

a = a ^ b
b = a ^ b
a = a ^ b
print(f"a = {a} and b = {b}")


# 2nd way
c = 30
d = 40
print(f"c = {c} and d = {d}")

c , d = d, c
print(f"c = {c} and d = {d}")


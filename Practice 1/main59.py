# Namedtuple

from collections import namedtuple


# Namedtuples are used to create class which don't have any methods, only have data. Namedtuples are immutable

# lets create a class named Point which will be having two data members -> x and y.

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1,y=2)
p2 = Point(x=1,y=2)
p3 = Point(x=3,y=4)

print(p1 == p2) # True
print(p1 == p3) # False
print(f"Point({p1.x}, {p1.y})")
print(f"Point({p2.x}, {p2.y})")
print(f"Point({p3.x}, {p3.y})")


# namedtuples are immutable,
# we can't write syntax like -> p1.x = 5 or p1.y = 2 -> will give error


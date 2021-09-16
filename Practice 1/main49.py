# magic methods => https://rszalski.github.io/magicmethods/



class Point:
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

    def __eq__(self, o: object) -> bool: # here o: object is an annotation (just a type of hint, python ignores these annotations), here it means the argument in the second position is an object and the return type is boolean. The __eq__() is a magic method used to check the equality of two objects.
        return self.x == o.x and self.y == o.y

    def __gt__(self, o: object) -> bool: # The __gt__() is used to check for any object is greater than another object or not, this implementation also works for less than operation between two objects
        return self.x > o.x and self.y > o.y

    def __add__(self, o):
        return Point(self.x + o.x, self.y + o.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2) # True => using __eq__() method internally

p3 = Point(3, 4)
print(p1 > p3) # False  => using __gt__() method internally

p4 = p1 + p3
print(p4)
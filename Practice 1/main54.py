# method and constructor overriding
# multilevel inheritance 

class Animal:
    def __init__(self, eyes, tail):
        self.eyes = eyes
        self.tail = tail
    def walk(self):
        print("I am animal and I can walk.")
class Dog(Animal):
    def __init__(self, eyes, legs, tail ):
        super().__init__(eyes, tail)
        self.eyes = eyes
        self.legs = legs
    def walk(self):
        print("I am a dog and I also can walk.")
class Bird(Animal):
    def __init__(self, eyes, wings, tail):
        super().__init__(eyes, tail)
        self.eyes = eyes
        self.wings = wings
    def walk(self):
        print("I am a bird , I prefer flying instead of walking.")

a = Animal(2,1)
d = Dog(2, 4,1)
b = Bird(2, 2, 1)

a.walk()
print(f"Animal is having {a.eyes} eyes")
d.walk()
print(f"Dog is having {d.eyes} eyes and {d.legs} legs and having {d.tail} tails")
b.walk()
print(f"Bird is having {b.eyes} eyes and {b.wings} wings and having {b.tail} tails")
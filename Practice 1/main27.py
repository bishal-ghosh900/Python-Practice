# Class and Constructors and Objects

class Animal:

    hands = 4

    def __init__(self, legs): # -> Constructor 
        self.legs = legs # -> "self" is same as "this" in java

    def run(self):
        print(f"I am runnning using my {self.legs} legs")


animal = Animal(4) # -> animal is an object and Animal is the class 
animal.run() # I am runnning using my 4 legs
print(animal.hands) # 4
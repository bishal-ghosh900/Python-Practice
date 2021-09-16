# class method with decorator and inheritance

class Animal :

    def __inti__(self, eyes = 2):
        self.eyes = eyes


class Dog(Animal): # => inheritance (Dog IS-A Animal)

    def __init__(self, eyes):
        super().__inti__(eyes) # => getting the reference of the parent class from super() and calling the constructor using this reference. If we override the constructor here then the parent class constructor will be replace by it , so we have to call parent constructor by ourselves =>   super().__init__()

    @classmethod # => decorator to create class method
    def walk(cls):
        print("I can walk")

bukky = Dog(eyes = 2)
bukky.walk()
print(bukky.eyes)



# multiple inheritance

class Human:
    def __init__(self):
        pass

    def walk(self):
        print("I am a human, I can walk")
class Learner:
    def __init__(self):
        pass
    def walk(self):
        print("I am a learner, I can walk")
class Student(Human, Learner):
    def __init__(self):
        super().__init__()

s = Student()
s.walk() # I am a human, I can walk
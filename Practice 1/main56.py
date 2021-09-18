# abstract class

from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def interest(self):
        pass

class SBI(Bank):
    
    def interest(self):
        print(4.5)

class BOI(Bank):
    
    def interest(self):
        print(5.5)

#bank = Bank()  => type error
s = SBI()
b = BOI()
s.interest()
b.interest()
# property ( getter and setter in pythonic way ) and creating custom exception class

class InvalidAge(Exception) :
    pass

class Person :
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @property # => decorator to set property
    def age(self): # => it is getter
        return self.__age

    @age.setter
    def age(self, age): # => it is setter  
        if 0 < age < 200:
            self.__age = age
        else:
            raise InvalidAge("Give a valid age.")

p1 = Person("Bisal", "Ghosh", 21)
p1.age = 27
print(p1.age) # 27
# p1.age = -1 => gives an error ->  __main__.InvalidAge: Give a  valid age.

# we can do this implementation another way but in that implementation the code will be repeatated , so the upper implementation is best to declare property
# class Person :
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.__age = age
    
    
#     def get_age(self): # => it is getter
#         return self.__age

#     def set_age(self, age): # => it is setter  
#         if 0 < age < 200:
#             self.__age = age
#         else:
#             raise ValueError("give a valid age")
#     age = property(get_age, set_age)


# p1 = Person("Bisal", "Ghosh", 21)
# p1.age = 27
# print(p1.age)

# in this implementation the age can be set using the setter method and also the age property, same for the getter part also, thats why we are using the upper implementation
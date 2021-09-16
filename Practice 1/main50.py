# private members

# In python there we can prefix any data member with __ (dunder sign) , then it will be private. In reality it don't get private, if we declare any data member with __ , that data member actually get a differet name from python , which is like =>  _classname__fieldname. So in the below implementation if we change "eyes" field member to "__eyes" , then python will change it to "_Animal__eyes" . We can't access "eyes" by using "a.eyes" (here think "a" is Animal object) as eyes is changed to "_Animal__eyes" , so if we want to access "eyes", then we have to access it by using "a._Animal__eyes"

class Animal:
    def run(self):
        print("I can run")

    __eyes = 2
a = Animal()
# print(a.eyes) => error -> Animal object has no attribute eyes
print(a._Animal__eyes) # 2
a.run()
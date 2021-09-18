# extending built-in types
class Text(str):
    def indexOf(self, word):
        return self.index(word)
t = Text("I love python")
print(t.indexOf("python"))

class ArrayList(list):
    def appendWith(self, *value):
        for i in value:
            self.append(i)

l = ArrayList()
l.appendWith(3, 4, 7, 1, 9)
print(l)
print(*l)



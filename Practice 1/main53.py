# closure 

# A closure is a function that remembers its outer variables and can access them

def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

m = multiplier(10)(2)

print(m) # 20


# defected way of closure print
# def doThis():
#     arr = []
#     for x in range(1, 4):
#         arr.append(lambda  y: y * x)
#     return arr
# q1, q2,q3 = doThis()
# print(q1(10), q2(10), q3(10))
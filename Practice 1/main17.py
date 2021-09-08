# print "F" letter with using "x" letter and list 

#   xxxxx
#   xx
#   xxxxx
#   xx
#   xx

numbers = [5, 2, 5, 2, 2]

for i in numbers :
    output = ''
    for j in range(i):
        output += "x"
    print(output)

print("----------------------------")

for i in numbers :
    for j in range(i):
        print("x", end="")
    print("")
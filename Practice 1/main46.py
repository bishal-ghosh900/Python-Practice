# find the most repeated character in the sentence
from pprint import pprint

name = "This is a common interview question"

# method 1 ->

max = -1
j = -1
for i in name:
    count = name.count(i)

    if max < count:
        max = count
        j = name.index(i)
print(f"max character is {name[j]} counting is {max}")


# method 2 ->

nameDt = {}

for char in name:
    nameDt[char] = (nameDt[char] + 1) if (char in nameDt) else 1

pprint(nameDt, width = 1)

nameDt_real = sorted(nameDt.items(), key= lambda key:key[1], reverse=True)

print(nameDt_real)


print(f"The pair of the max occured character and its occurence is" , nameDt_real[0])

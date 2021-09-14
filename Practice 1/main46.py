# find the most repeated character in the sentence

name = "This is a common interview question"

max = -1
j = -1
for i in name:
    count = name.count(i)

    if max < count:
        max = count
        j = name.index(i)
print(f"max character is {name[j]} counting is {max}")